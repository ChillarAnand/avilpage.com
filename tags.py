"""
Append Top tags, year count to archive.html
"""
import collections
import json

from bs4 import BeautifulSoup


def get_year_post_count():
    year_count = {}
    filename = 'output/archive.html'
    soup = BeautifulSoup(open(filename), 'html.parser')
    text = soup.get_text()
    for year in range(2012, 2030):
        if text.count(str(year)) > 1:
            year_count[year] = text.count(str(year)) - 1
    return year_count


def get_top_tags_html(tag_data):
    top_tags_html = '<div id="top-tags"><ul itemprop="keywords" class="tags">'
    items = 0

    tag_counter = collections.Counter(tag_data)

    for tag, count in tag_counter.most_common():
        # print(tag, count[0])
        if items == 12:
            break
        if tag.strip() in ('how-to',  'django-tips-tricks', 'featured', 'tech'):
            continue
        print(tag, count[0])
        li = '<li><a class="tag p-category" href="/tags/{}.html" rel="tag">{}<span class="badge badge-light">{}</span></a></li>'.format(tag.lower(), tag, count[0])
        top_tags_html += li
        items += 1

    top_tags_html += '</ul></div> \n\n<hr>'
    return top_tags_html


def get_year_count_html():
    year_count = get_year_post_count()

    year_html = '<div id="year"><ul itemprop="keywords" class="tags">'
    for year, count in year_count.items():
        li = '<li><a class="tag p-category" href="/tags/cat_{}.html" rel="tag">{}<span class="badge badge-light">{}</span></a></li>'.format(year, year, count)
        year_html += li

    year_html += '</ul></div> \n\n<hr>'
    return year_html


tag_cloud_file = 'output/assets/js/tag_cloud_data.json'
tag_data = json.load(open(tag_cloud_file))

top_tags_html = get_top_tags_html(tag_data)
year_count_html = get_year_count_html()

index_file = 'templates/list_post.tmpl'
lines = open(index_file).readlines()

with open(index_file, 'w') as fh:
    for line in lines:
        if '<hr>' in line:
            continue

        if "top-tags" in line:
            print(line)
            line = top_tags_html

        if 'id="year"' in line:
            print(line)
            line = year_count_html

        fh.write(line)
