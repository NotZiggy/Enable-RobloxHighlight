import json
import os
import urllib.request

rblxpath = "C:\Program Files (x86)\Roblox\Versions"
r = json.loads(urllib.request.urlopen("https://clientsettings.roblox.com/v1/client-version/WindowsPlayer").read())
rblxpath = rblxpath + "\\" + r["clientVersionUpload"]
if os.path.exists(rblxpath + "\\ClientSettings"):
    #print("Folder Found!")
    rblxpath = rblxpath + "\\ClientSettings"
else:
    os.mkdir(rblxpath + "\\ClientSettings")
    #print("Folder Created!")
    rblxpath = rblxpath + "\\ClientSettings"
with open(rblxpath + "\\ClientAppSettings.json", "w") as cas:
    cas.write("{\"FFlagRenderHighlightPass3\": \"True\"}")
    cas.close()
print("FFlagRenderHighlightPass3: True")
print("Done!")
os.system("pause")