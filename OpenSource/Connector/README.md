# Connector

__Connector__ is a program to simplify the SSH-Tunneling process via a Bastion host. This is designed to run on your local computer. Here we have provided binaries for Ubuntu and MacOS. If you are using Windows, first install the windows subsystem for linux (WSL) and use the binary for Ubuntu. Always if you require, you can compile the program following instructions give below. 

* For the Connector to work you must have a Bastion host on the public subnet and your Rstudio server or Jupyter notebook must be installed on the private subnet. 
* User names for both bastion host and the compute instance running on the private subnet must be the same.


## How to use it

### Using the precompiled binary


#### On Ubuntu and MacOS

```{bash}
After downloading the binary just run

./connector

```

#### On Windows

* Use powershell to run the connector

```{bash}
.\connector.exe
```


Commandline arguments for the Connector are as follows. 

```{bash}
Usage: connector [OPTIONS] 
    -b = [Required] Ip of the bastion host
    -d = [Required] Ip of the destination
    -k = [Required] Path to the private key
    -u = [Required] User name
    -j = [Optional] Jupyter-Notebook port 8888 forward to localhost
    -r = [Optional] Rstudio-server port 8787 forward to localhost
    -s = [Optional] Only shell access
    -f = [Optional] SFTP port (22) forward to localhost
```


### Compiling

NOTE: You will need gcc installed on your computer. To compile just run

```{bash}
make
```

This will produce a binary called connector, which you can execute following instructions given under "Using the precompiled binary". 


### IMPORTANT NOTEs: 

At a given time, you can only use this to connect to either jupyter, Rstudio server, get a terminal connection or forward SFT to localhost. 

### For jupyter:

If you coose to connect to the jupyter notebook, connector will create a tunel, forward the port 8888 to your localhost and open a terminal session to the instance running jupyter but will not launch jupyter. You are required to launch it manually by typing the following command on the terminal that was opened by connector. 


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

Now refer to the line containing 
    http://localhost:8888/?token=dfgdfg543545d4fgdf5g4d3543gd54gd35fgd5f4d3fdgffdf
This is your login URL on the local computer. Now you can paste this on the Laptop/Desktop browser to access the Jupyter Notebook.

Example:

    http://localhost:8888/?token=dfgdfg543545d4fgdf5g4d3543gd54gd35fgd5f4d3fdgffdf


### For Rstudio server:

    http://localhost:8787/

If the installation was done using the __Myinstallaer__, the default user name for Rstudio server is __oci__ and the password is the one you setup during the installation process.

### For terminal connection

Using the commandline argument -s with other required arguments will provide you a terminal connection __without any port forwarding.__ 


### For SFTP forwarding to localhost

Using the commanline argument -f with other required arguments will forward the SFTP port 22 to localhost via the bastion host. Then on your SFTP client use localhost as the destination and port 22 as the port to connect for file transfer. 


```{}
E.g. 

On Filezilla: 
    Host = localhost
    Port = 22
    Logon type = Key file
    User = This could be either ubuntu or opc
    Key file = Path to the key file
```

If you encounter the following error on Linux or Mac operating systems, 

```{bash}
bind [127.0.0.1]:22: Permission denied
channel_setup_fwd_listener_tcpip: cannot listen to port: 22
Could not request local forwarding.
```

just run the connector as sudo. 

    E.g. sudo ./connector <other input arguments>