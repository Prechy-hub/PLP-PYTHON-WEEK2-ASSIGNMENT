import os

def read_and_write_file(input_file: str, output_file: str):
    """
    Reads the content of input_file, modifies it, and writes it to output_file.
    Modification: Converts all text to uppercase.
    """
    try:
        with open(input_file, "r") as f:
            content = f.read()

        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def error_handling_lab(base_dir: str):
    """
    Prompts the user for a filename and attempts to read it.
    Handles errors gracefully if the file doesn't exist or can't be read.
    Always looks for the file inside the same folder as file-handling.py
    """
    filename = input("Enter the filename to read: ")
    filepath = os.path.join(base_dir, filename)

    try:
        with open(filepath, "r") as f:
            content = f.read()
            print("File content:\n")
            print(content)

    except FileNotFoundError:
        print(f"Error: File '{filename}' does not exist in {base_dir}.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Get the directory where file-handling.py is located
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Build file paths relative to the script location
    input_path = os.path.join(BASE_DIR, "input.txt")
    output_path = os.path.join(BASE_DIR, "output.txt")

    # Part 1: File Read & Write Challenge
    read_and_write_file(input_path, output_path)

    # Part 2: Error Handling Lab
    error_handling_lab(BASE_DIR)