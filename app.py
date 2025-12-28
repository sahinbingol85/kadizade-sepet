from flask import Flask, render_template, abort

app = Flask(__name__)

# --- DÜKKAN BİLGİLERİ ---
dukkan_bilgisi = {
    'isim': 'Kadızade Ticaret',
    'slogan': 'Doğallığın ve Emeğin Buluştuğu Yer',
    'uzun_yazi': """
        Ankara'nın kalbi Samanpazarı'nda, zamanın yavaş aktığı, el emeğinin kıymetinin bilindiği bir dükkandayız. 
        Kadızade Ticaret olarak, plastiğin soğukluğuna inat, doğanın sıcaklığını evlerinize taşıyoruz. 
        Söğüt ağacının esnekliği, kamışın zarafeti ve ustalarımızın nasırlı ellerinden çıkan sanat eserleri... 
        İster ekmeklerinizi saklayın, ister çamaşırlarınızı düzenleyin; her sepetin bir hikayesi, her örgünün bir yaşanmışlığı var.
    """,
    # Senin güncellediğin adres ve telefon:
    'adres': 'Kale Mah. Can Sok. 7/A, Samanpazarı, Altındağ/Ankara',
    'telefon': '+90 312 324 26 68',
    'facebook': 'https://www.facebook.com/kadizade.ticaret/?locale=tr_TR'
}

# --- ÜRÜN LİSTESİ ---
urunler = [
    {"ad": "Ekmek Sepetleri", "resim": "sepet1.jpg"},
    {"ad": "Çamaşır Sepetleri", "resim": "sepet2.jpg"},
    {"ad": "Piknik ve Gezi", "resim": "sepet3.jpg"},
    {"ad": "Dekoratif Modeller", "resim": "sepet4.jpg"}
]

# --- BLOG YAZILARI ---
blog_yazilari = [
    {
        "id": 1,
        "baslik": "Hasırın Hikayesi: Topraktan Evinize",
        "tarih": "28 Aralık 2025",
        "resim": "blog1.jpg",
        "ozet": "Bir sepetin örülmesi sadece dalların birleşmesi değil, sabrın ve geleneğin birleşmesidir.",
        "icerik": """
            <p>Sepetçilik, insanlık tarihinin en eski zanaatlarından biridir. Plastik poşetlerin, fabrikasyon kutuların olmadığı zamanlarda atalarımız doğanın sunduğu dalları, kamışları ve sazları kullanarak hayatlarını kolaylaştırdı.</p>

            <p>Ankara Samanpazarı'nda yıllardır bu geleneği sürdürüyoruz. Peki iyi bir sepet nasıl anlaşılır? Öncelikle malzemesine bakmalısınız. Gerçek söğüt dalı esnektir, kırılmaz ama bükülür. Rengi zamanla oturur, koyulaşır ve güzelleşir.</p>

            <p>Bizim dükkanımızda her sepetin bir hikayesi vardır. Kimi bir köy evinde ekmek saklamak için, kimi modern bir evde dergilik olmak için yola çıkar. Ama hepsinin ortak noktası ustasının el emeğidir.</p>

            <p>Bu blogda ("Sepetçinin Defteri") sizlere sepet bakımı, dekorasyon fikirleri ve Samanpazarı'ndan hikayeler anlatacağız. Takipte kalın.</p>
        """
    }
]


# --- ROTALAR (SAYFA YÖNLENDİRMELERİ) ---

@app.route('/')
def ana_sayfa():
    return render_template('index.html', bilgi=dukkan_bilgisi, urunler=urunler)


@app.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html', bilgi=dukkan_bilgisi)


@app.route('/blog')
def blog():
    return render_template('blog.html', bilgi=dukkan_bilgisi, yazilar=blog_yazilari)


@app.route('/blog/<int:id>')
def blog_detay(id):
    # İstenen ID'deki yazıyı bul, yoksa 404 hatası ver
    yazi = next((y for y in blog_yazilari if y['id'] == id), None)
    if yazi is None:
        abort(404)
    return render_template('blog_detay.html', bilgi=dukkan_bilgisi, yazi=yazi)


# --- UYGULAMAYI BAŞLAT ---
if __name__ == '__main__':
    app.run(debug=True)