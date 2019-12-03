from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
import sys


###scope
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
FILE_NAME = "emails.txt"


def getThreadIds(service,query):
    try:
        response = service.users().threads().list(userId='me', q=query).execute()
        threads = []

        if 'threads' in response:
            threads.extend(response['threads'])
        ####if there are more from the same sender on other pages
        ###do until there are no next page tokens left
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().threads().list(userId='me', q=query,
                                            pageToken=page_token).execute()
            threads.extend(response['threads'])
        return threads
    except errors.HttpError as error:
        print("An error occured %s" %error)
def moveThreadsToTrash(service,threads):
    found = False
    for i in range(0,len(threads)):
        try:
            service.users().threads().trash(userId='me',id = (threads[i]["id"])).execute()
            found = True
        except Exception as e:
            print(e)
            return False
    return [True,found]



    
    
    


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

    #####get a bunch of senders
    run  = False
    email_list = [line.rstrip('\n') for line in open(FILE_NAME)]
    if len(email_list) >0:
        run = True
        for i in range(0,len(email_list)):
            query = email_list[i]
            return_threads = getThreadIds(service,query)
            
            success = moveThreadsToTrash(service,return_threads)
            if(success):
                if success[1]:
                    print("Threads successfully moved to trash for " +query)
                else:
                    print("No threads found")
            else:
                print("Threads not successfully removed for sender: " +query)
    if not run:
        print("Nothing in the emails.txt file to delete emails for.")
    
    
if __name__ == '__main__':
    main()