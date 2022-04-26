Python Template repository
--------------------------

This repository comes with a pre-defined python package structure. 

Self-Setup
~~~~~~~~~~
Once a repository is created from this template, it will setup itself with a github action, 
deriving the actual package name from the repository name.

Pre-Defined Docker
~~~~~~~~~~~~~~~~~~
Furthermore it comes with pre-defined docker images for deep learning (derived from either a base conda one or the NVIDIA NGC PyTorch one).
The docker images are automatically built on each PR and can be automatically uploaded to dockerhub via github actions after each commit to main.
For this to work, the user needs to set the secrets **DOCKERHUB_USERNAME** and **DOCKERHUB_TOKEN** to the associated username and token respectively.

PyPi-Publishing
~~~~~~~~~~~~~~~
Whenever a release is created on github, there is a github action running to automatically test if the package can be built and installed and tries to automatically publish it to PyPi and PyPi-Test.
The PyPi release is only triggered, if the PyPi-Test release succeeds. For this to work the user has to set the secrets **TEST_PYPI_API_TOKEN** and **PYPI_API_TOKEN**.
These tokens can either be obtained on a general per-user basis or per project after publishing manually for the first time.

Automatic Testing
~~~~~~~~~~~~~~~~~
Tests lying under the ``tests`` directory, are automatically run after each commit. The dependencies will thereby be cached on a weekly basis to speedup the development progress.
In order to get proper code coverage details, users may want to alter the ``ci.yaml`` file in the workflows directory to include ``--source=YOUR_PACKAGE_NAME`` to the ``coverage run`` command in the ``Tests`` step.
Furthermore users can specify the **CODECOV_TOKEN** secret to upload their coverage results to codecov.


