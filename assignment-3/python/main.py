import os
import sys
import maya.cmds as cmds
import maya.standalone

maya.standalone.initialize()

'''
Try to find asset environment variable.
If missing/unset, exit program.
'''
try:
    ASSET = os.getenv('asset')
except:
    print('Environment variable $asset not found')
    sys.exit(1)

if(ASSET == None):
    print('Environment variable $asset not set')
    sys.exit(1)

'''
Create save path and maya file from CWD
If save path is invalid, exit program
'''
cwd = os.path.dirname(os.getcwd())
saveDir = 'assets\\{assetName}\\maya\\scenes\\assignment3.ma'.format(assetName = ASSET)
savePath = os.path.join(cwd, saveDir)
if(not os.path.exists(savePath)):
    print('Invalid save path, please make sure:\n1) The shell script was run\n2) This file is run from inside the python directory')
    sys.exit(2)

cmds.file(new=True)
cmds.file(rn=(savePath))

'''
Generate empty group with asset name
'''
cmds.group(empty=True, n=ASSET)

'''
Save maya file to dir as mayaAscii
'''
cmds.file(save=True, typ=('mayaAscii'))