FROM ubuntu:18.04 AS tesseract5-build

# Version
ENV TESSERACT_VERSION=5.0.0-alpha-20210401

# Working directory
RUN mkdir tess5-build
WORKDIR /tess5-build

# Setting up source code for build
RUN apt-get update
RUN apt-get install -y curl wget unzip
RUN wget https://github.com/tesseract-ocr/tesseract/archive/refs/tags/5.0.0-alpha-20210401.zip
RUN unzip 5.0.0-alpha-20210401.zip
RUN rm 5.0.0-alpha-20210401.zip
WORKDIR /tess5-build/tesseract-5.0.0-alpha-20210401


# Building tesseract
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y autoconf automake libtool pkg-config libpng-dev libjpeg8-dev libtiff5-dev g++ # or clang++ (presumably)
RUN apt-get install -y zlib1g-dev libleptonica-dev
RUN ./autogen.sh
RUN ./configure --enable-debug
RUN LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make
RUN make install
RUN ldconfig

# Downloading language data
WORKDIR /usr/local/share/tessdata
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
ENV TESSDATA_PREFIX=/usr/local/share/tessdata/

# Clean environment for tesseract
FROM ubuntu:18.04

# Copying tesseract5 build
COPY --from=tesseract5-build /usr/local/bin/ /usr/local/bin/
COPY --from=tesseract5-build /usr/local/share/tessdata/ /usr/local/share/tessdata/
COPY --from=tesseract5-build /usr/local/lib/ /usr/local/lib/
COPY --from=tesseract5-build /sbin/ldconfig /sbin/
COPY --from=tesseract5-build /sbin/ldconfig.real /sbin/
COPY --from=tesseract5-build /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu

# Env variables for Tesseract
ENV TESSDATA_PREFIX=/usr/local/share/tessdata/ LDFLAGS=-L/usr/local/lib CFLAGS=-I/usr/local/include
RUN ldconfig