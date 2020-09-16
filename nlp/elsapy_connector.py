from elsapy.elsclient import ElsClient
from elsapy.elsdoc import FullDoc, AbsDoc

class elsapy_connector():
    def __init__(self):
        pass

    def pii_search(self, df, rows = None):
        res = []
        count = 0
        if rows:
            df = df.loc[:rows-1]
        pii = df['pii'].dropna()
        for i in pii:
            data = FullDoc(sd_pii = i)
            if data.read(client):
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