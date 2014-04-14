import imaplib
import email
from bs4 import BeautifulSoup
OUTPUT_DIRECTORY="C:\Users\Vaseem\Documents\GitHub\Fetch-Email-Using-IMAP\email"

def printEmail(emailString):
    message = email.message_from_string(emailString)
    print "From : " + message['From']
    print "To : " + message['To']
    print "Subject : " + message['Subject']
    print "TEXT BODY : "
    if message.is_multipart():
        for payload in message.get_payload():
            soup = BeautifulSoup(payload.get_payload())
            print soup.get_text()
            print "--------------------"
            print payload.get_payload()
    else:
        soup = BeautifulSoup(message.get_payload())
        print soup.get_text()
        print "--------------------"
        print message.get_payload()
        
def saveToFolder(num,data):
    f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, num), 'wb')
    f.write(data)
    f.close()

def printInboxEmails(imap):
    status,data = imap.select("INBOX")
    
    if status == 'OK' :
        status,data = imap.search(None,"ALL")
        emailIds = data[0].split()
        for i in range(-1,-2,-1):
            rv,data = imap.fetch(emailIds[i], "(RFC822)")
            if rv != 'OK' :
                print "ERROR getting message", i
                return
            printEmail(data[0][1])
            saveToFolder(i,data[0][1])
        

def fetch(username,password):
    imap = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        imap.login(username,password)
    except imaplib.IMAP4.error:
        print "LOGIN FAILED... "

    status,mailboxes = imap.list()
    printInboxEmails(imap);
    imap.logout()
    

def main() :
    username = raw_input("Enter emailid : ")
    password = raw_input("Enter password : ")
    fetch(username,password)

main()
    
