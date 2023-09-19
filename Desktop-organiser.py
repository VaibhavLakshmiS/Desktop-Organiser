import os

# Path to the Desktop
# desktop_path = os.path.expanduser("~\\Desktop")
desktop_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# Categories for files and their extensions
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Docs': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Music': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mkv', '.mov'],
}

def organize(directory, dry_run=True, selected_categories=None):
    """
    Move files into categorized folders.
    """
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # If it's a file, check its category and move it
        if os.path.isfile(filepath):
            for category, extensions in file_categories.items():
                if selected_categories and category not in selected_categories:
                    continue

                if any(filename.endswith(ext) for ext in extensions):
                    folder_path = os.path.join(directory, category)

                    # Make folder if it doesn't exist
                    if not os.path.exists(folder_path) and not dry_run:
                        os.mkdir(folder_path)

                    # New path for the file
                    new_filepath = os.path.join(folder_path, filename)

                    # Print the intended action
                    print(f'{"Intend to" if dry_run else "Moved"} move {filename} to {folder_path}')

                    # Move the file, unless it's a dry run
                    if not dry_run:
                        os.rename(filepath, new_filepath)

if __name__ == '__main__':
    print("Select a mode:")
    print("1) Dry Run")
    print("2) Customizable")
    
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        organize(desktop_path)
    elif choice == "2":
        categories = list(file_categories.keys())
        print("Available categories:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}) {category}")
        selected = input("Enter the numbers of the categories you want to organize (comma-separated): ").split(',')
        selected_categories = [categories[int(i)-1] for i in selected]
        
        directory_choice = input(f"Do you want to organize the Desktop or another directory? (D for Desktop, enter the path for another directory): ")
        if directory_choice == 'D':
            directory_choice = desktop_path

        dry_run_choice = input("Do you want to perform a dry run? (Y/N): ").upper() == 'Y'
        
        organize(directory_choice, dry_run=dry_run_choice, selected_categories=selected_categories)
