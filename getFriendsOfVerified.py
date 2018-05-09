fh = open("friends_verified.txt","r")
 

ids = []

count = 1
for line in fh:
	if (count == 2 or count ==3):
		line = line.split("[")
		line = line[1]
		line = line.split("]")
		line = line[0]
		line = line.split(",")[:1000]
		ids.extend(line)
	else:
		line = line.split("[")
		line = line[1]
		line = line.split("]")
		line = line[0]
		line = line.split(",")
		ids.extend(line)
	count +=1

ids = [i.lstrip(" ") for i in ids]
print ids
string = "\n".join(ids)

fr = open("usernames","a+")
fr.write(string)

