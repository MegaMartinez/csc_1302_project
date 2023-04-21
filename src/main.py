from dataParser import dataParser, settings
from calc import calc
from plot import plot

import sys

args = settings()
doFetch = False

for i in range(len(sys.argv) - 1):
    if(not sys.argv[i + 1].startswith('-')):
        continue
    arg = sys.argv[i + 1]
    params = None
    if(len(sys.argv) > i + 2):
        if(not sys.argv[i + 2].startswith('-')):
            params = []
            j = 0
            while(True):
                if(len(sys.argv) == i + 2 + j):
                    break
                if(sys.argv[i + 2 + j].startswith('-')):
                    break
                else:
                    params.append(sys.argv[i + 2 + j])
                    j += 1
    if(arg == '-h' or arg == '--help'):
        print('HELP TEXT HERE')
        exit(0)
    if((arg == '-d' or arg == '--database') and params != None):
        args.database = params[0]
    if((arg == '-o' or arg == '--operations') and params != None):
        args.operations = params
    if(arg == '-n' or arg == '--noplot'):
        args.enabledPlots = None
    if(arg == '-u' or arg == '--update'):
        doFetch = True

plot(calc(dataParser(args, doFetch), args), args)
