===============
HOW TO USE THIS
===============

Create a skeleton for your new project
======================================

::

    $ svn export http://svn.github.com/niteoweb/niteoweb.skel.plone.git niteoweb.<shortname>
    $ cd niteoweb.<shortname>
    $ mv src/niteoweb/zulu src/niteoweb/<shortname>
    $ mkdir docs/sphinx/_static


Commit skeleton to repository
=============================

::

    $ svn mkdir https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/niteoweb.<shortname> -m "create package dir"
    $ svn mkdir https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/niteoweb.<shortname>/{trunk,tags,branches} -m "create svn structure"
    $ svn co https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/niteoweb.<shortname>/trunk ./
    $ ln -s development.cfg buildout.cfg
    $ svn add *


Customize
=========

 * Use search&replace to replace all placeholder strings with meaningful ones:
   Zulu, zulu, TODO.
 * Remove this entire paragraph ("How to use this") from README.rst.
 * Start coding :).


Initialize buildout and start Zope
==================================

::

    $ virtualenv -p python2.6 --no-site-packages ./
    $ bin/python bootstrap.py
    $ bin/buildout
    $ bin/instance fg



#################### REMOVE ALL BUT THE FOLLOWING LINE ####################

See `docs/README.rst <https://sphinx.niteoweb.com/niteoweb.zulu>`_.