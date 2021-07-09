# flask-tess5

A docker environment for running a flask server with Tesseract-OCR v.5

## Set up

Clone the repo
```bash
git clone https://github.com/CakeCrusher/flask-tesseract5.git
```
Navigate to amalgamation directory
```bash
cd amalgamation
```
Initiate docker compose
```bash
docker-compose up
```

## Docker images

Tesseract-OCR v.5
```bash
docker pull cakecrusher/tesseract5
```
Flask server with Tesseract-OCR v.5
```bash
docker pull cakecrusher/flask-ocr
```