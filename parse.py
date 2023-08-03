import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate_google_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def list_files_with_details(service):
    try:
        response = service.files().list(fields='files(id, name, mimeType, owners, permissions)').execute()
        files = response.get('files', [])
        return files
    except Exception as e:
        print(f"An error occurred while listing files: {str(e)}")
        return []

def main():
    creds = authenticate_google_drive()
    service = build('drive', 'v3', credentials=creds)

    files = list_files_with_details(service)
    output_data = []

    for file_info in files:
        file_name = file_info['name']
        file_type = file_info['mimeType']
        owners = [owner['displayName'] for owner in file_info['owners']]
        permissions = file_info.get('permissions', [])
        shared_with = {}
        for perm in permissions:
            role = perm['role']
            user_email = perm.get('emailAddress', 'Unknown User')
            if perm['type'] == 'user':
                shared_with.setdefault(role, []).append(user_email)
            elif perm['type'] == 'domain':
                shared_with.setdefault(f"{role} (Organization)", []).append(user_email)

        file_details = {
            'File Name': file_name,
            'File Type': file_type,
            'Owner(s)': owners,
            'Shared With': shared_with
        }
        output_data.append(file_details)

    print(json.dumps(output_data, indent=2))

    export_option = input("\nDo you want to export the list as a JSON file? (yes/no): ").lower()
    if export_option == 'yes':
        try:
            with open('files_details.json', 'w') as file:
                json.dump(output_data, file, indent=2)
            print("Data exported to 'files_details.json'")
        except Exception as e:
            print(f"An error occurred while exporting data: {str(e)}")

if __name__ == '__main__':
    main()
