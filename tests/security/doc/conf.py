# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import pathlib

path = pathlib.Path(__file__).resolve() / '..' / '..' / 'security'
sys.path.insert(0, os.path.abspath('../security'))
sys.path.append(os.path.abspath('..'))

# sys.path.insert(0, os.path.abspath('..\src'))
sys.path.insert(0, os.path.abspath(path))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Security Tests'
copyright = '2025, SUSE'
author = 'QE Security'
release = '1.0'

tests_repo = 'https://github.com/os-autoinst/os-autoinst-distri-opensuse/'
tests_repo_base_url = f"{tests_repo}/tree/master"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
]

templates_path = ['_templates']
exclude_patterns = ['_build']
#include_patterns = ['security/**.pm']

extlinks = {
    'repo': (f'{tests_repo}/%s', '%s'),
    'master': (f'{tests_repo}/blob/master/%s', '%s')
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
