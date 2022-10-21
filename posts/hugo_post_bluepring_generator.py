import os
from datetime import datetime, timezone

FOLDER_NAME = "newPost"
utc_dt = datetime.now().astimezone().astimezone(timezone.utc)
MD_FILE_HEADER = """---
weight: 1
title: "Theme Documentation - Basics"       # <<< Change here
date: {}
lastmod: 2020-03-06T21:29:01+08:00
draft: false                
author: "Divyansh"
authorLink: "https://dillonzq.com"
description: "Change Me"                    # <<< Change here
images: []
resources:
- name: "featured-image"
  src: "featured-image.jpg"

tags: ["installation", "configuration"]     # <<< Change here
categories: ["documentation"]               # <<< Change here

lightgallery: true

toc:
  auto: false
---

""".format(utc_dt.isoformat(timespec='seconds'))


os.mkdir(FOLDER_NAME)
with open("{}/index.en.md".format(FOLDER_NAME), "w") as f:
    f.write(MD_FILE_HEADER)
