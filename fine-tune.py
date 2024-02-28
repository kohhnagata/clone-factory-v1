import os
from openai import OpenAI

client = OpenAI(api_key="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")

cleaned_chat_history_path = "/Users/kohei/Desktop/Pocoloco-Test/cleaned_chat_history"

# Get all files in the directory
files = os.listdir(cleaned_chat_history_path)

# Order files by creation time (oldest first)
files.sort(key=lambda f: os.path.getmtime(os.path.join(cleaned_chat_history_path, f)))

# Pick the first file as training data
training_file_path = os.path.join(cleaned_chat_history_path, files[0])

# Pick the last file as validation data
validation_file_path = os.path.join(cleaned_chat_history_path, files[-1])

# Open and upload files
training_file = client.files.create(
    file=open(training_file_path, "rb"), purpose="fine-tune"
)
validation_file = client.files.create(
    file=open(validation_file_path, "rb"), purpose="fine-tune"
)

# Create fine-tuning job
suffix_name = "pocoloco-test"
response = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    validation_file=validation_file.id,
    model="gpt-3.5-turbo",
    suffix=suffix_name,
)