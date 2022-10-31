
# ANIM T380 Midterm

## Tristan Holub (tjh347)

---

### Description

This project creates a GUI that loads images from a folder and associated notes. It allows a user to edit these notes, remove notes, or add new notes to each individual image.

The user also has the option of editing an email list from a default list stored in config, selecting a different list stored in config, and creating their own config to store for future uses.

Finally, the user is able to trigger an email prompt containing all the image paths and notes from the reports. There is also an option to export an additional CSV with the image notes and information to view in excel.

---
## DISCLAIMER:
### This was built on/for a windows machine. I can't guarentee it will operate on another OS since it relies on a windows process call.
---

### Project Structure
```
project
│   README.md
│   code files (c#)   
│
└───bin
│   └───Release
│       └───net6.0-windows
│           │   PipelineMidterm.exe (Launch from here)
│   
└───email_configs
│   │   email configuration files (.ecfg)
│   
└───exports
│   │   email configuration files (.ecfg)
│       
└───image_notes
│   │   preset image txt notes
│   
└───images
    │   images files
```
>The project requires the above structure to operate, as it locates the config, export, notes, and image directories based on the working directory the exe is launched from.

### Setup
> Every image in `images` must have a corresponding txt file of the same name in the `image_notes` directory.
>> Image notes have a format of: 1st line artist, every other line is an individual note for that image

> Email Configurations must have a `.ecfg` extension and be located in the `email_configs` directory
>> The format for new configs is: 1st line `title`, every other line `Name, Email`

### Usage 
>Execute the exe file located in `bin\Release\net6.0-windows` as shown above

>The optional CSV file will be generated in the exports folder

>When editing the email list, your edits will persist unless you select another config from the dropdown.

