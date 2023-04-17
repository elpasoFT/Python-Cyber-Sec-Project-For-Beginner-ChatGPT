import subprocess
import time

def show_wifi():
    print("Sistem analiz ediliyor")
    time.sleep(1)
    print("Bulunan Wi-Fi ağları: ")
    try:
        veri = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
        sistemler = [i.split(":")[1][1:-1] for i in veri if "All User Profile" in i]
        for i in sistemler:
            try:
                sonuç = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split(
                    '\n')
                sonuç = [b.split(":")[1][1:-1] for b in sonuç if "Key Content" in b]
                try:
                    print(" \\{:<30}| Şifre:  {:<}".format(i, sonuç[0]))
                except IndexError:
                    print(" \\{:<30}| Şifre:  {:<}".format(i, ""))
            except subprocess.CalledProcessError as e:
                print(f"{i} ağına erişilirken bir hata oluştu: {e}")
    except subprocess.CalledProcessError as e:
        print("Wi-Fi ağlarına erişilirken bir hata oluştu: ", e)

if __name__ == '__main__':
    print("""Wi-Fi Görüntüleyici

                        -www.siberguvenlikblogu.com-
    """)
    while True:
        show_wifi()
        exe = input("\n \n \n1'e basarak yeniden sistemi analiz edebilirsiniz \n2'ye basarak çıkış yapabilirsiniz ")
        if exe.isdigit():
            exe = int(exe)
            if exe == 1:
                print("")
                time.sleep(1)
            elif exe == 2:
                print("Çıkış yapılıyor...")
                time.sleep(1)
                break
            else:
                print("Hatalı bir seçim yaptınız, lütfen tekrar deneyin.\n")
        else:
            print("Hatalı bir seçim yaptınız, lütfen tekrar deneyin.\n")
