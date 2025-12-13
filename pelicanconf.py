AUTHOR = 'Kayleigh McMillan'
SITENAME = 'Ace Defective'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll - (Cleaned up default Pelican links)
#LINKS = (
#    ("Key2Pee (Project)", "#"),  # Placeholder until project page is ready
#)

# Social widget - (Updated for Patronage Model)
SOCIAL = (
    ('GitHub', 'https://github.com/[YOUR_GITHUB_USERNAME]'),
    ('Sponsor on GitHub', 'https://github.com/sponsors/[YOUR_GITHUB_USERNAME]'),
    ('Buy me a Coffee', 'https://ko-fi.com/[YOUR_KOFI_USERNAME]'),
    ('Mastodon', 'https://hachyderm.io/@AceDefective'),
)

DEFAULT_PAGINATION = 10

# ---------------------------------------------------------------------
# SECURITY & STATIC FILE CONFIGURATION
# ---------------------------------------------------------------------
# This tells Pelican to copy the security config to the root of the site
# preventing the browser from blocking it.
STATIC_PATHS = [
    'images', 
    'staticwebapp.config.json'
]

EXTRA_PATH_METADATA = {
    'staticwebapp.config.json': {'path': 'staticwebapp.config.json'},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True