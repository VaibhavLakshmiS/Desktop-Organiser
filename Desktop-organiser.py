# Import necessary libraries 
import os
import json
import logging
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Desktop Organizer")
root.geometry("300x250")

# Desktop path 
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')


if not os.path.exists("config.json"):
    print("Error: config.json not found.")
    exit()

# Loading the details from config.json 
with open("config.json", "r") as file:
    file_categories = json.load(file)
# creates the log 
logging.basicConfig(filename="organizer.log", level=logging.INFO, format='%(asctime)s - %(message)s')

# this function helps to recognise files with same name and adds a numeric value to distinguish them 

def move_with_rename(source, destination):
    if source == destination:
        return

    base, extension = os.path.splitext(destination)
    count = 1

    while os.path.exists(destination) and source != destination:
        destination = "%s (%d)%s" % (base, count, extension)
        count += 1

    os.rename(source, destination)
    logging.info("Moved %s to %s" % (source, destination))

# this function helps to organise the files or if the dry run mode is selected it will tell its intended action 

def organize(directory, dry_run=True, selected_categories=None):
    for root, dirs, files in os.walk(directory, topdown=True):
        # Skip already categorized files
        if any(category in root for category in file_categories):
            continue
        
        for filename in files:
            filepath = os.path.join(root, filename)
            
            for category, extensions in file_categories.items():
                if selected_categories and category not in selected_categories:
                    continue
                
                if any(filename.endswith(ext) for ext in extensions):
                    folder_path = os.path.join(directory, category)
                    
                    # Create folder if it doesn't exist and it's not a dry run
                    if not os.path.exists(folder_path) and not dry_run:
                        os.mkdir(folder_path)
                    
                    new_filepath = os.path.join(folder_path, filename)

                    # Print the intended action using old-style string formatting
                    if dry_run:
                        print("Intend to move %s to %s" % (filename, folder_path))
                    else:
                        print("Moved %s to %s" % (filename, folder_path))
                        move_with_rename(filepath, new_filepath)

def seems_organized(directory):
    #"""Check if the directory seems to be organized based on the categories."""
    subdirectories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    organized_categories = [cat for cat in file_categories if cat in subdirectories]
    
    for cat, extensions in file_categories.items():
        for ext in extensions:
            for file in os.listdir(directory):
                if file.endswith(ext) and cat not in organized_categories:
                    return False  # Found a mismatch, directory doesn't seem organized
    return True
def choose_option():
    print("\nSelect the target location:")
    print("1) Desktop")
    print("2) Downloads")
    print("3) Custom")
    choice = input("Enter the number of your choice: ")

    directory = None
    if choice == "1":
        directory = desktop_path
    elif choice == "2":
        directory = downloads_path
    elif choice == "3":
        directory = input("Enter the full path to your custom directory: ")
    else:
        print("Invalid choice.")
        return choose_option()

    # Check if the directory exists
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return choose_option()
    return directory

def organize_directory(directory, dry_run_mode=True):
    try:
        organize(directory, dry_run=dry_run_mode)
        if dry_run_mode:
            messagebox.showinfo("Dry Run Complete", "Review the console for the dry run actions.")
        else:
            messagebox.showinfo("Organization Complete", "Files have been organized!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def start_dry_run():
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        organize_directory(directory, dry_run_mode=True)

def start_organize():
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        organize_directory(directory, dry_run_mode=False)
label = tk.Label(root, text="Desktop Organizer", font=("Arial", 16))
label.pack(pady=20)

btn_dry_run = tk.Button(root, text="Start Dry Run", command=start_dry_run)
btn_dry_run.pack(pady=10)

btn_organize = tk.Button(root, text="Organize", command=start_organize)
btn_organize.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=root.destroy)
btn_exit.pack(pady=20)
root.mainloop()
def main():
    while True:  # Main loop to keep the program running until the user chooses to exit.
        print("\nSelect a mode:")
        print("1) Dry Run")
        print("2) Customizable")
        print("3) Exit")
        mode = input("Enter the number of your choice: ")

        if mode == "3":
            print("Exiting...")
            break  # This will exit the while loop and end the program.

        directory = choose_option()

        if mode == "1":
            if seems_organized(directory):
                proceed = input("The directory seems already organized. Do you still want to proceed? (yes/no): ").strip().lower()
                if proceed != 'yes':
                    continue  # Skips to the next iteration of the loop, i.e., back to the menu.
            organize(directory, dry_run=True)
            proceed = input("\nDry run complete. Would you like to proceed with the actual organization? (yes/no): ").strip().lower()
            if proceed == 'yes':
                organize(directory, dry_run=False)
        elif mode == "2":
            categories = list(file_categories.keys())
            print("\nAvailable categories:")
            for idx, category in enumerate(categories, 1):
                print("%d) %s" % (idx, category))
            selected = input("Enter the numbers of the categories (comma-separated): ").split(',')
            selected_categories = [categories[int(i)-1] for i in selected]
            if seems_organized(directory):
                proceed = input("The directory seems already organized. Do you still want to proceed? (yes/no): ").strip().lower()
                if proceed != 'yes':
                    continue  # Skips to the next iteration of the loop.
            organize(directory, dry_run=False, selected_categories=selected_categories)

if __name__ == '__main__':
    main()
