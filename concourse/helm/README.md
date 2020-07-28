# Install Concourse with Helm 3

Add the concourse Helm repo and create the required namespace:

```
helm repo add concourse https://concourse-charts.storage.googleapis.com/
kubectl create ns concourse
```

To install with local user:

```
helm upgrade concourse concourse/concourse -f values.yaml -n concourse --version 9.0.0 --install --timeout 1200s --set concourse.web.externalUrl=http://concourse.shared.tanzu.build
```

To install with GitHub auth make a copy of the template yaml file and add your Org ClientId and ClientSecret:

```
helm upgrade concourse concourse/concourse -f values-github.yaml -n concourse --version 9.0.0 --install --timeout 1200s --set concourse.web.externalUrl=http://concourse.shared.tanzu.build
```