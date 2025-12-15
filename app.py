from flask import Flask, render_template

app = Flask(__name__)

# Dükkan bilgilerini her yerde kullanmak için global bir değişkene alalım
dukkan_bilgisi = {
    'isim': 'Kadızade Ticaret',
    'slogan': 'Doğallığın ve Emeğin Buluştuğu Yer',
    'uzun_yazi': """
        Ankara'nın kalbi Samanpazarı'nda, zamanın yavaş aktığı, el emeğinin kıymetinin bilindiği bir dükkandayız. 
        Kadızade Ticaret olarak, plastiğin soğukluğuna inat, doğanın sıcaklığını evlerinize taşıyoruz. 
        Söğüt ağacının esnekliği, kamışın zarafeti ve ustalarımızın nasırlı ellerinden çıkan sanat eserleri... 
        İster ekmeklerinizi saklayın, ister çamaşırlarınızı düzenleyin; her sepetin bir hikayesi, her örgünün bir yaşanmışlığı var.
    """,
    'aciklama': 'Ankara Samanpazarı\'nda yılların tecrübesiyle, el emeği hasır sepetleri sizlerle buluşturuyoruz.',
    'adres': 'Kale Mah. Can Sok., Samanpazarı, Altındağ/Ankara',
    'telefon': '0312 324 26 68',
    'facebook': 'https://www.facebook.com/kadizade.ticaret/?locale=tr_TR'
}

@app.route('/')
def ana_sayfa():
    # Ürün listesi (Resim isimlerinin klasöründekilerle aynı olduğundan emin ol)
    urunler = [
        {"ad": "Ekmek Sepetleri", "resim": "sepet1.jpg"},
        {"ad": "Çamaşır Sepetleri", "resim": "sepet2.jpg"},
        {"ad": "Piknik ve Gezi", "resim": "sepet3.jpg"},
        {"ad": "Dekoratif Modeller", "resim": "sepet4.jpg"}
    ]
    return render_template('index.html', bilgi=dukkan_bilgisi, urunler=urunler)

@app.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html', bilgi=dukkan_bilgisi)

if __name__ == '__main__':
    app.run(debug=True)