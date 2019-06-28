import requests,sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup

url = sys.argv[1]

response = requests.get(url)
soup = BeautifulSoup(response.text,features="html.parser")
metas = soup.find_all('meta')

#get first element from array or return None
# obj = next(iter(arr),None)

descriptions = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'].lower() == 'description' ]
descriptions1 = [ meta.attrs['content'] for meta in metas if 'property' in meta.attrs and meta.attrs['property'].lower() == 'og:description' ]
titles = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'].lower() == 'title' ]
titles1 = [ meta.attrs['content'] for meta in metas if 'property' in meta.attrs and meta.attrs['property'].lower() == 'og:title' ]
title = soup.find('title')
images = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'].lower() == 'image' ]
images1 = [ meta.attrs['content'] for meta in metas if 'property' in meta.attrs and meta.attrs['property'].lower() == 'og:image' ]

domain_name = urlparse(response.url).netloc
#import pdb;pdb.set_trace()

if descriptions == [] and titles == [] and images == [] and descriptions1 == [] and titles1 == [] and images1 == []:
    print('No content Available for {}'.format(domain_name))
    sys.exit()
print('Domain : ',domain_name)
if len(descriptions) > 0 and descriptions[0] != '':
    print('Description : ',descriptions[0].replace('\n',''))
elif len(descriptions1) > 0 and descriptions1[0] != '':
    print('Description : ',descriptions1[0].replace('\n',''))

if len(titles) > 0 and titles[0] != '':
    print('Title : ',titles[0].replace('\n',''))
elif len(titles1) > 0 and titles1[0] != '':
    print('Title : ',titles1[0].replace('\n',''))
elif title != '':
    print('Title : ',title.text.replace('\n',''))
if len(images) > 0 and images[0] != '':
    print('Image : ',images[0].replace('\n',''))
elif len(images1) > 0 and images1[0] != '':
    print('Image : ',images1[0].replace('\n',''))
if domain_name == 'www.youtube.com':
    youtube_embed = [ meta.attrs['content'] for meta in metas if 'property' in meta.attrs and meta.attrs['property'].lower() == 'og:video:url' ]
    if next(iter(youtube_embed),None) != None:
        print('Youtube Embed link : ',youtube_embed[0])

