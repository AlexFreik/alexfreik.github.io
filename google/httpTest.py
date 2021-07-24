# py script that does this:
# 1. send get request in google drive for list of files in Notes folder
# 2. extracts info from request
# 3. Then goes in each subfolder and fill info for them in similar way
# 4. At the end it writes in the file "DriveTree" info that it has gathered 

import requests
import json

def getExtractedInfo(parsedJson):
    parsedJson = parsedJson["items"]
    ans = {}
    for item in parsedJson:
        assert item["kind"] == "drive#file"
        assert len(item["parents"]) == 1
        itemInfo = {"title": item["title"],
                "mimeType": item["mimeType"],
                "parentId": item["parents"][0]["id"]}
        ans[item["id"]] = itemInfo
    return ans




def makeRequest(folderId, apiKey):
    url = 'https://www.googleapis.com/drive/v2/files?q=' + folderId + '+in+parents&key=' + apiKey
    r = requests.get(url)
    
    print(r.status_code)
    
    parsed = json.loads(r.content)
    extractedIno = getExtractedInfo(parsed)
    httpLog = json.dumps(parsed, indent=4, sort_keys=True)
    

    extractedLog = json.dumps(getExtractedInfo(parsed), indent=4, sort_keys=True)
    with open("httpLog.json", "w") as f:
        f.write(extractedLog)


def main():
    with open("apiKey.txt", "r") as f:
        apiKey = f.read()[:-1]  # last char is end of line
    
    folderId = '"1CQQHfA5_bgEhP6T0iH9Xp6xDz7D5lbIU"'
    makeRequest(folderId, apiKey)


if __name__ == "__main__":
    main()
