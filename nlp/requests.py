import requests
import json
import string
import pandas as pd
from math import ceil

class request_handler():
    def __init__(self):
        self.apikey = '222a2a95a093a5c6049c145c09ed85a9'

    def get_summary(self,search_string):
        search_string = search_string.replace(' ','%20')
        url = f'https://api.elsevier.com/content/search/scopus?start=0&count=25&query={search_string}&apiKey={self.apikey}'
        res = requests.get(url)
        res = json.loads(res.text)
        summary = {}
        try:
            summary['total_results'] = int(res['search-results']['opensearch:totalResults'])
            summary['search_terms'] = res['search-results']['opensearch:Query']['@searchTerms']
        except Exception as e:
            summary['total_results'] = 0
            summary['search_terms'] = search_string

        summary['link_used'] = url
        return summary

    def get_urls(self,search_string, total_results = 25 ):
        #url generation
        start=0
        end=ceil(total_results/25)
        final_count = total_results%25
        count = 25
        urls = []
        for i in range(end):
            print (i, end)
            if i == end-1:
                count = final_count
            url = f'https://api.elsevier.com/content/search/scopus?start={start}&count={count}&query={search_string}&apiKey={self.apikey}'
            start+=25
            urls.append(url)
        return urls

    def get_res(self, url = ''):
        error_collection=[]
        res = requests.get(url)
        x = json.loads(res.text)
        ids = {}
        try:
            results = pd.DataFrame(x['search-results']['entry'])
            ids = pd.DataFrame(x['search-results']['entry'])['dc:identifier']
            scopus_ids = ",".join(format(i.split(':')[1])for i in ids).split(',')
            results['dc:identifier'] = scopus_ids
            return results
        except Exception as e:
            return  pd.DataFrame()
