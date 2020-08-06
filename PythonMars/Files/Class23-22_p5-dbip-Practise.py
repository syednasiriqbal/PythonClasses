###This is test file created by me ###

var='2.12.2.4'

file=open('Files/phonesPractise.txt','w+')
file.write('env: preprod')
file.write('RELEASES_ROOT: "."')
file.write('RELEASE: "'+str(var)+'"')
file.write('HSM_HOST: 10.122.0.29')


