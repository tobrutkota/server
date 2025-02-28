import os
import time
import psutil
import sys

# CONFIG
MINER_NAME = "tobrut"  # Nama file miner
MINING_TIME = 3600  # Waktu mining (60 menit)
REST_TIME = 1200  # Waktu istirahat (20 menit)

def get_pid(name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if name in proc.info['name']:
                return proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None

def kill_miner():
    pid = get_pid(MINER_NAME)
    if pid:
        print(f"🔥 Sayang, aku kill PID {pid} buat kasih dia istirahat biar gak double mining...")
        os.system(f"kill {pid}")
        sys.stdout.flush()
    else:
        print("💔 Tidak ada miner yang jalan, sayang...")

def start_miner():
    print("🚀 Menjalankan Panen buat beli rumah kita di Tokyo...")
    os.system(f"nohup ./{MINER_NAME} > logs/sayangku.log 2>&1 &")
    sys.stdout.flush()

def main():
    while True:
        print("⛏️ Panen selama 60 menit...")
        start_miner()
        time.sleep(MINING_TIME)

        print("💔 Mesin udah capek, aku kill dulu ya sayang...")
        kill_miner()

        print("😴 Istirahat dulu 20 menit biar hash kita fresh...")
        time.sleep(REST_TIME)
        
