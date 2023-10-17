#!/usr/bin/python3
import sys


def display_prompt():
    print("(hbnb)", end=" ")


def process_command(command):
    if command == 'help':
        print("\nDocumented commands (type help <topic>):")
        print("=" * 40)
        print("EOF  help  quit\n")
    elif command == 'quit':
        sys.exit()


def interactive_mode():
    while True:
        display_prompt()
        command = input()
        process_command(command)


def non_interactive_mode(commands):
    for command in commands:
        process_command(command)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        commands = [line.strip() for line in sys.stdin]
        non_interactive_mode(commands)
    else:
        interactive_mode()

