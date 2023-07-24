#!bin/bash

#Run the following command to uninstall all conflicting packages:

for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done -y

#Update the apt package index and install packages to allow apt to use a repository over HTTPS:

sudo apt-get update -y
sudo apt-get install ca-certificates curl gnupg -y

#Add Docker’s official GPG key:

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

#Use the following command to set up the repository:

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null -y

#Update the apt package index:

sudo apt-get update -y

#Install Docker Engine, containerd, and Docker Compose.

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

#To run Docker without root privileges

#Create the docker group

sudo groupadd docker -y

#Add your user to the docker group

sudo usermod -aG docker $USER -y

#Log out and log back in so that your group membership is re-evaluated

newgrp docker

#Verify that you can run docker commands without sudo

docker run hello-world
