# Example Tekton pipeline for ACS scanning of an application

Contains resources to create a pipeline to build using s2i and use ACS to scan the image before deployment
Before applying create a file `acs.env` containing two key/value pairs for `rox_api_token` and `rox_central_endpoint` used by the acs tasks. To create the CI token in ACS, go to Platform Configuration -> Integrations -> API token, then generate a token with Role set to _Continuous Integration_.

Example:
```
cat <<EOF > acs.env
rox_central_endpoint=central-stackrox.apps.cluster01.labs.local:443
rox_api_token=my-ci-token-value
EOF
```