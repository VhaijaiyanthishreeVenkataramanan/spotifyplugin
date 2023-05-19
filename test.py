import re 

class bcolors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[99m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colour(colour, text):
    if colour == 'red':
        return "* " + (bcolors.FAIL + text + bcolors.ENDC)
    elif colour == 'green':
        return "* " + (bcolors.OKGREEN + text + bcolors.ENDC)
    elif colour == 'white':
        return (bcolors.WHITE + text + bcolors.ENDC)
    elif colour == 'bold':
        return (bcolors.BOLD + text + bcolors.ENDC)
    elif colour == "blue":
        return "* " + (bcolors.CYAN + text + bcolors.ENDC)
    elif colour == "yellow":
        return "* " + (bcolors.WARNING + text + bcolors.ENDC)

def osprinter(osname, gpattern, *bpattern):
        bad = None
        gpattern = str(gpattern)0
        good = re.findall(gpattern, osname)
        if bpattern:
            bpattern = str(bpattern)
            bad = re.findall(bpattern, osname)
        if len(good) > 0:
            text = (osname + " is being used. ")
            print((colour("green",text)))
            #self.report_list.append(text)
        elif bad is not None:
            text = (osname + " is being used. This is NOT recommended for new installations")
            print((colour("blue", text)))
            #self.report_list.append(text)
        else:
            text = (osname + " is being used. This is not currently supported.")
            print((colour(text, "red")))
            #self.report_list.append(text)

def os():
        print("   Checking the habitability of your environment...\n  ---------------------------------------------------\n")
        #self.report_list.append("   Checking the habitability of your environment...\n  ---------------------------------------------------\n")
        try:
            with open ('/etc/os-release') as os:
                osnamelist = os.readlines()
                for line in osnamelist:
                    if "PRETTY" in line:
                        reosname = re.findall("[\"](.*?)[\"]", line)
                        self.osname = reosname[0]
            if "Red Hat" in self.osname:
                gpattern = "7(\.[3-9])|8(\.[0-9])"
                bpattern = "6(\.[8-9])"
                self.osprinter(self.osname, gpattern, bpattern)
            elif "CentOS" in self.osname:
                with open('/etc/centos-release') as cenrel:
                    relname = cenrel.readline()
                    self.osname = relname.rstrip()
                    gpattereosnamern = "7(\.[3-9])|8(\.[0-9])"
                    bpattern = "6(\.[8-9])"
                    self.osprinter(self.osname, gpattern, bpattern)
            elif "Oracle" in self.osname:
                gpattern = "7(\.[3-9])|8(\.[0-9])"
                bpattern = "6(\.[8-9])"
                self.osprinter(self.osname, gpattern, bpattern)
            elif "Amazon" in self.osname:
                if "Amazon Linux 2" in self.osname:
                    text = (osname + " is being used. Support of Amazon Linux 2 is covered by Tier 2 support.")
                    self.report_list.append(text)
                    print((colour("blue", text)))
                else:
                    gpattern = "2017(\.[3-9])|2018(\.[0-3])"
                    self.osprinter(self.osname, gpattern)
            elif "Debian" in self.osname:
                    gpattern = "9(\.[0-9])|10(\.[0-9])|9|10"
                    self.osprinter(self.osname, gpattern)
            elif "Ubuntu" in self.osname:
                gpattern = "16.04|18.04|20.04"
                self.osprinter(self.osname, gpattern)
            elif "SUSE" in self.osname:
                gpattern = "1[2-9]"
                self.osprinter(self.osname, gpattern)
        except FileNotFoundError as e:
            self.osname = uname().sysname + " " + platform.mac_ver()[0]
            gpattern = "10(\.1[2-5].*)"
            self.osprinter(self.osname, gpattern)