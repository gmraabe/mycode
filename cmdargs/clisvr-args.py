#!/usr/bin/env python3
# clisvr-args.py
# Micah Raabe

# Lab 63 - Argument Parsing

import argparse, socket
from datetime import datetime

def server(port):
    x = "Your choice was server and it will run on port " + str(port)
    return x

def client(port):
    x = "Your choice was client and it will run on port " + str(port)
    return x

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    parser.add_argument('-t', metavar='TYPE', type=str, default='UDP', help='Protocol Type (default UDP)')

args = parser.parse_args()
function = choices[args.role]
print(function(args.p) + ' with a protocol type of ' + args.t)
