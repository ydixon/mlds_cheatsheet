# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'notes_cheatsheet'
copyright = '2022'
author = 'Dickson Yu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.mathjax',
                'sphinx.ext.githubpages',
                # 'recommonmark',
                'myst_parser',
                ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme" #'alabaster'

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': False,
    'display_version': False
#    'logo_only': True,
}

def setup(app):
    app.add_css_file('custom.css')


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

myst_enable_extensions = [
    "amsmath",
    # "colon_fence",
    # "deflist",
    "dollarmath",
    # "fieldlist",
    # "html_admonition",
    # "html_image",
    # # "linkify",
    # "replacements",
    # "smartquotes",
    # "strikethrough",
    # "substitution",
    # "tasklist",
]

myst_dmath_double_inline = True