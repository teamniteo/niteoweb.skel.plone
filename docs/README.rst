============
Zulu project
============

:Project title: Zulu
:Project id: niteoweb.zulu
:Latest version: |release|
:Author: NiteoWeb Ltd.
:URL: http://zulu.com
:Docs: https://sphinx.niteoweb.com/niteoweb.zulu
:Source: https://niteoweb.repositoryhosting.com/svn/niteoweb_zulu
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
