from lib import *


def configure_requirement():
    p = p_start("Configuring Requirements", 0.1)
    os.system("apt install build-essential openjdk-8-jdk openjdk-8-jre ant maven python-dev -y > /dev/null 2>&1")
    os.system("echo JAVA_HOME=\"/usr/lib/jvm/java-8-openjdk-amd64\" >> /etc/environment")
    p_stop(p)
    add_steps("[+] All the Requirements Configured Successfully")


def install_mininet():
    p = p_start("Installing Mininet", 0.1)
    os.system("apt install mininet -y > /dev/null 2>&1")
    p_stop(p)
    add_steps("[+] Mininet Installed Successfully")


def install_floodlight():
    print(ORANGE + "[*] Installing FloodLight:" + END)
    os.system("git clone git://github.com/floodlight/floodlight.git")
    os.system("cd floodlight")
    os.system("git submodule init")
    os.system("git submodule update")
    os.system("mvn compile")
    os.system("mvn package -DskipTests")
    os.system("sudo mkdir /var/lib/floodlight")
    os.system("sudo chmod 777 /var/lib/floodlight")
    os.system("cd ..")
    steps.append("[+] FloodLight Installed Successfully")
    print_steps()


def cleanup():
    p = p_start("Clean everything Up", 0.1)
    os.system("rm -rf !(floodlight)")
    p_stop(p)
    add_steps("[+] Enjoy Mininet And FloodLight")


def main():
    if __name__ == "__main__":
        if platform.linux_distribution() != ('Ubuntu', '16.04', 'xenial'):
            print(RED + "[-] This3 Code Can only Run on Ubuntu 16.04 Xenial." + END)
        check_sudo()
        configure_requirement()
        print_steps()
        install_mininet()
        install_floodlight()
        cleanup()


main()
