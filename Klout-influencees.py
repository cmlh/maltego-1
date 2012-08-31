#!/usr/bin/python
# Twitter ID to weighted influencers
# minor tweak
import sys
from MaltegoTransform import *
from pyklout import Klout

api = Klout("YOUR API KEY HERE")
me = MaltegoTransform();
me.debug("Starting Transform"); #Debug Info

name = str(sys.argv[1])
data = api.identity(name,'twitter')
user_id = data['id']
# fails hard if you feed it a name that doesn't have a Klout account
# really must find Python equivalent of Try::Tiny for this problem.
list = api.influences(user_id)

for inf in list['myInfluencees']:
    name = str(inf['entity']['payload']['nick']);
    score = str(int(inf['entity']['payload']['score']['score']));
    NewEnt = me.addEntity("AffiliationTwitter",name); 
    NewEnt.setWeight(score);
    NewEnt.addAdditionalFields("affiliation.uid","UID","",name);
    nurl = "http://twitter.com/" + name;
    NewEnt.addAdditionalFields("affiliation.profile-url","Profile URL","",nurl);
    NewEnt.addAdditionalFields("twitter.screen-name","Screen Name","",name);


me.returnOutput();
