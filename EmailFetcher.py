import imaplib
import FeatureExtractor as fe

INBOX_DIRECTORY="email/inbox"   #Path where Inbox emails are saved
Num_MAIL=201  #Number of mails to save on disk
MAILBOX = "[Gmail]/All Mail"


def saveToFolder(num,data,directory):
    f = open('%s/%s.eml' %(directory, -num), 'wb')
    f.write(data)
    f.close()


def saveEmails(imap):
    status,data = imap.select(MAILBOX)
    
    if status == 'OK' :
        status,data = imap.search(None,"ALL")
        emailIds = data[0].split()

        for i in range(-1,-Num_MAIL,-1):
            rv,mail = imap.fetch(emailIds[i], "(RFC822)")
            if rv != 'OK' :
                print "ERROR getting message", -i
                return
            #fe.parseEmail(mail[0][1])
            saveToFolder(i,mail[0][1],INBOX_DIRECTORY)
    else :
        print "Unable to access ",MAILBOX


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
    saveEmails(imap)
    imap.logout()
