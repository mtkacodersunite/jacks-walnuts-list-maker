import csv
with open('walnuts.tsv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='	', quotechar='|')
	for row in spamreader:
		print "Book Title: ", row[0]
		print "Author: ", row[3]
		print "Walnuts: ", row[1]
		print "Quick Comment: ", row[2]
		print "Description: ", row[4]
		print "Genre: ", row[5], " ", row[6]
		print "\n<hr>\n"
