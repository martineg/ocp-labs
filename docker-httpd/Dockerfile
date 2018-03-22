FROM python:3.5

LABEL maintainer="Martin Eggen <meggen@redhat.com>"

COPY srv/index.html /srv/index.html

WORKDIR /srv

EXPOSE 8000

CMD python -m http.server
