# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:13:17 2018

@author: miroslav
"""

#from markov_python.cc_markov import MarkovChain

from bs4 import BeautifulSoup

#import re

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
#soup = BeautifulSoup(''.join(doc))
soup = BeautifulSoup(html_doc, 'html.parser')

#print soup.prettify()

#print soup.text
print soup.
