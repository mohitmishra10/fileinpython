#file 

# def fileFunction(file="File1.txt"):
#     try:
#         File=open(file,"a+t")
#         File.writelines(["Roll no.:45\n","Name : Mohit Mishra\n"])
#         File.seek(0)
#         print(File.readlines())
#     except Exception as e:
#         print(e)

# fileFunction()
def fileFunction(file="File1.txt"):
    try:
        File=open(file,"a+t");
        File.writelines(["Roll no.: 109\n","Name : Maaz\n","Class : SYCO-B\n"]);
        File.seek(0);
        print(File.readlines());
    except Exception as e:
        print(e);

fileFunction();