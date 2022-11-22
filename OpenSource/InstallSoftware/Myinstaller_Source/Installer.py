def OL_installer(package):


    """
    Install packages on Oracle linux and CentOS

    :param package: [str] Package to install (Key for the dictionary)
    :return: [dictionary] Commands to install software
    """


    install_libs = """
    sudo dnf update -y
    sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
    sudo dnf update -y
    sudo dnf install git -y
    sudo dnf install make automake gcc gcc-c++ kernel-devel -y
    sudo dnf install python3-pip -y
    sudo pip3 install --upgrade pip
    pip3 install pandas
    pip3 install Bio
    sudo yum install java-1.8.0-openjdk -y
    sudo dnf -y install gcc-gfortran
    sudo dnf install openmpi openmpi-devel -y
    pip3 install biopython
    """

    FASTQC = """
    wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip
    unzip fastqc_v0.11.9.zip
    chmod 777 FastQC/fastqc
    sudo cp FastQC/fastqc /usr/local/bin
    cd 
    sudo rm -fr FastQC fastqc_v0.11.9.zip
    """

    Cutadapt = """
    sudo pip3 install cutadapt 
    """

    Multiqc = """
    sudo pip3 install multiqc
    """

    Samtools = """
    sudo dnf install samtools -y
    """

    Vcftools = """
    sudo dnf -y install vcftools
    """

    Clustalw = """
    wget http://www.clustal.org/download/current/clustalw-2.1.tar.gz
    tar -xvf clustalw-2.1.tar.gz
    cd clustalw-2.1
    ./configure
    make
    sudo make install
    cd 
    sudo rm -rf clustalw-2.1.tar.gz clustalw-2.1
    """

    Muscle = """
    wget https://github.com/rcedgar/muscle/releases/download/v5.1/muscle5.1.linux_intel64
    chmod 777 muscle5.1.linux_intel64
    sudo mv muscle5.1.linux_intel64 /usr/local/bin/muscle
    """

    Mafft = """
    wget https://mafft.cbrc.jp/alignment/software/mafft-7.490-gcc_fc6.x86_64.rpm
    sudo rpm -i mafft-7.490-gcc_fc6.x86_64.rpm
    cd 
    sudo rm -rf mafft-7.490-gcc_fc6.x86_64.rpm
    """

    Prank = """
    wget http://wasabiapp.org/download/prank/prank.linux64.170427.tgz
    tar -xvf prank.linux64.170427.tgz
    sudo rm -rf $PWD/fprank/bin/lib
    sudo mv $PWD/prank/bin/prank /usr/local/bin/
    cd 
    sudo rm -rf prank prank.linux64.170427.tgz
    """

    Trinity = """
    wget https://github.com/trinityrnaseq/trinityrnaseq/releases/download/Trinity-v2.14.0/trinityrnaseq-v2.14.0.FULL.tar.gz
    sudo tar -xvf trinityrnaseq-v2.14.0.FULL.tar.gz -C /opt/
    sudo ln -s /opt/trinityrnaseq-v2.14.0/Trinity /usr/local/bin/trinity
    sudo rm -rf $PWD/trinityrnaseq-v2.14.0.FULL.tar.gz
    """

    Busco = """
    git clone https://gitlab.com/ezlab/busco.git
    cd busco/
    sudo python3 setup.py install --user
    sudo python3 setup.py install
    sudo rm -rf /home/$(whoami)/busco 
    cd
    """

    STAR = """
    wget https://github.com/alexdobin/STAR/archive/2.7.10a.tar.gz
    tar -xvf 2.7.10a.tar.gz
    cd STAR-2.7.10a/source
    make STAR
    sudo mv STAR /usr/local/bin/
    cd
    sudo rm -rf /home/$(whoami)/2.7.10a.tar.gz STAR-2.7.10a
    """

    SUBREAD = """
    wget https://github.com/torkian/subread-1.6.1/archive/refs/heads/master.zip
    unzip master.zip
    cd subread-1.6.1-master/src
    make -f Makefile.Linux
    cd ../bin/utilities
    mv * /usr/local/bin/
    cd ../
    sudo rm -rf utilities
    sudo mv * /usr/local/bin/
    cd 
    sudo rm -rf /home/$(whoami)/master.zip subread-1.6.1-master
    """

    HIstat2 = """
    wget https://cloud.biohpc.swmed.edu/index.php/s/oTtGWbWjaxsQ2Ho/download
    mv download download.zip
    unzip download.zip
    cd hisat2-2.2.1
    sudo mv hisat2* /usr/local/bin/
    sudo mv extract_* /usr/local/bin/
    cd 
    sudo rm -rf download.zip  hisat2-2.2.1
    """

    TopHat = """
    wget https://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.Linux_x86_64.tar.gz
    tar -xvf tophat-2.1.1.Linux_x86_64.tar.gz
    cd tophat-2.1.1.Linux_x86_64/
    rm -rf AUTHORS intervaltree LICENSE README sortedcontainers
    sudo mv * /usr/local/bin
    cd 
    sudo rm -rf tophat-2.1.1.Linux_x86_64  tophat-2.1.1.Linux_x86_64.tar.gz
    """

    BWA = """
    git clone https://github.com/lh3/bwa.git
    cd bwa; make
    sudo mv bwa /usr/local/bin/
    cd 
    sudo rm -rf bwa/
    """

    Bowtie = """
    sudo dnf -y install bowtie
    """

    kallisto = """
    wget https://github.com/pachterlab/kallisto/releases/download/v0.46.1/kallisto_linux-v0.46.1.tar.gz
    tar -xvf kallisto_linux-v0.46.1.tar.gz 
    sudo mv kallisto/kallisto /usr/local/bin
    cd 
    sudo rm -rf tophat-2.1.1.Linux_x86_64  tophat-2.1.1.Linux_x86_64.tar.gz
    sudo rm -rf kallisto kallisto_linux-v0.46.1.tar.gz 
    """

    TEtranscripts = """
    pip3 install TEtranscripts
    """

    HTSeq = """
    pip3 install HTSeq
    """

    NCBI = """
    wget https://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz
    tar -xvf ncbi-blast-2.13.0+-x64-linux.tar.gz
    cd ncbi-blast-2.13.0+/bin/
    sudo mv * /usr/local/bin/
    cd 
    sudo rm -rf ncbi*
    """

    Mothur = """
    wget https://github.com/mothur/mothur/releases/download/v1.48.0/Mothur.linux_7.zip
    unzip Mothur.linux_7.zip
    cd mothur/
    rm LICENSE 
    sudo mv * /usr/local/bin
    cd 
    sudo rm -rf mothur  Mothur.linux_7.zip
    """

    FastTree = """
    wget wget http://meta.microbesonline.org/fasttree/FastTree.c
    gcc -DUSE_DOUBLE -O3 -finline-functions -funroll-loops -Wall -o FastTree FastTree.c -lm 
    sudo mv FastTree /usr/local/bin/
    cd 
    sudo rm -rf FastTree*
    """

    Phylip = """
    wget http://evolution.gs.washington.edu/phylip/download/phylip-3.697.tar.gz
    tar -xvf phylip-3.697.tar.gz
    cd phylip-3.697/src
    mv Makefile.unx makefile
    make install
    cd ../exe/
    sudo mv * /usr/local/bin/
    cd 
    sudo rm -rf phylip-3.697  phylip-3.697.tar.gz
    """

    Autodock = """
    sudo dnf install autodocksuite -y
    """

    Autodock_vina = """
    wget https://vina.scripps.edu/wp-content/uploads/sites/55/2020/12/autodock_vina_1_1_2_linux_x86.tgz
    tar -xvf autodock_vina_1_1_2_linux_x86.tgz
    sudo cp autodock_vina_1_1_2_linux_x86/bin/* /usr/local/bin
    cd 
    sudo rm -rf autodock_vina_1_1_2_linux_x86.tgz autodock_vina_1_1_2_linux_x86
    """

    Openbabel = """sudo dnf install openbabel -y"""

    GROMACS = """sudo dnf install gromacs -y"""

    NWchem = """sudo dnf install nwchem -y"""

    Quantum_ESPRESSO = """sudo dnf install quantum-espresso -y"""

    Xtandem = """
    wget http://ftp.thegpm.org/projects/tandem/source/2015-12-15/tandem-linux-15-12-15-2.zip
    unzip tandem-linux-15-12-15-2.zip
    cd tandem-linux-15-12-15-2/bin/
    sudo chmod 777 tandem.exe
    sudo mv tandem.exe /usr/local/bin/
    cd 
    sudo rm -rf tandem-linux-15-12-15-2  tandem-linux-15-12-15-2.zip
    """

    Jupyter_Notebook = """
    sudo dnf install epel-release -y
    sudo dnf install python3 -y
    sudo dnf install python3-pip -y
    sudo pip3 install --upgrade pip
    sudo pip3 install jupyter"""

    Rstudio_server = """
    sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
    sudo dnf install dnf-plugins-core -y
    export R_VERSION=4.1.3
    curl -O https://cdn.rstudio.com/r/centos-8/pkgs/R-${R_VERSION}-1-1.x86_64.rpm
    sudo yum install R-${R_VERSION}-1-1.x86_64.rpm -y
    /opt/R/${R_VERSION}/bin/R --version
    sudo ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R
    sudo ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript
    wget https://download2.rstudio.org/server/rhel8/x86_64/rstudio-server-rhel-2022.07.1-554-x86_64.rpm
    sudo yum install rstudio-server-rhel-2022.07.1-554-x86_64.rpm -y
    systemctl status rstudio-server.service
    sudo rm -rf R-*.rpm rstudio-*.rpm
    echo "                                                                                                           "
    echo "                                                                                                           "
    echo "                                                                                                           "
    echo "---------------------------- SETUP Your Rstudio User Account ----------------------------"
    echo "                                                                                                           "
    echo "                                                                                                           "
    echo "                                                                                                           "
    sudo adduser oci
    sudo passwd oci
    echo Your user name for Rstudio server = oci
    echo Your passwd for Rstudio server = Password you just set up in this session
    sleep 10
    sudo chcon -R -t bin_t /usr/lib/rstudio-server/bin/
    sudo rstudio-server restart
    """

    cmd_dic = {"install_libs":install_libs, "FASTQC":FASTQC, "Cutadapt":Cutadapt, "Multiqc":Multiqc, "Samtools":Samtools,
               "Vcftools":Vcftools, "Clustalw":Clustalw, "Muscle":Muscle, "Mafft":Mafft, "Prank":Prank, "Trinity":Trinity,
               "Busco":Busco, "STAR":STAR, "SUBREAD":SUBREAD, "HIstat2":HIstat2, "TopHat":TopHat, "BWA":BWA, "Bowtie":Bowtie,
               "kallisto":kallisto, "TEtranscripts":TEtranscripts, "HTSeq":HTSeq, "NCBI":NCBI, "Mothur":Mothur, "FastTree":FastTree,
               "Phylip":Phylip, "Autodock":Autodock, "Autodock_vina":Autodock_vina, "Openbabel":Openbabel, "GROMACS":GROMACS,
               "NWchem":NWchem, "Quantum_ESPRESSO":Quantum_ESPRESSO, "Xtandem":Xtandem, "Jupyter_Notebook":Jupyter_Notebook,
               "Rstudio_server":Rstudio_server}

    return cmd_dic[package]



