infile = open("BillOfRights.txt", "r")
   
content = []

plist = infile.readline()
while plist:
    alist.append(plist)
    plist = infile.readline()

infile.close()

content2 = []

for elem in content:
    elem2 = elem.lower()
    content2.append(elem2)

outfile = open("Justabill.txt", "w")

for elem3 in content2:
    outfile.write(elem3 + '\n')


outfile.close()