#!/bin/bash

mkdir packages
# Spin up a docker container to pull in the dependencies so we can build on Amazon Linux for the native libs
docker run --rm -v "$PWD":/var/task lambci/lambda:build-python3.7 pip3 install -r requirements.txt -t packages
