import argparse
import requests
import os

def DownloadFile(url,path):
    local_filename = path + url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 

path = "/Users/varunwarudkar/Library/Mobile Documents/com~apple~CloudDocs/Git/Python_100_days/Python/"

parser = argparse.ArgumentParser()

# Add command line Arguments 
parser.add_argument("url", help="url of file to download")
parser.add_argument("path", help="path of file to store as output")
parser.add_argument("path1", help="path of file to store as output")
#Parse the arguements
#args = parser.parse_args()
args, unknown = parser.parse_known_args()

#Use the Arguments in your code
print(args.url)
print(args.path)
#path = path + args.url.split('/')[-1]
#print(path)
path = args.path + " " + args.path1
print(path)
DownloadFile(args.url,path)


#python3 085_commadline.py http://hep.uchicago.edu/images/jpeg/boucle_meuse.jpg /Users/varunwarudkar/Library/Mobile Documents/com~apple~CloudDocs/Git/Python_100_days/Python/