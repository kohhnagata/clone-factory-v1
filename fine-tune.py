import os
import json
from openai import OpenAI
from sklearn.model_selection import train_test_split

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

cleaned_chat_history_path = "./cleaned_chat_history"

def combine_and_split_data(path, train_split=0.8):
    all_data = []
    for filename in os.listdir(path):
        if filename.startswith('.') or filename.endswith('.swp'):
            continue
        filepath = os.path.join(path, filename)
        with open(filepath, 'rb') as f:  
            for line in f:
                try:
                    decoded_line = line.decode('utf-8', 'ignore')
                    data = json.loads(decoded_line)
                    all_data.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {filename}: {e}")
                except UnicodeDecodeError as e:
                    print(f"Unicode decode error in file {filename}: {e}")

    training_data, validation_data = train_test_split(
        all_data, test_size=1 - train_split, random_state=42
    )

    train_file = os.path.join(path, "for-training.jsonl")
    val_file = os.path.join(path, "for-validation.jsonl")

    with open(train_file, "w", encoding='utf-8') as f:
        for item in training_data:
            json.dump(item, f)
            f.write("\n")

    with open(val_file, "w", encoding='utf-8') as f:
        for item in validation_data:
            json.dump(item, f)
            f.write("\n")

    return train_file, val_file

def start_fine_tuning(training_file_path, validation_file_path):
    """
    Uploads training and validation files and initiates fine-tuning with GPT-3.5 Turbo.

    Args:
        training_file_path (str): Path to the training JSONL file.
        validation_file_path (str): Path to the validation JSONL file.
    """

    if not os.path.exists(training_file_path) or not os.path.exists(validation_file_path):
        print(f"Error: Training or validation file not found at {training_file_path} or {validation_file_path}")
        return

    try:
        training_file = client.files.create(file=open(training_file_path, "rb"), purpose="fine-tune")
        validation_file = client.files.create(file=open(validation_file_path, "rb"), purpose="fine-tune")

        suffix_name = "pocoloco-test"
        response = client.fine_tuning.jobs.create(
            training_file=training_file.id,
            validation_file=validation_file.id,
            model="gpt-3.5-turbo",
            suffix=suffix_name,
        )
        print(f"Fine-tuning job started. Response: {response}")
    except Exception as e:
        print(f"Error during fine-tuning: {e}")


if __name__ == "__main__":
    training_file_path, validation_file_path = combine_and_split_data(cleaned_chat_history_path)
    start_fine_tuning(training_file_path, validation_file_path)
    print("Chat clone generation using GPT-3.5 Turbo initiated.")
