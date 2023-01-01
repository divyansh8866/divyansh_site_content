---
weight: 1
title: "Getting started with Serverless"       # <<< Change here
date: 2023-01-01T00:26:20+00:00
lastmod: 2023-01-01T00:26:20+00:00
draft: false                
author: "Divyansh"
authorLink: "https://divyanshpatel.com"
description: "Getting started with Serverless"                    # <<< Change here
images: []
resources:
- name: "featured-image"
  src: "featured-image.jpg"

tags: ["serverless", "aws"]     # <<< Change here
categories: ["serverless"]               # <<< Change here

lightgallery: true

toc:
  auto: false
---

<!--more-->

# Getting started with serverless

To get started with the Serverless Framework and AWS, you will need to do the following:

- Install the Serverless Framework CLI:

To install the Serverless Framework CLI, you will need to have Node.js and npm (the Node.js package manager) installed on your local machine. You can then run the following command to install the Serverless Framework CLI:

```yaml
npm install -g serverless

```

- Set up your AWS credentials:

To use the Serverless Framework with AWS, you will need to set up your AWS credentials. You can do this by running the following command:

```yaml

serverless config credentials --provider aws --key YOUR_AWS_ACCESS_KEY --secret YOUR_AWS_SECRET_KEY
```

- Create a new serverless application:

To create a new serverless application, you can run the **`serverless create`** command and specify the name of your application and the cloud provider you want to use. For example:

```yaml

serverless create --template aws-nodejs --path my-app
```

This will create a new directory called **`my-app`** that contains the basic structure of a serverless application, including a configuration file (**`serverless.yml`**) and a sample function (**`handler.js`**).

1. Define your functions and events:

Next, you will need to define your functions and the events that trigger them in the **`serverless.yml`** configuration file. This file is written in YAML and specifies all of the different components of your serverless application, including the functions, events, and resources needed by the application.

Here is an example of a simple function that is triggered by an HTTP request:

```yaml
functions:
  hello:
    handler: handler.hello
    events:
      - http:
          path: /
          method: get
```

This function is defined in the **`handler.js`** file and is triggered by an HTTP GET request to the root path (**`/`**).

- Deploy your application:

Once you have defined your functions and events, you can deploy your application to AWS by running the **`serverless deploy`** command. This will create all of the necessary resources in AWS and deploy your code to the cloud.

```yaml
serverless deploy
```

That's it! You should now have a working serverless application on AWS. You can test your function by sending an HTTP request to the URL provided by the Serverless Framework after the deployment is complete.


----

{{< admonition type=tip title="Reference" open=false >}}
[Serverless website](https://www.serverless.com) 

{{< /admonition >}}