from flask import Flask   #Bu satır, Python'da Flask kütüphanesini içeri aktarır (import eder). Flask, web uygulaması oluşturmanıza yardımcı olan ana bileşendir.

app = Flask(__name__) #Bu, bir Flask uygulaması örneği (instance) oluşturur. Uygulamanın çalışacağı ana nesnedir. __name__ değişkeni, Flask'ın nerede çalıştığını bilmesi için standart bir Python parametresidir.

@app.route('/') #Flask'a, hemen altındaki fonksiyonu hangi URL (web adresi) isteği geldiğinde çalıştırması gerektiğini söyler.
def home(): #Bu, web isteği geldiğinde çalışacak olan Python fonksiyonunu tanımlar. Bu fonksiyona genellikle bir isim verilir (home gibi)
    return "Merhaba, Buluttan Selam!"
