import inquirer


def software_category():


    """
    Get software category

    :return: [array] software category
    """


    questions = [
        inquirer.Checkbox(
            name="software_category",
            message="Select software category",
            choices=["Genomics", "Computational chemistry", "Proteomics", "IDEs"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_category"]


def install_IDE():


    """
    Get IDE to install
    :return: [array] ide/s
    """


    questions = [
        inquirer.Checkbox(
            name="ide",
            message="Select the integrated development environment",
            choices=["Rstudio_server", "Jupyter_Notebook"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["ide"]


def install_computational_chemistry():


    """
    Get computational chemistry list

    :return: [array] computational chemistry list
    """


    questions = [
        inquirer.Checkbox(
            name="software_chemistry",
            message="Select computational chemistry software",
            choices=["Autodock", "Autodock_vina", "Openbabel", "GROMACS", "NWchem", "Quantum_ESPRESSO"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_chemistry"]



def install_proteomics():


    """
    Get proteomics list

    :return: [array] proteomics list
    """


    questions = [
        inquirer.Checkbox(
            name="software_proteomics",
            message="Select Proteomics software",
            choices=["Xtandem"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_proteomics"]



def install_genomics_parent():


    """
    Get genomics parent list
    :return: [array] genomics list
    """


    questions = [
        inquirer.Checkbox(
            name="genomics_parent",
            message="Select Genomics software category",
            choices=["Quality control", "File format", "Multiple-alignment", "Genome assembly", "Mapping tools",
                     "Analysis", "Tool-kits", "Metagenomics", "Phylogenetics"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["genomics_parent"]



def install_genomics_QC():


    """
    Get genomics QC list

    :return: [array] genomics QC list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_qc",
            message="Select Genomics QC software",
            choices=["FASTQC", "Cutadapt", "Multiqc"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_qc"]


def install_genomics_format():


    """
    Get genomics file format list

    :return: [array] genomics file format list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_format",
            message="Select Genomics file format tools",
            choices=["Samtools", "Vcftools"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_format"]



def install_genomics_multialignment():


    """
    Get genomics alignment list

    :return: [array] genomics alignment list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_multialignment",
            message="Select Genomics multi-alignment tools",
            choices=["Clustalw", "Muscle", "Mafft", "Prank"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_multialignment"]



def install_genomics_assembly():


    """
    get assembly list

    :return: [array] assembly list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_assembly",
            message="Select Genomics assembly tools",
            choices=["Trinity", "Busco"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_assembly"]



def install_genomics_mapping():


    """
    Get genomics mapping

    :return: [array] genomics mapping list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_mapping",
            message="Select Genomics mapping tools",
            choices=["STAR", "SUBREAD", "HIstat2", "TopHat", "BWA", "Bowtie"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_mapping"]



def install_genomics_analysis():


    """
    Get genomics analysis list

    :return: [array] genomics analysis list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_analysis",
            message="Select Genomics analysis tools",
            choices=["kallisto", "TEtranscripts", "HTSeq"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_analysis"]



def install_genomics_tookkit():


    """
    Get genomics toolkit

    :return: [array] genomics toolkit list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_tookkit",
            message="Select Genomics took-kits (e.g. NCBI tool-kit)",
            choices=["NCBI"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_tookkit"]



def install_genomics_metagenomics():


    """
    Get metagenomics list

    :return: [array] metagenomics list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_metagenomics",
            message="Select metagenomics tools",
            choices=["Mothur"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_metagenomics"]



def install_genomics_pylogenetics():


    """
    Get pylogenetics list

    :return: [array] pylogenetics list
    """


    questions = [
        inquirer.Checkbox(
            name="software_genomics_pylogenetics",
            message="Select pylogenetics tools",
            choices=["FastTree", "Phylip"]
        )
    ]

    selected_software = inquirer.prompt(questions)
    return selected_software["software_genomics_pylogenetics"]


