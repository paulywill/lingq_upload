# lingq_upload

This python script is to work with LingQ.com [API](https://www.lingq.com/apidocs/).

File ``.env`` has to be created and requires the following:

```
#APIKey="Token api_number"
APIKey="Token [https://www.lingq.com/accounts/apikey]"

# There is an address as per API POST doc that includes a two letter language code (ie 'fr' = french)
postAddress="https://www.lingq.com/api/v2/xx/lessons/"

# Specify private if material is copyrighted or personal
status="private"

# Manual create a course and reference this collection ID
collectionID="xxxxxx"

# Full path name (created on Mac OSX)
mypath="/Users/paulywill/Coding/python/lingq_upload/mp3"
```