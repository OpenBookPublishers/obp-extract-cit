FROM openjdk:11-slim-buster

WORKDIR /ebook_automation

RUN apt-get update && \
    apt-get install -y libsaxonb-java zip
RUN rm -rf /var/cache/apt/*

COPY run ./
COPY Extract-citations-from-book.xsl ./

ENV OUTDIR=/ebook_automation/output

CMD bash run file
