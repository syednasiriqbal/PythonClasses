
ipfile=open('Files/ip.txt','r')
dbfile=open('Files/db.txt','r')

# print(ipfile.readlines())
# # print(dbfile.readlines())

# listx=([ (ipcontent,dbcontent) for ipcontent in ipfile.readlines() for dbcontent in dbfile.readlines()])

# # print([ (ipcontent,dbcontent) for ipcontent in zip(ipfile.readlines(),dbcontent in dbfile.readlines()] )

listx=[ (ipcontent+dbcontent).replace('\n','@',1).rstrip() for ipcontent,dbcontent in zip(ipfile.readlines(),dbfile.readlines()) ]


print(*listx,sep='\n')



# ===========================================================================================================
   
evennumbers=[2,4,6,8,10]
oddnumbers=[1,3,5,7,9]
primenumbers=[2,3,5,7]
# print(list((zip(evennumbers,oddnumbers,primenumbers))))

for i,j,k in zip(evennumbers,oddnumbers,primenumbers):
    print(i,j,k)