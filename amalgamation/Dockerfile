FROM cakecrusher/tesseract5 AS ut5

FROM python:3.7-slim

# Setting up code env
RUN mkdir code
WORKDIR /code

# Installing libraries
RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6
COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying Tesseract-OCR v.5
COPY --from=ut5 /usr/local/bin/ /usr/local/bin/
COPY --from=ut5 /usr/local/share/tessdata/ /usr/local/share/tessdata/
COPY --from=ut5 /usr/local/lib/ /usr/local/lib/
COPY --from=ut5 /sbin/ldconfig /sbin/
COPY --from=ut5 /sbin/ldconfig.real /sbin/
COPY --from=ut5 /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu

# Env variables for Tesseract
ENV TESSDATA_PREFIX=/usr/local/share/tessdata/ LDFLAGS=-L/usr/local/lib CFLAGS=-I/usr/local/include
RUN ldconfig

# Copy code
COPY . .

# Env variables to run flask in development flask
ENV FLASK_APP=server.py FLASK_ENV=development FLASK_RUN_HOST=0.0.0.0

# Initiate the server
EXPOSE 8080
CMD [ "python", "server.py" ]