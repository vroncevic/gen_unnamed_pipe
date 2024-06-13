Unnamed pipe generator
=======================

**gen_unnamed_pipe** is toolset for generation of apache virtual host skeleton for
development embedded applications.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool modules and provide instructions on
how to install the tool modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_unnamed_pipe python checker| |gen_unnamed_pipe python package| |github issues| |documentation status| |github contributors|

.. |gen_unnamed_pipe python checker| image:: https://github.com/vroncevic/gen_unnamed_pipe/actions/workflows/gen_unnamed_pipe_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_unnamed_pipe/actions/workflows/gen_unnamed_pipe_python_checker.yml

.. |gen_unnamed_pipe python package| image:: https://github.com/vroncevic/gen_unnamed_pipe/actions/workflows/gen_unnamed_pipe_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_unnamed_pipe/actions/workflows/gen_unnamed_pipe_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_unnamed_pipe.svg
   :target: https://github.com/vroncevic/gen_unnamed_pipe/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_unnamed_pipe.svg
   :target: https://github.com/vroncevic/gen_unnamed_pipe/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-unnamed-pipe/badge/?version=latest
   :target: https://gen-unnamed-pipe.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|gen_unnamed_pipe python3 build|

.. |gen_unnamed_pipe python3 build| image:: https://github.com/vroncevic/gen_unnamed_pipe/actions/workflows/gen_unnamed_pipe_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_unnamed_pipe/actions/workflows/gen_unnamed_pipe_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_unnamed_pipe/releases

To install **gen_unnamed_pipe** type the following

.. code-block:: bash

    tar xvzf gen_unnamed_pipe-x.y.z.tar.gz
    cd gen_unnamed_pipe-x.y.z/
    #python3
    python3 setup.py install_lib
    python3 setup.py install_data
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen-unnamed-pipe

Dependencies
-------------

**gen_unnamed_pipe** tool-module requires other modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_unnamed_pipe** is based on Template mechanism

Generator structure

.. code-block:: bash

    gen_unnamed_pipe/
        ├── conf/
        │   ├── gen_unnamed_pipe.cfg
        │   ├── gen_unnamed_pipe.logo
        │   ├── gen_unnamed_pipe_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── unp_close.template
        │       ├── unp_make.template
        │       ├── unp_read.template
        │       ├── unp.template
        │       └── unp_write.template
        ├── __init__.py
        ├── log/
        │   └── gen_unnamed_pipe.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        ├── py.typed
        └── run/
            └── gen_unnamed_pipe_run.py
    
    6 directories, 16 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2017 - 2024 by `vroncevic.github.io/gen_unnamed_pipe <https://vroncevic.github.io/gen_unnamed_pipe>`_

**gen_unnamed_pipe** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_unnamed_pipe/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`