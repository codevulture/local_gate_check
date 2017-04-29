import json
from review_type import GerritReview

if __name__ == '__main__':
    """
    Maintain a list of change id's which needs review.
    """
    username = ""
    password = ""
    #Hiding user/pass for anonymous reasons :)
    review = GerritReview(username, password)
    resp = review.list_project()

    json_resp = json.loads(resp.text.lstrip(')]}\''))
    #there is a problem with response it has some chars in starting
    #which leads to not loading of json properly

    count = 0
    change_id_list = []
    for i in json_resp:
        count += 1
        change_id_list.append(i['id'])
    print "Found --  %s  -- core reviewed and your unreviewed patches" % count
    print "Change Ids Found %r " % change_id_list


    #TODO: For each change id review the patch ;)
    for i in change_id_list:
        resp2 = review.fetch_plus_2_change(i)
