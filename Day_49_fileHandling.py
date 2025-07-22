 #READING FILE 

f = open('myfile.txt', 'r')

text = f.read()
print(text)
f.close()

# WRITING FILE

f=open('myfile.txt', 'w')  # 'w' mode will overwrite the file
t=f.write("hello World")
f.close()


with open('myfile.txt', 'r') as f:
    print(f.read())
