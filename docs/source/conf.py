# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
project = u'gen_unnamed_pipe'
copyright = u'2020, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.0.3'
release = u'https://github.com/vroncevic/gen_unnamed_pipe/releases/'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'gen_unnamed_pipedoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'gen_unnamed_pipe.tex', u'gen\\_unnamed\\_pipe Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'gen_unnamed_pipe', u'gen_unnamed_pipe Documentation',
    [author], 1
)]
texinfo_documents = [(
    master_doc, 'gen_unnamed_pipe', u'gen_unnamed_pipe Documentation',
    author, 'gen_unnamed_pipe', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
