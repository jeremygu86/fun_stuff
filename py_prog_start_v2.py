# Author: Wenxiao $$$
__author__ = 'wenxiaog'
# Purpose: Study python
# Created date: 2015/6/30 $$$
# Last updated: 2015/11/28

## ---- 1.Create Package ---- ##
## Ask Haoran Cai

# http://pythoncentral.io/how-to-create-a-python-package/
# http://blog.163.com/yang_jianli/blog/static/161990006201162152724339/
# http://python-packaging.readthedocs.org/en/latest/everything.html?highlight=git

## ---- 2.GitHub ---- ##
## Ask Haoran Cai
# https://help.github.com/articles/create-a-repo/



### Part 1: Load packages and the easiest examples
import os
import sys
print('Python %s on %s' % (sys.version, sys.platform))
print 'Python\'s defult directory:\n ', os.getcwd()

import numpy
np = numpy
from numpy import matrix
from numpy import linalg
from numpy.random import normal # normal(0,1,[5,2]) # mean, sd, size


import pandas
pd = pandas

import scipy
sp = scipy

import sklearn
sk = sklearn

import matplotlib
import matplotlib.pyplot as plt

# import graphlab
# gl = graphlab

def Folder(new_folder):
    print os.path.join(os.getcwd(),new_folder)
    directory = os.path.join(os.getcwd(),new_folder)
    print os.path.exists(directory)
    if not os.path.exists(directory):
        print "Path is created in ", os.getcwd()
        os.makedirs(directory)
    else:
        print new_folder, 'already exists so is not created.'

# 2015/7/4
# Import the regular expression library
import re

# Import the datetime library
import datetime
print 'This was last run on: {0}'.format(datetime.datetime.now())

#2015/7/9
from copy import deepcopy

# get web data
from bs4 import BeautifulSoup
import requests

# 2015/7/25: call r in python
## Method 1: pip install rpy2
# import rpy2
# def exr(rcommand):
#     import rpy2.robjects
#     print rpy2.robjects.r(rcommand)

## Method 2: open a pipe
from StringIO import StringIO
from subprocess import Popen, PIPE


## Vocabulary

# rpy2
# rpy2.robjects.r(command_str) # 'getwd()'





## Dazhengli.py
#### Basic Information $$$$
### Author: $$$
### Purpose: $$$
### Created date: $$$

## Last updated: $$
## Main updates: $$
## Note: $$
## $$
#### End $$$$

import os
# a = %pwd
# b = os.getcwd()
# print a
# print b

### Create a new folder
#new_folder = 'introduction_to_sframes'
def Folder(new_folder):
    print os.path.join(os.getcwd(),new_folder)
    directory = os.path.join(os.getcwd(),new_folder)
    print os.path.exists(directory)
    if not os.path.exists(directory):
        print "Path is created in ", os.getcwd()
        os.makedirs(directory)
    else:
        print new_folder, 'already exists so is not created.'

## Install, Import and update packages
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
##in progress
# package = 'numpy'
# abbrev = 'np'
# scr = "import "+ package +" as "+  abbrev
# print scr
# exec scr
# np1 = np.array([1,2,3])
# type(np1)
# def install_and_importV2(package,abbrev):
#     # import importlib
#     package = 'numpy'
#     abbrev = 'np'
#     scr = "import "+ package +" as "+  abbrev
#
#     #np1 = np.array([1,2,3])
#     #type(np1)
#
#     try:
#         print scr
#         exec scr
#     except ImportError:
#         import pip
#         pip.main(['install', package])
#     finally:
#         globals()[package] = importlib.import_module(package)


# Example
# install_and_import('transliterate')

# Automatically update all packages
def update_all():
    import pip
    from subprocess import call
    for dist in pip.get_installed_distributions():
        print dist
        call("pip install --upgrade " + dist.project_name, shell=True)

# not done.
# Automatically update the packageAZQ34
# def update_one(up_dist):
#     if up_dist in str(pip.get_installed_distributions()):
    # else:



##### The End #####
## still working on source.r :(
# import os,sys
# os.getcwd()
# sys.path.append(os.path.abspath("/Users/wenxiaog/pycharm/work2015"))
# import test_justtest as initialization
## can't load numpy
## ref: http://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files
def initial():
    print 'Initialization is completed. :) HAVE FUN'
initial()