import os
import re
import sys
import json
from datetime import datetime, timedelta

def is_unnecessary_content(content):
    """
    Checks if the message content is an automatic reaction message or similar unnecessary content.
    """
    unnecessary_patterns = [
    re.compile(r"reaccion\w*\s+.*\s*a tu mensaje", re.IGNORECASE),
    re.compile(r"reacted\s+.*\s*to your message", re.IGNORECASE),
    # Adjusted pattern to capture encoding artifacts and broader range of characters
    re.compile(r"reaccion[oó]\s+[\s\S]*?\s*a tu mensaje", re.IGNORECASE),
]
    return any(pattern.search(content) for pattern in unnecessary_patterns)

def clean_content(content):
    """
    Cleans the message content by removing URLs, emojis, non-word characters, and unnecessary content.
    """
    if is_unnecessary_content(content):
        return ""

    content = re.sub(r'http\S+', '', content)  # Remove URLs
    content = re.sub(r'[^\w\s]', '', content)  # Remove emojis and non-text characters
    return content.strip()

def parse_chat_to_json(input_data):
    """
    Parses the given Instagram chat history data into a list of messages grouped by time periods,
    ensuring each period contains at least one message from each participant if possible.

    Args:
    input_data (dict): The chat history as a dictionary.

    Returns:
    list: A list of dictionaries, each containing a group of messages.
    """
    messages = input_data['messages']
    participants = {p['name']: "user" if "kohei" not in p['name'].lower() else "assistant" for p in input_data['participants']}
    parsed_messages = []

    current_time = None
    current_messages = []
    has_user = has_assistant = False

    for message in reversed(messages):  # Instagram messages are in reverse chronological order
        sender_name = message['sender_name']
        content = message.get('content', '')
        timestamp_ms = message['timestamp_ms']
        role = participants.get(sender_name, "user")

        # Clean content
        content = clean_content(content)
        if not content:  # Skip empty, whitespace-only, or unnecessary messages
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
