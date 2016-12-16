=========
Software
=========

:date: 2016-01-10 18:13
:save_as: software/index.html
:url: software

.. contents::
    :depth: 0

``poultry``
===========

:documentation: http://poultry.readthedocs.org/en/latest/
:code: https://github.com/dimazest/poultry
:pypi: https://pypi.python.org/pypi/poultry

Poultry is a tweet collection manager. With it I've collected the London
Olympics tweets. Also, it easily gathered tweets about the major European music
festivals.

``google-ngram-downloader``
===========================

:code: https://github.com/dimazest/google-ngram-downloader
:pypi: https://pypi.python.org/pypi/google-ngram-downloader

An easy way to access ngram counts in a streaming fashion:

.. code-block:: python

    >>> from google_ngram_downloader import readline_google_store
    >>>
    >>> fname, url, records = next(readline_google_store(ngram_len=5))
    >>> fname
    'googlebooks-eng-all-5gram-20120701-0.gz'
    >>> url
    'http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20120701-0.gz'
    >>> next(records)
    Record(ngram=u'0 " A most useful', year=1860, match_count=1, volume_count=1)


``turing-machine``
==================

:code: https://github.com/dimazest/turing_machine
:pypi: https://pypi.python.org/pypi/turing_machine
:notebook: http://nbviewer.ipython.org/github/dimazest/turing_machine/blob/master/Turing%20machine.ipynb


A simulator of a Turing machine implemented as a generator. The most pythonic
implementation in the whole Internet!


This webpage
============

.. :code: https://bitbucket.org/dimazest/dima_qmul_homepage/src

It's is created with `Pelican <http://docs.getpelican.com>`_ and a bunch of
plugins, most notable being `pelican_publications
<https://github.com/dimazest/pelican_publications>`_ (a fork of
https://github.com/adamreeve/pelican_publications), which nicely shows `the
papers I'm interested in <{filename}/pages/bibliography.rst>`_.
