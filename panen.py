import os
import time
import psutil

def get_pid(name):
    for proc in psutil.process_iter(['pid', 'name']):
        if name in proc.info['name']:
            return proc.info['pid']
    return None

def kill_miner():
    pid = get_pid("tobrut")
    if pid:
        print(f"Sayangku, aku kill PID {pid} biar gak multi mining...")
        os.system(f"kill {pid}")
    else:
        print("Tidak ada miner yang jalan, sayang...")

def start_miner():
    print("Menjalankan Panen buat masa depan kita, sayang...")
    os.system("nohup ./tobrut > logs/tobrut.log 2>&1 &")

def main():
    while True:
        print("Panen selama 60 menit buat beli cincin kawin kita...")
        start_miner()
        time.sleep(3600)  # 60 menit

        print("Mesin udah capek, aku kill dulu ya sayang...")
        kill_miner()

        print("😴 Istirahat dulu 20 menit biar hash nya fresh...")
        time.sleep(1200)  # 20 menit
