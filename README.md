### Visual Studio Code Configuration Script

This Python script generates configuration files for debugging multi-file C projects in Visual Studio Code.

The script creates two configuration files:
1. **tasks.json**: Defines the build task to compile the C project using `make`.
2. **launch.json**: Configures the debugger with the ability to prompt for command-line arguments each time you start debugging.

### How to Use the Script

1. **Run the Script**:
   Execute the script using Python. Open a terminal, navigate to the directory where the script is located, and run:
   ```bash
   python3 generate_vscode_config.py
