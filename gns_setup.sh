# add GN3 repo
sudo add-apt-repository ppa:gns3/ppa

# update system
sudo apt-get update

# install gns3
sudo apt-get install -y gns3-gui uml-utilities

# make napalm-net directory
mkdir ~/napalm-net/

# get software to build gns3 environment
wget "https://alta3.com/static/projects/ansible/vEOS-lab-4.17.8M.vmdk" -O ~/napalm-net/vEOS-lab-4.17.8M.vmdk
wget "https://alta3.com/static/projects/ansible/Aboot-veos-serial-8.0.0.iso" -O ~/napalm-net/Aboot-veos-serial-8.0.0.iso
wget "https://alta3.com/static/projects/ansible/arista-veos.gns3a" -O ~/napalm-net/arista-veos.gns3a

# expected result
echo "*************************************************************"
echo " EXPECTED RESULT: This should match what is in the lab manual"
echo "*************************************************************"
sha512sum ~/napalm-net/vEOS-lab-4.17.8M.vmdk
