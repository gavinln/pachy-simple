# pachy-simple

* Source code - [Github][10]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[10]: https://github.com/gavinln/pachy-simple

## About

This project provides a [Ubuntu (16.04)][20] [Vagrant][30] Virtual Machine
(VM) used for reproducible data science using [Pachyderm][40].

It has [Docker][50] installed using [Ansible][60]

[20]: http://releases.ubuntu.com/14.04/
[30]: http://www.vagrantup.com/
[40]: http://www.pachyderm.io/open_source.html
[50]: https://www.docker.com/
[60]: https://www.ansible.com/

## Setting up Pachyderm

1. Install [Minikube][70]

[70]: https://kubernetes.io/docs/tasks/tools/install-minikube/

2. Install [kubectl][80]

[80]: https://kubernetes.io/docs/tasks/tools/install-kubectl/

3. Start Minikube

    ```
    minikube start
    ```

4. Display the status of Minikube

    ```
    minikube status
    ```

## Running the VM

1. Change to the root of the project

    ```
    cd pachy-simple
    ```

3. Set up the Minikube config directory

    ```
    set MK_CONFIG_DIR=%USERPROFILE%\.minikube
    ```

2. To start the virtual machine(VM) type

    ```
    vagrant up
    ```

3. Connect to the VM

    ```
    vagrant ssh pachy-simple
    ```

## Requirements

The following software is needed to get the software from github and run
Vagrant to set up the Python development environment. The Git environment
also provides an [SSH  client][200] for Windows.

* [Oracle VM VirtualBox][210]
* [Vagrant][220]
* [Git][230]

[200]: http://en.wikipedia.org/wiki/Secure_Shell
[210]: https://www.virtualbox.org/
[220]: http://vagrantup.com/
[230]: http://git-scm.com/
