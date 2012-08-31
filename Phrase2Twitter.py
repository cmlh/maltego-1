#!/usr/bin/python
#
# If you have a list of Twitter names in a text file you can paste them
# into Maltego and they will appear as Phrase entities. You can select
# them all and choose 'Change Type', which provides a popup menu of
# entity types. If you pick Twitter Affiliation you'll end up with 
# what looks like Twitter accounts, but they are only *titled* based 
# on the name. Generally, when presented with a list of Twitter account
# names, you want to populate the entity name, the UID, the screen name,
# and I threw in the URL just for good measure.
#
#
#
import sys
from MaltegoTransform import *
name = str(sys.argv[1])
me = MaltegoTransform();
me.debug("Starting Transform"); #Debug Info
NewEnt = me.addEntity("AffiliationTwitter",name); 
NewEnt.setWeight(100);
NewEnt.addAdditionalFields("affiliation.uid","UID","",name);
nurl = "http://twitter.com/" + name;
NewEnt.addAdditionalFields("affiliation.profile-url","Profile URL","",nurl);
NewEnt.addAdditionalFields("twitter.screen-name","Screen Name","",name);

me.returnOutput();
