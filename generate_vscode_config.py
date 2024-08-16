import os
import json
import platform

def create_tasks_json(subfolder=""):
    tasks = {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "build",
                "type": "shell",
                "command": "make",
                "group": {
                    "kind": "build",
                    "isDefault": True
                },
                "problemMatcher": "$gcc",
                "options": {
                    "cwd": os.path.join("${workspaceFolder}", subfolder)
                }
            }
        ]
    }
    return tasks

def create_launch_json(subfolder="", program_name=None, include_program=True):
    # Determine the debugger mode (gdb for Linux, lldb for macOS)
    debugger = "gdb" if platform.system() == "Linux" else "lldb"
    
    configurations = {
        "name": f"({debugger}) Launch",
        "type": "cppdbg",
        "request": "launch",
        "program": os.path.join("${workspaceFolder}", subfolder, program_name) if include_program and program_name else "${workspaceFolder}/<your_program_name>",
        "args": ["${input:programArgs}"],
        "stopAtEntry": False,
        "cwd": os.path.join("${workspaceFolder}", subfolder),
        "environment": [],
        "externalConsole": False,
        "MIMode": debugger,
        "setupCommands": [
            {
                "description": "Enable pretty-printing for lldb" if debugger == "lldb" else "Enable pretty-printing for gdb",
                "text": "settings set target.auto-var-init true" if debugger == "lldb" else "-enable-pretty-printing",
                "ignoreFailures": True
            }
        ],
        "preLaunchTask": "build"
    }

    launch = {
        "version": "0.2.0",
        "configurations": [configurations],
        "inputs": [
            {
                "id": "programArgs",
                "type": "promptString",
                "description": "Enter the program arguments (space-separated)",
                "default": ""
            }
        ]
    }
    return launch

def write_json_file(directory, filename, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as f:
        json.dump(content, f, indent=4)

def main():
    subfolder = input("Enter the subfolder for your project (leave blank if none): ").strip()
    include_program = input("Do you want to include the program name in the launch.json? (yes/no): ").strip().lower() == "yes"
    program_name = None
    if include_program:
        program_name = input("Enter the name of your program (e.g., 'push_swap'): ").strip()

    tasks_json = create_tasks_json(subfolder)
    launch_json = create_launch_json(subfolder, program_name, include_program)

    vscode_dir = os.path.join(".vscode")
    write_json_file(vscode_dir, "tasks.json", tasks_json)
    write_json_file(vscode_dir, "launch.json", launch_json)

    print(f"Configuration files have been generated in the {vscode_dir} directory.")

if __name__ == "__main__":
    main()
