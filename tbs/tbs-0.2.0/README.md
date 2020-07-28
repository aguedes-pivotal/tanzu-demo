# Install Tanzu Build Service Beta 0.2.0

First download the packages from Tanzu Network:
https://network.pivotal.io/products/build-service

Login to your repository using Docker:
```
docker login https://harbor.shared.tanzu.build
```

Use duffle to relocate the images from GCR to your own container registry. This will upload all the container images you need to your container registry and generate a `relocated.json` file that will be required to install TBS.
```
duffle relocate -f packages/build-service-0.2.0.tgz -m relocated.json -p harbor.shared.tanzu.build/tbs-images
```

Create a credentials.yml file with your kubeconfig credentials and your self-signed CA if you're using one:
```
name: build-service-credentials
credentials:
 - name: kube_config
   source:
     path: "PATH-TO-KUBECONFIG"
   destination:
     path: "/root/.kube/config"
 - name: ca_cert
   source:
     path: ""
   destination:
     path: "/cnab/app/cert/ca.crt"
```

Install TBS with the following:
```
duffle install tbs -c credentials.yml  \
    --set kubernetes_env=shared-enterprise \
    --set docker_registry=harbor.shared.tanzu.build \
    --set docker_repository=harbor.shared.tanzu.build/tbs-images \
    --set registry_username="aguedes" \
    --set registry_password="MY_REGISTRY_PASSWORD" \
    --set custom_builder_image="harbor.shared.tanzu.build/tbs-images/default-builder" \
    -f packages/build-service-0.2.0.tgz \
    -m relocated.json
```

Useful commands to test if installation was successful:
```
kp custom-cluster-builder list
kp custom-cluster-builder status full
kp stack list
kp store list
```

Create a namespace for your builds:
```
kubectl create ns aguedes-builds
```

Set the context to use this new namespace (I use kubens for this):
```
kubens aguedes-builds
```

Create GitHub and Harbor secrets (credentials will be asked for both - for GitHub creds you should use a personal token instead of your password or SSH):
```
kp secret create harbor-shared --registry harbor.shared.tanzu.build --registry-user aguedes
kp secret create git-aguedes --git https://github.com --git-user aguedes-pivotal
```

Create an Image:
```
kp image create petclinic harbor.shared.tanzu.build/tbs-aguedes/petclinic \
  --custom-cluster-builder full \
  --namespace aguedes-builds \
  --wait \
  --git https://github.com/aguedes-pivotal/spring-petclinic \
  --git-revision master
```

To check the status of the image and the builds do the following:
```
kp image list
kp image status petclinic
kp build list petclinic
kp build status petclinic
kp build logs petclinic
```

To delete an image:
```
kp image delete petclinic
```

To uninstall TBS:
```
duffle uninstall tbs -c credentials.yml -m relocated.json
```