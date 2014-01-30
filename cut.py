import sys

files_list = sys.argv[1:]

for filename in files_list:
	target = open(filename)
	print "\n"
	print "filename:", filename
	print target.read()
	target.close()