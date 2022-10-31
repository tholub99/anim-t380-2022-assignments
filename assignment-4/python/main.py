import os
import re
import sys
import maya.cmds as cmds
import maya.standalone
import argparse

maya.standalone.initialize()

parser = argparse.ArgumentParser(description='This script iterates files!')
parser.add_argument('fileName', metavar='f', type=str,
                    help="Declare file name")

parser.add_argument('--new', dest='isNew', action='store_const',
                    const=True, default=False,
                    help="Create New File")

args = parser.parse_args()
global CWD = os.getcwd()
global FILE_FORMAT = '{asset}.{task}.{artist}.{version}.{ext}'

'''
Checks fileName for valid naming conventions
'''
def isValidName(fileName, isNew):
    if(isNew):
        res = re.fullmatch('^(\w+\.){2}(\w+)$', fileName)
        if(res == None):
            print('Invalid name for new file, follow the format:\nassetName.type.user')
            return False
    else:
        res = re.fullmatch('^(\w+\.){3}(\d+)(\.ma)$', fileName)
        if(res == None):
            print('Invalid name for iterable file, follow the format:\nassetName.type.user.#.ma')
            return False
    
    return True

'''
Creates a new file at iteration 1
'''
def CreateNewFile(asset, task, artist):
    asset_info = {
        'asset': asset,
        'task': task,
        'artist': artist, # usually built-in
        'version': 1,
        'ext': 'ma'
    }
    cmds.file(new=True)
    cmds.file(rn=(os.path.join(CWD, FILE_FORMAT.format(**asset_info))))
    
'''
Iterate File
'''
def IterateFile():
    fileName = cmds.file(q=True, sn=True)
    m = re.search('(\d+)\.ma', fileName)
    nextItr = str(int(m.group(1)) + 1) + '.ma'
    
    '''
    Rename File
    '''
    cmds.file(rn=(re.sub('(\d+)\.ma', nextItr, fileName)))


'''
MAIN
Open File or Create New File
'''
if(not isValidName(args.fileName, args.isNew)):
    sys.exit(1)

if(args.isNew):
    print('Creating New File...')
    CreateNewFile(args.fileName, CWD)

elif(cmds.file(os.path.join(CWD, args.fileName), q=True, ex=True)):
    print('Opening File')
    cmds.file(os.path.join(CWD, args.fileName), o=True)
    IterateFile()
else:
    print('File Not Found')
    sys.exit(2)
    
'''
Save file to dir as mayaAscii
'''
print('Saving')
cmds.file(save=True, typ=('mayaAscii'))