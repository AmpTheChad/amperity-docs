# -*- coding: utf-8 -*-
#
# MARKUP documentation build configuration file.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

sys.path.append(os.path.abspath('../../_ext'))


# might be needed for Canny, if yes, should be here
# import jwt
# 
# canny_private_key = 'bd4601a9-32d6-8632-ac89-cd091e213c0b'
# 
# def create_canny_token(user):
#   user_data = {
#     'avatarURL': user.avatar_url, # optional but preferred
#     'email': user.email,
#     'id': user.id,
#     'name': user.name,
#   }
#   return jwt.encode(user_data, canny_private_key, algorithm='HS256')
# 


# -- General configuration -----------------------------------------------------


# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# 
# Cannot do this just yet:
# extensions = ['sphinx.ext.todo', 'recommonmark']
# because it breaks the search when RST and MD files are in the same location by truncating a SINGLE CHARACTER from the search result link :(
extensions = ['sphinx.ext.todo']

# autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', '../../_templates']

# The suffix of source filenames.
source_suffix = ['.rst']

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Amp360'
#copyright = u''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '0.0.1'
# The full version, including alpha/beta/rc tags.
# release = '0.0.1-1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'

# highlight_language = 'ruby'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# A string of reStructuredText that will be included at the beginning of every source file that is read.
rst_prolog = """
.. include:: ../../tokens/external_links.txt
.. include:: ../../tokens/internal_links.txt
.. include:: ../../tokens/names.txt
"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'amperity'
#html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../../_themes/']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Amp360"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = "../../images/logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# This setting overrides a version # stamp inserted at the bottom of every
# page. It's just a hack, but it's the hack that achieves the desired behavior.
# html_last_updated_fmt = 'current version of MARKUP documentation'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
   '**': ['localtoc.html'],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#    '404': '/internal/404.html',
html_additional_pages = {
    'bi_connect': 'bi_connect.html',
    'destination_facebook_ads': 'destination_facebook_ads.html',
    'sendto_active_campaign': 'sendto_active_campaign.html',
    'sendto_acxiom': 'sendto_acxiom.html',
    'sendto_adobe_aep': 'sendto_adobe_aep.html',
    'sendto_adobe_campaign': 'sendto_adobe_campaign.html',
    'sendto_adobe_customer_attributes': 'sendto_adobe_customer_attributes.html',
    'sendto_adobe_marketo': 'sendto_adobe_marketo.html',
    'sendto_amazon_pinpoint': 'sendto_amazon_pinpoint.html',
    'sendto_amazon_redshift': 'sendto_amazon_redshift.html',
    'sendto_amazon_s3': 'sendto_amazon_s3.html',
    'sendto_attentive_mobile': 'sendto_attentive_mobile.html',
    'sendto_aws_connect': 'sendto_aws_connect.html',
    'sendto_azure_blob_storage': 'sendto_azure_blob_storage.html',
    'sendto_bazaarvoice': 'sendto_bazaarvoice.html',
    'sendto_bi_tools': 'sendto_bi_tools.html',
    'sendto_bluecore': 'sendto_bluecore.html',
    'sendto_braze': 'sendto_braze.html',
    'sendto_campaign_monitor': 'sendto_campaign_monitor.html',
    'sendto_cheetah_digital': 'sendto_cheetah_digital.html',
    'sendto_cordial': 'sendto_cordial.html',
    'sendto_criteo': 'sendto_criteo.html',
    'sendto_databricks': 'sendto_databricks.html',
    'sendto_domo': 'sendto_domo.html',
    'sendto_dynamic_yield': 'sendto_dynamic_yield.html',
    'sendto_evocalize': 'sendto_evocalize.html',
    'sendto_experian': 'sendto_experian.html',
    'sendto_facebook_ads': 'sendto_facebook_ads.html',
    'sendto_google_ads': 'sendto_google_ads.html',
    'sendto_google_cloud_storage': 'sendto_google_cloud_storage.html',
    'sendto_google_customer_match': 'sendto_google_customer_match.html',
    'sendto_hubspot': 'sendto_hubspot.html',
    'sendto_infutor': 'sendto_infutor.html',
    'sendto_kibo': 'sendto_kibo.html',
    'sendto_klaviyo': 'sendto_klaviyo.html',
    'sendto_koupon_media': 'sendto_koupon_media.html',
    'sendto_listrak': 'sendto_listrak.html',
    'sendto_liveramp': 'sendto_liveramp.html',
    'sendto_mailchimp': 'sendto_mailchimp.html',
    'sendto_microsoft_ads': 'sendto_microsoft_ads.html',
    'sendto_microsoft_dataverse': 'sendto_microsoft_dataverse.html',
    'sendto_monetate': 'sendto_monetate.html',
    'sendto_neustar': 'sendto_neustar.html',
    'sendto_optimizely': 'sendto_optimizely.html',
    'sendto_oracle_data_cloud': 'sendto_oracle_data_cloud.html',
    'sendto_oracle_dmp': 'sendto_oracle_dmp.html',
    'sendto_oracle_responsys': 'sendto_oracle_responsys.html',
    'sendto_pebblepost': 'sendto_pebblepost.html',
    'sendto_persado': 'sendto_persado.html',
    'sendto_power_bi': 'sendto_power_bi.html',
    'sendto_powerreviews': 'sendto_powerreviews.html',
    'sendto_sailthru': 'sendto_sailthru.html',
    'sendto_salesforce_marketing_cloud': 'sendto_salesforce_marketing_cloud.html',
    'sendto_sftp': 'sendto_sftp.html',
    'sendto_snapchat': 'sendto_snapchat.html',
    'sendto_tableau': 'sendto_tableau.html',
    'sendto_throtle': 'sendto_throtle.html',
    'sendto_tiktok_ads': 'sendto_tiktok_ads.html',
    'sendto_vibes': 'sendto_vibes.html',
    'sendto_zendesk': 'sendto_zendesk.html'
}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sourcelink = False

# This is set to "False" because we don't want to show the default copyright, but
# do want to show the custom string defined by the "copyright" general setting (above).

html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.

# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Amp360'


# Edit this page on GitHub link
html_context = {
    "display_github": True, # Integrate GitHub
    "github_path": "https://github.com/amperity/amperity-docs/tree/main/amperity_amp360/source/", # Path in the checkout to the docs root
}