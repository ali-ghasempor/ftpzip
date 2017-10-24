# Author : Ali Ghasempour
# 25 Oct 2017
# This Program will Download file using FTP protocol with ZIP compressing feature .
# Compression will be on server and download ZIP file trough FTP
# As an Input you will pass " IP username password directory_path " ( with space separated ) and after reviewing files select
# which file you want to get . File will be save on your current directory in ZIP format .
# This program was written in Linux , However it works on Windows with FTP server with some modification ( Change / to \ ).
# Please make sure your FTP server would authenticate user , Also check user chroot .

from ftplib import FTP as ftp
from os import system as sys

# class ftpclass with using functions

class ftpclass :

    # constractor to initilaize variables
    def __init__(self, host, user, password, path):
        self.host = host
        self.user = user
        self.password = password
        self.path = path

    # connect to FTP server
    def ftpCon(self):
        try:
            self.con = ftp(self.host)
            self.con.login(self.user, self.password)
            self.con.cwd(self.path)
        except:
            print("connection error")

    # show specified path files
    def showFile(self):
        self.con.dir()

    # download file
    def getFile(self, filename):
        try:
            # compress file
            print(self.path)
            sys("cd " + self.path + "/;" + "zip " + filename+".zip " + filename)
            self.con.retrbinary("RETR " + filename+".zip", open(filename+".zip", 'wb').write)
        except:
            # if file dosen't exist remove it
            sys("rm " + filename+".zip")
            print("Error")
            return -1
    def closeCon(self):
        self.con.close()

# read data
rddata = input("Enter IP username password directory : ")
try:
    ip , user , password , directory = rddata.split()
except:
    print("Enter in correct format ( use space to seperate )")
con1 = ftpclass(ip , user , password ,directory)
con1.ftpCon()
con1.showFile()
filename = input("Please Enter Filename : ")
con1.getFile(filename)
con1.closeCon()