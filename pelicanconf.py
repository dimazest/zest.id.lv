#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pelican_publications

AUTHOR = 'Dmitrijs Milajevs'
SITENAME = 'Dmitrijs Milajevs'
SITESUBTITLE = ''
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
    ('Software', 'software'),
    ('Bibliography', 'bibliography.html'),
    ('Reading list', 'reading-list.html'),
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
#DISQUS_SITENAME = 'dmitrijsmilajevs-qmul'
GITHUB_URL = 'https://github.com/dimazest'
GOOGLE_ANALYTICS = 'UA-1173947-7'
LINKEDIN_URL = 'http://www.linkedin.com/in/dmitrijsmilajevs'

STATIC_PATHS = (
    'images',
    'static/',
    'papers/*',
)

EXTRA_PATH_METADATA = {
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

READERS = {'html': None}

LOGO_PATH = 'images/cover.jpg'

CACHE_CONTENT = False
