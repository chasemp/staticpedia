#!/usr/bin/python3

try:
    import requests
except ImportError:
    print('Install requests3 library')
import getpass
import sys
import json

def main():
    req = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikisource/all-access/2019/01/all-days'
    r = requests.get(req)
    results = json.loads(r.content.decode('utf-8'))
    if '-v' in sys.argv:
        print(results)

    #{u'items': [{u'access': u'all-access', u'articles': [{u'article':
    # /w/api.php?action=query&format=json&prop=extracts&meta=&titles=Armpit_fart&redirects=1&explaintext=1
    for key, value in results['items'].items():
        print((key, value))
main()
