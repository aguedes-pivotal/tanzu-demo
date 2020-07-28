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
<<<<<<< HEAD
```


helm upgrade harbor harbor/harbor -n harbor --version 1.4.1 \
    --set expose.ingress.hosts.core=harbor.shared.tanzu.build \
    --set expose.ingress.annotations.'kubernetes\.io/ingress\.class'=contour \
    --set expose.ingress.annotations.'certmanager\.k8s\.io/cluster-issuer'=letsencrypt-prod \
    --set externalURL=https://harbor.shared.tanzu.build \
    --set expose.tls.secretName=harbor-harbor-ingress-cert \
    --set notary.enabled=false \
    --set persistence.persistentVolumeClaim.registry.size=50Gi
=======
```
>>>>>>> 9bce99f1d1d0b48f2d760b3e6ca5e3d03db5bc1f
