f = open("demofile.txt", "r")
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline())

f.seek(0)
print(f.readline(5))
print(f.readline(7))


f.seek(0)
print(f.read(5))
print("Next line\n\n")
print(f.read(8))
f.seek(0)


for x in f:
    print(x)

    
f.close()
