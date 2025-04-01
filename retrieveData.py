from ftplib import FTP
import pandas as pd
import json

username = 'anonymous'
password = 'samuel.wakelam@gmail.com'
# Connect to the FTP server (replace with BoM's actual FTP server address)
ftp = FTP('ftp.bom.gov.au')
ftp.login(username, password)
ftp_directory = "/anon/gen/fwo/"
ftp.cwd(ftp_directory)
files = ftp.nlst()  # List available files
print("Available files:", files)

with open('melbourneObservations.xml', 'wb') as dataFile:
    ftp.retrbinary('RETR IDV60920.xml', dataFile.write)

