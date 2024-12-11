with open("sample.txt","r") as file:
    for line in file:
        print(line.strip()) #strip removes the new line character

# Another way to read all the content
with open("sample.txt","r") as file:
    content = file.read()
    print(content)

# Writing the contents into a file
with open("dummy.txt",mode="w") as file:
    file.write("Hello World\n")
    file.write("Hi Man\n")

# Writing in append mode
with open("dummy.txt",mode="a") as file:
    file.write("Hey folks\n")
    file.write("Say Hello To my friend\n")

#Write multiple lines into a file via list.
lines_list = ["Hello World\n", "Hi Guys\n", "Bye friend\n"]
with open("dummy.txt",mode="w") as file:
    file.writelines(lines_list)

# Writing and then reading a file
with open("dummy.txt",mode="w+") as file:
    file.write("Hey folks\n")
    file.write("Say Hello To my friend\n")

    file.seek(0) #Move cursor to the beginning
    contents = file.read()
    print(contents)