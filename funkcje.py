#!/usr/bin/python
# -*- coding: utf-8 -*-
#import osmium as o

import os, sys
from subprocess import (PIPE, Popen)

##
# Helpers
##
def run(cmd):
    '''
    Uruchom proces zewnętrzny, procesy zdefiniowane w konfig.py
    '''
    return Popen(cmd, stdout=PIPE, shell=True).stdout.read()

def filesizemb(filepath):
    if os.path.exists(filepath):
        return (float(os.path.getsize(filepath))/1048576)
    return -1

def usage():
    print 'Usage: ./extract.py obszar wykonaj'
    print '         obszar - określenie zasięgu ekstraktu'
    print '         wykonaj - wartości: sql || www'
    sys.exit()
##
# Helpers end
##
