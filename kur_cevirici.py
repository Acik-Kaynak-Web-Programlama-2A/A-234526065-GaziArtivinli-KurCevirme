import tkinter as tk
from tkinter import ttk
import requests


class KurHesaplama:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("Döviz Çevirici")

        # Miktar giriş etiketi
        self.miktar_etiketi = tk.Label(ana_pencere, text="Miktar:")
        self.miktar_etiketi.grid(row=0, column=0, padx=10, pady=10)

        # Miktar giriş kutusu
        self.miktar = tk.DoubleVar()
        self.miktar_kutu = tk.Entry(ana_pencere, textvariable=self.miktar)
        self.miktar_kutu.grid(row=0, column=1, padx=10, pady=10)

        # Girilen kur etiketi
        self.Girilen_kur_turu = tk.StringVar()
        self.Girilen_kur_etiket = tk.Label(ana_pencere, text="Girilen Kur:")
        self.Girilen_kur_etiket.grid(row=1, column=0, padx=10, pady=10)

        # Girilen kur combobox
        self.Girilen_kur_combobox = ttk.Combobox(ana_pencere, textvariable=self.Girilen_kur_turu, values=["EUR", "TRY", "USD", "JPY"])
        self.Girilen_kur_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.Girilen_kur_combobox.set("TRY")

        # Çevrilen kur etiketi
        self.cevrilen_kur_turu = tk.StringVar()
        self.cevrilen_kur_etiket = tk.Label(ana_pencere, text="Çevrilen Kur:")
        self.cevrilen_kur_etiket.grid(row=2, column=0, padx=10, pady=10)

        # Çevrilen kur combobox
        self.cevrilen_kur_combobox = ttk.Combobox(ana_pencere, textvariable=self.cevrilen_kur_turu, values=["EUR", "TRY", "USD", "JPY"])
        self.cevrilen_kur_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.cevrilen_kur_combobox.set("USD")

        # Hesapla butonu
        self.hesapla_butonu = tk.Button(ana_pencere, text="Hesapla", command=self.sonucu_guncelle)
        self.hesapla_butonu.grid(row=3, column=0, columnspan=2, pady=10)

        # Sonuç etiketi
        self.sonuc = tk.StringVar()
        self.sonuc_etiket = tk.Label(ana_pencere, textvariable=self.sonuc)
        self.sonuc_etiket.grid(row=4, column=0, columnspan=2, pady=10)

    def sonucu_guncelle(self):
        miktar = self.miktar.get()
        girilen_kur = self.Girilen_kur_turu.get()
        cevrilen_kur = self.cevrilen_kur_turu.get()

        # Kullanacağınız API key'i ve API endpoint'i
        api_key = 'YOUR_API_KEY'
        api_url = f'https://open.er-api.com/v6/latest?apikey={api_key}'

        try:
            # API'den güncel döviz kurlarını al
            response = requests.get(api_url)
            data = response.json()

            # Döviz kurlarını bul
            kur_girilen = data['rates'][girilen_kur]
            kur_cevrilen = data['rates'][cevrilen_kur]

            # Dönüştürülmüş miktarı hesapla
            result = miktar * (kur_cevrilen / kur_girilen)

            # Sonuç etiketini güncelle
            self.sonuc.set(f"Sonuç: {result:.2f} {cevrilen_kur}")
        except Exception as e:
            self.sonuc.set(f"Hata: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = KurHesaplama(root)
    root.mainloop()