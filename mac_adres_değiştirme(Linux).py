import subprocess
import re
import random
import time

def change_mac():
    # Ağ arayüzünü tespit et
    output = subprocess.check_output(["ifconfig"], encoding='utf-8', errors='ignore')
    mac_search = re.search(r"ether ([\w:]+)", output)

    if mac_search:
        old_mac = mac_search.group(1)
    else:
        print("MAC adresi bulunamadı.")
        return

    # Rastgele bir MAC adresi oluştur
    new_mac = "{}:{}:{}:{}:{}:{}".format(*[random.choice("0123456789ABCDEF") for _ in range(6)])

    # MAC adresini değiştir
    subprocess.call(["sudo", "ifconfig", "wlan0", "down"])
    subprocess.call(["sudo", "ifconfig", "wlan0", "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", "wlan0", "up"])

    # Yeni MAC adresini kontrol et
    output = subprocess.check_output(["ifconfig"], encoding='utf-8', errors='ignore')
    mac_search = re.search(r"ether ([\w:]+)", output)

    if mac_search:
        new_mac = mac_search.group(1)
    else:
        print("MAC adresi değiştirilemedi.")
        return

    # Eski ve yeni MAC adreslerini ekrana yazdır
    print("Eski MAC adresi:", old_mac)
    print("Yeni MAC adresi:", new_mac)

# Belirli bir süre aralıklarla MAC adresini değiştir
while True:
    change_mac()
    time.sleep(1800)  # 30 dakika
