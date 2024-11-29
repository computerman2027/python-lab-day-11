words=0
max_len=0
with open("demofile2.txt",'r') as f:
    for line in f:
        w=line.split()
        words+=len(w)
        if w:
            max_len=max(max_len,len(max(w,key=len)))

print("total words = ",words)

print("Length of the longest word : ",max_len)
