import maya.standalone
import maya.cmds as cmds
import argparse

maya.standalone.initialize(name='python')

parser = argparse.ArgumentParser(description='Get maya command help')
parser.add_argument('cmdName', type=str, help="Command to Show Help")

args = parser.parse_args()
helpInfo = cmds.help(args.cmdName)
print(helpInfo)
