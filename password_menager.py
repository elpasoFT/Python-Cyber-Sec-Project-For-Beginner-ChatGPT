#sadece taslaktır , aktif çalışabilmesi için bir veritabanı oluşturulup entegre edilmesi gerekir



import tkinter as tk
from tkinter import messagebox
import json

def kaydet():
    # Kullanıcının girdiği verileri sözlük olarak oluştur
    veri = {
        "site": site_entry.get(),
        "kullanici_adi": kullanici_adi_entry.get(),
        "sifre": sifre_entry.get()
    }
    
    # JSON dosyasına verileri ekle
    with open("veriler.json", "a") as f:
        json.dump(veri, f)
        f.write("\n")
        
    # Kullanıcıya başarılı mesajı göster
    messagebox.showinfo("Başarılı", "Veriler başarıyla kaydedildi.")

def sifre_goster():
    # Şifreyi gizleme/seçenekleri değiştirme
    if sifre_entry.cget("show") == "*":
        sifre_entry.config(show="")
        sifre_goster_btn.config(text="Şifreyi Gizle")
    else:
        sifre_entry.config(show="*")
        sifre_goster_btn.config(text="Şifreyi Göster")
        
# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Parola Yöneticisi")

# Site girdisi
site_label = tk.Label(pencere, text="Site:")
site_label.grid(row=0, column=0)
site_entry = tk.Entry(pencere)
site_entry.grid(row=0, column=1)

# Kullanıcı adı girdisi
kullanici_adi_label = tk.Label(pencere, text="Kullanıcı Adı:")
kullanici_adi_label.grid(row=1, column=0)
kullanici_adi_entry = tk.Entry(pencere)
kullanici_adi_entry.grid(row=1, column=1)

# Şifre girdisi
sifre_label = tk.Label(pencere, text="Şifre:")
sifre_label.grid(row=2, column=0)
sifre_entry = tk.Entry(pencere, show="*")
sifre_entry.grid(row=2, column=1)

# Şifre göster/gizle butonu
sifre_goster_btn = tk.Button(pencere, text="Şifreyi Göster", command=sifre_goster)
sifre_goster_btn.grid(row=2, column=2)

# Kaydet butonu
kaydet_btn = tk.Button(pencere, text="Kaydet", command=kaydet)
kaydet_btn.grid(row=3, column=1)

# Pencereyi çalıştır
pencere.mainloop()
