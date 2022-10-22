---
weight: 1
title: "Python - Create .exe from .py file"     
date: 2022-10-22T17:52:53+00:00
lastmod: 2022-10-22T17:52:53+00:00
draft: false                
author: "Divyansh"
authorLink: "https://divyanshpatel.com"
description: "This post will show you on how to create stand alone .exe file from .py file"                  
images: []
resources:
- name: "featured-image"
  src: "featured-image.jpg"

tags: ["python", "pyinstaller", "pip"]     # <<< Change here
categories: ["Python"]               # <<< Change here

lightgallery: true

toc:
  auto: false
---

<!--more-->

# Create .exe from .py 
`python` `pyinstaller`

> Developer : __Divyansh Patel__

## Requirements 
Install python package : `pyinstaller`

___Note : be sure to use pip / pip3 based on your pip version.___
``` python
pip install pyinstaller
```

## Method
### Step 1 : ___Navigate in CMD to the directory___ where your .py file is residing which is to be converted to .exe.
### Step 2 : ___Use following command___ and execute in the same directory where your python file is present.
___Nore : Please replace file_name with your file name.___
``` python
pyinstaller --onefile <file_name>.py
```
### Step 3 : you will see additional files generated, To find the executable file, ___open the dist folder___.

Now you have stand alone executable file. Enjoy...
----
{{< admonition type=tip title="Reference" open=false >}}
[pyinstaller website](https://pyinstaller.org/en/stable/) 

[pip package](https://pypi.org/project/pyinstaller/)
{{< /admonition >}}
