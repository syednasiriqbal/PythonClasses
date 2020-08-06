
# releasefile=open('Files/nocontent.txt','a+')
with open('Files/nocontent.txt','r') as releasefile:
    # with open('Files/nocontent.txt','w') as releasefilewrite:
    listx=releasefile.read().replace('2.12.4.40','2.12.4.60')
    with open('Files/nocontent.txt','r+') as releasefilewrite:
            releasefilewrite.write(listx)
# releasefile.close()
print(listx)
print(releasefile.closed)
print(releasefile.mode)





# listx[1]='RELEASE: "2.12.4.400"\n'
# releasefile=open('Files/nocontent.txt','w')
# new_content=''.join(listx)

# releasefile.write(new_content)
# releasefile.close()




# listx=(releasefile.readlines().replace('2.12.4.20','2.12.4.40',1))




# print(listx)
# # # print(dbfile.readlines())





# listx=([ releasecontent in releasefile.readlines() ])

# # print([ (ipcontent,dbcontent) for ipcontent in zip(ipfile.readlines(),dbcontent in dbfile.readlines()] )

# listx=[ (ipcontent+dbcontent).replace('\n','@',1).rstrip() for ipcontent,dbcontent in zip(ipfile.readlines(),dbfile.readlines()) ]


# print(*listx)