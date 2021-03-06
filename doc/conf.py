#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
from recommonmark.transform import AutoStructify
github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
    app.add_stylesheet('custom.css')


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_copybutton']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:

source_suffix = ['.rst', '.md']

from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}


# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Binder'
copyright = '2017, The Binder Team'
author = 'The Binder Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1b'
# The full version, including alpha/beta/rc tags.
release = '0.1b'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Binder Logo
html_logo = '_static/images/logo.png'
html_favicon = '_static/images/favicon.png'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Binderdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Binder.tex', 'Binder Documentation',
     'The Binder Team', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'binder', 'Binder Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Binder', 'Binder Documentation',
     author, 'Binder', 'One line description of project.',
     'Miscellaneous'),
]

# -- Scripts --------------------------------------------------------------

# Grab the latest version of the configuration file examples and howtos
print('Updating with latest configuration files list...')
url_config = "https://raw.githubusercontent.com/jupyter/repo2docker/master/docs/source/config_files.rst"
resp = requests.get(url_config)
with open('./config_files.rst', 'w') as ff:
    ff.write('.. DO NOT EDIT THIS FILE, IT IS IMPORTED IN `conf.py`...\n\n')
    ff.write(resp.text)

# Grab the latest version of the configuration file examples
print('Updating latest howto pages from repo2docker...')
howto_imports = ["languages.rst", "user_interface.rst"]
url_howto = "https://raw.githubusercontent.com/jupyter/repo2docker/master/docs/source/howto/{}"
for rst_file in howto_imports:
    this_url = url_howto.format(rst_file)
    resp = requests.get(this_url)
    dir_howto = os.path.join(os.path.dirname(__file__), 'howto')
    if not os.path.exists(dir_howto):
        os.makedirs(dir_howto)
    path_write = os.path.join(dir_howto, rst_file)
    with open(path_write, 'w') as ff:
        ff.write('.. THIS PAGE IS AUTOMATICALLY IMPORTED FROM {}.\n.. DO NOT EDIT IT DIRECTLY.\n'.format(this_url))
        ff.write(resp.text)
