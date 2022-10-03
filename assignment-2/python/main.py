import sys
import maya.cmds as cmds
import maya.standalone
import argparse

maya.standalone.initialize()

parser = argparse.ArgumentParser(description='This script creates a snowman!')
parser.add_argument('height', metavar='H', type=str,
                    help="Declare snowman height: tall/short")

parser.add_argument('--nox', dest='hasExtras', action='store_const',
                    const=False, default=True,
                    help="Hide extra snowman features")

args = parser.parse_args()
if(args.height != 'tall' and args.snow_height != 'short'):
    print('invalid snowman height parameter, must be: [ tall | short ], you gave: ' + args.snow_height)
    sys.exit(0)
    

cmds.file(new=True)
cmds.file(rn=('holub_assignment2.ma'))

#Generate Body
if(args.height == 'tall'):
    cmds.polySphere(r=1.25, n=('bodyLower'))
    cmds.move(-1.7, y=True)
    
cmds.polySphere(r=1, n=('bodyBase'))

cmds.polySphere(r=0.75, n=('bodyUpper'))
cmds.move(1.4, y=True)

#Generate Hat
cmds.polyCylinder(r=0.7, h=0.1, n=('hatBrim'))
cmds.move(2, y=True)

cmds.polyCylinder(r=0.4, h=1, n=('hatCrown'))
cmds.move(2.5, y=True)

if(args.hasExtras):
    #Generate Buttons
    cmds.polySphere(r=0.1, n=('buttonLower'))
    cmds.move(0.95, z=True)

    cmds.polySphere(r=0.1, n=('buttonMiddle'))
    cmds.move(0, 0.25, 0.9)

    cmds.polySphere(r=0.1, n=('buttonUpper'))
    cmds.move(0, 0.5, 0.8)

    #Generate Face
    cmds.polySphere(r=0.1, n=('eyeLeft'))
    cmds.move(0.25, 1.7, 0.6)

    cmds.polySphere(r=0.1, n=('eyeRight'))
    cmds.move(-0.25, 1.7, 0.6)

    cmds.polyCone(r=0.1, h=0.5, n=('nose'))
    cmds.move(0, 1.5, 0.95)
    cmds.rotate('85deg', 0, 0)

cmds.file(save=True, typ=('mayaAscii'))