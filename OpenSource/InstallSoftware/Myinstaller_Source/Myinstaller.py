#!/usr/bin/env python3
import logging
import os
import help
import getOS
import Installer
import verifyInstall
import selectionUtill
from termcolor import colored


def collect_selections(selected_software):


    """
    Select packages to install

    :param selected_software: [array] array to store selected software
    :return: [array] selected packages
    """


    software_cat = selectionUtill.software_category()
    for i in software_cat:
        if i == "Computational chemistry":
            selected_software = selected_software + selectionUtill.install_computational_chemistry()
        elif i == "Proteomics":
            selected_software = selected_software + selectionUtill.install_proteomics()
        elif i == "Genomics":
            for gensoft in selectionUtill.install_genomics_parent():
                if "Qulity control" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_QC()
                elif "File format" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_format()
                elif "Multiple-alignment" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_multialignment()
                elif "Genome assembly" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_assembly()
                elif "Mapping tools" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_mapping()
                elif "Analysis" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_analysis()
                elif "Tool-kits" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_tookkit()
                elif "Metagenomics" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_metagenomics()
                elif "Phylogenetics" in gensoft:
                    selected_software = selected_software + selectionUtill.install_genomics_pylogenetics()
                else:
                    pass
        elif i == "IDEs":
            selected_software = selected_software + selectionUtill.install_IDE()
        else:
            print("Default")

    return selected_software


def print_selection(selection):


    """
    Display selected software

    :param selection: [array] Selected software
    :return: None
    """


    print(colored("\nInstalling following software\n", "green"))
    counter = 1
    while counter < len(selection)+1:
        print(counter, " - ", selection[counter-1])
        counter += 1
    return None


if __name__ == '__main__':

    help.help_function()
    myOS = getOS.get_operating_system()
    print("The Operating system is: {0}\n".format(myOS))
    while True:
        selected_software = []
        installation_status = {}
        selection = collect_selections(selected_software)
        print_selection(selection)
        verification = input(colored("Are you happy with the selection; Should I proceed with the installation? (Y/n) : ", "green"))

        if verification.lower() == "y":
            print(colored("Installing your software collection ............. \n", "yellow"))
            if myOS == "OL":
                cmd_libs = Installer.OL_installer(package="install_libs")
                print(cmd_libs)
                os.system(cmd_libs)
                for sel in selection:
                    package_install_cmd = Installer.OL_installer(sel)
                    print(package_install_cmd)
                    os.system(package_install_cmd)
                break

            elif myOS == "CentOS":
                cmd_libs = Installer.OL_installer(package="install_libs")
                print(cmd_libs)
                os.system(cmd_libs)
                for sel in selection:
                    package_install_cmd = Installer.OL_installer(sel)
                    print(package_install_cmd)
                    os.system(package_install_cmd)
                break

            elif myOS == "Ubuntu":
                cmd_libs = Installer.ubuntu_installer(package="install_libs")
                print(cmd_libs)
                os.system(cmd_libs)
                for sel in selection:
                    package_install_cmd = Installer.ubuntu_installer(sel)
                    print(package_install_cmd)
                    os.system(package_install_cmd)
# Verification starts here ...................................................................................
#                 for app in selection:
#                     app_cmd = verifyInstall.get_app_cmd(app=app)
#                     verification = verifyInstall.verifier(app_cmd=app_cmd)
#                     if verification[1] == 0:
#                         installation_status[app] = "Success"
#                     elif verification[1] == 1:
#                         installation_status[app] = "Failed"
#                     else:
#                         logging.error("{0} -- Verification failure".format(app))
#                         pass
# Verification ends here .....................................................................................
                break

            else:
                logging.info("Confused about the OS")
                pass

        elif verification.lower() == "n":
            print(colored("\nRunning selection again ............. \n", "yellow"))
            del selected_software
            logging.info("User re-running software selection")
            pass
        else:
            print("Invalid input. Accespted inputs are (Y/n) \n")
            verification = input(colored("Are you happy with the selection; Should I proceed with the installation? (Y/n) : ", "green"))
