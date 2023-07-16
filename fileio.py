from requests import options, post
from os.path import isfile
from fake_useragent import UserAgent
def fileio(filepath):
  """
  File.io, max 2 GB.
  """
  if not isfile(filepath):
    raise OSError('File not found or is a directory.')
  headers = {
    'User-Agent': UserAgent(browser=['edge', 'chrome', 'ff', 'safari']),
    'Origin': 'https://www.file.io',
    'Referer': 'https://www.file.io/',
  }
  filename = filepath.split('/')[-1] if '/' in filepath else filepath
  with open(filepath, 'rb') as file:
    req = post('https://file.io/', headers=headers, params={'title': filename}, files={'file': file.read()})
  req.raise_for_status()
  json = req.json()
  return json['link']
