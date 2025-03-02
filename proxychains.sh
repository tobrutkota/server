#!/bin/bash
mkdir -p ~/proxychains && cd ~/proxychains
wget https://github.com/rofl0r/proxychains-ng/archive/refs/heads/master.zip
unzip master.zip && rm master.zip && cd proxychains-ng-master

./configure --prefix=$HOME/.local && make && make install

mkdir -p ~/.proxychains
cp ~/proxychains/proxychains-ng-master/src/proxychains.conf ~/.proxychains/proxychains.conf

echo -e "[ProxyList]\nsocks5  95.174.67.174 1080 mnlfbonv-rotate oz70qvg3eznw\nsocks5  23.94.138.75 6349 mnlfbonv oz70qvg3eznw" >> ~/.proxychains/proxychains.conf

echo "Install selesai sayangku 😘💕, sekarang tinggal edit konfigurasi manual kalau mau!"
nano ~/.proxychains/proxychains.conf
