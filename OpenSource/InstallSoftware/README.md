# Myinstaller

## Desctiption

Myinstaller is a python package designed to simplify the software installation process for bioinformaticiens. It provides a commandline based GUI to select software and install them automatically. Currently, it supports Ubuntu, Oracle Linux and CentOS operating systems. 

## How to download installer

```{bash}
wget Need to update later
```

## How to use

Once downloaded run 

```{bash}
chmod 777 <path>/Myinstaller
./Myinstaller
```

Then follow the instructions on the GUI

## Installing Rstudio 

__NOTE:__ If you choose to install Rstudio, during the setup process you will be asked to choose a password for the Rstudio server.

### Login credentials:

* __User name__ = oci
* __password__ = Password you choose during the installation process
* __port__ = 8787

#### If you choose to install Rstudio server on the public subnet (Not recommended)

__NOTE:__ Open port 8787 on the OCI VCN and the Linux OS

    http://Ip-addresss:8787

#### If you choose to install Rstudio server on the private subnet

First you will be required to create a ssh tunnel and forward port 8787 to localhost.

    http://localhost:8787


## Installing Jupyter Note book

If you choose to install jupyter notebook on an OCI instance, once the installation is complete, you will need to run the following command to launch the notebook. 

```{bash}
jupyter-notebook
```

This will produce an output similar to below

```{bash}
[I 23:03:02.132 NotebookApp] Serving notebooks from local directory: /home/opc
[I 23:03:02.132 NotebookApp] Jupyter Notebook 6.4.10 is running at:
[I 23:03:02.132 NotebookApp] http://localhost:8888/?token=dfgdfg543545d4fgdf5g4d3543gd54gd35fgd5f4d3fdgffdf
[I 23:03:02.132 NotebookApp]  or http://127.0.0.1:8888/?token=dfgdfg543545d4fgdf5g4d3543gd54gd35fgd5f4d3fdgffdf
[I 23:03:02.132 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 23:03:02.137 NotebookApp] No web browser found: could not locate runnable browser.
[C 23:03:02.138 NotebookApp] 
```


#### If you choose to install Jupyter notebook on the public subnet (Not recommended)

__NOTE:__ Open port 8888 on the OCI VCN and the Linux OS


    http://Ip-addresss:8888

#### If you choose to install Jupyter notebook on the private subnet

First you will be required to create a ssh tunnel and forward port 8888 to localhost.
To start the jupyter notebook type the following command on the terminal after ssh into the OCI-instance. 


```{bash}
jupyter-notebook
```


Refer to the terminal output of the "jupyter-notebook" command and copy the localhost URL with the token. 

Example:

    http://localhost:8888/?token=dfgdfg543545d4fgdf5g4d3543gd54gd35fgd5f4d3fdgffdf

Now you can paste this on the Laptop/Desktop browser to access the Jupyter Notebook.

#### Shutting down Jupyter notebook

To shutdown the jupyter notebook, press __Crtl+c__ 

```{bash}
^C[I 06:58:57.198 NotebookApp] interrupted
Serving notebooks from local directory: /home/opc
0 active kernels
Jupyter Notebook 6.4.10 is running at:
http://localhost:8888/?token=6925ea8a9db2dcbeb5530181e4b44a56722faf84c0a64ee2
 or http://127.0.0.1:8888/?token=6925ea8a9db2dcbeb5530181e4b44a56722faf84c0a64ee2
Shutdown this notebook server (y/[n])? 
```

Type the answer y for the question "Shutdown this notebook server (y/[n])?"

```{bash}
Shutdown this notebook server (y/[n])? y
[C 06:58:59.614 NotebookApp] Shutdown confirmed
[I 06:58:59.614 NotebookApp] Shutting down 0 kernels
[I 06:58:59.615 NotebookApp] Shutting down 0 terminals
```


