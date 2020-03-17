# Install Concourse with Helm 3

```
kubectl create ns concourse
helm upgrade concourse concourse/concourse -f values.yaml -n concourse --version 9.0.0 --install --timeout 1200s --set concourse.web.externalUrl=http://concourse.tanzu.alexguedes.com
```