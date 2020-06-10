FROM quay.io/openshift/origin-jenkins-agent-base:4.4

RUN curl -O https://storage.googleapis.com/hey-release/hey_linux_amd64 && \
    chmod +x ./hey_linux_amd64 && \
    mv ./hey_linux_amd64 /usr/local/bin/hey

USER 1001
