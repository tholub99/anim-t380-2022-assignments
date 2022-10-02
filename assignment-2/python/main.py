import argparse

#parser = argparse.ArgumentParser(description='This script creates a bunch of cubes.')
#parser.add_argument('num_cubes', type=int, help="Number of cubes")

#args = parser.parse_args()

import maya.standalone
maya.standalone.initialize()

import maya.cmds as cmds

cmds.file(new=True)
cmds.file(rn=('test.ma'))

#Generate Body
cmds.polySphere(r=1, n=('bodyLower'))

cmds.polySphere(r=0.75, n=('bodyUpper'))
cmds.move(1.4, y=True)
#Generate Hat (brim + top)
cmds.polyCylinder(r=0.7, h=0.1, n=('hatBrim'))
cmds.move(2, y=True)

cmds.polyCylinder(r=0.4, h=1, n=('hatCrown'))
cmds.move(2.5, y=True)
#Generate Buttons (3 sphere on lower)
cmds.polySphere(r=0.1, n=('buttonLower'))
cmds.move(0.95, z=True)

cmds.polySphere(r=0.1, n=('buttonMiddle'))
cmds.move(0, 0.25, 0.9)

cmds.polySphere(r=0.1, n=('buttonUpper'))
cmds.move(0, 0.5, 0.8)
#Generate Face (eyes + nose)
cmds.polySphere(r=0.1, n=('eyeLeft'))
cmds.move(0.25, 1.7, 0.6)

cmds.polySphere(r=0.1, n=('eyeRight'))
cmds.move(-0.25, 1.7, 0.6)

cmds.polyCone(r=0.1, h=0.5, n=('nose'))
cmds.move(0, 1.5, 0.95)
cmds.rotate('85deg', 0, 0)

print("Meshes in the Maya scene:")
print(maya.cmds.ls(geometry=True))

cmds.file(save=True, typ=('mayaAscii'))