FROM ubuntu

RUN apt-get update
RUN apt-get install -y ruby-dev

WORKDIR "/webpage"
CMD ["bundle","exec jekyll serve"]

