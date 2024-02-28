import sys
import json
import re
from datetime import datetime, timedelta

def parse_chat_to_json(input_text):
    """
    Parses the given chat history text into a list of messages grouped by time periods,
    ensuring each period contains at least one user and one assistant message.

    Args:
    input_text (str): The chat history as a multiline string.

    Returns:
    list: A list of dictionaries, each containing a group of messages.
    """
    lines = input_text.split('\n')
    messages = []

    current_time = None
    current_messages = []
    has_user = has_assistant = False

    for line in lines:
        if "] " in line:
            parts = line.split('] ')
            timestamp_sender = parts[0][1:]
            message_content = '] '.join(parts[1:])
            
            if ": " in message_content:
                sender, content = message_content.split(': ', 1)
                role = "user" if "Kohei" not in sender else "assistant"
                content = re.sub(r'[^\w\s]|http\S+', '', content)

                timestamp = datetime.strptime(timestamp_sender, "%m/%d/%y, %I:%M:%S %p")

                if current_time is None or timestamp - current_time > timedelta(hours=1):
                    if has_user and has_assistant:
                        messages.append({"messages": current_messages})
                    current_messages = []
                    current_time = timestamp
                    has_user = has_assistant = False

                current_messages.append({"role": role, "content": content.strip()})
                if role == "user":
                    has_user = True
                else:
                    has_assistant = True

    if has_user and has_assistant:
        messages.append({"messages": current_messages})

    return messages

def clean_chat_history(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        chat_history = file.read()

    parsed_messages = parse_chat_to_json(chat_history)

    output_file_path = output_file_path.rstrip('.txt') + '.jsonl'

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for message_group in parsed_messages:
            json.dump(message_group, file, ensure_ascii=False)
            file.write('\n')

    print(f"Formatted chat history saved to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_chat_history.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    clean_chat_history(input_file_path, output_file_path)
