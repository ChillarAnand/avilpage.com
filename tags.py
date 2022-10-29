"""
<ul itemprop="keywords" class="tags">
<li><a class="tag p-category" href="../../tags/arduino.html" rel="tag">arduino</a></li>
            <li><a class="tag p-category" href="../../tags/how-to.html" rel="tag">how-to</a></li>
        </ul>
"""
import collections
import json

tag_cloud_file = 'output/assets/js/tag_cloud_data.json'

tag_data = json.load(open(tag_cloud_file))

counter = collections.Counter(tag_data)

html = '<div id="top-tags"><ul itemprop="keywords" class="tags">'
items = 0

for tag, count in counter.most_common():
    # print(tag, count[0])

    if items == 18:
        break
    if tag.strip() in ('how-to',  'django-tips-tricks', 'featured', 'tech'):
        continue
    print(tag, count[0])
    li = '<li><a class="tag p-category" href="/tags/{}.html" rel="tag">{}<span class="badge badge-light">{}</span></a></li>'.format(tag, tag, count[0])
    html += li
    items += 1

html += '</ul></div> \n\n<hr>'

index_file = 'templates/list_post.tmpl'

lines = open(index_file).readlines()
with open(index_file, 'w') as fh:
    for line in lines:
        if '<hr>' in line:
            continue

        if "top-tags" in line:
            print(line)
            line = html
        fh.write(line)
