import FeatureExtractor as fe
import EmailFetcher as ef
import gui

def main() :
        print "\nFetching Emails...\n"
        #gui.interfaceFetchEmails()
        print "Extracting Features...\n"
        fe.extractFeatures()

main()
