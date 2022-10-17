import os
import re
import sys
import maya.cmds as cmds
import maya.standalone
import argparse

maya.standalone.initialize()

parser = argparse.ArgumentParser(description='This script creates a snowman!')
parser.add_argument('fileName', metavar='f', type=str,
                    help="Declare file name")

parser.add_argument('--new', dest='isNew', action='store_const',
                    const=True, default=False,
                    help="Create New File")

args = parser.parse_args()
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

    
def CreateNewFile(fileName, cwd):
    cmds.file(new=True)
    cmds.file(rn=(os.path.join(cwd, fileName + '.1.ma')))
    
'''
Iterate File name
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
Open File or Create New File
'''
cwd = os.getcwd()
if(not isValidName(args.fileName, args.isNew)):
    sys.exit(1)

if(args.isNew):
    print('Creating New File...')
    CreateNewFile(args.fileName, cwd)

elif(cmds.file(os.path.join(cwd, args.fileName), q=True, ex=True)):
    print('Opening File')
    cmds.file(os.path.join(cwd, args.fileName), o=True)
    IterateFile()
else:
    print('File Not Found')
    sys.exit(2)
    
'''
Save file to dir as mayaAscii
'''
print('Saving')
cmds.file(save=True, typ=('mayaAscii'))