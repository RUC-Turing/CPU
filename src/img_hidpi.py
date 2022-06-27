import re
import urllib.parse
from bs4 import BeautifulSoup

regexp = re.compile('[\S\s]+@2x\.[a-z]+$')

def on_page_content(html: str, page, config, files) -> str:
  soup = BeautifulSoup(html, features="html.parser")
  for img in soup.select('img'):
    src_encoded = img['src']
    src = urllib.parse.unquote(src_encoded)
    if regexp.match(src):
      del img['src']
      img['srcset'] = src_encoded + ' 2x'
  for img in soup.select('p > img:only-child'):
    img['style'] = 'display: block; margin: 0 auto; '
  return str(soup)
