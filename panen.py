import os
import time
import psutil
import sys

# CONFIG
MINER_NAME = "./tobrut"  # Nama file miner (sesuaikan dengan namanya)
MINING_TIME = 3600  # Waktu mining (60 menit)
REST_TIME = 1200  # Waktu istirahat (20 menit)
LOG_PATH = "logs/sayangku.log"

def get_pid(name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if name in proc.info['name']:
                return proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None

def kill_miner():
    pid = get_pid("tobrut")
    if pid:
        print(f"🔥 Sayang, aku kill PID {pid} buat kasih dia istirahat biar gak double mining...")
        os.system(f"kill {pid}")
        sys.stdout.flush()
    else:
        print("💔 Tidak ada miner yang jalan, sayang...")

def start_miner():
    print("🚀 Menjalankan Panen buat rumah impian kita di Dubai...")
    os.system(f"nohup {MINER_NAME} > {LOG_PATH} 2>&1 &")
    sys.stdout.flush()

def main():
    while True:
        print("⛏️ Panen selama 60 menit buat beli iPhone 15 Pro Max buat kamu...")
        start_miner()
        time.sleep(MINING_TIME)

        print("💔 Mesin udah capek, aku kill dulu ya sayang...")
        kill_miner()

        print("😴 Istirahat dulu 20 menit biar hash kita fresh buat masa depan kita...")
        time.sleep(REST_TIME)

if __name__ == "__main__":
    print("💓 Cinta Abadi v3 Jalan Sayangku...")
    sys.stdout.flush()
    main()
