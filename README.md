### Visual Studio Code Configuration Script

This Python script generates configuration files for debugging multi-file C projects in Visual Studio Code.

The script creates two configuration files:
1. **tasks.json**: Defines the build task to compile the C project using `make`.
2. **launch.json**: Configures the debugger with the ability to prompt for command-line arguments each time you start debugging.

### How to Use the Script

1. **Enable Breakpoints**:
   To use breakpoints effectively, ensure that the compiler generates debugging information by adding the `-g` flag to your 
   compilation flags. Update your Makefile's `CFLAGS (or equivalent)` line like this:
   ```bash
   CFLAGS = -Wall -Wextra -Werror -g
2. **Run the Script**:
   Execute the script using Python. Open a terminal, navigate to the directory where the script is located, and run:
   ```bash
   python3 generate_vscode_config.py
3. **Compile and Debug**:
   After the script generates the `tasks.json` and `launch.json` files, press `F5` in Visual Studio Code. This will:

   * Trigger the build task, compiling the project using the make command.
   * Start the debugger, prompting you to enter any required command-line arguments.
   * Begin the debugging session, where you can use breakpoints to inspect the code's execution.

### Note

This script has been tested and confirmed to work on both macOS and Linux environments. Ensure that your system has the necessary development tools installed, such as make, a C compiler (e.g., gcc), and Python 3. While the script is designed to generate Visual Studio Code configuration files, it may require additional adjustments if you're using a different operating system.
