#!/bin/bash
#a script that makes request and display response
echo "$(curl -s -w '%{size_download}' -o /dev/null $1)"
