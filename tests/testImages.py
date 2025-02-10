import unittest
import json
from iiif2annos import ocr
from PIL import Image
import math

class TestImage(unittest.TestCase):

    def testCanvasImageMissmatch(self):
        with open("tests/fixtures/canvas.json", "r") as file:
            canvas = json.load(file)

            image = Image.open("tests/fixtures/images/gallica_ark_12148_bpt6k1526005v_f20_small.jpg")

            annos = ocr.run_ocr(image, canvas, "", 0) 

            edgar = annos[0]
            self.assertEqual(edgar["body"]["value"], "EDGAR")
            self.assertEqual(edgar["target"].split("#")[1], "xywh=1189,692,289,52")
