from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors


###scope
SCOPES = ["https://www.googleapis.com/auth/gmail.metadata"]

def main():
    creds = None


    #####gets/stores credentials for use later
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    ####used for most of the heavy lifting
    service = build('gmail', 'v1', credentials=creds)

    query = input("Type in the email address to search/delete for:")
    try:
        response = service.users().threads().list(userId='me', q=query).execute()
        threads = []

        if 'threads' in response:
            threads.extend(response['threads'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().threads().list(userId=user_id, q=query,
                                            pageToken=page_token).execute()
            threads.extend(response['threads'])

        for i in range(0,len(threads)):
            print(threads[i]["id"])
    except errors.HttpError as error:
        print("An error occured %s" %error)
if __name__ == '__main__':
    main()