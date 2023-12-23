# Seed
Seed is a cool python tool for creating a file with ports that let you comunicate your files
between each other.
With python code, obviously.
It's pretty cool, check it out.

`import Seed`

`Seeds.createNewSeed('name', '0000000001', 'EDIT') # It has to be 10 digits long`

`ports = Ports()`

`ports.get_ports(seed_path) # will print all ports and will connect to seed (!! Important)`

`ports.openNewPort('1222') # 4 digits required, ports preopened are 0001 and 9999`

`ports.editAvailablePort('1222', 'print("hello world")') # will change port value`

`ports.subscribeToPort('1222') # will make a while loop on reading and running that port.`

Console:

`Port found: 0001
Port found: 9999
hello world`
