from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class VanE(TestCase):
    def test_feladat01(self):
        keresett='e'
        mondat="Nincs"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = False
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat02(self):
        keresett='E'
        mondat="Nincs"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = False
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat03(self):
        keresett='a'
        mondat="Alma"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat04(self):
        keresett='A'
        mondat="Alma"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat05(self):
        keresett='r'
        mondat="Megy a szekér"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat06(self):
        keresett='R'
        mondat="Megy a szekér"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat07(self):
        keresett='e'
        mondat="aaaaaaaaa a aaaaaaaaaa aaaaaaaaaaE"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat08(self):
        keresett='e'
        mondat="aaaaaaaaa a aaaaaaaaaa aaaaaaaaaae"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat09(self):
        keresett='e'
        mondat="aaaaaaaaa a aaaaaaaaaa aaaaaaaaaaE aaaaaaaaaaa"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)
    def test_feladat10(self):
        keresett='e'
        mondat="aaaaaaaaa a aaaaaaaaaa aaaaaaaaaae aaaaaaaaaaaaaaaaa"
        aktualis = feladatok.van_e(keresett,mondat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű van -e a következő mondatban: "+mondat)

