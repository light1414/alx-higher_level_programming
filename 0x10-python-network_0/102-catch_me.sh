#!/bin/bash
# script that writes a request to 0.0.0.0:5000/catch_me receives the response "You got me!".
curl -o /dev/null -sw "You find me!" 0.0.0.0:5000/catch_me
