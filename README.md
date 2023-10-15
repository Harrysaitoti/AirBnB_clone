Command Interpreter Description
Purpose: The command interpreter is a program that provides a command-line interface for users to interact with the system. It interprets user commands and executes corresponding actions.

How to Start It
Interactive Mode:

Open your terminal or command prompt.
Navigate to the directory where the command interpreter script is located.
Type ./interpreter.py (replace interpreter.py with the actual name of your interpreter script).
Press Enter.
You will see a prompt indicating that the interpreter is ready to accept commands.
Non-Interactive Mode:

You can run the interpreter in non-interactive mode by piping commands through the terminal.
For example, you can use echo "command" | ./interpreter.py to execute a single command.
How to Use It
Once the command interpreter is started, you can use it in the following ways:

Interactive Mode:

You'll be presented with a prompt (e.g., (hbnb)) indicating that the interpreter is ready to accept commands.
Type a command and press Enter to execute it.
The interpreter will process the command and provide output accordingly.
To exit the interpreter, type quit and press Enter.
Non-Interactive Mode:

You can pass a series of commands through stdin (standard input) from a file or using echo.
The interpreter will execute each command sequentially and provide output as needed.
The interpreter will automatically exit once all commands have been processed.

Examples
Interactive Mode:
./interpreter.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit


Non-Interactive Mode:
$ echo "help" | ./interpreter.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
cat test_commands
help
quit

cat test_commands | ./interpreter.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
