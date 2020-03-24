# Sonobuoy

The Sonoboys binaries can be downloaded from here: https://github.com/vmware-tanzu/sonobuoy

To run Sonobuoy with the CIS benchmark provided by Aquasec do the following:

```sonobuoy run --plugin https://raw.githubusercontent.com/vmware-tanzu/sonobuoy-plugins/master/cis-benchmarks/kube-bench-plugin.yaml --wait
results=$(sonobuoy retrieve)
sonobuoy results $results```