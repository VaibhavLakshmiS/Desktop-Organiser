#The **Desktop Organiser Tool** is a Python script that helps you tidy up your cluttered desktop
![Demo](desktop.gif)

The **Desktop Organiser Tool** is a Python script that helps you tidy up your cluttered desktop or download directory by automatically organizing files into predefined categories. This tool allows you to perform a dry run to preview the organization before making any changes or customize the organization based on your preferences.

## Features

- Organises files on your desktop or download directory into predefined categories.
- Provides a dry run option to preview the organization without making changes.
- Customizable: You can choose specific categories to organize and the target location.
- Checks if the directory is already organized and prompts before proceeding.
- Logging: Records the organization process in a log file for reference.

## Requirements

- Python 3.5 or higher
- A `config.json` file with predefined categories

## Getting Started

1. Clone this repository to your local machine:
-2.Create a config.json file with predefined categories.
See Sample config.json.
-3.Run the script:
-bash
-python organizer.py

Usage
Select a Mode:

Dry Run: Preview the organization without making changes.
Customizable: Choose specific categories and target location for organization.
Exit: Terminate the program.
Choose the Target Location:

Desktop
Downloads
Custom: Enter the full path to your custom directory.
Follow the prompts to customize the organization or perform a dry run.

If the directory is already organized, you'll be prompted to confirm before proceeding.

Review the organization and decide whether to proceed with the actual organization.

The tool will move and rename files based on your selections

Enjoy using it to have cluttered free desktop space and more ! 

Note: This tool is still in development ( Adding more features to make it more user intuitive stay tuned ! ) 
