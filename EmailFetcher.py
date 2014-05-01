import imaplib

INBOX_DIRECTORY="email\inbox"   #Path where Inbox emails are saved
SENT_DIRECTORY="email\sent"  #Path where Sent emails are saved
Num_MAIL=21  #Number of mails to save on disk

def saveToFolder(num,data,directory):
    f = open('%s/%s.eml' %(directory, -num), 'wb')
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
            #parseEmail(mail[0][1])
            if mailbox == "INBOX":
                saveToFolder(i,mail[0][1],INBOX_DIRECTORY)
            elif mailbox == "[Gmail]/Sent Mail":
                saveToFolder(i,mail[0][1],SENT_DIRECTORY)
    else :
        print "Unable to access ",mailbox

def login(username,password):
    #username = raw_input("Enter emailid : ")
    #password = raw_input("Enter password : ")
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
