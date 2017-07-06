import os


files = os.listdir('/Users/mazhang/Desktop/mazhang2718.github.io/photoStuff')

target = open("photos.yml", 'w')

target.write('---')

counter = 0

for file in files:
	target.write("-\n")
	target.write("  image: " + file + "\n")
	if (counter % 2 == 0):
		target.write("  align: left\n")
	else:
		target.write("  align: right\n")
	counter+=1

target.close()

