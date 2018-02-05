import os
import re
import requests
from tqdm import *


def main():
    download = 'star wars'
    path = './download/{}'.format(download)

    response = requests.get(
        'https://thenounproject.com/search/json/icon/?q={}&page=1&limit=30&raw_html=false'.format(download)).text
    svg_list = re.findall(
        '"term_slug": "([^"]*)".*?"icon_url": "([^"]*)".*?"username": "[^"]*".*?"permalink": "([^"]*)"', response)
    author_list = []

    if not os.path.exists(path):
        os.makedirs(path)
    for index, icon in enumerate(tqdm(svg_list)):
        r = requests.get(icon[1], stream=True)
        with open('{0}/{1:03d}_{2}.svg'.format(path, index, icon[0]), 'wb') as fd:
            for chunk in r.iter_content(2048):
                fd.write(chunk)
        author_list.append(icon[2])

    with open("{}/authors.txt".format(path), "w") as text_file:
        text_file.write("https://thenounproject.com" + "\nhttps://thenounproject.com".join(list(set(author_list))))
    with open("{}/icon_authors.txt".format(path), "w") as text_file:
        text_file.write('\n'.join(
            ['{0:03d}_{1} -> {2}'.format(index, icon[0], icon[2][1:]) for index, icon in enumerate(svg_list)]))


if __name__ == '__main__':
    main()
