from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class VanE(TestCase):
    def test_feladat01(self):
        mondat="nincs"
        aktualis = feladatok.megszamol_szamokat(mondat)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a mondatban hányyszor szerepel szám: "+mondat)
    def test_feladat02(self):
        mondat="1Nincs 1itt nagybet1"
        aktualis = feladatok.megszamol_szamokat(mondat)
        elvart = 3
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a mondatban hányyszor szerepel szám: "+mondat)
    def test_feladat03(self):
        mondat="Nincs i11 nagy11bet"
        aktualis = feladatok.megszamol_szamokat(mondat)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a mondatban hányyszor szerepel szám: "+mondat)