import EmailFetcher as ef

def read_from_disk(directory):
    emails = []
    for i in range(1,ef.Num_MAIL):
        print "\n\n----------------------------------------- Processing mail no:%d --------------------\n"%(i)
        f = open('%s/%s.eml' %(directory, i), 'r')
        data=f.read()
        f.close()
        ef.printEmail(data)
        emails.append(data)
    return emails

def extractFeatures():
    inboxEmails = read_from_disk(ef.INBOX_DIRECTORY)
    sentEmails = read_from_disk(ef.SENT_DIRECTORY)
