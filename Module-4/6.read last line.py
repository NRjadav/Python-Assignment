
f=open("example1.txt","r")

last_line=f.readlines()[-1]

print(last_line)

f.close()