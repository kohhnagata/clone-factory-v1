import os
import re
import sys
import json
from datetime import datetime, timedelta

def is_unnecessary_content(content):
    unnecessary_patterns = [
        re.compile(r"reaccion\w*\s+.*\s+a tu mensaje", re.IGNORECASE),
        re.compile(r"reacted\s+.*\s*to your message", re.IGNORECASE),
        re.compile(r"reaccion[oó]\s+[\s\S]*?\s*a tu mensaje", re.IGNORECASE),
    ]
    return any(pattern.search(content) for pattern in unnecessary_patterns)

def clean_content(content):
    if is_unnecessary_content(content):
        return ""
    content = re.sub(r'http\S+', '', content)  
    content = re.sub(r'[^\w\s]', '', content)  
    return content.strip()

def parse_chat_to_json(input_data, custom_user_name):
    messages = input_data['messages']
    participants = {p['name']: "user" if custom_user_name.lower() not in p['name'].lower() else "assistant" for p in input_data['participants']}
    parsed_messages = []

    current_time = None
    current_messages = []
    has_user = has_assistant = False

    for message in reversed(messages):  
        sender_name = message['sender_name']
        content = message.get('content', '')
        timestamp_ms = message['timestamp_ms']
        role = participants.get(sender_name, "user")

        content = clean_content(content)
        if not content:  
            continue

        timestamp = datetime.fromtimestamp(timestamp_ms / 1000.0)
        if current_time is None or timestamp - current_time > timedelta(hours=1):
            if has_user and has_assistant:
                parsed_messages.append({"messages": current_messages})
            current_messages = []
            current_time = timestamp
            has_user = has_assistant = False

        current_messages.append({"role": role, "content": content})
        if role == "user":
            has_user = True
        else:
            has_assistant = True

    if has_user and has_assistant:
        parsed_messages.append({"messages": current_messages})

    return parsed_messages

def clean_chat_history(input_file_path, output_file_path, user_name):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        chat_history = json.load(file)

    parsed_messages = parse_chat_to_json(chat_history, user_name)

    output_file_path = output_file_path.rstrip('.json') + '.jsonl'

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for message_group in parsed_messages:
            if message_group['messages']:  
                json.dump(message_group, file, ensure_ascii=False)
                file.write('\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clean_chat_history.py <input_file_path> <output_file_path> <user_name>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    user_name = sys.argv[3]
    clean_chat_history(input_file_path, output_file_path, user_name)
