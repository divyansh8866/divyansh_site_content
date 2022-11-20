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
## Configuration (Web Console)

![Web Console](config.png)

`Name` **Required** : Name of the database. \
`Location` **Optional**:  Uniform resource identifier (uri) of data catlog which can be used by client. \
`Description` **Optional**: Description of the database.

---

## Configuration (serverless)

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
``` yaml

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

{{< admonition type=tip title="Tip" open=false >}}
Change `serverless` to `sls` in windows path variables to make deployment command easier.
{{< /admonition >}}

---

# Tables

{{< style "img { height: 19.25rem; }" >}} ![glue tables](table.jpg) {{< /style >}} 

The metadata definition for the data in a data store is a table in the AWS Glue Data Catalog. You can manually create a table in the AWS Glue console or generate a table when you run a crawler. The values of your table's metadata are shown in the Tables list in the AWS Glue console. When you develop ETL (extract, transform, and load) jobs, you use table definitions to identify sources and targets.

## Configuration (Web Console)

![glue tables](web-consol/1.png)
![glue tables](web-consol/2.png)

{{< admonition type=tip title="Tip" open=false >}}
If the Data source is in another account, you might need to give cross account permission.
{{< /admonition >}}

![glue tables](web-consol/3.png)
![glue tables](web-consol/4.png)
![glue tables](web-consol/5.png)
