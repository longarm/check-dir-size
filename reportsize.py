#!/usr/bin/env python2

import os
import string

def reportSize():

    #content = os.popen('du -sh *').read() 
    content = ''' 11G  a/b/v/d  alpha
    
                  111G a/c/d/e beta
                  
                  150m  a/bd/dfe delta
                  
                  '''
    lines = content.split('\n')
    for line in lines:
        if(line.strip() != ''):
            tokens = line.split(' ')
            tokens = filter(None, tokens)
            oSize = tokens[0]
            length = len(oSize)
            unit = oSize[length - 1].upper()
            if (unit == 'G'):
                size = oSize[0:length - 1]
                if (string.atoi(size) >= 100):
                    # mail content to somebody
                    return

if __name__ == '__main__':
    reportSize()                    
