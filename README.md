# tanzu-demo

## Platform steps

### Creating and getting access to cluster
1. Head to https://cloud.vmware.com and go to **Console** on the top right side to access **Tanzu Mission Control**.
2. Create a "Provisioned" cluster on AWS (AWS Creds will have to be configured first).
3. Click on the cluster that has been provisioned and use the "Access this cluster" menu to download the `kubeconfig` file.
4. Copy the contents of the file downloaded into `~/.kube/config`.

_Note that you will need to download and install the `tmc` cli to be able to authenticate to the cluster for the first time. Instructions on how to do that can be found here: https://tanzuemea.tmc.cloud.vmware.com/clidownload_

5. Use your `kubectl` tool to make sure you have access to the cluster: `kubectl cluster-info`.

### Overview
6. Show around the TMC mission control dashboard and the information you can view from the cluster. Show and explain concepts of **Cluster Groups** and **Workspaces**.
7. Let's create a Workspace now. To do that go to the **Workspaces** menu option and make sure you create a workspace with at least on **Namespace** on it.

### Policies
8. To demonostrate how policies work, go to **Policies**, select to create a policy by Namespace and select **Image registry**. Select the **Workspace** (or a specific namespace if you want) and **Add image registry policy**. You should add your own Harbor repository here (i.e.: harbor.tanzu.alexguedes.com).
9. Try and run a Kubernetes Pod now using a Docker Hub image: `kubectl -n aguedes-ns run --image=nginx --restart=Never nginx` - it should fail with the following: `Error from server (failed to match image policies: spec.containers[0].image: Forbidden: no matching image policy): admission webhook "validation.policies.tmc.cloud.vmware.com" denied the request: failed to match image policies: spec.containers[0].image: Forbidden: no matching image policy`.
10. Let's now try the same thing with an image part of the Harbor repository configured: `kubectl -n aguedes-ns run --image=harbor.tanzu.alexguedes.com/nginx/nginx:v1 --restart=Never nginx`.

### Inspections
11. Go to **Inspections** and run **New inspection**. Select the cluster created at the start. (This can take over 4 hours, so have a previoursly ran test to show results).

## Application deployment steps [WIP]

![Demo flow](https://raw.githubusercontent.com/aguedes-pivotal/tanzu-demo/master/images/demo-flow.png "Demo flow")

### Application deployment requirements
Three clusters will be used for the demo with the following configuration:
**Management Kubernetes Cluster**
* Tanzu Mission Control managed Cluster deployed with ClusterAPI to AWS
* Tanzu Kubernetes Grid - Kubernetes 1.17
* Tanzu Harbor - Enterprise-grade container registry
* Concourse - Declarative CI/CD pipelines

**AWS pre-production (Provisioned) and GCP production (Attached) Kubernetes Clusters**
* Drupal 8.8.3
* PostgreSQL 12
* Datadog Agent

### Configuring Tanzu Build Service

1. Show how kpack works and how it can be configured to push to Docker Registry - see **kpack** sub-directory.
2. Make a change to GitHub repo and show a new image getting created on the management cluster. GitHub repo: https://github.com/aguedes-pivotal/drupal8-cnb
3. Show Harbor and talk about image scanning, signage and replication.

### Deploying to Kubernetes

4. Check **k8s** sub-directory and use **drupal-k8s.yml** as an example.

### CI/CD with Concourse for VMware Tanzu

5. A Concourse pipeline will be used and will be triggered by a commit to the master branch on the application source code repository on Github. The configuration for this Concourse pipeline can be found inside the **concourse** sub-directory.

### Show Datadog

6. Show how Datadog was deployed to the cluster and walk through how the integration works.