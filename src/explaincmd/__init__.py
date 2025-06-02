import argparse
import configparser
import os
import sys
from pathlib import Path

from openai import OpenAI

# ... (rest of the code remains the same)

CONFIG_DIR = Path.home() / '.config' / 'explaincmd'
CONFIG_FILE = CONFIG_DIR / 'config.ini'
def get_api_key():
    if CONFIG_FILE.exists():
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        return config['DEFAULT']['api_key']
    return os.environ.get('OPENAI_API_KEY')

def setup_config(api_key):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'api_key': api_key}
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
    print(f"API key saved to {CONFIG_FILE}")


def query_gpt4(prompt):
    api_key = get_api_key()
    if not api_key:
        print("Error: OpenAI API key not found. Please set it using 'explaincmd --setup YOUR_API_KEY'")
        sys.exit(1)

    client = OpenAI(api_key=get_api_key())


    try:
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a silent assitant that just outputs minimal ASCII explanations. Nothign more."},
            {"role": "user", "content": "explain command lsof -i :3412 | awk 'NR>1 {print $2}' | xargs kill -9"},
            {"role": "assistant", "content": (
                "lsof -i :3412 | awk 'NR>1 {print $2}' | xargs kill -9\n"
                "│    │         │     │                │       │\n"
                "│    │         │     │                │       └─ signal 9 (SIGKILL - no mercy)\n"
                "│    │         │     │                └─ x = execute, args = arguments\n" 
                "│    │         │     └─ NR = Number of Records (skip header)\n"
                "│    │         └─ awk = \"Aho, Weinberger, Kernighan\" (text processing)\n"
                "│    └─ -i = internet connections\n"
                "└─ ls + of = \"list open files\""
            )},
            {"role": "user", "content": f"explain command {prompt}"}
        ],
        max_tokens=300)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: API request failed. {str(e)}")
        sys.exit(1)



def main():
    parser = argparse.ArgumentParser(description="Get UNIX commands from text explanations using AI")
    parser.add_argument('--setup', metavar='API_KEY', help='Setup OpenAI API key')
    parser.add_argument('query', nargs=argparse.REMAINDER, help='The task description to get a UNIX command for (everything after --setup will be treated as the query)')
    args = parser.parse_args()

    if args.setup:
        setup_config(args.setup)
        print("API key set successfully.")
    elif args.query:
        query = ' '.join(args.query)
        suggested_command = query_gpt4(query)
        print(suggested_command)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()