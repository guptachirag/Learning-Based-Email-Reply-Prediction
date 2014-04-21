import email
from bs4 import BeautifulSoup
import EmailFetcher as ef
from pprint import pprint
interrogative_words=["could", "when", "where","how"]
negative_words=["unsubscribe","no-reply","noreply","mailer"]

def words_present(all_text,keyword_list):   #checks if any word in all_text is present in keyword_list
    if any(word in all_text for word in keyword_list):
        return True
    return False

def extract_text( email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()

def parseEmail(emailString):
    message = email.message_from_string(emailString)

    feature={}
    feature["From"]=email.utils.parseaddr(message['From'])[1]
    feature["Subject"]=message['Subject']
    feature["is_automated_mail"]=words_present(feature["From"],negative_words)
    emailText = extract_text(message)

    print "From : " +   feature["From"]
    print "To : " + message['To']
    print "Subject : " + message['Subject']
    print "TEXT BODY : "
    if emailText != None:
        emailText = BeautifulSoup(emailText).get_text()
        print emailText
        #feature["emailText"]=emailText
        feature["is_interrogative_text"]=words_present(emailText,interrogative_words)
    else:
        feature["is_interrogative_text"]=False

    return feature


def read_from_disk(directory):
    emails = []
    for i in range(1,ef.Num_MAIL):
        print "\n\n----------------------------------------- Processing mail no:%d --------------------\n"%(i)
        try:
            f = open('%s/%s.eml' %(directory, i), 'r')
            data=f.read()
            f.close()
            emails.append(parseEmail(data))
        except:
            return emails
    return emails

def extractFeatures():
    inboxEmails_feature = read_from_disk(ef.INBOX_DIRECTORY)
    sentEmails_feature = read_from_disk(ef.SENT_DIRECTORY)
    for i in inboxEmails_feature:
        print "\n\n-----------------------------------------------------------\n"
        pprint(i)
