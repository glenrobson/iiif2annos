# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Run all tests:
```
python -m unittest discover -s tests
```

Run a single test:
```
python -m unittest tests.testImages.TestImage.testCanvasImageMissmatch
```

Run the OCR tool:
```
python iiif2annos/ocr.py --lang frk --base-output-uri http://localhost:5500/newspaper <manifest_url> <output_dir>
```

Dependencies: `pip install -r requirements.txt`. Also requires `tesseract` installed and on `$PATH`.

## Architecture

All logic lives in `iiif2annos/ocr.py`. The `OCR` class is the main entry point; `ocr.py` is also runnable as a CLI script via `__main__`.

### IIIF version handling

The codebase supports both IIIF Presentation API v2 and v3. V2/v3 diverge at every data structure level — canvases, services, annotations, and annotation containers all have different keys. The pattern throughout is to check `'id' in canvas` (v3) vs `'@id'`-style keys (v2) and branch accordingly. Functions `canvases()`, `get_service()`, `buildIIIFImage()`, `buildAnno()`, `mkannotations()`, and `addAnnotations()` all contain this v2/v3 branching.

### Coordinate system

Images downloaded from IIIF may differ in resolution from the canvas dimensions declared in the manifest. `run_ocr()` computes `xRatio`/`yRatio` from `canvas["width"] / img.width` and `canvas["height"] / img.height`, then scales all tesseract bounding boxes to canvas coordinates before writing annotation targets.

### Data flow

1. `downloadManifest()` fetches a manifest URL → parsed JSON
2. `OCR.ocr()` iterates canvases, fetches each full image via IIIF Image API, calls `run_ocr()`
3. `run_ocr()` runs `pytesseract.image_to_data()`, filters empty/negative-confidence results, scales coords, and calls `buildAnno()` for each word
4. `mkannotations()` wraps the annotation list into an AnnotationPage (v3) or AnnotationList (v2)
5. `addAnnotations()` mutates the canvas to point to the annotation list
6. `save()` writes `manifest.json` and one JSON file per canvas to the output directory

### Test fixtures

Tests use local JSON fixtures in `tests/fixtures/` (v2 manifest, v3 manifest, a canvas JSON) and a small image file. Tests import `iiif2annos.ocr` directly and call module-level functions — no mocking of HTTP calls; the image test uses a local file.
