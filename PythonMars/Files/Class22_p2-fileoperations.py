#### Time in Video  around Time 24:00 ####

#FileNotFoundError: [Errno 2] No such file or directory: 'Files/Sample.txt'
# file=open('Files/SamlpleSyed.txt','w')   # This will create a File if not Existed
# file=open('Files/SamlpleSyed.txt','r+')
# for line in file:
#     print(line, end='')

# print(file.name)
# print(file.readable())
# print(file.writable())
# file.close()
# print(file.closed)
# print(file.mode)

# with open('Files/SamlpleSyed2.txt','w+') as rf:
#     with open('Files/SamlpleSyed.txt','r') as wf:
#         i=0
#         for line in wf:
#             if i==2:
#                 rf.write(line)
#                 i=i+1

# rf.close()
# wf.close()

with open('Files/SamlpleSyed.txt','r') as rf:
    with open('Files/SamlpleSyed2.txt','w') as wf:
        for line in rf:
            # if line == 2:
                wf.write(line)

rf.close()
wf.close()



with open('Files/SamlpleSyed2.txt','w+') as rf:
    with open('Files/SamlpleSyed.txt','r') as wf:
        i=0
        for line in wf:
            if i==2:
              print(line)
              rf.write(line)
            i= i+1

rf.close()
wf.close()