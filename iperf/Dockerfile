FROM docker.io/centos:7
RUN yum install -y iperf3
ENTRYPOINT trap : TERM INT; sleep infinity & wait # Listen for kill signals and exit quickly.
