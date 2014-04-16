import imaplib
import email
from bs4 import BeautifulSoup

OUTPUT_DIRECTORY="email" #Path where emails are saved
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

def saveToFolder(num,data):
    f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, -num), 'wb')
    f.write(data)
    f.close()

def read_from_disk():
    for i in range(1,Num_MAIL):
        print "\n\n----------------------------------------- Processing mail no:%d --------------------\n"%(i)
        f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, i), 'r')
        data=f.read()
        f.close()
        printEmail(data)

def saveInboxEmails(imap):
    status,data = imap.select("INBOX")

    if status == 'OK' :
        status,data = imap.search(None,"ALL")
        emailIds = data[0].split()

        for i in range(-1,-Num_MAIL,-1):
            rv,mail = imap.fetch(emailIds[i], "(RFC822)")
            if rv != 'OK' :
                print "ERROR getting message", i
                return
            #printEmail(mail[0][1])
            saveToFolder(i,mail[0][1])

def login():
    username = raw_input("Enter emailid : ")
    password = raw_input("Enter password : ")
    imap = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        imap.login(username,password)
    except imaplib.IMAP4.error:
        print "LOGIN FAILED... "

    status,mailboxes = imap.list()
    saveInboxEmails(imap)
    imap.logout()

def main() :
    login()
    read_from_disk()

main()
    
