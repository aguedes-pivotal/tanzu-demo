# Configuring DataDog for Kubernetes

Create the Service Account and Cluster Roles for Datadog:
```
kubectl create -f "https://raw.githubusercontent.com/DataDog/datadog-agent/master/Dockerfiles/manifests/rbac/clusterrole.yaml"
kubectl create -f "https://raw.githubusercontent.com/DataDog/datadog-agent/master/Dockerfiles/manifests/rbac/serviceaccount.yaml"
kubectl create -f "https://raw.githubusercontent.com/DataDog/datadog-agent/master/Dockerfiles/manifests/rbac/clusterrolebinding.yaml"
```

Configure PSP:
```
kubectl create rolebinding privileged-role-binding-datadog --clusterrole=vmware-system-tmc-psp-privileged  --user=system:serviceaccount:default:datadog-agent
```

Create secret with API key (get this from Datadog):
```
kubectl create secret generic datadog-secret --from-literal api-key="INSERT API KEY"
```

Apply the DataDog DaemonSet:
```
kubectl apply -f datadog-daemonset.yml
```