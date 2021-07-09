# flask-tess5

### Inside the tesseract5-setup directory run
  docker build -t ubuntu-tesseract5 .
### Inside the video-preprocessing directory run
  docker-compose up
### Once everything is set up and the server is running
  send a get request to localhost:5000/test
    a proof-test.jpg image should be generated in media with text identified
