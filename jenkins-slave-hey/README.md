# jenkins-slave-hey

Provides a docker image with hey HTTP load generator as a Jenkins slave.

## Build in OpenShift
```bash
oc process -f https://raw.githubusercontent.com/redhat-cop/containers-quickstarts/master/.openshift/templates/jenkins-slave-generic-template.yml \
-p NAME=jenkins-slave-hey \
-p SOURCE_REPOSITORY_URL=https://github.com/martineg/ocp-labs.git \
-p SOURCE_REPOSITORY_REF=jenkins-slave-hey \
-p SOURCE_CONTEXT_DIR=jenkins-slave-hey \
-p DOCKERFILE_PATH=Dockerfile -p \
BUILDER_IMAGE_NAME=quay.io/openshift/origin-jenkins-agent-base:4.4 \
| oc create -f -
```