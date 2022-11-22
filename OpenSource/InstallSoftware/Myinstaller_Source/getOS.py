from termcolor import colored


def get_operating_system():

    """
    Get the operating system generic name.

    :return: Operating system name
    """


    with open("/etc/os-release", "r") as os_info:
        get_os = os_info.readlines()[0]
        if "Ubuntu" in get_os:
            my_os = "Ubuntu"
        elif "Oracle Linux" in get_os:
            my_os = "OL"
        elif "CentOS" in get_os:
            my_os = "CentOS"
        else:
            print(colored("Operating system detection failed\n", "red"))

            while 1:
                my_os_no = int(input("*** Select your operating system ***\n"
                              "[1] Ubuntu\n"
                              "[2] Oracle Linux\n"
                              "[3] CentOs\n"
                              "Enter the number here: "))
                if my_os_no == 1:
                    my_os = "Ubuntu"
                    break
                elif my_os_no == 2:
                    my_os = "OL"
                    break
                elif my_os_no == 3:
                    my_os = "CentOS"
                    break
                else:
                    print(colored("Invalied input. Try again\n", "red"))
    return my_os
