# tanzu-demo

## Platform steps

### Creating and getting access to cluster
1. Head to https://cloud.vmware.com and go to *Console* on the top right side to access *Tanzu Mission Control*.
2. Create a "Provisioned" cluster on AWS (AWS Creds will have to be configured first).
3. Click on the cluster that has been provisioned and use the "Access this cluster" menu to download the `kubeconfig` file.
4. Copy the contents of the file downloaded into `~/.kube/config`.

_Note that you will need to download and install the `tmc` cli to be able to authenticate to the cluster for the first time. Instructions on how to do that can be found here: https://tanzuemea.tmc.cloud.vmware.com/clidownload_

5. Use your `kubectl` tool to make sure you have access to the cluster: `kubectl cluster-info`.

### Overview
6. Show around the TMC mission control dashboard and the information you can view from the cluster. Show and explain concepts of *Cluster Groups* and *Workspaces*.
7. Let's create a Workspace now. To do that go to the *Workspaces* menu option and make sure you create a workspace with at least on *Namespace* on it.

### Policies
8. To demonostrate how policies work, go to *Policies*, select to create a policy by Namespace and select *Image registry*. Select the *Workspace* (or a specific namespace if you want) and *Add image registry policy*. You should add your own Harbor repository here (i.e.: harbor.tanzu.alexguedes.com).
9. Try and run a Kubernetes Pod now using a Docker Hub image: `kubectl -n aguedes-ns run --image=nginx --restart=Never nginx` - it should fail with the following: `Error from server (failed to match image policies: spec.containers[0].image: Forbidden: no matching image policy): admission webhook "validation.policies.tmc.cloud.vmware.com" denied the request: failed to match image policies: spec.containers[0].image: Forbidden: no matching image policy`.
10. Let's now try the same thing with an image part of the Harbor repository configured: `kubectl -n aguedes-ns run --image=harbor.tanzu.alexguedes.com/nginx/nginx:v1 --restart=Never nginx`.

### Inspections
11. Go to *Inspections* and run *New inspection*. Select the cluster created at the start. (This can take over 4 hours, so have a previoursly ran test to show results).

## Application deployment steps

![Demo flow](https://raw.githubusercontent.com/aguedes-pivotal/tanzu-demo/master/images/demo-flow.png "Demo flow")

