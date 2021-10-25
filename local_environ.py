# Python program to explain os.environ object 
  
# importing os module 
import os
  
# Add a new environment variable 

os.environ['DOCDB_USER']='usr_aapersonalization_dev'
os.environ['DOCDB_PASS']='0@3rQb7dHQ'
os.environ['DOCDB_HOST']='docdb-aapersonalization-dev.cluster-cgwmheq2buot.us-east-1.docdb.amazonaws.com'

os.environ['RICH_FTP_PROMOTION_HOST']='staging-ftp.richrelevance.com'
os.environ['RICH_FTP_PROMOTION_USER']='belcorp'
os.environ['RICH_FTP_PROMOTION_PWD']='3qhHwaCx'

# Get the value of
# Added environment variable 
print( os.environ['DOCDB_USER'])