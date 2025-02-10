import unittest
import json
from iiif2annos import ocr

class TestManifest(unittest.TestCase):

    def testv2(self):
        with open("tests/fixtures/v2.json", "r") as file:
            manifest = json.load(file)
            canvases = ocr.canvases(manifest, sequence=0)

            self.assertEqual(len(canvases), 2)

    def testv3(self):
        with open("tests/fixtures/v3.json", "r") as file:
            manifest = json.load(file)
            canvases = ocr.canvases(manifest, sequence=0)

            self.assertEqual(len(canvases), 2)