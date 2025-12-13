AUTHOR = 'Kayleigh McMillan'
SITENAME = 'Ace Defective'
SITEURL = ""
SITETITLE = "Ace Defective"
SITESUBTITLE = "System Failure: A Devlog"
SITEDESCRIPTION = "Man vs Machine. A documentation of breakage."
SITELOGO = "" 
# (We can add a logo path later, e.g., SITELOGO = "/images/logo.png")

PATH = "content"
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# ---------------------------------------------------------------------
# THEME CONFIGURATION (FLEX)
# ---------------------------------------------------------------------
THEME = "themes/Flex"
THEME_COLOR = 'dark'  # The critical Dark Mode setting
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False # Force Dark Mode always
PYGMENTS_STYLE = 'monokai' # Dark code highlighting

# ---------------------------------------------------------------------
# FEED SETTINGS
# ---------------------------------------------------------------------
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ---------------------------------------------------------------------
# LINKS & SOCIAL
# ---------------------------------------------------------------------
# Blogroll (Empty for now)
LINKS = ()

SOCIAL = (
    ('github', 'https://github.com/YOUR_GITHUB_USER'),
    ('coffee', 'https://ko-fi.com/YOUR_KOFI_USER'),
    ('mastodon', 'https://hachyderm.io/@AceDefective'),
)

MAIN_MENU = True
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

DEFAULT_PAGINATION = 10

# ---------------------------------------------------------------------
# STATIC FILES & SECURITY
# ---------------------------------------------------------------------
STATIC_PATHS = [
    'images', 
    'staticwebapp.config.json'
]

EXTRA_PATH_METADATA = {
    'staticwebapp.config.json': {'path': 'staticwebapp.config.json'},
}

# RELATIVE_URLS = True