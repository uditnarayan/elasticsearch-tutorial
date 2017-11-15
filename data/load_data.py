import json
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

def test():
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res['created'])

    res = es.get(index="test-index", doc_type='tweet', id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


def load_laureate_json():
    print("Please wait. This will take a minute.")
    with open('laureate.json', 'r') as f:
        data = f.read()

    data = json.loads(data)
    laureates = data['laureates']
    total = len(laureates)

    loaded = 0
    failed = 0
    index = 0
    for laureate in laureates:
        index += 1
        id = int(laureate['id'])
        laureate['id'] = id
        died = laureate['died']

        for prize in laureate['prizes']:
            prize['year'] = int(prize['year'])
            prize['share'] = int(prize['share'])

        try:
            res = es.index(index="nobel_prize", doc_type='laureate', id=id, body=laureate)
            loaded += 1
        except:
            failed += 1

    es.indices.refresh(index="nobel_prize")
    print('Total:  {count}'.format(count=total))
    print('Loaded: {count}'.format(count=loaded))
    print('Failed: {count}'.format(count=failed))


load_laureate_json()