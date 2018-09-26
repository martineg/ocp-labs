Simple Flask application to demonstrate S2I builds.
Includes an endpoint `/invalidate` to make application seem unhealthy in order to demonstrate built-in self healing capabilities in OpenShift.

Includes version and basic environment-based feature toggle to demonstrate various deployment strategies in OpenShift.

Define and build the Python Jenkins slave

```
    oc process -f https://raw.githubusercontent.com/redhat-cop/containers-quickstarts/master/jenkins-slaves/templates/jenkins-slave-generic-template.yml \
    -p NAME=jenkins-slave-python \
    -p SOURCE_CONTEXT_DIR=jenkins-slaves/jenkins-slave-python \
    -p DOCKERFILE_PATH=Dockerfile \
    -p BUILDER_IMAGE_NAME=openshift/jenkins-slave-base-centos7 \
    | oc create -f -
```

and then create the build pipeline

```
oc new-build 'https://github.com/martineg/ocp-labs#python-jenkins-build' --context-dir=s2i-flask --name=s2i-flask-pipeline
```
