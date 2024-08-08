import os, sys

def iterate_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print("The directory does not exist.")
        return

    # Check if the path is indeed a directory
    if not os.path.isdir(directory):
        print("The provided path is not a directory.")
        return

    # List all files and directories in the provided directory
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            print("File:", filename)
            print("Directory:", filename)

def main():
    if len(sys.argv) > 1:
        for index, arg in enumerate(sys.argv[1:]):
            print(f"Iterating files in {index + 1}: {arg}")
            iterate_files(arg)
    else:
        print("No additional arguments passed to the script.")

if __name__ == "__main__":
    main()