# iiif2annos
Read a manifest, OCR the images, create AnnotationLists and add them to a copy of the manifest

This tool uses the [tesseract](https://tesseract-ocr.github.io/) OCR engine. Ensure you have this installed and on your $PATH before running the code below. 

```
usage: ocr.py [-h] [--base-output-uri OUTPUTURI] [--lang LANG] [-c] manifest output

Read a manifest, OCR all the pages then adds the results as annotation lists

positional arguments:
  manifest              URL to Manifest file
  output                Output directory for annotation lists

options:
  -h, --help            show this help message and exit
  --base-output-uri OUTPUTURI
                        Output URI for annotations and annotation list
  --lang LANG           Language to pass to the OCR engine see: https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html
  -c, --confidence      Include OCR confidence value in text of the annotation?
```

This should work with v2 manifests and v3 manifest. For v2 AnnotationLists are created for v3 AnnotationPages are created. 

## Example

```
python iiif2annos/ocr.py --lang frk --base-output-uri http://localhost:5500/newspaper https://preview.iiif.io/cookbook/update_newspaper/recipe/0068-newspaper/newspaper_issue_1-manifest.json  newspaper
```


Using these blogs as a guide:

 * https://nanonets.com/blog/ocr-with-tesseract/#ocr-with-pytesseract-and-opencv 
 * https://pypi.org/project/pytesseract/


# Testing

Unit tests are in the tests folder and can be run with:

python -m unittest discover -s tests

Run single test:

python -m unittest tests.testImages.TestImage.testCanvasImageMissmatch
