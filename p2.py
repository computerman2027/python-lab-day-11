f = open("demofile3.txt", "w")
f.write("Now the file!1\n")
f.write("Now the file!2\n")

f = open("demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.write("Now the file has more content2!\n")

f.write("Now the file has more content33!\n")

f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
