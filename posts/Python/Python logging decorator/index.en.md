---
weight: 1
title: "Python logging decorator"       # <<< Change here
date: 2023-01-01T02:12:42+00:00
lastmod: 2023-01-01T02:12:42+00:00
draft: false                
author: "Divyansh"
authorLink: "https://divyanshpatel.com"
description: "Python logging decorator"                    # <<< Change here
images: []
resources:
- name: "featured-image"
  src: "featured-image.jpg"

tags: ["python"]     # <<< Change here
categories: ["python"]               # <<< Change here

lightgallery: true

toc:
  auto: false
---

<!--more-->

# Python logging decorator

Here is an example of a Python decorator class that can be used for logging with a specified logging level:

To use this decorator, you would need to import the **`logging`**
 module and define a logger for your module or application. Then, you can use the decorator like this:

```jsx
import functools
import logging

class LoggingDecorator:
    
    def __init__(self, logger=None, level = logging.INFO):
        logging.basicConfig(level=level)
        self.logger = logger or logging.getLogger(__name__)
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.info(f'Starting {func.__name__}')
            result = func(*args, **kwargs)
            self.logger.debug(f'Finished {func.__name__}')
            return result
        return wrapper

# Use the decorator
@LoggingDecorator(level = logging.INFO)
def my_function():
    print("code her")
    pass

my_function()
```

This will cause the decorated function to log a debug message with the function name and result when it completes execution. The logging level can be specified as an argument to the decorator, so you can use the same decorator class to log at different levels (e.g., **`logging.INFO`**, **`logging.ERROR`**, etc.).

You can also modify the decorator class to accept additional arguments, such as a logger name or a log message format string.