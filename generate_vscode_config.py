import os
import json

def create_tasks_json(subfolder=""):
    tasks = {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "build",
                "type": "shell",
                "command": "make",
                "options": {
                    "cwd": f"${{workspaceFolder}}/{subfolder}".rstrip('/')
                },
                "group": {
                    "kind": "build",
                    "isDefault": True
                },
                "problemMatcher": "$gcc"
            }
        ]
    }
    
    os.makedirs(".vscode", exist_ok=True)
    with open(".vscode/tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def create_launch_json(subfolder="", program_name=None, include_program=True):
    launch = {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "(gdb) Launch",
                "type": "cppdbg",
                "request": "launch",
                "program": f"${{workspaceFolder}}/{subfolder}/{program_name}".rstrip('/') if include_program else "",
                "args": [
                    "${input:programArgs}"
                ],
                "stopAtEntry": False,
                "cwd": f"${{workspaceFolder}}/{subfolder}".rstrip('/'),
                "environment": [],
                "externalConsole": False,
                "MIMode": "gdb",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": True
                    }
                ],
                "preLaunchTask": "build" if include_program else ""
            }
        ],
        "inputs": [
            {
                "id": "programArgs",
                "type": "promptString",
                "description": "Enter the program arguments (space-separated)",
                "default": ""
            }
        ]
    }
    
    with open(".vscode/launch.json", "w") as f:
        json.dump(launch, f, indent=4)

def main():
    subfolder = input("Enter the subfolder containing Makefile (relative to workspace, leave empty if in root): ").strip()
    include_program = input("Include program name in launch configuration? (y/n): ").strip().lower() == 'y'
    program_name = input("Enter the output binary name (e.g., test): ").strip() if include_program else ""
    
    create_tasks_json(subfolder=subfolder)
    create_launch_json(subfolder=subfolder, program_name=program_name, include_program=include_program)

    print("VS Code configuration files generated successfully!")

if __name__ == "__main__":
    main()
