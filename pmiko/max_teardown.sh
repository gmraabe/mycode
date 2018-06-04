#!/bin/bash
#~Alta3
#MAX_TEARDOWN

#ssh101 TEARDOWN
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
echo "ssh Done!"

#d2 TEARDOWN
echo "Cleaning up lab..."
echo "[0/4 complete]: stopping servers"
sudo docker stop indy &> /dev/null
echo "[1/4 complete]"
sudo docker rm indy &> /dev/null
echo "[2/4 complete]"
sudo docker network rm ansible-net &> /dev/null
echo "[3/4 complete]"
rm /tmp/labrunning &> /dev/null
echo "[4/4 complete]"
echo "d2 Done!"



#modules TEARDOWN
echo "Cleaning up lab..."
echo "[0/4 complete]: stopping servers"
sudo docker stop bender fry zoidberg farnsworth indy &> /dev/null
echo "[1/4 complete]"
sudo docker rm bender fry zoidberg farnsworth indy &> /dev/null
echo "[2/4 complete]"
sudo docker network rm ansible-net &> /dev/null
echo "[3/4 complete]"
rm /tmp/labrunning &> /dev/null
echo "[4/4 complete]"
echo "modules Done!"



###Alternative method teardown
#!/bin/bash

#wget https://alta3.com/static/projects/ansible/ssh101/teardown.sh -O teardown.sh
#bash teardown.sh

#wget https://alta3.com/static/projects/ansible/d2/teardown.sh -O teardown.sh
#bash teardown.sh
    
#wget https://alta3.com/static/projects/ansible/modules/teardown.sh -O teardown.sh
#bash teardown.sh




