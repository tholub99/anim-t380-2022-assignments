import maya.standalone
maya.standalone.initialize(name='python')
import maya.cmds as cmds
import argparse

parser = argparse.ArgumentParser(description='Get maya command help')
parser.add_argument('cmdName', type=str, help="Command to Show Help")

args = parser.parse_args()
helpinfo = cmds.help(args.cmdName)
print(helpinfo)