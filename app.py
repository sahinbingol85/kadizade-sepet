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
    'instagram': 'https://www.instagram.com/sepetimde_'
}

# --- ÜRÜN LİSTESİ (5 ÜRÜN) ---
urunler = [
    {"ad": "Ekmek Sepetleri", "resim": "sepet1.jpg"},
    {"ad": "Çamaşır Sepetleri", "resim": "sepet2.jpg"},
    {"ad": "Piknik ve Gezi", "resim": "sepet3.jpg"},
    {"ad": "Dekoratif Modeller", "resim": "sepet4.jpg"},
    {"ad": "Teşhir Kovaları", "resim": "sepet5.jpg"}
]

# --- BLOG YAZILARI (3 YAZI - YENİSİ EKLENDİ) ---
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
    },
    {
        "id": 2,
        "baslik": "Evin Unutulan Dili: Neden Doğal Dokulara Özlem Duyuyoruz?",
        "tarih": "7 Ocak 2026",
        "resim": "blog2.jpg",
        "ozet": "Modern evlerin soğuk mükemmelliğinde aradığımız sıcaklık, belki de bir söğüt dalının kusurlu kıvrımında saklıdır. Nostaljiye kısa bir yolculuk...",
        "icerik": """
            <p>Eskiden evlerin bir kokusu, bir dokusu vardı. Hatırlar mısınız büyüklerimizin evlerini? Ahşap kokan merdivenler, yün kokan yorganlar ve mutfak köşesinde sessizce duran, içine soğan, patates ya da yeni pişmiş ekmek konulan o heybetli hasır sepetler...</p>

            <h3 style="color:#5D4037; margin-top:30px;">Plastik Çağında Ruh Arayışı</h3>
            <p>Şimdi evlerimiz daha "şık", daha parlak ama sanki biraz daha soğuk. Her yer fabrikasyon, pürüzsüz ve mükemmel yüzeylerle kaplı. Ama insanın ruhu pürüz arıyor, yaşanmışlık arıyor. Elimiz gayriihtiyari bir ahşap masanın damarlı dokusuna ya da bir sepetin el örgüsü boğumlarına gitmek istiyor. Çünkü dokunmak, hissetmektir.</p>

            <p>Doğal malzemeler nefes alır, yaşar ve sizinle birlikte yaşlanır. Bir plastik saklama kabı eskiyince çöp olur, ama iyi örülmüş bir söğüt/kamış sepet eskiyince "yadigar" olur. Rengi güneşle oturur, hikayesi derinleşir.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Samanpazarı'ndaki Zaman Tüneli</h3>
            <p>Ankara Kalesi'nin gölgesindeki dükkanımıza (Kadızade Ticaret) gelen misafirlerimizde hep aynı bakışı görüyoruz. Bir çamaşır sepetine ya da küçük bir ekmekliğe dokunduklarında yüzlerine yayılan o tebessüm, aslında çocukluklarına yapılan kısa ve sıcak bir yolculuk.</p>

            <p>Biz sadece bir eşya satmıyoruz; unuttuğunuz o sıcaklık hissini, evin kaybolan ruhunu geri veriyoruz. Evinizin bir köşesinde doğaya yer açın. İnanın, o köşenin enerjisi değişecek.</p>
        """
    },
    # --- YENİ EKLENEN 3. YAZI (BUGÜN) ---
    {
        "id": 3,
        "baslik": "Sofranın Kalbi: Sıcak Ekmek ve Hasırın Dostluğu",
        "tarih": "14 Ocak 2026",
        "resim": "blog3.jpg",
        "ozet": "Fırından yeni çıkmış o mis kokulu ekmeğin en iyi dostu neden plastiği değil de hasırı sever? Sofranızın bereketini koruyan doğal sırlar ve bakım ipuçları.",
        "icerik": """
            <p>Pazar sabahlarını düşünün... Bütün aile bir arada, çay demlenmiş, peynir zeytin hazır. Ancak o sofranın asıl yıldızı, fırından yeni çıkmış, dumanı üzerinde tüten, kokusu tüm evi saran taze ekmektir. O ekmeği böldüğünüzde çıkan "çıt" sesi, aslında mutluluğun sesidir.</p>

            <p>Peki, bu kadar özenle hazırlanan, binbir emekle sofraya gelen ekmeğe nasıl davranıyoruz? Onu havasız poşetlere mi hapsediyoruz, yoksa soğuk plastik kaplarda terlemesine mi izin veriyoruz? Gelin, ekmeğinize hak ettiği değeri vermenin yollarını konuşalım.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Ekmeğin En Büyük Düşmanı: Nem</h3>
            <p>Ekmek, fırından çıktıktan sonra da "yaşayan" bir gıdadır. İçindeki nemi yavaş yavaş dışarı verir. Eğer ekmeği hava almayan metal, cam veya plastik bir kutuya koyarsanız, bu nem içeride hapsolur. Sonuç bellidir:</p>
            <ul>
                <li><strong>Yumuşama:</strong> O sevdiğiniz çıtır kabuk, dakikalar içinde lastik gibi olur.</li>
                <li><strong>Küflenme:</strong> Hapsolan nem, bakteriler için bir yuva oluşturur ve ekmeğin ömrünü kısaltır.</li>
                <li><strong>Tat Kaybı:</strong> Ekmeğin o kendine has aroması, plastik kokusuyla karışarak kaybolur.</li>
            </ul>

            <h3 style="color:#5D4037; margin-top:30px;">Doğal Söğüt Sepetin Sırrı: "Nefes Alma"</h3>
            <p>İşte atalarımızın neden yüzyıllardır hasır ve söğüt sepet kullandığının cevabı burada gizli. Kadızade Ticaret olarak Samanpazarı'nda ördüğümüz sepetler, tamamen doğal dallardan oluşur.</p>
            <p>Söğüt dallarının arasındaki o milimetrik boşluklar, sepetin sürekli hava almasını sağlar. Bu doğal sirkülasyon sayesinde ekmeğin fazla nemi uçar gider, ama ekmek kurumaz. Sepet, ekmeği kucaklar; onu hem sıcak tutar hem de terlemesini engeller. Bu, doğanın bize sunduğu en basit ama en mükemmel mühendisliktir.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Sofrada Görsel Bir Şölen</h3>
            <p>İşin bir de estetik boyutu var. Beyaz bir porselen tabağın yanına, fabrikasyon bir plastik kap koymakla; el emeği, toprak tonlarında bir hasır sepet koymak arasındaki farkı hayal edin. Hasır sepet, masaya bir "ruh" katar. Soğuk kış günlerinde sofrayı ısıtır, misafirlerinize "burada her şey doğal ve samimi" mesajını verir.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Küçük Bir İpucu: Ekmek Sepeti Temizliği</h3>
            <p>Müşterilerimizden sıkça duyduğumuz bir soru var: <em>"Peki bu sepetleri nasıl temizleyeceğiz?"</em> Cevabı çok basit:</p>
            <ul>
                <li>Kırıntıları dökmek için sepeti ters çevirip hafifçe sirkelemeniz yeterlidir.</li>
                <li>Eğer kirlenirse, nemli bir bezle silip (asla suya sokmadan) havadar bir yerde kurumaya bırakabilirsiniz.</li>
                <li>İçine keten veya pamuklu bir bez sererek (peçete) kullanmak, hem temizliği kolaylaştırır hem de sunumu güzelleştirir.</li>
            </ul>

            <p>Evinizin bereketini, doğanın kucağında saklayın. Bir dahaki sefere fırından eve dönerken, ekmeğinizi poşetten çıkarmayı unutmayın. Farkı, o ilk lokmada hissedeceksiniz.</p>
        """
    },
    # --- 4. YAZI ---
    {
        "id": 4,
        "baslik": "Derle, Topla, Nefes Al: Ev Düzeninde Doğallığın Büyüsü",
        "tarih": "21 Ocak 2026",
        "resim": "blog4.jpg",
        "ozet": "Evinizdeki dağınıklık zihninizi de yoruyor olabilir mi? Plastik kutular yerine doğal sepetlerle evinizi (ve ruhunuzu) ferahlatmanın yolları.",
        "icerik": """
            <p>Kış aylarının ortasındayız. Dışarısı soğuk, evlerimiz ise sığınağımız. Ancak bazen bu sığınak, etrafa saçılmış eşyalar, birikmiş çamaşırlar ve plastik kutuların soğuk görüntüsüyle üzerimize gelebilir. Japonların meşhur "sadeleşme" felsefesini duymuşsunuzdur; derler ki: <em>"Eviniz düzenliyse, zihniniz de düzenlidir."</em></p>

            <p>Peki, bu düzeni sağlarken evin sıcaklığını nasıl koruyacağız? Her şeyi gri plastik kutulara doldurmak evi toplar belki ama o eve "yuva" sıcaklığını vermez. İşte tam bu noktada, yüzyıllık dostumuz hasır sepetler devreye giriyor.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Görünmeyen Tehlike: Kirli Sepetleri</h3>
            <p>Banyo veya yatak odasında kullandığınız kirli çamaşır sepetine hiç dikkat ettiniz mi? Genelde plastik tercih edilir "kolay temizlenir" diye. Oysa plastik, hava geçirmez.</p>
            <ul>
                <li><strong>Koku ve Küf:</strong> Nemli havluları veya spor kıyafetlerini plastik bir sepete attığınızda, hava almadığı için bakteriler hızla çoğalır. O ağır koku, aslında bakterilerin sesidir.</li>
                <li><strong>Doğal Çözüm:</strong> Söğüt ve kargıdan ördüğümüz çamaşır sepetleri ise yaşayan bir yapıya sahiptir. Gözenekli dokusu sayesinde hava sürekli içeride dolaşır. Çamaşırlarınız beklerken kurumaya devam eder, kötü kokular hapsolmaz, uçar gider.</li>
            </ul>

            <h3 style="color:#5D4037; margin-top:30px;">Dekorasyonun Joker Elemanı</h3>
            <p>Hasır sepetler sadece kirliler için değildir. Salonun köşesinde duran o şık, büyük sepeti düşünün...</p>
            <p>Kışın koltuk şallarını ve battaniyeleri içine rulo yapıp koyduğunuzda, hem dağınıklık biter hem de sanki bir dekorasyon dergisinden fırlamış gibi bir görüntü oluşur. Çocuk odasında oyuncakları, çalışma odasında dergileri toparlar. Plastik bir kutuyu dolabın içine saklamak istersiniz, ama el örmesi bir sepeti gururla sergilersiniz.</p>

            <h3 style="color:#5D4037; margin-top:30px;">Samanpazarı'ndan Bir Tavsiye</h3>
            <p>Kadızade Ticaret olarak, sepetlerimizi örerken sağlamlığa çok önem veriyoruz. Büyük boy çamaşır ve düzenleme sepetlerimiz, içine ağır yükler girse bile formunu bozmayacak şekilde, sıkı teknikle örülür. </p>

            <p>Bu hafta sonu evinize şöyle bir bakın. Gözünüzü yoran o plastik kutuları, havasız hurçları bir kenara bırakın. Doğanın dokusunu evinize davet edin. Göreceksiniz; sadece eviniz değil, içiniz de ferahlayacak.</p>
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