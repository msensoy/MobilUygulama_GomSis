# Veri Tabanına Kaydedilen Ortam Sıcaklık ve Nem Bilgilerini Web Sitesinde Yayınlama

Projenin amacı ARM mimarisine sahip bir mikrodenetleyici olan Raspberry Pi kartı ve DHT11 sensörü ile ortam sıcaklık ve nem bilgilerini veri tabanına kaydedip daha sonra bu verileri web ortamında paylaşmaktır. Proje sürecinde Raspberry Pi kartında Linux komutları kullanımı, paket yükleme ve kurulumu, veri tabanı kurulumu ve işlemleri, web sunucu kurulumu ve web sitesi oluşturma hakkında bilgi öğrenmek amaçlanmıştır. </br>
Projenin adım adım yapılışını [Youtube Video Link](https://www.youtube.com/watch?v=r5sigewGcic&feature=youtu.be) 'inde bulabilirsiniz.
Projenin sunum videosu 	[Sunum Video Link](https://drive.google.com/file/d/1rsY7nLWzuy_pqki4QvN_ZhUBQu4s97Nz/view) 'inde yer alan videodan izleyebilirsiniz.
## Proje Gereksinimleri
  ### Donanım
     Raspberry Pi 4
     DHT11 Sensör
     Micro SD Kart 16 GB
     Adaptör 5V-3A  USB-C
     Bağlantı için gerekli kablolar
  ### İşletim Sistemi
     Raspbian İşletim Sistemi
## İşletim Sisteminin Kurulumu
SD Card Formatter programı ile SD Kart formatlanabilir. Daha sonra "Win32 Disk Imager" programı ile SD Kart'a önceden indirilen Rasbian işletim sistemi yüklenebilir.</br>
[Rasbian işletim sistemi indirme linki](https://www.raspberrypi.org/downloads/raspbian/) </br>
[SD Card Formatter programı indirme linki](https://www.sdcard.org/downloads/formatter/) </br>
[Win32 Disk Imager programı indirme linki](https://sourceforge.net/projects/win32diskimager/) </br>
##  DHT11 Sıcaklık ve Nem Ölçüm Sensörü  
Sıcaklık ve nem ölçümlerinde kullanılabilecek bir sensördür. Maksimum +-%5 civarı bir hassasiyet sağlamaktadır.
Sensör Pinleri : </br>
    VCC= 3.3 Volt beslemeye pini => Raspberry Pi 3.3 Volt Çıkış pinine bağlanacak </br>
    GND= Toprak bağlantı pini => Raspberry Pi ground pinine bağlanacak </br>
    DATA= Ölçülen verilerin okunacağı pini => Raspberry Pi GPIO 17 pinine bağlanacak </br>
![NGINX](https://github.com/msensoy/GomSisProje/blob/master/Resimler/model.PNG)    
    
##  DHT11 Kütüphanesi Kurulumu
Raspberry Pi’ a herhangi bir paket yüklenmeden önce paket güncellenmesi yapılması gerekir.
`sudo apt-get update` komutu ile güncelleme yapılır.
`sudo apt-get install build-essential python-dev` komutu ile Python dev paketleri yüklenir.
`git clone https://github.com/adafruit/Adafruit_Python_DHT.git` komutu ile kaynak kodlar Github sitesinden indirilir. İndirilen klasör içinde kurulum dosyası yer almaktadır.
`cd Adafruit_Python_DHT` komutu ile indirilen klasöre geçiyoruz. 
`sudo python setup.py install` komutuyla klasörün içindeki "setup" dosyası kurulur. Kurulum bittikten sonra hazır hale gelmesi için sistemin yeniden başlatılması gerekecektir.
`sudo reboot`  komutu ile sistem yeniden başlatılır.
Adafruit, sensörünüzün düzgün çalışıp çalışmadığını kontrol etmek için kullanabileceğiniz örnek bir komut dosyası sağlar. Bunun için sırasıyla şu komutlar girilir : </br>
`cd Adafruit_Python_DHT` komutu ile İndirilen kütüphanenin klasörüne geçiş yapılır. </br> 
`cd examples` komutu ile örneklerin bulunduğu klasörün içine girilir. </br>
`python AdafruitDHT.py 11 17` komutu çalıştırılır ve ölçülen değerler ekrana gelir. </br>
Örnek komut dosyası iki parametre alır. Birincisi, DHT11'i temsil etmek için “11” olarak ayarlanan sensör tipidir. İkincisi GPIO numarasıdır. </br>
    **!Not: Komut dosyasındaki GPIO numaralandırılması BCM numaralandırmaya göre ayarlanmıştır.**
## NGINX Web Sunucusu Kurulumu
![NGINX](https://github.com/msensoy/GomSisProje/blob/master/Resimler/nginx.PNG) </br>
    NGNIX tasarlanırken düşük hafıza kullanımı, yüksek eş zamanlı çalışma ve yüksek performans sağlayacak şekilde tasarlanan açık kaynak kodlu bir web sunucusudur. 
    Varsayılan olarak, Nginx'in dosya yüklemelerinde 1 MB sınırı vardır. Dosya yükleme boyutunu ayarlamak için Nginx’in ngx_http_core_module modülünün bir parçası olan client_max_body_size yönergesini kullanabilirsiniz. Bu yönerge http, sunucu veya konum bağlamında ayarlanabilir.
    Linux platformu haricinde  Unix, BSD, Windows gibi platformlarda çalışabilmektedir.
    Raspberry Pi’yı web sunucusu olarak kullanabilmek için ilk olarak Raspbian üzerinde Nginx kurulmalıdır.
    `sudo apt-get install nginx` komutu ile Nginx kurulumu yapılır.
    Kurulum tamamlandıktan sonra Nginx servisi başlatılması gerekir.
    `/etc/init.d/nginx start` komutu ile Nginx servisi başlatılır.
    Kontrol etmek için bilgisayardan tarayıcıyı açılıp Raspberry Pi’e ait IP adresi yazılır ve nginx sayfası çıkması gerekir.
## SQLite Kurulumu    
![SQLite](https://github.com/msensoy/GomSisProje/blob/master/Resimler/sqlite.PNG) </br>
    Verileri yazmak için Raspberry Pi üzerine kurulan veri tabanı yazılımıdır. Yapılan uygulamada çok büyük miktarlarda veri tutulmadığından bu uygulama için SQLite veri tabanı kullanıldı. Sqlite kütüphanesi 500 KiB’den küçüktür. Daha fazla yer saklamak için gereksiz özellikler devre dışı bırakılabilir. Kütüphanenin boyutu 300 KiB’ye kadar düşürülebilir. 
    Uygulamamız web tabanlı bir uygulama olacağından proje klasörünü Nginx web sunucumuzun doküman kök dizini içinde açmamız daha iyi olacaktır.
    Bu klasöre Raspberry Pi kullanıcısının yazma yetkisi olmadığından burada klasör veya dosya açarken komutları «sudo» ile birlikte kullanmak gerekecektir.
    Linux dosya sisteminde normal kullanıcı (user), /home klasörünün altındaki kendisine ait alanda komutları çalıştırabilir. Ancak kök dizini içerisindeki diğer klasörlerde herhangi bir işlem yapma yetkisi yoktur.
    Kök dizinindeki tüm dosyalarda değişiklikleri ancak süper kullanıcı (Super user) yapabilir.
    Normal bir kullanıcıda iken değişiklik yapmak için kullanıcıya süper yetki verilmesi gerekir. Bunun içinde kodların önünde «sudo» ifadesi yer alır.
    Ör: sudo + pi => superuser  (sudo = Super-User DO)
    `cd /var/www` komutu ile kök dizininde bulunan klasörleri  /var’ın altında yer alan /www klasörüne geçilir.
    `sudo apt-get install sqlite3` komutu ile SQLite dosyası indirilir.
    İndirme işleminden sonra veri tabanı kurulu olacaktır. Artık ölçüm verilerini saklayacağımız tablomuzu oluşturabiliriz.
    `sudo sqlite3 veriler.db` komutu ile ‘veriler’ adında database oluşturulur.
    Tablo oluşturmak için gerekli komutlar girilir:
    `BEGIN;`
    `CREATE TABLE degerler (zaman DATETIME, sicaklik NUMERIC, nem NUMERIC);`
    `.quit` ile işlemi tamamlayıp çıkıyoruz.
    Veri tabanı dosyamızın sahibi olarak www-data kullanıcısını atayalım. Böylece NGINX web sunucusunun veri tabanı dosyamızı okuyabilmesi sağlanır.
    `sudo chown www-data:www-data /var/www/veriler.db`
    Veri tabanı dosyamız ve içinde oluşturduğumuz tablomuz hazır.
    Şimdi Raspberry Pi’a bağlı DHT11 sensöründen veri okumaya ve bu verileri veri tabanına yazma süreçlerine geçilebilir.
    `/var/www` klasöründe iken terminalde `sudo nano veri_oku.py` komutu ile yeni bir Python dosyası açıp verileri okuyacak ve veri tabanına yazacak kodu buraya yazıyoruz.
    Yazdığımız kodu test etmek için komut satırında
    `sudo python ./veri_oku.py` komutunu girdiğimizde veri tabanına kayıt yapıp bir satır aşağıya inmesi gerekir.
    Programımız hatasız olarak çalıştığında sıcaklık ve nem verileri sensörden okunup veri tabanına yazılacak ve tekrar komut satırına dönülecektir.
## Flask Framework Kurulumu
![Flask Logo](https://github.com/msensoy/GomSisProje/blob/master/Resimler/flask.PNG) </br>
    Veri tabanına keydedilen verileri web ortamında yayınlamak için Python diliyle yazılmış olan mikro framework olan Flask kullanıldı.     Flask bir mikro framework olmasına rağmen küçük boyutlu ve kolay öğrenilmesi nedeniyle web uygulamaları ve API’lar geliştirmek için uygundur. Flask’i kurmadan önce Python paket yöneticisi pip’i kurmamız gerekiyor.
    `sudo apt-get install python-pip` komutu ile "pip" kurulur.
    `pip install` flask komutu flask komutu ile Flask'ın kurulumu sağlayanacaktır.
    `sudo mkdir sicaklik_nem` komutu ile /var/www klasörünün altında web sitesi için gerekli dosyalar oluşturulur.
    `cd sicaklik_nem` komutu ile oluşturulan dosyaya geçilir. </br>
     Web sitesi 2 Back-End ve Front-End bölümden oluşur.
     Bir web projesinin son kullanıcının görmediği çekirdek yazılım kısmına Back-End denir.
     Kullanıcıların görmediği kısımların ve ana sistemin arkayüzün geliştirilme işlemidir. Bir programın hangi programlama diliyle  yazılacağını bulmak, bu yazılımın programlama dilleriyle meydana getirilmesi ve bir veritabanına bağlanması gibi işlevlerin tümü Backend yazılım tasarımına girer.
    `sudo nano uygulama.py` komutu ile ‘uygulama’ adında bir Python dosyası açılıp içine kodlar yazılır.
    Web sitesinin ön yüzünün HTML, CSS ve JavaScript gibi teknolojileri kullanarak web sitesinin görsel tarafını oluşturma işlemi front-end olarak tanımlanır. Web sitesinin yapımında kullanılacak renk, içerik yerleşimi, yazı tipi vb. tasarım çalışmalarını kapsar. 
    `sudo mkdir templates` komutu ile ‘templates’ klasörü oluşturulur.
    `cd templates` komutu ile oluşturulan klasöre geçiş yapılır.
    `sudo nano index.html` komutu ile ‘index’ adlı bir HTML dosyası açılıp içine kodlar yazılır.
 ### Web Sitesini Yayına Alma   
`python uygulama.py` komutu ile uygulama Flask geliştirme sunucusu ile çalıştırılır. Bu işlemler tamamlandıktan sonra veritabanındaki kaydedilen veriler sitede gözükür. </br>
`sudo python veri_oku.py` kodu çalışğında veritabanına yeni bir kayıt eklenir. Ardından `python uygulama.py` komutu ile tekrar sunucu çalıştırılarak güncel web sitesine erişilebilir.</br>
![Sonuc](https://github.com/msensoy/GomSisProje/blob/master/Resimler/sonuc.PNG) </br>
 ### Sistemin Otomatikleştirilmesi
Manuel olarak çalıştırılan uygulamada verilerin otomatik olarak siteye gönderilebilmesi için Linux'un görev yöneticisi "cron" dan yararlanılabilir. Sistemin her 15 dk da bir çalışması için adım adım yapılacaklar :</br>
	1- /var/www/ klasör dizinine geçilir. </br>
	2- Terminal ekranına `sudo chmod +x veri_oku.py` komutu yazılır. Bu komut "veri_oku.py" dosyamızın çalıştırılabilir olmasını sağlar.</br>
	3- `sudo chown root:root /var/www/veri_oku.py` komutu yazılır. Bu komut "veri_oku.py" dosyamızın sahibini root kullanıcısı olarak ayarlar. Çünkü GPIO pinlerine erişebilmek için bu kodun root kullanıcısı tarafından çalıştırılması gerekir.</br>
	4- `sudo chmod 777 veriler.db` komutu ile veritabanı dosyamıza bütün kullanıcılar için yazma yetkisi verilir.</br>
	5- `sudo crontab -u root -e` komutu ile zamanlanmış görev eklenebilir. Bu komutu girdikten sonra ekrana açılacak olan dökümanın en alt satırına `*/15 * * * * /usr/bin/python /var/www/veri_oku.py` kodunu eklediğimizde işlemimiz tamamlanmış olacaktır. </br>
![Sonuc](https://github.com/msensoy/GomSisProje/blob/master/Resimler/cron.PNG) </br>
![Sonuc](https://github.com/msensoy/GomSisProje/blob/master/Resimler/sonucOtomatiklestirme.PNG) </br>
















