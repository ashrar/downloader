from download import Download
class HttpDownload(Download):
    def __init__(self, url, filestat):
        Download.__init__(self, url, filestat)
    
    def run(self):
        pass
    
    