#!/usr/bin/python

from credential_manager import GerritAuth

class GerritReview():
    def __init__(self, username, password, base_url='https://review.openstack.org/a/'):
        self.base_url = base_url
        self.req = GerritAuth(username, password)
        #change base_url and remove /a/ if non-authenticated req is needed

    def fetch_plus_2_change(self, change_id):
        #TODO: Make generic so other projects could be added :D

        data = {
            "labels": {
            "Code-Review": +1
            }
        }

        headers={'Content-Type': 'application/json'}
        endpoint = self.base_url + "changes/%s/revisions/current/review" % change_id
        proj_list  = self.req.authenticated_post_req(endpoint, headers=headers, data=data)
        return proj_list

    def fetch_plus_1_change(self):
        #TODO:run full test suites if all  passes then proceed.
        pass

    def list_project(self):
        endpoint = self.base_url + "changes/"
        payload = self.create_payload()
        proj_list = self.req.authenticated_get_req(endpoint, payload)
        return proj_list

    def create_payload(self):
        #This is the most important part of code as everything depends on
        #payload but needs to be made more configurable :P
        #Hiding Query for anynymous reason :D
        #query = {} #Query
        return query
