FROM python:3.8.0-slim-buster

WORKDIR /ebook_automation

# https://github.com/geerlingguy/ansible-role-java/issues/64#issuecomment-393299088
RUN mkdir -p /usr/share/man/man1
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk libsaxonb-java zip
RUN rm -rf /var/cache/apt/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run ./
COPY ./src/ ./src/
COPY Extract-citations-from-book.xsl ./

ENV OUTDIR=/ebook_automation/output

CMD bash run file
