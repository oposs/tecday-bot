#!/bin/sh
. venv/bin/activate
sanic sanicbot:app -H 0.0.0.0 -p 8080 -d