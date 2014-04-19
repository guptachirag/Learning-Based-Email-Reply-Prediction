import imaplib
import email
from bs4 import BeautifulSoup

<<<<<<< HEAD
INBOX_DIRECTORY="email\inbox"   #Path where Inbox emails are saved
SENT_DIRECTORY="email\sent"  #Path where Sent emails are saved
=======
OUTPUT_DIRECTORY="email" #Path where emails are saved
>>>>>>> 1c00f155520d4059b5cd170d73060def55c4dc6b
Num_MAIL=20  #Number of mails to save on disk

def extract_text( email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()
    
def printEmail(emailString):
    message = email.message_from_string(emailString)
    print "From : " + message['From']
    print "To : " + message['To']
    print "Subject : " + message['Subject']
    print "TEXT BODY : "
    emailText = extract_text(message)
    if emailText != None:
        emailText = BeautifulSoup(emailText).get_text()
    print emailText

<<<<<<< HEAD
def saveToFolder(num,data,directory):
    f = open('%s/%s.eml' %(directory, -num), 'wb')
=======
def saveToFolder(num,data):
    f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, -num), 'wb')
>>>>>>> 1c00f155520d4059b5cd170d73060def55c4dc6b
    f.write(data)
    f.close()

def saveEmails(imap,mailbox):
    status,data = imap.select(mailbox)
    
    if status == 'OK' :
        status,data = imap.search(None,"ALL")
        emailIds = data[0].split()

        for i in range(-1,-Num_MAIL,-1):
            rv,mail = imap.fetch(emailIds[i], "(RFC822)")
            if rv != 'OK' :
                print "ERROR getting message", -i
                return
            #printEmail(mail[0][1])
            if mailbox == "INBOX":
                saveToFolder(i,mail[0][1],INBOX_DIRECTORY)
            elif mailbox == "[Gmail]/Sent Mail":
                saveToFolder(i,mail[0][1],SENT_DIRECTORY)
    else :
        print "Unable to access ",mailbox

def login():
    username = raw_input("Enter emailid : ")
    password = raw_input("Enter password : ")
    imap = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        imap.login(username,password)
    except imaplib.IMAP4.error:
        print "LOGIN FAILED... "

    status,mailboxes = imap.list()
    #print status,mailboxes
    saveEmails(imap,"INBOX")
    saveEmails(imap,"[Gmail]/Sent Mail")
    imap.logout()
