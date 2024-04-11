"""
Update 4/11/2024:
Figured out how to retrieve emmails and their contents through IMAP and the email library. 
Next steps will be extracting relevant information into a CSV.
Todo: 
1. Log onto email and extract first email !
    -Figure out how to remotely access email
        -IMAPCLIENT !
    -Extract email contents !
    -Print it !
2. Parse email out into CSV
    -Using standard I/O?
    -Python library maybe

"""
import email
import csv
import email.policy
from imapclient import IMAPClient
HOST = "imap.mail.yahoo.com"
USERNAME = "user"
PASSWORD = "password"

#Initialize IMAP Client using user and password
with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)

    server.select_folder("INBOX", readonly=True) #Selects the INBOX folder to view
    messages = server.search(['TEXT','insurance', 'UNSEEN']) #search for all emails with the requested keyword and returns a list of message IDs matching the criteria

    #Opens a CSV writer to export the data onto a CSV file
    with open('contents.csv', 'w', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',  quoting=csv.QUOTE_MINIMAL)#CSV writer initialization

        #Loop through every email from messages list and assigns the UID to uid and the rest of the data to message_data
        for uid, message_data in server.fetch(messages, "RFC822").items():
           
            email_message = email.message_from_bytes(message_data[b"RFC822"], policy=email.policy.default) #creating a message data variable

            #iterates through the body of the message and finds only the plain text
            for part in email_message.walk():
                if(part.get_content_type() == "text/plain"):
                    print("1 \n")
                    print(uid, email_message.get("From"))
                    print(part)
                    
            spamwriter.writerow([str(uid),email_message.get("From"),email_message.get("Subject")])
            #print(uid, email_message.get("From"), email_message.get("Subject"))

