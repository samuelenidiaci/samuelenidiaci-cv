FROM python:3.8.18-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get upgrade -y

RUN apt install wget -y

WORKDIR /texlive

RUN wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
RUN zcat < install-tl-unx.tar.gz | tar xf -
RUN cd install-tl-* && perl ./install-tl --no-interaction --scheme=basic --no-doc-install --no-src-install

ENV PATH="${PATH}:/usr/local/texlive/2023/bin/x86_64-linux"

RUN tlmgr init-usertree

RUN tlmgr install latexmk texliveonfly

WORKDIR /app