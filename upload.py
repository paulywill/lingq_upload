#!/usr/bin/env python

from os.path import isfile, join
from os import listdir
import sys
import requests
import os
from dotenv import load_dotenv
from requests_toolbelt.multipart.encoder import MultipartEncoder

load_dotenv()
key = os.getenv("APIKey")
postAddress = os.getenv("postAddress")
mypath = os.getenv("mypath")
mp3DIR = os.getenv("mp3DIR")
status = os.getenv("status")
collectionID = os.getenv("collectionID")


def __main__():
    # Create list/array of mp3
    mp3s = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    mp3s.sort(reverse=False)
    for mp3 in mp3s:
       
        m = MultipartEncoder([
                    ('title', mp3[0:11]),
                    ('text', mp3[0:11]),
                    ('status',status),
                    ('collection',collectionID),
                    ('audio', (mp3, open(mypath + '/' + mp3, 'rb'), 'audio/mpeg'))]   
                )

        h = {'Authorization': key,
            'Content-Type': m.content_type}

        r = requests.post(postAddress, data=m, headers=h)
        print(r.status_code)
        print(r.text)


if __name__ == "__main__":
    __main__()
