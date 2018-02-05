import re
import requests


def main():
    download = 'star wars'

    response = requests.get(
        'https://thenounproject.com/search/json/icon/?q={}&page=1&limit=30&raw_html=false'.format(download)).text
    svg_list = re.findall(
        '"term_slug": "([^"]*)".*?"icon_url": "([^"]*)".*?"username": "[^"]*".*?"permalink": "([^"]*)"', response)
    author_list = []

    for index, icon in enumerate(svg_list):
        r = requests.get(icon[1], stream=True)
        with open('./download/{0:03d}_{1}.svg'.format(index, icon[0]), 'wb') as fd:
            for chunk in r.iter_content(2048):
                fd.write(chunk)
        author_list.append(icon[2])

    with open("./download/authors.txt", "w") as text_file:
        text_file.write("https://thenounproject.com" + "\nhttps://thenounproject.com".join(list(set(author_list))))
    with open("./download/icon_authors.txt", "w") as text_file:
        text_file.write('\n'.join(
            ['{0:03d}_{1} -> {2}'.format(index, icon[0], icon[2][1:]) for index, icon in enumerate(svg_list)]))


if __name__ == '__main__':
    main()
