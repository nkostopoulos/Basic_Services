DHCP server on Ubuntu 16.04  
  
First, install the dhcp server software  
sudo apt-get update  
sudo apt-get install -y isc-dhcp-server  
  
Then, configure the interface where the DHCP server listens to  
sudo vim /etc/default/isc-dhcp-server  
  
Then, configure the DHCP values  
sudo vim /etc/dhcp/dhcpd.conf  
  
Restart the server  
sudo systemctl restart isc-dhcp-server  
  
Based on tutorial by https://thelinuxcode.com/install-configure-dhcp-server-ubuntu-16-04-16-10/  
  
Request IP address with: sudo dhclient enp0s8  
