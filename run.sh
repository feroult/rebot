#!/bin/bash

docker run -it \
    -e OPENAI_API_KEY=$OPENAI_API_KEY \
    rebot
