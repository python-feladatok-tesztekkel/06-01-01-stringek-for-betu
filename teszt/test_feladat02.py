from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class VanE(TestCase):
    def test_feladat01(self):
        mondat="nincs"
        aktualis = feladatok.megszamol_nagybetuket(mondat)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a mondatban hányyszor szerepel nagybetű: "+mondat)
    def test_feladat02(self):
        mondat="Nincs itt nagybetŰ"
        aktualis = feladatok.megszamol_nagybetuket(mondat)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a mondatban hányyszor szerepel nagybetű: "+mondat)
    def test_feladat03(self):
        mondat="Nincs iTT nagybetŰ"
        aktualis = feladatok.megszamol_nagybetuket(mondat)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy a mondatban hányyszor szerepel nagybetű: "+mondat)