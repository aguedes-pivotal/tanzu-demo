# Install Tanzu Build Service Beta 0.1.0

First download the packages from Tanzu Network:
https://network.pivotal.io/products/build-service

Login to your repository using Docker:
```
docker login https://harbor.shared.tanzu.build
```

Use duffle to relocate the images from GCR to your own container registry. This will upload all the container images you need to your container registry and generate a `relocated.json` file that will be required to install TBS.
```
duffle relocate -f packages/build-service-0.1.0.tgz -m relocated.json -p harbor.shared.tanzu.build/tbsbeta
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
duffle install tbsbeta -c credentials.yml  \
    --set kubernetes_env=shared-enterprise \
    --set docker_registry=harbor.shared.tanzu.build \
    --set registry_username="aguedes" \
    --set registry_password="MY_REGISTRY_PASSWORD" \
    --set custom_builder_image="harbor.shared.tanzu.build/tbsbeta/default-builder" \
    --set admin_users="shared-enterprise" \
    -f packages/build-service-0.1.0.tgz \
    -m packages/relocated.json
```

Useful commands to test if installation was successful:
```
pb builder list
pb stack status
pb store list
pb builder status default --cluster
```

Create and target your project first:
```
pb project create aguedes-project
pb project target aguedes-project
```

Create GitHub and Harbor secrets:
```
pb secrets registry apply -f secrets/configure-registry.yml
pb secrets git apply -f secrets/configure-repo.yml
```

Create an Image (two examples - a Spring Boot one and a PHP one):
```
pb image apply -f secrets/drupal-image.yml
pb image apply -f secrets/petclinic-image.yml
```

To check the status of the image and the builds do the following:
```
pb image list
pb image builds harbor.shared.tanzu.build/drupal8/druapl8-cnb
pb image status harbor.shared.tanzu.build/drupal8/druapl8-cnb
pb image build harbor.shared.tanzu.build/drupal8/druapl8-cnb -b 1
pb image logs harbor.shared.tanzu.build/drupal8/druapl8-cnb -b 1 -f
```

To delete an image:
```
pb image delete harbor.shared.tanzu.build/drupal8/druapl8-cnb
```

To uninstall TBS:
```
duffle uninstall tbsbeta -c credentials.yml -m packages/relocated.json
```