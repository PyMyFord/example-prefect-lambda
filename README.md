# example-prefect-lambda

> Start your car from an AWS Lambda.

## Caveats

This tutorial does not cover authentication. **You will need to keep your URL secret in order to avoid others from starting your car!!** The minimum viable security for this tutorial is to require that a user pass a specific, secret header string or GET param. Do not leave this endpoint open to the world after completing this tutorial.

---

This is an example script that uses [PyMyFord/prefect](https://github.com/PyMyFord/prefect/) from an AWS Lambda running Python 3 to start a car remotely.

## Setup

### Generate a code bundle zipfile

You can either clone this repository or copy the code into your own `handler.py`. You will also need to create a new virtual environment:

```shell
$ virtualenv v-env
```

Once you have the following in your directory, you can zip it into a .zip file to upload to AWS Lambda.

```shell
$ ls
v-env/
handler.py
```

Zip the files like this:

```shell
$ zip -r9q prefect-lambda *
```

### Create a new Lambda

Navigate to the [AWS lambda console](https://console.aws.amazon.com/lambda/home) and click on "Create Function":

<img width="757" alt="image" src="https://user-images.githubusercontent.com/693511/71313819-2fe58580-240c-11ea-86f8-51dcd4044889.png">

Select the option to 'author the lambda from scratch.' Set the runtime to Python 3 (the latest as of writing is 3.8). The other default settings are fine for now:

<img width="846" alt="image" src="https://user-images.githubusercontent.com/693511/71313823-425fbf00-240c-11ea-81ff-10950f7bd1e5.png">

### Upload your code

#### Option 1: Web Console

Scroll to "Function Code" and select "upload a .zip". Upload the .zip you created in the previous step.

#### Option 2: `aws` CLI

You can also use the AWS command line utility (`aws`) to do this:

```shell
$ AWS_PROFILE=personal aws lambda update-function-code --function-name my-prefect-lambda --zip-file fileb://prefect-lambda.zip
```

### Set the environment variables

You must set `prefectuser` and `prefectpass` in the Environment Variables section of the console.

### Add an _API Gateway_ trigger

Scroll to the "Designer" section of the lambda page and click "Add Trigger":

<img width="918" alt="image" src="https://user-images.githubusercontent.com/693511/71313849-de89c600-240c-11ea-8f91-e7c09c81caba.png">

Select "API Gateway" from the dropdown:

<img width="857" alt="image" src="https://user-images.githubusercontent.com/693511/71313856-f7927700-240c-11ea-9e20-e0314765cd45.png">

Create a new API Gateway:

<img width="790" alt="image" src="https://user-images.githubusercontent.com/693511/71313868-2b6d9c80-240d-11ea-9c02-1f8c9e224c4d.png">

Press "Add".

Back on the lambda function screen, under the Designer section, click on the API Gateway to highlight it (it will turn light blue). The next section will become an API Gateway inspector, and will show you your new API Gateway trigger URL. **Note this, but protect it: This tutorial does not cover authentication, so anyone with this URL will be able to start your car!**

## Usage

```shell
$ curl https://[your_api_gateway_url].execute-api.us-east-1.amazonaws.com/[your_extension]
```
