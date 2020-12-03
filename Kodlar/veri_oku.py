#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3
import Adafruit_DHT

def verileri_al(sicaklik,nem):
        baglanti = sqlite3.connect('veriler.db')
        imlec = baglanti.cursor()
        imlec.execute("INSERT INTO degerler  VALUES(datetime('now'),(?),(?))",(sicaklik,nem))
        baglanti.commit()
        baglanti.close()

def sicaklik_ve_nem_oku():
        nem,sicaklik = Adafruit_DHT.read_retry(11,17)
        verileri_al(sicaklik,nem)

if __name__ == '__main__':
	sicaklik_ve_nem_oku()
