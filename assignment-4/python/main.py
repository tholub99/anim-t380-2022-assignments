import os
import maya.cmds as cmds
import maya.standalone

maya.standalone.initialize()


BASE_NAME = 'asset.model.tholub'
'''
Open File
If file exists:
Parse Name
If not:
Create new file starting at 1 (0?)
'''
if(cmd.file(ex=(fileName))):
    cmd.file(o=(fileName))
else:
    print('Creating new file')
    cmd.file(new=True)
    cmd.file(rn=(os.path.join(os.getcwd(), BASE_NAME + '.1')))
    
'''
Increment File name
'''
splitName = cmd.file(sn=True).split('.')
splitName[3] = str(int(splitName[3]) + 1)

'''
Rename File
'''
cmd.file(rn=((os.path.join(os.getcwd(), splitName.join('.')))))

'''
Save interated file to dir as mayaAscii
'''
cmds.file(save=True, typ=('mayaAscii'))