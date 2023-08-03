# Spine - Lists Google Drive Files and Info

Spine is a Python script that allows you to parse through your Google Drive files and export the data in JSON format. With Spine, you can quickly list all your files, identify shared files, view permissions, and export the information for further analysis or sharing.

## Installation

To get started with Spine, follow these steps:

* Clone this project to a new directory on your local machine:
```
git clone https://github.com/your-username/spine.git
cd spine
```

### Set up a Python virtual environment to keep the dependencies isolated:
```
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### Install the required dependencies using pip from the provided requirements.txt file:
```
pip install -r requirements.txt
```

### Authentication
-----------------------------------------------------------

Before using Spine to access your Google Drive, you need to authenticate it with your Google account. Follow the instructions in the Google Drive API Python Quickstart guide to set up the necessary credentials and obtain the credentials.json file.

* Visit the Google Developers Console: https://console.developers.google.com/

* Create a new project or select an existing one.

* Enable the Google Drive API for your project.

* Create credentials for the project:

  * Go to "Credentials" in the left sidebar.
  * Click "Create credentials" and choose "OAuth client ID."
  * Select "Desktop app" as the application type.
  * Download the credentials as a JSON file and save it as credentials.json in the spine directory.

### Usage
----------------------------------------------------

Once you have set up the virtual environment and authenticated Spine with Google Drive, you are ready to use the script.

Make sure you have activated the virtual environment:
```
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

Run the Spine script:
```
python3 parse.py
```
The script will list all your Google Drive files, and it will display them with blue text if they are shared with you and green text if you are sharing them with others.

The script will also show the list of users with whom each file is shared, organized by permissions (editor, viewer).

You have the option to export the file list and permission details to a JSON file. When prompted, type 'yes' or 'no' to export the data.

If you choose to export the data, it will be saved in a file named files_details.json in the spine directory.
