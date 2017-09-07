# pcars 

[![Build Status](https://travis-ci.org/jamesremuscat/pcars.svg?branch=master)](https://travis-ci.org/jamesremuscat/pcars)
[![Coverage Status](https://coveralls.io/repos/jamesremuscat/pcars/badge.svg?branch=master&service=github)](https://coveralls.io/github/jamesremuscat/pcars?branch=master)

## INTRODUCTION

pcars is a Python client for the Project CARS UDP data stream.

## Quickstart

```python
from pcars.stream import PCarsStreamReceiver

class MyPCarsListener(object):
    def handlePacket(self, data):
        # You probably want to do something more exciting here
        # You probably also want to switch on data.packetType
        # See listings in packet.py for packet types and available fields for each
        print data


listener = MyPCarsListener()
stream = PCarsStreamReceiver()
stream.addListener(listener)
stream.start()
```
