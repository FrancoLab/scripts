import sys
iimport os


def rename_items(directory):
    """
    Recursively rename all files and folders to lowercase with spaces replaced by underscores.
    Traverses depth-first to handle nested directories properly.
    """
    # Get all items in the current directory
    try:
        items = os.listdir(directory)
    except PermissionError:
        print(f"Permission denied: {directory}")
        return
    except Exception as e:
        print(f"Error accessing {directory}: {e}")
        return

    # First, process all files in the current directory
    for item in items:
        current_path = os.path.join(directory, item)

        # Skip if it's a directory (we'll handle directories in the second pass)
        if os.path.isdir(current_path):
            continue

        # Create the new name (lowercase with spaces replaced by underscores)
        new_name = item.lower().replace(' ', '_')

        # Skip if the name is already in the desired format
        if new_name == item:
            continue

        new_path = os.path.join(directory, new_name)

        try:
            # Rename the file
            os.rename(current_path, new_path)
            print(f"Renamed file: {current_path} -> {new_path}")
        except Exception as e:
            print(f"Error renaming {current_path}: {e}")

    # Now get the updated list of items (some may have been renamed)
    try:
        items = os.listdir(directory)
    except Exception as e:
        print(f"Error accessing {directory} after file renaming: {e}")
        return

    # Process all directories in the current directory
    for item in items:
        current_path = os.path.join(directory, item)

        if os.path.isdir(current_path):
            # First, recursively process the contents of this directory
            rename_items(current_path)

            # Then rename the directory itself
            new_name = item.lower().replace(' ', '_')

            # Skip if the name is already in the desired format
            if new_name == item:
                continue

            new_path = os.path.join(directory, new_name)

            try:
                # Rename the directory
                os.rename(current_path, new_path)
                print(f"Renamed directory: {current_path} -> {new_path}")
            except Exception as e:
                print(f"Error renaming directory {current_path}: {e}")


def main():
    # Use the current directory if no directory is specified
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
    else:
        root_directory = os.getcwd()

    print(f"Starting renaming process in: {root_directory}")
    print("This will convert all folder and file names to lowercase and replace spaces with underscores.")

    # Ask for confirmation before proceeding
    confirmation = input("Do you want to continue? (y/n): ")
    if confirmation.lower() != 'y':
        print("Operation cancelled.")
        return

    # Start the renaming process
    rename_items(root_directory)
    print("Renaming process completed.")


if __name__ == "__main__":
    main()
