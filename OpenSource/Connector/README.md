# Connector

__Connector__ is a program to simplify the SSH-Tunneling process via a Bastion host. The Connector is designed to run on your local computer. Here we have provided binaries for Ubuntu, macOS and Windows. Using Windows, you could also run Ubuntu through Windows Subsystem for Linux (WSL). If required, you can always compile the program following the instructions below. 

* For the Connector to work, you must have a Bastion host on the public subnet, and your Rstudio server or Jupyter notebook must be installed on the private subnet. 
* User names for both the bastion host and the compute instance running on the private subnet must be the same.


## How to use it

### Using the precompiled binary


#### On Ubuntu and macOS

```{bash}
After downloading, change the directory to the place where you saved it.
Type: chmod 777 connector and then run as follows


./connector

```

#### On Windows

* Use PowerShell to run the Connector

```{bash}
.\connector.exe
```


Commandline arguments for the Connector are as follows. 

```{bash}
Usage: Connector [OPTIONS] 
-b = [Required] Ip of the bastion host
-d = [Required] Ip of the destination
-k = [Required] Path to the private key
-u = [Required] User name
-j = [Optional] Jupyter-Notebook port 8888 forward to localhost
-r = [Optional] Rstudio-server port 8787 forward to localhost
-s = [Optional] Only shell access
-f = [Optional] SFTP port (22) forward to localhost
-p = [Optional] Forward the port number given after -p to localhost
```


### Compiling

NOTE: You will need gcc installed on your computer. To compile, just run

```{bash}
make
```

This will produce a connector binary, which you can execute following instructions given under "Using the precompiled binary". 


### IMPORTANT NOTEs: 

You can only use this at a given time to connect to either the jupyter, Rstudio server, get a terminal connection, or forward SFT to localhost. 

### For jupyter:

Suppose you choose to connect to the jupyter notebook. In that case, Connector will create a tunnel, forward port 8888 to your localhost and open a terminal session to the instance running jupyter but will not launch jupyter. You are required to launch it manually by typing the following command on the terminal that was opened by the Connector. 


```{bash}
jupyter-notebook
```

This will produce an output similar to below.

```{bash}
[I 23:03:02.132 NotebookApp] Serving notebooks from local directory: /home/opc
[I 23:03:02.132 NotebookApp] Jupyter Notebook 6.4.10 is running at:
[I 23:03:02.132 NotebookApp] http://localhost:8888/?token=dfgdfg543545d4fgdf5g4d3543gd54gd35fgd5f4d3fdgffdf
[I 23:03:02.132 NotebookApp] or http://127.0.0.1:8888/?token=dfgdfg543545d4fgdf5g4d3543gd54gd35fgd5f4d3fdgffdf
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

If the installation was done using the __Myinstallaer__, the default user name for the Rstudio server is __oci__, and the password is the one you set up during the installation process.

### For terminal connection

Using the command line argument -s with other required arguments will provide you with a terminal connection __without any port forwarding.__ 


### For SFTP forwarding to localhost

Using the command line argument -f with other required arguments will forward the SFTP port 22 to localhost via the bastion host. Then on your SFTP client, use localhost as the destination and port 22 as the port to connect for file transfer. 


```{}
E.g. 

On Filezilla: 
Host = localhost
Port = 22
Logon type = Key file
User = This could be either Ubuntu or opc
Key file = Path to the key file
```

If you encounter the following error on Linux or Mac operating systems, 

```{bash}
bind [127.0.0.1]:22: Permission denied
channel_setup_fwd_listener_tcpip: cannot listen to port: 22
Could not request local forwarding.
```

just run the Connector as sudo. 

	E.g. sudo ./connector <other input arguments>


### Forwarding a given port number to localhost

Using the command line argument -p and providing a port number will forward the given port number to localhost. 

	E.g. ./connector <other required arguments> -p 8080 will forward port 8080 to localhost.


If you encounter the following error on Linux or Mac operating systems, 

```{bash}
bind [127.0.0.1]:80: Permission denied
channel_setup_fwd_listener_tcpip: cannot listen to port: <Port number you asked for>
Could not request local forwarding.
```

just run the Connector as sudo. 

	E.g. sudo ./connector <other input arguments>