import csv
import FeatureExtractor as fe

FILE = "Output.csv"

def listtocsv(inboxEmailFeatures,Output,result_1,result_2,result_3):
	inboxSize = len(inboxEmailFeatures)
	with open(FILE,'wb') as csvfile:
		writer=csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in range(0,inboxSize):
			row = inboxEmailFeatures[i]
			row.append(Output[i])
			row.append(result_1[i])
			row.append(result_2[i])
			row.append(result_3[i])
			writer.writerow(row)
