import os
from googleapiclient.http import MediaFileUpload

class Video:
    title = "test upload"
    description = "test description"
    category = "22"
    keywords = "test"
    privacyStatus = "private"

    def getFileName(self, type):
        for file in os.listdir(os.environ.get("VIDEO_DIR", "videos")):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file
                break
            elif type == "thumbnail" and file.split(".", 1)[1] != "mp4":
                return file
                break

