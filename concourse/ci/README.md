# Configure Concourse Pipelines

Login to Concourse:
```
fly -t tanzu login --concourse-url http://concourse.tanzu.alexguedes.com
```

Set pipeline:
```
fly -t tanzu set-pipeline -p drupal-app -c pipeline.yml -l k8s.yml -l drupal-app.yml
```