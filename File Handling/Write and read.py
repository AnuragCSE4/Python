with open("Hello.txt","a+") as myfile:
    myfile.write("Hii Anu !!!\n")
    myfile.write("Hii Anurag !!!\n")
    myfile.seek(0)      # This line is used for put the cursor at 0th posion.
                        # Because our file is open in append mode so after writing into file cursor will be at the end position.
    content = myfile.read()
    print(content)