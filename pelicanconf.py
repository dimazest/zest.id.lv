#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pelican_publications

AUTHOR = 'Dmitrijs Milajevs'
SITENAME = 'Dmitrijs Milajevs'
SITESUBTITLE = 'at Queen Mary University of London'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = 'theme'
EXTRA_TEMPLATES_PATHS = 'templates',

PLUGIN_PATHS = ('src/pelican-plugins', )
PLUGINS = (
    'extract_toc',
    'html_rst_directive',
    pelican_publications,
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# Menu
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Blog', 'index.html#blog'),
    ('Software', 'software'),
    ('Bibliography', 'bibliogrpahy.html'),
#    ('Brexit', 'brexit')
)

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/dimazest'),
    ('Facebook', 'https://www.facebook.com/dimazest'),
    ('Github', 'https://github.com/dimazest'),
    ('Bitbucket', 'https://bitbucket.org/dimazest'),
)

MAIL_USERNAME = 'dimazest'
MAIL_HOST = 'gmail.com'

TWITTER_USERNAME = 'dimazest'
DISQUS_SITENAME = 'dmitrijsmilajevs-qmul'
GITHUB_URL = 'https://github.com/dimazest'
GOOGLE_ANALYTICS = 'UA-1173947-7'
LINKEDIN_URL = 'http://www.linkedin.com/in/dmitrijsmilajevs'

STATIC_PATHS = (
    'images',
    'static/',
    'papers/*',
    #'static/ANDailment.csv',
)

EXTRA_PATH_METADATA = {
    #'static/ANDailment.csv': {'path': 'ANDailment.csv'},
    #'static/aclsrw2016_results.csv': {'path': 'aclsrw2016/results.csv'},
    #'static/aclsrw2016.zip': {'path': 'aclsrw2016/supplement.zip'},
    #'static/brexit/brexit_timeline.csv': {'path': 'brexit/brexit_timeline.csv'},
    #'static/brexit/brexit_tweets_ids.csv.gz': {'path': 'brexit/brexit_tweet_ids.csv.gz'},

    #'static/thesis/phraserel.csv': {'path': 'thesis/phraserel.csv'},
    #'static/thesis/phraserel-raw.csv': {'path': 'thesis/phraserel-raw.csv'},
    #'static/thesis/emnlp2013_turk_HighSim.txt': {'path': 'thesis/emnlp2013_turk_HighSim.txt'},
    #'static/thesis/emnlp2013_turk_MedSim.txt': {'path': 'thesis/emnlp2013_turk_MedSim.txt'},
    #'static/thesis/emnlp2013_turk_LowSim.txt': {'path': 'thesis/emnlp2013_turk_LowSim.txt'},
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

READERS = {'html': None}

LOGO_PATH = 'images/cover.jpg'

CACHE_CONTENT = False
