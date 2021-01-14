#myfile = open("Hello2.txt","x")    # It will create a file named "Hello2.txt" if the file is not exist. But if already exist then  it will through error.
myfile = open("Hello3.txt","w")     # It will create a file named "Hello3.txt" if the file is not exist. But if already exist then it overrite it.
myfile.close()      #This is used for closing the file.

############### Test #######################
myfile = open("Hey.txt","x")
myfile.write("Hiiii Anu !!!!!!")
myfile.close()

########### In the following program I have used 'with' keyword and then execution of writing into a file is wrote inside it.
# This is because when we come out from the block of 'with' then file will automatically close.  
'''
with open("Hello.txt","w") as myfle:
    myfle.write("Hello Anu !!!\n")
    myfle.write("Hello Anurag !!!\n")
'''

###### Syntax of file handling #########
#Variable_Name_For_File = open("File_Path\File_Name.File_Extention","File_Mode")
#Variable_Name_For_Storing_File = open("File_Name.File_Extention","File_Mode")

########### Explanation ##########
'''
Variable_Name_For_Storing_File = You can named anything to variable according to your choice and remembering the variable name.
File_Path = If you wanna create/Open file into/from any another path/location of drive.
            If you wanna create/open file into/from same directory then it is not necessary to write the path.
            By default the program access the same path on which the program file is exist.
File_Name = If you wanna create a new file then you can choose any name of the file according to your need.
            But if there's a file already exist then you have to wrote exact name of the file to open.
File_Name.Extension = In this 'Exension' is tell the type of file. For example "txt","docx","csv" etx. which file formate you wanna use.
File_Mode = This is used for open a file into a specific mode to use the file accordingly. By default file mode be "r"
           # "r" = It it used for read only
           # "w" = It is used for write only
           # "x" = It is open a file
           # "a" = It is used for write ann append into a file.
        #### Following note are From python help section you can use 'help(open)' manually into the pyhton shell to know about its working.  
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)

'''