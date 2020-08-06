
from os import close


try:
    print("File Operations")
    file=open('Files/july.txt','r+')
    # if file.writable:
    #     file.write("Hello, This is Pakistan\n")

    if file.readable:
        content=file.read()
        print(content)
    
    if file.closed == False:
        file.close()

except Exception as e:
    print("Exception is -",e)


try:
    with open('Files/nocontent.txt','r') as releasefile:
        listx=releasefile.read().replace('2.12.4.40','2.12.4.60')
    with open('Files/nocontent.txt','r+') as releasefilewrite:
            releasefilewrite.write(listx)
except Exception as Error:
    print("Exception is -",Error)