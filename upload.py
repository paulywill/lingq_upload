#!/usr/bin/env python

#import eyed3
import sys
import requests
import os
from dotenv import load_dotenv
from requests_toolbelt.multipart.encoder import MultipartEncoder

load_dotenv()
key = os.getenv("APIKey")
#mp3DIR = os.getenv("mp3DIR")
#status = os.getenv("status")
#collectionID = os.getenv("collectionID")







def __main__():
    for args in sys.argv[1:]:

        title = args 
        transcript = ''

        m = MultipartEncoder([
                    ('title',title),
                    ('text',transcript),
                    ('status','private'),
                    ('collection','495095'),
                    ('audio', (args, open(args, 'rb'), 'audio/mpeg'))]   
                )

        h = {'Authorization': key,
            'Content-Type': m.content_type}

        r = requests.post('https://www.lingq.com/api/v2/fr/lessons/', data=m, headers=h)
        print(r.status_code)
        print(r.text)


if __name__ == "__main__":
    __main__()
