#!/bin/bash 
# a script that sends GET req to URL and display response 
curl -sfL "$1" -X GET
