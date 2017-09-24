# Python Bit Calculator (Web)

A web base bit calculator that produces a conversion table of bit/byte values.

## Screenshot

![Python Bit Calculator (Web)](doc/bitcalc.png?raw=true)

## Basic Requirements

* Functional install of Docker
* A bit of time to get the container running

## Quick start

* Copy `./config.py.example` to `./config.py`
* Open config.py and set a non-default value for `SECRET_KEY`
* Make any desired changes to `docker-compose.yml`
* Run `docker-compose up` and wait for the image to build and start
* Open your browser and connect to `127.0.0.1` (or whatever IP and port you expect)

## About
- This was primarily a learning exercise to build out a web UI for [pybitcalc](https://github.com/miliarch/pybitcalc).
- Inspired by [Matisse's Bit Calculator](http://www.matisse.net/bitcalc)
- Units conform to [Ubuntu Units Policy](https://wiki.ubuntu.com/UnitsPolicy)
