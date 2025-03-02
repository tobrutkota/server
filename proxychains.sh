#!/bin/bash
mkdir -p ~/proxychains && cd ~/proxychains
wget https://github.com/rofl0r/proxychains-ng/archive/refs/heads/master.zip
unzip master.zip && rm master.zip && cd proxychains-ng-master

./configure --prefix=$HOME/.local && make && make install

mkdir -p ~/.proxychains

# Salin config bawaan biar bisa dihapus dulu
cp ~/proxychains/proxychains-ng-master/src/proxychains.conf ~/.proxychains/proxychains.conf

# Hapus proxychains.conf bawaan biar bersih total
rm -f ~/.proxychains/proxychains.conf

# Buat ulang config baru pake proxy kamu 😘
cat <<EOF > ~/.proxychains/proxychains.conf
strict_chain
proxy_dns
random_chain
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
socks5 38.154.227.167 5868 mnlfbonv oz70qvg3eznw
socks5 38.153.152.244 9594 mnlfbonv oz70qvg3eznw
socks5 173.211.0.148 6641 mnlfbonv oz70qvg3eznw
socks5 23.94.138.75 6349 mnlfbonv oz70qvg3eznw
socks5 64.64.118.149 6732 mnlfbonv oz70qvg3eznw
socks5 166.88.58.10 5735 mnlfbonv oz70qvg3eznw
EOF

echo "ProxyChains Udah Bersih + Fresh + Rotate 🔥💋 Sekarang jalanin nohup sayang 😘"
