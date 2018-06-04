#!/bin/bash

# TEARDOWN
echo "Cleaning up lab..."
echo "[0/4 complete]: stopping servers"
sudo docker stop john paul george stuart pete ringo &> /dev/null
echo "[1/4 complete]"
sudo docker rm john paul george stuart pete ringo &> /dev/null
echo "[2/4 complete]"
sudo docker network rm ansible-net &> /dev/null
echo "[3/4 complete]"
rm /tmp/labrunning &> /dev/null
echo "[4/4 complete]"
echo "Done!"


