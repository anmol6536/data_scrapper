from elsapy.elsclient import ElsClient
from elsapy.elsdoc import FullDoc, AbsDoc
from . import requests

class elsapy_connector():
    def __init__(self):
        req = requests.request_handler()
        print (req.apikey)
        self.client = ElsClient(req.apikey)
        pass

    def pii_search(self, df, rows = None):
        res = []
        count = 0
        if rows:
            df = df.loc[:rows-1]
        pii = df['pii'].dropna()
        for i in pii:
            data = FullDoc(sd_pii = i)
            if data.read(self.client):
                if type(data.data['originalText']) == str:
                    res.append([i, data, 'Paper found'])
                else:
                    res.append([i, data, 'No full text article found'])

                count += 1

            else:
                res.append([i, data, 'No full text article found'])
                count += 1

            if not count%20:
                print (f'{count} articles processed')
