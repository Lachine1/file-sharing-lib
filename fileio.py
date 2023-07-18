from requests import options, post
from os.path import isfile
from fake_useragent import UserAgent
def fileio(filepath='', file_content=''):
  """
  File.io, max 2 GB.
  """
  if filepath:
    if not isfile(filepath):
      raise OSError('File not found or is a directory.')
  headers = {
    'User-Agent': UserAgent(browser=['edge', 'chrome', 'ff', 'safari']),
    'Origin': 'https://www.file.io',
    'Referer': 'https://www.file.io/',
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "Content-Type": "multipart/form-data",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
    }
  }
  if filepath:
    filename = filepath.split('/')[-1] if '/' in filepath else filepath
  if filename:
    with open(filepath, 'rb') as file:
      req = post('https://file.io/', headers=headers, params={'title': filename}, files={'file': file})
  else:
    req = post('https://file.io/', headers=headers, params={'title': filename}, files={'file': ('file10.txt', file_content.encode('utf-8'))})
  req.raise_for_status()
  json = req.json()
  return json['link']
