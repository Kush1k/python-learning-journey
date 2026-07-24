with open("practice.txt","w") as f:
    f.write("Hi everyone\n we are learning file I/O")
    f.write("using Java \n I like programming in Java")

with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("Java","Python")
print(new_data)
