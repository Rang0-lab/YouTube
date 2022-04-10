import os
from googleapiclient.http import MediaFileUpload

class Video:
    title = "test upload"
    description = "test description"
    category = "22"
    keywords = "test"
    privacyStatus = "private"

    def getFileName(self, type):
        for file in os.listdir("C:\\Users\\37120\\Desktop\\VisualStud\\videos"):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file
                break
            elif type == "thumbnail" and file.split(".", 1)[1] != "mp4":
                return file
                break

