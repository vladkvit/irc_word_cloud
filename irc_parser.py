import sys

f = open('../#unmatlabic.log', 'r', encoding="utf8")
fout = open( '../formatted.txt', 'w', encoding='utf8' )

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

	fout.writelines( parts[1] )
	#print( parts[1].encode(sys.stdout.encoding, errors='replace') )
	#print( parts[1], end='\n' )

f.close()
fout.close()