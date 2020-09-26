# # Open function to open the file "tools.txt"  
# # (same directory) in append mode and 


# #CTRL+K then CTRL+C adds the # in VS for selected lines. CTRL+K then CTRL+U removes the # in VS for selected lines.
# # # Program to show various ways to read and 
# # # write data in a file. 
# #file1 = open("rough.txt","w") 
# # L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
  
# # # \n is placed to indicate EOL (End of Line) 
# # file1.write("Hello \n") 
# # file1.writelines(L) 
# # file1.close() #to change file access modes 
# # file1.close()

# file1 = open("myfile.txt","r+")  
  


# print ("Output of ReadLine function is ")
# print( file1.readline(5) )
# print()

# print ("Output of Read function is ")
# print( file1.read() )
# print()

# # seek(n) takes the file handle to the nth 
# # bite from the beginning. 
# file1.seek(0)  
  
# print ("Output of Readline function is ")
# print (file1.readline() )
# print ()

# file1.seek(0) 
  
# # To show difference between read and readline 
# print ("Output of Read(9) function is ")
# print (file1.read(9) )
# print ()

# file1.seek(0) 
  
# print ("Output of Readline(9) function is ")
# print (file1.readline(9) )

# file1.seek(0) 
# # readlines function 
# print ("Output of Readlines function is ")
# print (file1.readlines(5) )
# print ()


# file1.seek(0)
# print("print one by one")
# print (file1.readline() )
# print (file1.readline() )
# print (file1.readline() )
# print (file1.readline() )
# file1.close() 


# get  seperate link and names in two groups

                                                # namefile=open("myfile.txt","w")
                                                # linkfile=open("links.txt","w")
                                                # toolsfile=open("tools.txt","r")
                                                # nextline=""
                                                # c=0
                                                # for _ in range(146):
                                                #     nextline=toolsfile.readline()
                                                #     print(nextline)
                                                #     c=c+1
                                                #     if c%3==1:
                                                #         namefile.write(nextline)
                                                #     elif c%3==2:
                                                #         linkfile.write(nextline)
                                                    

                                                # namefile.close()
                                                # linkfile.close()
                                                # toolsfile.close()

#put all file values in a list:


                                                # l=[]
                                                # f1=open("links.txt","r")
                                                # for _ in range(50):
                                                #     l.append(f1.readline().replace("\n",""))
                                                # print(l)
                                                # f1.close()

list1=['dnscan ', 'Knockpy ', 'Sublist3r ', 'massdns ', 'nmap ', 'masscan ', 'EyeWitness ', 'DirBuster ', 'dirsearch ', 'Gitrob ', 'git-secrets ', 'sandcastle ', 'bucket_finder ', 'GoogD0rker ', 'Wayback Machine ', 'waybackurls ', 'Sn1per ', 'XRay ', 'wfuzz ', 'patator ', 'datasploit ', 'hydra ', 'changeme ', 'MobSF ', 'Apktool ', 'dex2jar ', 'sqlmap ', 'oxml_xxe ', 'XXE Injector ', 'The JSON Web Token Toolkit', 'ground-control ', 'ssrfDetector ', 'LFISuit ', 'GitTools ', 'dvcs-ripper ', 'tko-subs ', 'HostileSubBruteforcer ', 'Race the Web ', 'ysoserial', 'PHPGGC', 'CORStest', 'retire-js ', 'getsploit ', 'Findsploit ', 'bfac ', 'WPScan ', 'CMSMap ', 'Amass ', 'Extra Tools']
list2=['https://github.com/rbsec/dnscan', 'https://github.com/guelfoweb/knock', 'https://github.com/aboul3la/Sublist3r', 'https://github.com/blechschmidt/massdns', 'https://nmap.org', 'https://github.com/robertdavidgraham/masscan', 'https://github.com/ChrisTruncer/EyeWitness', 'https://sourceforge.net/projects/dirbuster/', 'https://github.com/maurosoria/dirsearch', 'https://github.com/michenriksen/gitrob', 'https://github.com/awslabs/git-secrets', 'https://github.com/yasinS/sandcastle', 'https://digi.ninja/projects/bucket_finder.php', 'https://github.com/ZephrFish/GoogD0rker/', 'https://web.archive.org', 'https://gist.github.com/mhmdiaa/adf6bff70142e5091792841d4b372050 ', 'https://github.com/1N3/Sn1per/', 'https://github.com/evilsocket/xray', 'https://github.com/xmendez/wfuzz/', 'https://github.com/lanjelot/patator', 'https://github.com/DataSploit/datasploit', 'https://github.com/vanhauser-thc/thc-hydra', 'https://github.com/ztgrace/changeme', 'https://github.com/MobSF/Mobile-Security-Framework-MobSF/ ', 'https://github.com/iBotPeaches/Apktool', 'https://sourceforge.net/projects/dex2jar/', 'http://sqlmap.org/', 'https://github.com/BuffaloWill/oxml_xxe/', 'https://github.com/enjoiz/XXEinjector', ' https://github.com/ticarpi/jwt_tool', 'https://github.com/jobertabma/ground-control', 'https://github.com/JacobReynolds/ssrfDetector', 'https://github.com/D35m0nd142/LFISuite', 'https://github.com/internetwache/GitTools', 'https://github.com/kost/dvcs-ripper', 'https://github.com/anshumanbh/tko-subs', 'https://github.com/nahamsec/HostileSubBruteforcer ', 'https://github.com/insp3ctre/race-the-web', 'https://github.com/GoSecure/ysoserial', 'https://github.com/ambionics/phpggc', 'https://github.com/RUB-NDS/CORStest', 'https://github.com/RetireJS/retire.js', 'https://github.com/vulnersCom/getsploit', 'https://github.com/1N3/Findsploit', 'https://github.com/mazen160/bfac', 'https://wpscan.org/', 'https://github.com/Dionach/CMSmap', 'https://github.com/OWASP/Amass', 'http://projectdiscovery.io']
text=""
list3=[]
for i in range(len(list1)):
    text='''<a id=tools href=" '''+list2[i]+''' ">'''+ list1[i] +'''</a>'''
    list3.append(text)
print(list3)