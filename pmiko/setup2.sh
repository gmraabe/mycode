#!/bin/bash
if [ -f "/tmp/labrunning" ] ; then
  echo "                                       "
  echo -e "\033[0;31m        ▄██████████████▄▐█▄▄▄▄█▌       \033[0m" 
  echo -e "\033[0;31m        ██████▌▄▌▄▐▐▌███▌▀▀██▀▀        \033[0m" 
  echo -e "\033[0;31m        ████▄█▌▄▌▄▐▐▌▀███▄▄█▌          \033[0m" 
  echo -e "\033[0;31m        ▄▄▄▄▄██████████████▀           \033[0m" 
  echo "                                       "
  echo " --> ! You forgot to teardown.sh ! <-- "
  echo "                                       "
  echo " Take 10s to think about what you did. "
  secs=$((10))
  while [ $secs -gt 0 ]; do
    echo -ne "                   $secs\033[0K\r"
    sleep 1
    : $((secs--))
  done
  echo " Lab setup failed! You know what to do."
  exit 1
else
  touch /tmp/labrunning
fi
echo "Building lab..."

### Create networks
sudo docker network create --opt com.docker.network.driver.mtu=1450 --subnet 10.10.1.0/24 ansible-net

sudo docker build -q --build-arg user=john   --tag ssh-pn $HOME/.config/dockerfiles/ansible/ssh-pn
sudo docker build -q --build-arg user=paul   --tag ssh-pp $HOME/.config/dockerfiles/ansible/ssh-pp
sudo docker build -q --build-arg user=george --tag ssh-ps $HOME/.config/dockerfiles/ansible/ssh-ps
sudo docker build -q --build-arg user=stuart --tag ssh-kn $HOME/.config/dockerfiles/ansible/ssh-kn
sudo docker build -q --build-arg user=pete   --tag ssh-kp $HOME/.config/dockerfiles/ansible/ssh-kp
sudo docker build -q --build-arg user=ringo  --tag ssh-ks $HOME/.config/dockerfiles/ansible/ssh-ks

### Launch containers and connect networks
sudo docker run -d  --name john      -h john   --ip 10.10.1.2 --network ansible-net ssh-pn 
sudo docker run -d  --name paul      -h paul   --ip 10.10.1.3 --network ansible-net ssh-pp
sudo docker run -d  --name george    -h george --ip 10.10.1.4 --network ansible-net ssh-ps
sudo docker run -d  --name stuart    -h stuart --ip 10.10.1.5 --network ansible-net ssh-kn
sudo docker run -d  --name pete      -h pete   --ip 10.10.1.6 --network ansible-net ssh-kp
sudo docker run -d  --name ringo     -h ringo  --ip 10.10.1.7 --network ansible-net ssh-ks

echo "Complete!"
