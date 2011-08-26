===============
HOW TO USE THIS
===============

Create a skeleton for your new project
======================================

.. code-block:: bash

    $ svn export http://svn.github.com/nzupan/niteoweb.skel.plone.git niteoweb.<shortname>


Commit skeleton to repository
=============================

.. code-block:: bash

    $ cd niteoweb.<shortname>
    $ svn mkdir https://niteoweb.repositoryhosting.com/svn/niteoweb_<shortname>/niteoweb.<shortname> -m "creating package dir"
    $ svn add .
    $ svn ci -m "initial skeleton commit"

Customize
=========

 * Use search&replace to replace all placeholder strings with meaningful ones:
   Zulu, zulu, TODO.
 * Remove this entire paragraph from README.


============
Zulu project
============

:Project title: Zulu
:Project id: niteoweb.zulu
:Latest version: |release|
:Author: NiteoWeb Ltd.
:URL: http://zulu.com
:Source: http://sphinx.niteoweb.com/niteoweb.zulu
:Source: http://niteoweb.repositoryhosting.com/svn/niteoweb_zulu
:Framework: Plone 4.1
:Server: Omega

Quick Start
===========

.. sourcecode:: bash

  $ cd ~/work
  $ svn co https://niteoweb.repositoryhosting.com/svn/niteoweb_zulu/niteoweb.zulu/trunk niteoweb.zulu
  $ cd niteoweb.zulu/
  $ virtualenv -p python2.6 --no-site-packages ./
  $ bin/python bootstrap.py
  $ bin/buildout
