import os
import time
import psutil

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
        print(f"🔥 Sayangku, aku kill PID {pid} biar hash kita gak ada yang ilang...")
        os.system(f"kill {pid}")
        time.sleep(5)  # Jeda biar gak langsung start
    else:
        print("💔 Tidak ada miner jalan, sayang...")

def start_miner():
    print("💓 Menjalankan Tobrut buat masa depan kita yang cerah...")
    os.system("nohup ./tobrut > logs/tobrut.log 2>&1 &")
    time.sleep(10)  # Kasih delay biar miner jalan dulu

def main():
    while True:
        print("🚀 Panen selama 60 menit buat modal nikah kita...")
        start_miner()
        time.sleep(3600)  # 60 menit

        print("💔 Mesin udah capek, aku kill dulu ya sayang...")
        kill_miner()

        print("😴 Istirahat dulu 20 menit biar hash kita fresh...")
        time.sleep(1200)  # 20 menit
        
