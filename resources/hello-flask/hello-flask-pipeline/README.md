Contains resources to create a pipeline to build and scan the application.
Before applying create a secret `acs_token` containing two key values for `rox_api_token` and `rox_central_endpoint` used by the acs tasks.

 

Example:
```
oc create secret generic acs-token --from-literal rox_central_endpoint=central-stackrox.apps.cluster01.lab.:443 --from-literal rox_api_token=my-generated-ci-token
```
