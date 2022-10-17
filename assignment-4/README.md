
# ANIM T380 Assignment 4

## Tristan Holub (tjh347)

---

### Description

This assignment uses mayapy file commands to parse and iterate an asset file. Didn't have a lot of time this week so went with a really simple version that doesn't use the environment and updates the file name with regex.

### Usage 
>mayapy main.py [-h] [--new] f

This script iterates files!

positional arguments:
>  f :&emsp;Declare file name\
&emsp;New file :&emsp;&emsp;asset.type.user\
&emsp;Iterate file :&emsp; asset.type.user.#.ma

optional arguments:
> -h, --help :&emsp;show this help message and exit\
> --new :&emsp;&emsp;&ensp;Create New File


### Example

For new file:
> mayapy main.py --new asset.model.tholub

To iterate file:
> mayapy main.py asset.model.tholub.1.ma
