import urllib.request as req from urllib.parse import urlparse

url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'

def downloadURL(url, to=None):
    """Download a remote file specified by a URL to a 
      local directory.

      :param url: str
          URL pointing to a remote file.

      :param to: str
          Local path, absolute or relative, with a filename 
          to the file storing the contents of the remote file.
      """

      # TODO: Implement me!
      #pass
    if (to != None):
        

webget.download(url)