def ubuntu_installer(package):


    """
    Install packages on Ubuntu

    :param package: [str] Package to install (Key for the dictionary)
    :return: [dictionary] Commands to install software
    """


    install_libs = """
    sudo apt update
    sudo apt install git -y
    sudo apt install build-essential -y
    sudo apt install python3-pip -y
    sudo pip3 install --upgrade pip
    pip3 install pandas
    pip3 install Bio
    sudo apt install openjdk-8-jdk -y
    sudo apt install gfortran -y
    sudo apt install openmpi-bin libopenmpi-dev -y
    pip3 install biopython
    """

    FASTQC = """sudo apt install fastqc -y"""

    Cutadapt = """
    sudo pip3 install cutadapt 
    """

    Multiqc = """
    sudo pip3 install multiqc
    """

    Samtools = """
    sudo apt install samtools -y
    """

    Vcftools = """
    sudo apt -y install vcftools
    """

    Clustalw = """sudo apt install clustalw -y"""

    Muscle = """sudo apt install muscle -y"""

    Mafft = """sudo apt install mafft -y"""

    Prank = """sudo apt install prank -y"""

    Trinity = """sudo apt install trinity -y"""

    Busco = """sudo apt install busco -y"""

    STAR = """
    wget https://github.com/alexdobin/STAR/archive/2.7.10a.tar.gz
    tar -xvf 2.7.10a.tar.gz
    cd STAR-2.7.10a/source
    make STAR
    sudo mv STAR /usr/local/bin/
    cd
    sudo rm -rf /home/$(whoami)/2.7.10a.tar.gz STAR-2.7.10a
    """

    SUBREAD = """sudo apt-get -y install subread"""

    HIstat2 = """sudo apt install hisat2 -y"""

    TopHat = """
    wget https://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.Linux_x86_64.tar.gz
    tar -xvf tophat-2.1.1.Linux_x86_64.tar.gz
    cd tophat-2.1.1.Linux_x86_64/
    rm -rf AUTHORS intervaltree LICENSE README sortedcontainers
    sudo mv * /usr/local/bin
    cd 
    sudo rm -rf tophat-2.1.1.Linux_x86_64  tophat-2.1.1.Linux_x86_64.tar.gz
    """

    BWA = """
    git clone https://github.com/lh3/bwa.git
    cd bwa; make
    sudo mv bwa /usr/local/bin/
    cd 
    sudo rm -rf bwa/
    """

    Bowtie = """
    sudo apt -y install bowtie
    """

    kallisto = """sudo apt install kallisto -y"""

    TEtranscripts = """
    pip3 install TEtranscripts
    """

    HTSeq = """
    pip3 install HTSeq
    """

    NCBI = """
    wget https://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/ncbi-blast-2.13.0+-x64-linux.tar.gz
    tar -xvf ncbi-blast-2.13.0+-x64-linux.tar.gz
    cd ncbi-blast-2.13.0+/bin/
    sudo mv * /usr/local/bin/
    cd 
    sudo rm -rf ncbi*
    """

    Mothur = """
    wget https://github.com/mothur/mothur/releases/download/v1.48.0/Mothur.linux_7.zip
    unzip Mothur.linux_7.zip
    cd mothur/
    rm LICENSE 
    sudo mv * /usr/local/bin
    cd 
    sudo rm -rf mothur  Mothur.linux_7.zip
    """

    FastTree = """
    wget wget http://meta.microbesonline.org/fasttree/FastTree.c
    gcc -DUSE_DOUBLE -O3 -finline-functions -funroll-loops -Wall -o FastTree FastTree.c -lm 
    sudo mv FastTree /usr/local/bin/
    cd 
    sudo rm -rf FastTree*
    """

    Phylip = """
    wget http://evolution.gs.washington.edu/phylip/download/phylip-3.697.tar.gz
    tar -xvf phylip-3.697.tar.gz
    cd phylip-3.697/src
    mv Makefile.unx makefile
    make install
    cd ../exe/
    sudo mv * /usr/local/bin/
    cd 
    sudo rm -rf phylip-3.697  phylip-3.697.tar.gz
    """

    Autodock = """
    sudo apt install autodock -y
    """

    Autodock_vina = """sudo apt install autodock-vina -y"""

    Openbabel = """sudo apt install openbabel -y"""

    GROMACS = """sudo apt install gromacs -y"""

    NWchem = """sudo apt install nwchem -y"""

    Quantum_ESPRESSO = """sudo apt install quantum-espresso -y"""

    Xtandem = """
    wget http://ftp.thegpm.org/projects/tandem/source/2015-12-15/tandem-linux-15-12-15-2.zip
    unzip tandem-linux-15-12-15-2.zip
    cd tandem-linux-15-12-15-2/bin/
    sudo chmod 777 tandem.exe
    sudo mv tandem.exe /usr/local/bin/
    cd 
    sudo rm -rf tandem-linux-15-12-15-2  tandem-linux-15-12-15-2.zip
    """

    Jupyter_Notebook = """
    sudo apt install python3 -y
    sudo apt install python3-pip -y
    sudo pip3 install --upgrade pip
    sudo pip3 install jupyter"""

    Rstudio_server = """
    sudo apt-get install r-base -y
    sudo apt-get install gdebi-core -y
    wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2022.07.1-554-amd64.deb
    sudo gdebi -n rstudio-server-2022.07.1-554-amd64.deb
    sudo rm -rf rstudio-server-2022.07.1-554-amd64.deb
    echo "                                                                                                           "
    echo "                                                                                                           "
    echo "                                                                                                           "
    echo "---------------------------- SETUP Your Rstudio User Account ----------------------------"
    echo "                                                                                                           "
    echo "                                                                                                           "
    echo "                                                                                                           "
    sudo adduser oci
    echo Your user name for Rstudio server = oci
    echo Your passwd for Rstudio server = Password you just set up in this session
    sleep 10
    """

    cmd_dic = {"install_libs":install_libs, "FASTQC":FASTQC, "Cutadapt":Cutadapt, "Multiqc":Multiqc, "Samtools":Samtools,
               "Vcftools":Vcftools, "Clustalw":Clustalw, "Muscle":Muscle, "Mafft":Mafft, "Prank":Prank, "Trinity":Trinity,
               "Busco":Busco, "STAR":STAR, "SUBREAD":SUBREAD, "HIstat2":HIstat2, "TopHat":TopHat, "BWA":BWA, "Bowtie":Bowtie,
               "kallisto":kallisto, "TEtranscripts":TEtranscripts, "HTSeq":HTSeq, "NCBI":NCBI, "Mothur":Mothur, "FastTree":FastTree,
               "Phylip":Phylip, "Autodock":Autodock, "Autodock_vina":Autodock_vina, "Openbabel":Openbabel, "GROMACS":GROMACS,
               "NWchem":NWchem, "Quantum_ESPRESSO":Quantum_ESPRESSO, "Xtandem":Xtandem, "Jupyter_Notebook":Jupyter_Notebook,
               "Rstudio_server":Rstudio_server}

    return cmd_dic[package]

