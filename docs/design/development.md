# AVL Development

Most AVL development activity centres around repositories belonging to the
[`agriculture-vlab` GitHub organization](https://github.com/agriculture-vlab).
This organization currently has two active repositories, `agriculture-vlab`
and `avl-jh-user-image`.

## The `agriculture-vlab` repository

The [`agriculture-vlab` repository](https://github.com/agriculture-vlab/)
contains code written expressly for the AVL project, implementing a Python API
and a command-line interface for AVL-specific functionality.

The repository also contains the source files, in Markdown format, for the AVL
documentation, including this document. These source files are processed
by [mkdocs](https://www.mkdocs.org/) into the published project documentation.

## The `avl-jh-user-image` repository

The [`avl-jh-user-image`
repository](https://github.com/agriculture-vlab/avl-jh-user-image)
is a single-purpose GitHub repository hosting a dockerfile which defines the
JupyterHub user image for the AVL Exploitation Subsystem notebook environment.
When a user starts the notebook environment, this is the container image with
which it is initialized.

The dockerfile in this repository takes as its base the `scipy-notebook` image
from the
[Jupyter docker-stacks project](https://github.com/jupyter/docker-stacks)
project and customizes it for the requirements of the AVL, mainly by
installing additional required packages such as xcube and updating selected
packages to fix known vulnerabilities.

The image is rebuilt automatically by the quay.io build service when the
GitHub repository is updated, and hosted in a docker image repository at
<https://quay.io/repository/bcdev/avl-user>.

## Deployment of the exploitation subsystem

The JupyterHub-based exploitation subsystem is deployed on a dedicated
Kubernetes cluster running on the AWS EKS service. JupyterHub is deployed
using the [helm](https://helm.sh/) package manager with a chart from the
[JupyterHub helm chart repository](https://jupyterhub.github.io/helm-chart/).
Deployment of the exploitation subsystem is fully documented in the operator
manual.
