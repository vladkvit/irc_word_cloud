import sys
import operator

f = open('../#unmatlabic.log', 'r', encoding="utf8")
fout = open( '../formatted.txt', 'w', encoding='utf8' )
fout2 = open( '../sortedwords.txt', 'w', encoding='utf8' )
fout3 = open( '../usernames.txt', 'w', encoding='utf8' )

wordcount = dict()
usernamecount = dict()

for line in f:
	#%line = line.encode(sys.stdout.encoding, errors='replace')
	if line == '':
		continue

	if line.startswith( '**** BEGIN LOGGING AT ' ):
		continue

	parts = line.split( '>	', 1 )
	
	if len( parts ) < 2:
		#includes "start logging" spacing and the *XYZ says lines
		continue

	sentence = parts[1]
	username = parts[0]
	username = username.split( '<', 1 )[1]

	if( username in usernamecount) == False:
		usernamecount[username] = 0

	usernamecount[username] += 1

	fout.writelines( sentence )
	words = sentence.split( ' ' )
	for word in words:
		if word == '':
			continue
		word = word.strip('\n')
		word = word.lower()

		if (word in wordcount) == False:
			wordcount[word] = 0
		wordcount[word] += 1

	#print( sentence.encode(sys.stdout.encoding, errors='replace') )
	#print( sentence, end='\n' )

f.close()
fout.close()

sorted_wordcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
sorted_usernames = sorted(usernamecount.items(), key=operator.itemgetter(1), reverse=True)

for item in sorted_wordcount:
    fout2.writelines( "{} {}\n".format( item[1], item[0]) )

fout2.close()

for item in sorted_usernames:
    fout3.writelines(  "{} {}\n".format( item[1], item[0]) )
fout3.close()