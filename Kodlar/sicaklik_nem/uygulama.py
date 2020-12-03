import sqlite3
import json
from flask import Flask, render_template
app = Flask(__name__)

def verileri_al():
	baglanti = sqlite3.connect('/var/www/veriler.db')
	baglanti.row_factory = sqlite3.Row
	imlec = baglanti.cursor()
	imlec.execute('Select * from degerler')
	sat = imlec.fetchall()
	baglanti.commit()
	baglanti.close
	return sat

@app.route('/')
def ana_sayfa():
	veriler = verileri_al()
	return render_template('index.html', degerler = veriler)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
