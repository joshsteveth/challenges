TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87

import xml.etree.ElementTree as ET 
import re
import collections
from itertools import product
from difflib import SequenceMatcher

TAG_HTML = re.compile(r'<category>([^<]+)</category>')

def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    root = ET.parse(RSS_FEED).getroot()
    result = []

    for child in root.iter():
        if child.tag == 'category':
            result.append(child.text.lower().replace('-', ' '))

    return result

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    result = {}
    for t in tags:
        if t in result:
            result[t] += 1
        else:
            result[t] = 1

    return collections.Counter(result).most_common(TOP_NUMBER)

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    pairs = product(tags, repeat=2)

    result = []
    for p in pairs:
        #exclude the same words
        if p[0] == p[1]: continue

        p = sorted(p)

        #also exclude if this pair is already in the result
        if p in result: continue


        sim = SequenceMatcher(None, p[0], p[1]).ratio()
        if sim >= SIMILAR: 
            result.append(p)

    return result


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
