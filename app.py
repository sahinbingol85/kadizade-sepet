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
    'adres': 'Kale Mah. Can Sok. 7/A, Samanpazarı, Altındağ/Ankara',
    'telefon': '+90 312 324 26 68',
    'facebook': 'https://www.facebook.com/kadizade.ticaret/?locale=tr_TR',
    # YENİ EKLENEN INSTAGRAM SATIRI:
    'instagram': 'https://www.instagram.com/sepetimde_'
}

# --- ÜRÜN LİSTESİ ---
urunler = [
    {"ad": "Ekmek Sepetleri", "resim": "sepet1.jpg"},
    {"ad": "Çamaşır Sepetleri", "resim": "sepet2.jpg"},
    {"ad": "Piknik ve Gezi", "resim": "sepet3.jpg"},
    {"ad": "Dekoratif Modeller", "resim": "sepet4.jpg"},
    {"ad": "Teşhir Ürünleri", "resim": "sepet5.jpg"}
]

# --- BLOG YAZILARI ---
blog_yazilari = [
    {
        "id": 1,
        "baslik": "Hasırın Hikayesi: Topraktan Evinize",
        "tarih": "28 Aralık 2025",
        "resim": "blog1.jpg",
        "ozet": "Bir sepetin örülmesi sadece dalların birleşmesi değil, sabrın, emeğin ve yüzyıllık bir geleneğin ilmek ilmek işlenmesidir.",
        "icerik": """
            <p>Sepetçilik, sadece bir eşya üretme işi değil, doğayla insan arasındaki en eski anlaşmalardan biridir. Toprağın bize sunduğu söğüt, kargı ve fındık dalları, ustanın elinde şekil bularak evinize girmeye hazırlanır. Kadızade Ticaret olarak, Samanpazarı'nın tarihi dokusunda bu kadim yolculuğa şahitlik ediyoruz.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Doğadan Toplama Süreci</h3>
            <p>Her şey doğru zamanda başlar. Sepet yapımında kullanılan söğütler, genellikle su kenarlarında yetişir ve sonbaharın bitip kışın başladığı, suyun çekildiği dönemlerde hasat edilir. Bu zamanlama çok önemlidir; çünkü dalın en esnek ama en dayanıklı olduğu anı yakalamak gerekir. Yanlış zamanda kesilen dal ya kırılır ya da örüldükten sonra çabuk bozulur.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Sabırla İşlenen İlmekler</h3>
            <p>Toplanan dallar hemen örülmez. Önce kabuklarının soyulması, bazılarının ise rengini alması için suda bekletilmesi veya kaynatılması gerekir. Ustanın önünde duran o ham dal yığını, saatler süren bir "parmak dansı" ile sepete dönüşür. Bir ekmek sepetini örmek dışarıdan bakıldığında kolay görünebilir, ancak her düğümde ustanın parmak uçlarındaki nasırların izi, gözlerindeki emeğin nuru vardır.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Neden Doğal Sepet?</h3>
            <p>Günümüzde her tarafımız plastik ve yapay malzemelerle çevrili. Ancak hiçbir plastik kap, bir söğüt sepetin verdiği nefesi veremez. Doğal sepetler:</p>
            <ul>
                <li><strong>Nefes Alır:</strong> İçine koyduğunuz ekmeği küflendirmez, soğanı patatesi çürütmez.</li>
                <li><strong>Doğaldır:</strong> Kimyasal barındırmaz, gıdayla teması güvenlidir.</li>
                <li><strong>Estetiktir:</strong> Evinize sıcak, rustik ve samimi bir hava katar.</li>
            </ul>

            <p>Biz Kadızade Ticaret'te, babadan oğula geçen bu mirası korumaya çalışıyoruz. Sattığımız her sepetin arkasında bir emek, bir hikaye ve doğanın sıcaklığı var. Yolunuz Ankara Kalesi tarafına, Samanpazarı'na düşerse, dükkanımıza uğrayıp hasırın o mis kokusunu içinize çekmenizi, bir çayımızı içmenizi bekleriz.</p>
        """
    }
]


# --- ROTALAR ---

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
    yazi = next((y for y in blog_yazilari if y['id'] == id), None)
    if yazi is None:
        abort(404)
    return render_template('blog_detay.html', bilgi=dukkan_bilgisi, yazi=yazi)


if __name__ == '__main__':
    app.run(debug=True)