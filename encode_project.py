import requests
import json
from urllib.parse import urlencode, quote_plus


class EncodeProject:
    def __init__(self, url, user_id=None, password=None):
        self.base_url = url
        self.user_id = user_id
        self.password = password
        self.headers = {'accept': 'application/json'}

    def login(self):
        # Currently, there is no authentication. Stubbed for when things change
        pass

    def get_request(self, end_point, data_id=None, params=None):
        if data_id:
            end_point = '{}/{}'.format(end_point, data_id)

        if params:
            end_point = '{}/?{}'.format(end_point, urlencode(
                params, quote_via=quote_plus))

#        url = '{}/{}/?frame=object'.format(self.base_url, end_point)
        url = '{}/{}'.format(self.base_url, end_point)

# https://www.encodeproject.org/search/?type=Experiment&status=released&assay_title=TF+ChIP-seq&award.project=ENCODE&advancedQuery=date_released%3A%5B2012-08-01+TO+2012-08-31%5D
        response = requests.get(url, headers=self.headers)
        return response


encode_project = EncodeProject('https://www.encodeproject.org')
encode_project.login()

date_range = '2012-08-01 TO 2012-08-31'
search_criteria = {'type': 'Experiment', 'status': 'released',
                   'assay_title': 'TF ChIP-seq', 'award.project': 'ENCODE',
                   'advancedQuery': 'date_released:[{}]'.format(date_range),
                   'frame': 'object'}
resp = encode_project.get_request('search', data_id=None, params=search_criteria)

print(json.dumps(resp.json(), indent=4))
