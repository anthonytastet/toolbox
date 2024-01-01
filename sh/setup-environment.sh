#!/bin/bash

# setup anthony's environment

apt update && \
apt upgrade -y && \
apt install -y xdg-utils && \
apt install -y firefox-esr && \
apt install -y git && \
git config --global user.name anthony && \
apt install -y gh && \
#su anthony -c "gh auth login" && \
#cd /home/anthony/ && \
#su anthony -c "gh repo clone custom-scripts" && \
#mv custom-scripts bin && \ 
apt install -y python3-venv python3-pip && \
pip3 install ansible && \
mkdir -p /etc/ansible/hosts && \
echo -e "[local]\n127.0.0.1   ansible_connection=local" > /etc/ansible/hosts/inventory.ini && \
ansible-playbook /home/anthony/toolbox/yaml/provisionning-debian.yaml -i /etc/ansible/hosts/inventory.ini
