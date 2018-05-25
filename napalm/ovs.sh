#Create an OpenVSwitch called napalm-net.
sudo ovs-vsctl add-br napalm-net

#Now we need to add a port on the new instance of OVS.
sudo ovs-vsctl add-port napalm-net host0 -- set Interface host0 type=internal

#Create a tap? a layer 2 device that acts like an ethernet adapater.
sudo ip tuntap add dev tap0 mode tap

#Turn up the tap.
sudo ip link set dev tap0 up

#Apply an IP address to the host port host0.
sudo ip addr add 172.16.2.100/24 dev host0

#Turn up the port host0.
sudo ip link set dev host0 up

#Place the tap in napalm-net.
sudo ovs-vsctl add-port napalm-net tap0

#Confirm that naplam-net has been correctly configured.
sudo ovs-vsctl show