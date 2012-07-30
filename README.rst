===============
HOW TO USE THIS
===============

Create a skeleton for your new project
======================================

::

    $ svn export http://svn.github.com/niteoweb/niteoweb.skel.plone.git niteoweb.<shortname>
    $ cd niteoweb.<shortname>
    $ mv src/niteoweb/zulu src/niteoweb/<shortname>


Commit skeleton to repository
=============================

::

    $ svn mkdir https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/niteoweb.<shortname> -m "create package dir"
    $ svn mkdir https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/niteoweb.<shortname>/{trunk,tags,branches} -m "create svn structure"
    $ svn co https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/niteoweb.<shortname>/trunk ./
    $ svn add *


Customize
=========

 * Use search&replace to replace all placeholder strings with meaningful ones:
   Zulu, zulu, TODO.
 * Remove this entire paragraph ("How to use this") from README.rst.
 * Start coding :).


Initialize buildout, run tests, start Zope
==========================================

::

    $ virtualenv -p python2.7 --no-site-packages ./
    $ bin/python bootstrap.py
    $ bin/buildout
    $ bin/test
    $ bin/instance fg


#################### REMOVE EVERYTHING UNTIL THIS LINE #########################

=============
niteoweb.zulu
=============

:Framework: `Plone 4.2 <http://plone.org>`_
:Bug tracker: https://github.com/niteoweb/niteoweb.zulu/issues
:Source: https://github.com/niteoweb/niteoweb.zulu
:Documentation: http://niteowebzulu.readthedocs.org/
:Code status:

    .. image:: http://travis-ci.org/niteoweb/niteoweb.zulu.png
       :align: left
       :target: http://travis-ci.org/niteoweb/niteoweb.zulu

.. topic:: Summary

    One or two sentences about the project ...

Additional info about the projects' background, rationale, etc.
