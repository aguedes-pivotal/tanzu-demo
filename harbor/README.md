# Harbor installation details

```
kubectl create ns harbor
helm install harbor harbor/harbor -n harbor --set expose.type=loadBalancer,expose.tls.enabled=false,externalURL=http://harbor.tanzu.alexguedes.com
```