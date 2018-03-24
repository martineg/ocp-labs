Basic httpd server to demo Docker strategy builds.
To instantiate, run `oc create -f cfg/docker-httpd.yaml`

To demo init containers, run `oc create -f cfg/docker-httpd-with-init.yaml`.
This creates a new deploymentconfig using an init container to modify the main container's environment before it starts up.
An additional route and service is created for this deployment.
This the docker-httpd image stream already exists.
