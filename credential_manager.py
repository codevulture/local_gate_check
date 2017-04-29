import json
import requests
from requests.auth import HTTPDigestAuth

class GerritAuth():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #url name = 'https://review.openstack.org/a/access/'
        #payload={'project': 'openstack/xyz'}

    def authenticated_get_req(self, url, payload={}):
        response = requests.get(url, params=payload, auth=HTTPDigestAuth(self.username, self.password))
        return response

    def authenticated_post_req(self, url, payload={}, headers={}, data=''):
        response = requests.post(url, params=payload, auth=HTTPDigestAuth(self.username, self.password), data=json.dumps(data), headers=headers)
        return response

    def authenticated_put_req(self):
        response = requests.put(url, params=payload, auth=HTTPDigestAuth(self.username, self.password))
        return response

    def authenticated_delete_req(self):
        response = requests.delete(url, params=payload, auth=HTTPDigestAuth(self.username, self.password))
        return response
