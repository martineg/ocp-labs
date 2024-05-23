# Example Tekton pipeline for ACS scanning of an application

Contains resources to create a pipeline to build using s2i and use ACS to scan the image before deployment
Before applying create a secret `acs_token` containing two key values for `rox_api_token` and `rox_central_endpoint` used by the acs tasks.

Example:
```
oc -n app1-dev create secret generic acs-token --from-literal rox_central_endpoint=central-stackrox.apps.cluster01.lab.:443 --from-literal rox_api_token=my-generated-ci-token
```

then apply the pipeline resources:
`oc create -k .`
