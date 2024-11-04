import urllib.request
url = input("Enter the Youtube-url\n")
name = input("Enter the name for the video\n")
name=name+".mp4"
try:
    print("Downloading starts...\n")
    urllib.request.urlretrieve(url, name)
    print("Download completed..!!")
except Exception as e:
    print(e)


import urllib.request
urllib.request.urlretrieve("blob:https://ua.udemy.com/b09f66ca-fca5-4ce6-b0a5-5f95445bd94d", 'video_name.mp4') 
