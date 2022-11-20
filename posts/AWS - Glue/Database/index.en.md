---
weight: 1
title: "AWS - Glue (Database)"       
date: 2022-11-19T21:56:23+00:00
lastmod: 2022-11-19T21:56:23+00:00
draft: false                
author: "Divyansh"
authorLink: "https://divyanshpatel.com"
description: "Overview and introduction to AWS - Glue"                  
images: []
resources:
- name: "featured-image"
  src: "featured-image.jpg"

tags: ["AWS", "Glue"]    
categories: ["documentation"]              

lightgallery: true

toc:
  auto: false
---

<!--more-->

![Glue Database](glue_architecture.png)

In this section we will be looking at Database in AWS Glue service. \
**Data catalog:** Metadata and the structure of the data is stored in Data Catalog. \
**Database:** It is used to create or access the database for the sources and targets. \
**Table:** Create one or more tables in the database that can be used by the source and target.

---

# Database
## Database Configuration (Web Console)

![Web Console](config.png)

`Name` **Required** : Name of the database. \
`Location` **Optional**:  Uniform resource identifier (uri) of data catlog which can be used by client. \
`Description` **Optional**: Description of the database.

---

## Database Configuration (serverless)

### Prerequisites
**Note:** Please run this command to set AWS credentials in Serverless framework.

```
serverless config credentials --provider aws --key <KEY> --secret <SECRET_KEY> -o
```

Following should be added in to `.env` file in same directory as `serverless.yml` file.
``` 
SERVICE_NAME=glue-database
```

Serverless Code 
``` yml

service: ${env:SERVICE_NAME}
frameworkVersion: '3'
useDotenv: true

provider:
  name: aws

resources: # CloudFormation template syntax
  Resources:
    GlueDatabase:
      Type: AWS::Glue::Database
      Properties: 
        CatalogId: ${aws:accountId}   # serverless inbuild ENV variable
        DatabaseInput: 
          Description: "description here"
          # LocationUri: String   #Optional
          Name: test_databavse
```

Command to run serverless file (please run from same directory as serverless.yml)

```
 serverless deploy
```
