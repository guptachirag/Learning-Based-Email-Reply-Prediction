import imaplib
import email

def printEmail(emailString):
    message = email.message_from_string(emailString)
    print "From : " + message['From']
    print "To : " + message['To']
    print "Subject : " + message['Subject']
    print "TEXT BODY : "
    if message.is_multipart():
        for payload in message.get_payload():
            print payload.get_payload()
    else:
        print message.get_payload()
        

def printInboxEmails(imap):
    status,data = imap.select("INBOX")
    
    if status == 'OK' :
        status,data = imap.search(None,"ALL")
        emailIds = data[0].split()
        for i in range(-1,-11,-1):
            status,data = imap.fetch(emailIds[i], "(RFC822)")
            printEmail(data[0][1])
        

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
    
