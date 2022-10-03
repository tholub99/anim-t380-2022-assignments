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
baseRad = 1.25
coreRad = 1
headRad = 0.75

if(args.height == 'tall'):
    cmds.polySphere(r=baseRad, n=('bodyBase'))
    cmds.move(-1.7, y=True)
    
cmds.polySphere(r=coreRad, n=('bodyCore'))

cmds.polySphere(r=headRad, n=('bodyHead'))
cmds.move(1.4, y=True)

#Generate Hat
brimRad = 0.7
brimHeight = 0.1
crownRad = 0.4
crownHeight = 1

cmds.polyCylinder(r=brimRad, h=brimHeight, n=('hatBrim'))
cmds.move(2, y=True)

cmds.polyCylinder(r=crownRad, h=crownHeight, n=('hatCrown'))
cmds.move(2.5, y=True)

if(args.hasExtras):
    #Generate Buttons
    buttonRad = 0.1
    
    cmds.polySphere(r=buttonRad, n=('buttonLower'))
    cmds.move(0.95, z=True)

    cmds.polySphere(r=buttonRad, n=('buttonMiddle'))
    cmds.move(0, 0.25, 0.9)

    cmds.polySphere(r=buttonRad, n=('buttonUpper'))
    cmds.move(0, 0.5, 0.8)

    #Generate Face
    eyeRad = 0.1
    noseRad = 0.1
    noseHeight = 0.5
    
    cmds.polySphere(r=eyeRad, n=('eyeLeft'))
    cmds.move(0.25, 1.7, 0.6)

    cmds.polySphere(r=eyeRad, n=('eyeRight'))
    cmds.move(-0.25, 1.7, 0.6)

    cmds.polyCone(r=noseRad, h=noseHeight, n=('nose'))
    cmds.move(0, 1.5, 0.95)
    cmds.rotate('85deg', 0, 0)

cmds.file(save=True, typ=('mayaAscii'))