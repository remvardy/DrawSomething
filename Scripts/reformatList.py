# m_Word[i] = "word"; 
Infile = open("2char.txt", 'rt')
Outfile = open("2charforvector.txt", 'wt')
imax = len(Infile.readlines())
index = 0
Infile.seek(0)

while index<imax:
	in_line = Infile.readline()
	Outfile.write("m_Word[" + str(index) + "]" + "=\""+ in_line[0:2] + "\";\n")
	print ("m_Word[" + str(index) + "]" + "=\""+ in_line[0:2] + "\";\n")
	
	index = index+1	

Infile.close()
Outfile.close()



	

