class Ports:
    def __init__(self):
        self.paths = ''
        
    def get_ports(self, path=str):
        """
        This will print all ports and will connect to the seed.
        THIS IS IMPORTANT
        
        Ports.get_ports(
            path = str | None
        ) -> None
        """
        self.paths = path
        with open(path, 'r') as seed:
            for line in seed.readlines():
                if line[0] == '/':
                    print("Port Found: {}".format(line[1:5]))
                elif line[0] != '/':
                    pass
    def subscribeToPort(self, port_number=str):
        """
        Will make a while loop which can't be escaped unless you close the program.
        It does have to be number tho.
        
        Ports.subscribeToPort(
            port_number = str | None
        ) -> None
        """
        num = port_number
        try:
            int(port_number)
        except:
            print("Invalid port number.")
        last_exec=''
        line_num=-1
        while True:
            with open(self.paths) as seed:
                    lineFound=0
                    found = False
                    for line in seed.readlines():
                        line_num=line_num+1
                        if line[0] == '/':
                            if line[1:5] == num:
                                lineFound=5
                                found = True
                                while line[17:1000] != last_exec:
                                    try:
                                        exec(line[17:1000])
                                    except:
                                        pass
                                    last_exec=line[17:1000]
                                    break
                                        
                                while line[17:1000] == last_exec:
                                    break
    def editAvailablePort(self, port_num, value):
        """
        It will edit an open port for it to run on others.
        If haves permissons.
        
        Ports.editAvailablePort(
            port_num = str | None,
            value = str | None
        ) -> None
        """
        num = port_num
        with open(self.paths, 'r') as seed:
            lines = seed.readlines()
        if lines[2][19:23]!='EDIT':
            print('Access Denied.')
        else:
            lin_num=-1
            for line in lines:
                lin_num=lin_num+1
                if line[0] == '/':
                    if line[1:5] == num:
                        lines[lin_num]="/"+num+": "+"PORT_DATA="+value+"\n"
            with open(self.paths, 'w') as seed:
                for lin in lines:
                    seed.write(lin)
                
    def openNewPort(self, port_num):
        """
        Opens a new port.
        Will not open a new port if already exists.
        
        Ports.openNewPort(
            port_num = str | None
        ) -> None
        """
        with open(self.paths, 'r') as file:
            lins = file.readlines()
        if lins[2][19:23]!='EDIT':
            print("Access Denied.")
        else:
            try:
                int(port_num)
            except:
                print("Function aborted: Invalid port number.")
                input("Press enter to continue... ")
                exit()
            with open(self.paths, 'r') as seed:
                for lines in seed:
                    if lines[0] == '/':
                        if lines[1:5] == port_num:
                            print("Function aborted: Port already open.")
                            input("Press enter to continue... ")
                            exit()
                    with open(self.paths, 'a') as seed:
                        seed.write('\n' + '/' + port_num + ': ' + "PORT_DATA=")
                        break
class Seeds:
    def createNewSeed(name, ID, perms):
        """
        Creates a new .seed file.
        Seed ID is required to be 10 numbers long.
        Perms: EDIT, VIEW
        
        VIEW: Can only subscribe to ports, not create nor edit them.
        EDIT: Can edit ports and open them.
        Right now seed ID's don't really matter but still put them.
        
        Seeds.createNewSeed(
            name = str | None,
            ID = str | None,
            perms = str | None
        ) -> None
        """
        import os
        import sys
        ids = list(ID)
        if ids.__len__==10:
            try:
                int(ids)
            except:
                print("Invalid Seed ID.")
                input("Press any key to continue...  ")
                exit()
            pass
        else:
            print("Invalid Seed ID.")
            input("Press any key to continue...  ")
            exit()
        full = name+'.seed'
        os.chdir(sys.path[0])
        files = os.listdir(sys.path[0])
        for file in files:
            if file == full:
                print("Seed already exists.")
                input('Press any key to continue...  ')
                exit()
        with open(full, 'a') as file:
            file.write("""SEED_NAME="{}"
SEED_ID={}
PERMS_FOR_EVERYONE={}
SEED_PORTS:
/0001: PORT_DATA=
/9999: PORT_DATA=""".format(name, ID, perms))