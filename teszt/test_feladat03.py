from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class Megszamol(TestCase):
    def test_feladat01(self):
        keresett='e'
        mondat="Nincs"
        aktualis = feladatok.megszamol(keresett,mondat)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű hányszor szerepel a mondatban: "+mondat)
    def test_feladat02(self):
        keresett='E'
        mondat="Nincs"
        aktualis = feladatok.megszamol(keresett,mondat)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű hányszor szerepel a mondatban: "+mondat)
    def test_feladat03(self):
        keresett='E'
        mondat="Nincs a betű"
        aktualis = feladatok.megszamol(keresett,mondat)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű hányszor szerepel a mondatban: "+mondat)
    def test_feladat04(self):
        keresett='e'
        mondat="Nincs a betű"
        aktualis = feladatok.megszamol(keresett,mondat)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű hányszor szerepel a mondatban: "+mondat)
    def test_feladat05(self):
        keresett='e'
        mondat="eaea eaea EAEA EAEA eaeaa mondatban: "
        aktualis = feladatok.megszamol(keresett,mondat)
        elvart = 10
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a(z) "+str(keresett)+" betű hányszor szerepel a mondatban: "+mondat)

