import sys
import json

def parse_chat_to_json(input_text):
    """
    Parses the given chat history text into a list of messages with 'role' and 'content' keys.
    
    Args:
    input_text (str): The chat history as a multiline string.
    
    Returns:
    list: A list of dictionaries, each containing the 'role' and 'content' of a message.
    """
    # Split the input text into lines
    lines = input_text.split('\n')
    
    # Initialize an empty list to store parsed messages
    messages = []
    
    # Iterate over each line in the chat history
    for line in lines:
        # Split line into components based on the structure
        if "] " in line:  # Check if line contains expected delimiter
            parts = line.split('] ')
            timestamp_sender = parts[0][1:]  # Remove leading '['
            message_content = '] '.join(parts[1:])  # Rejoin if ']' was part of the message
            
            # Further split to isolate sender and possibly adjust the structure if needed
            if ": " in message_content:
                sender, content = message_content.split(': ', 1)
                role = "user" if "Kohei" not in sender else "assistant"  # Assign role based on sender
                # Append parsed message to the list
                messages.append({"role": role, "content": content.strip()})
    
    return messages

def clean_chat_history(input_file_path, output_file_path):
    """
    Cleans the chat history from a given input file and writes the formatted result to the specified output file.
    
    Args:
    input_file_path (str): Path to the input chat history file.
    output_file_path (str): Path to the output file where the formatted result will be written.
    """
    # Read the input chat history file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        chat_history = file.read()

    # Parse the chat history
    parsed_messages = parse_chat_to_json(chat_history)

    # Ensure output file ends with .jsonl
    output_file_path = output_file_path.rstrip('.txt') + '.jsonl'  # Remove any existing .txt extension

    # Write the parsed messages to the output file in JSONL format
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for message in parsed_messages:
            json.dump(message, file, ensure_ascii=False)
            file.write('\n')  # Add newline to separate JSON objects

    print(f"Formatted chat history saved to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_chat_history.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    clean_chat_history(input_file_path, output_file_path)
