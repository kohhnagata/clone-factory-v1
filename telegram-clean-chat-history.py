import os
import re
import sys
import json
from datetime import datetime, timedelta

def clean_content(content):
    # Remove URLs
    content = re.sub(r'http\S+', '', content)
    # Remove emojis and non-word characters except spaces
    content = re.sub(r'[^\w\s]', '', content)
    return content

def parse_chat_to_json(input_data):
    messages = input_data['messages']
    grouped_messages = []

    current_time = None
    current_messages = []
    has_user = has_assistant = False

    for message in messages:
        if message['type'] == 'message':
            timestamp = datetime.fromisoformat(message['date'])
            sender = message['from']
            if isinstance(message.get('text'), list):
                # Combine text and text entities into a single string
                content = ''.join([str(item) if isinstance(item, str) else item.get('text', '') for item in message['text']])
            else:
                content = message.get('text', '')
            role = "user" if "kohei.eth ☂️" not in sender else "assistant"
            
            # Clean the content
            content = clean_content(content)

            if content.strip():  # Skip messages with empty content after cleaning
                if current_time is None or timestamp - current_time > timedelta(hours=1):
                    if has_user and has_assistant:
                        grouped_messages.append({"messages": current_messages})
                    current_messages = []
                    current_time = timestamp
                    has_user = has_assistant = False

                current_messages.append({"role": role, "content": content.strip()})
                if role == "user":
                    has_user = True
                else:
                    has_assistant = True

    if has_user and has_assistant:
        grouped_messages.append({"messages": current_messages})

    return grouped_messages

def clean_chat_history(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        chat_history = json.load(file)

    parsed_messages = parse_chat_to_json(chat_history)

    output_file_path = output_file_path.rstrip('.json') + '.jsonl'

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for message_group in parsed_messages:
            if message_group['messages']:  # Ensure there are messages in the group before writing
                json.dump(message_group, file, ensure_ascii=False)
                file.write('\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_chat_history.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    clean_chat_history(input_file_path, output_file_path)