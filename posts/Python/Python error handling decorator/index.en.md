---
weight: 1
title: "Python error handling decorator"     
date: 2022-10-22T17:52:53+00:00
lastmod: 2022-10-22T17:52:53+00:00
draft: false                
author: "Divyansh"
authorLink: "https://divyanshpatel.com"
description: "Python error handling decorator"                  
images: []
resources:
- name: "featured-image"
  src: "featured-image.jpg"

tags: ["python"]     # <<< Change here
categories: ["Python"]               # <<< Change here

lightgallery: true

toc:
  auto: false
---

<!--more-->

# Python error handling decorator

This decorator will catch any exceptions that occur when the decorated function (**`divide`**
 in this case) is called, and will handle the error by printing a message to the console. You can modify the decorator to handle the error in any way you like. For example, you might want to log the error, or return a default value instead of raising an exception.

```jsx
import functools

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Handle the error here
            print(f'An error occurred: {e}')
    return wrapper

@handle_errors
def divide(a, b):
    return a / b

divide(1, 0)  # An error occurred: division by zero
```