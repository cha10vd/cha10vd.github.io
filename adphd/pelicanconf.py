#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'victor'
SITENAME = u'AD(P)HD'
SITESUBTITLE = u'Science & Technology for the Inattentive Type'

SITEURL = 'http://vdn1m17.github.io'

PATH = 'content'

DEFAULT_DATE = 'fs' #file system timestamp information (mtime)
DEFAULT_DATE_FORMAT = '%d %b %Y' # %b = Month as locale's abbreviated name.

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook',  'https://www.facebook.com/vlnascimento'),
          ('Instagram','https://www.instagram.com/victordn.me/'),)


# Pagination
DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', \
        '{base_name}/page/{number}/index.html'),
)

# static paths will be copied without parsing their contents
STATIC_PATHS = ['assets']

# Not all metadata needs to be embedded in source file itself. For
# example, blog posts are often named following a YYYY-MM-DD-SLUG.rst
# pattern, or nested into YYYY/MM/DD-SLUG directories. To extract
# metadata from the filename or path, set FILENAME_METADATA or
# PATH_METADATA to regular expressions that use Python's group name
# notation (?P<name>...). If you want to attach additional metadata but
# don't want to encode it in the path, you can set
# EXTRA_PATH_METADATA

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'


### Plugins

PLUGIN_PATHS = [
    'plugins'
]

PLUGINS = [
        'ipynb.markup',
        'render_math.math'
        ]

# Sitemap
#SITEMAP = {
#    'format': 'xml',
#    'priorities': {
#        'articles': 0.5,
#        'indexes': 0.5,
#        'pages': 0.5
#    },
#    'changefreqs': {
#        'articles': 'monthly',
#        'indexes': 'daily',
#        'pages': 'monthly'
#    }
#}

# Comments
DISQUS_SITENAME = "adphd-1"

# Analytics
#GOOGLE_ANALYTICS = "UA-3546274-12"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'attila'

### Theme specific settings

HEADER_COVER = 'assets/images/page_header.jpg'

DISPLAY_PAGES_ON_MENU = False
DISLAY_THEMES_ON_MENU = True

AUTHORS_BIO = {
    "victor": {
        "name": "Victor Do Nascimento",
        "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
        "image": "assets/images/avatar.png",
        "linkedin":"https://www.linkedin.com/in/victor-luis-do-nascimento-38a493103/",
        "github": "cha10vd",
        "location": "Bournemouth",
        "bio": "PhD Candidade in Theoretical and Computational Chemistry at the University of Southampton"
    }
}

