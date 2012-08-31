Maltego
=======

This repository is a collection of things I have written for use with Paterva's Maltego OSINT & forensics application. The other tool I use heavily is Splunk, which is an enterprise grade datacenter logging application. Python is the favored tool of the guys from Paterva, Splunk is written in it as well as many of the free Splunkbase apps, and the Natural Language Tool Kit project uses it, too. I am new to Python, but it seems to be the language to use for the set of problems I enjoy solving.

Support Systems:
===========================

Maltego costs $650 and the minimum Splunk license is $5,000. If that's too steep for you the following will work:

Maltego Community Edition is free. You get *very* limited access to the Maltego community transform server and you have to solve a captcha every three days in order to continue using the system. The transforms I publish use either local resources or third party APIs and the only limits are those imposed by the API providers themselves. You CAN do useful work with MaltegoCE.

http://www.paterva.com/web5/client/community.php


Splunk has a free version of their system but it has a variety of limitations. Only two of those that appear to matter are the 500 meg a day cap on data and the lack of individual userids. 500 meg is enough space for about two million tweets or four million lines of IRC logs - the limit is a barrier to datacenter users, but not to someone doing studies of Twitter, IRC, or any other human generated, time stamped data. The login restriction is a bit of a bother - you get one account and it's got full permissions for the system, so you can only share your work with very trusted associates. There are no limits to web, command line, or API access.

http://www.splunk.com/view/free-vs-enterprise/SP-CAAAE8W

Accessing APIs
===========================

There are a variety of API calls that I use. Some are open and simply require that you know the URL. Others require a registration and they provide you with a unique key. Twitter itself uses an oauth scheme in order for you to gain access. Twitter API access is a bit of a chore for the uninitiated so I will probably create a howto for it, but in general the APIs that are interesting already have a Python package associated with them.

The following are APIs that I am considering for integration


Alchemy:
========

Maltego comes with access to the Alchemy API via some of its transforms. There are certain specific problems that the base transforms don't address so this is an area for development.

http://www.alchemyapi.com/products/


OpenCalais:
===========

Like Alchemy, this text search oriented API is bundled with Maltego's default transforms, but a framework to expand on its uses will be helpful.

http://www.opencalais.com/CommercialCalais


Klout:
======

Klout provides an influence rating on a scale of 1 to 100 for social media presences. Presented with a valid account name it can return the account's influencers and influencees. When working with memes moving in populations this influencer/influencee information is often more useful that the friend/follower information available with the default Maltego transforms.

http://klout.com/s/developers/home


DomainTools:
============

DomainTools provides advanced search capabilities on domains including historical data. The results from these calls are often fairly large amounts of text, at least in terms of what one can put in a Maltego entity. There may be a case for a transform that begins with a domain name and gets back a 'note', which is the technical term for expanded descriptive text associated with an entity.

http://www.domaintools.com/api/docs/


InfoChimps:
===========

InfoCchimps is a wonderland of datasets and API accessible big data services. I am curious about the TrstRank API, which provides an assessment of how much two given accounts interact over time and the Twiter Influence Metrics provide similar information to what the Klout API gives.

http://www.infochimps.com/marketplace/social


Sunlight:
=========

Sunlight Foundation offers a set of APIs specifically focused on members of Congress, their committee assignments, and other things of interest for both elections and policy making.

http://services.sunlightlabs.com/

Python Libraries
===========================

You will need to be familiar with Python to the level of using the pip command to install and upgrade certain packages. Maltego offers competing Python packages with different features. I have looked at all three and settled on MaltegoTransform-py-101 for my initial work.

http://www.paterva.com/web5/general/resources.php



I have looked at several of the Twitter specific Python packages on PyPI. The twitter package provides twitter-log, which is easily modified to produce CSV files suitable for use in Splunk or as flat file databases for Maltego transforms. The python-twitter package is a full featured Python wrapper for the Twitter API and I find it much easier to support when installing things on remote, headless systems.

http://pypi.python.org/pypi/twitter/1.9.0

http://pypi.python.org/pypi/python-twitter/0.8.2