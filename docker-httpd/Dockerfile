FROM python:3.5

LABEL maintainer="Martin Eggen <meggen@redhat.com>" \
    description="Basic web server to demonstrate Docker builds" \
    vcs-url="https://github.com/martineg/ocp-labs.git"

COPY srv/index.html /srv/index.html

WORKDIR /srv

EXPOSE 8000

CMD python -m http.server
