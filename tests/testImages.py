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

            for anno in annos:
                self.assertNotEqual(len(anno["body"]["value"].strip()), 0, f"Found empty anno: \n{json.dumps(anno, indent=4)}")

    def testRegionOCRCoordinates(self):

        image = Image.open("tests/fixtures/images/gallica_ark_12148_bpt6k1526005v_f20_small.jpg")
        canvas= {
            "id": "https://example.org/canvas",
            "width": 1000,
            "height": 1440
        }

        # Region offset in canvas coordinates (bottom right quarter)
        rx, ry, rw, rh = 500, 720, 500, 720

        # Convert canvas region to image pixel coordinates for cropping
        cropped = image.crop((rx, ry, rx + rw, ry + rh))

        region_canvas = dict(canvas)
        region_canvas["width"] = rw
        region_canvas["height"] = rh

        annos = ocr.run_ocr(cropped, region_canvas, "", 0, x_offset=rx, y_offset=ry)

        # EDGAR (canvas coords 1189,692) is within the region — coordinates should match the full-image result
        successeur = annos[2]
        self.assertEqual(successeur["body"]["value"], "Successeur")
        coords = successeur["target"].split("#xywh=")[1]
        x, y, w, h = [int(v) for v in coords.split(",")]
        self.assertEqual(x, 580)
        self.assertEqual(y, 1127)
        self.assertEqual(w, 103)
        self.assertEqual(h, 16)
