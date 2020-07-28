# Harbor installation details

If you're using a cluster provisioned by TMC, make sure you either configure the PSPs or disable them (only use it on non-prod environments):

```
kubectl create rolebinding privileged-role-binding \
    --clusterrole=vmware-system-tmc-psp-privileged \
    --user=system:serviceaccount:default:default
```

```
kubectl create ns harbor
helm repo add harbor https://helm.goharbor.io
helm install harbor harbor/harbor -n harbor --set expose.type=loadBalancer,expose.tls.enabled=false,registry.relativeurls=true,externalURL=http://harbor.shared.tanzu.build
```
