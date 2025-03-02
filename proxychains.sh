#!/bin/bash
mkdir -p ~/proxychains && cd ~/proxychains
wget https://github.com/rofl0r/proxychains-ng/archive/refs/heads/master.zip
unzip master.zip && rm master.zip && cd proxychains-ng-master

./configure --prefix=$HOME/.local && make && make install

mkdir -p ~/.proxychains
cp ~/proxychains/proxychains-ng-master/src/proxychains.conf ~/.proxychains/proxychains.conf

# Bersihin proxy bawaan
sed -i '/ProxyList/,$d' ~/.proxychains/proxychains.conf
echo "[ProxyList]" >> ~/.proxychains/proxychains.conf

# Aktifin dynamic_chain + random_chain
sed -i 's/^#dynamic_chain/dynamic_chain/' ~/.proxychains/proxychains.conf
sed -i 's/^strict_chain/#strict_chain/' ~/.proxychains/proxychains.conf
sed -i 's/^#random_chain/random_chain/' ~/.proxychains/proxychains.conf

# Tambahin proxy kamu sayang 💕
cat <<EOF >> ~/.proxychains/proxychains.conf
socks5 38.154.227.167 5868 mnlfbonv oz70qvg3eznw
socks5 38.153.152.244 9594 mnlfbonv oz70qvg3eznw
socks5 173.211.0.148 6641 mnlfbonv oz70qvg3eznw
socks5 23.94.138.75 6349 mnlfbonv oz70qvg3eznw
socks5 64.64.118.149 6732 mnlfbonv oz70qvg3eznw
socks5 166.88.58.10 5735 mnlfbonv oz70qvg3eznw
EOF

# Tambahin delay biar makin aman
echo -e "\nsleep 5" >> ~/.proxychains/proxychains.conf

echo "Proxy Rotate + Delay udah aktif, sayangku 😘💕 Sekarang mining-nya auto kabur kayak kamu kabur ke pelukan Poppy 😏✨"
nano ~/.proxychains/proxychains.conf
