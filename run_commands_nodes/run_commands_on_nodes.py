#!/bin/env python

import sys
import time
from getpass import getpass
from paramiko_func import sshCommand
import yaml

#calls paramiko_func
def sshConnect():
    if __name__=='__main__':
        sshCommand(hosts, 22, a[1], passWord, command_run)

#error if command is not configured correctly, needs; python f5_address user
if len(sys.argv) < 2:
    print ("Usage %s username" % sys.argv[0])
    sys.exit()

a = sys.argv[0:]

#password entry, self explanitory
passWord = getpass("Enter your password (leave blank if you have ssh key): ")
print("\n")

#pick the command type you need
def commandsIpick():
    command_file_handle = open('commands.yaml', 'r') #
    command_string = command_file_handle.read()
    command_file_handle.close()
    command_dict = yaml.load(command_string)
    command_keys = list(command_dict.keys())

    print ("Q Quit")
    for c, commandName in enumerate(command_keys):
        print(c+1, commandName)

    print("\n")
    commandPick = input("Choose the command type you need: ")
    print("\n")
    if commandPick.upper() == "Q":
            sys.exit(0)
    commandPick = int(commandPick) - 1
    command_run = command_dict[command_keys[commandPick]]
    command_keys = list(command_run.keys())
    #print(command_run)
    #print(command_keys)

    for c, commandName in enumerate(command_keys):
        print(c+1, commandName)

    print("\n")
    commandPick = input("Choose the command you need: ")
    print("\n")
    commandPick = int(commandPick) - 1
    command_run = command_run[command_keys[commandPick]]
    finalCommand = command_run
    print ("\n" + "Here is the command you are running: " +  finalCommand + "\n")
    #return command_run
    return finalCommand



#nodes yaml file to pull the node group and the individual node
def nodeStack():
    nodes_file_handle = open('nodes.yaml', 'r') #
    nodes_string = nodes_file_handle.read()
    nodes_file_handle.close()
    nodes_dict = yaml.load(nodes_string)

    nodesPick = -1
    while nodesPick < 0:
        nodes_keys = list(nodes_dict.keys())    
        command_run = commandsIpick()

        for i, nodesName in enumerate(nodes_keys):
            print(i+1, nodesName)

        print("\n")
        nodesPick = input("Choose the node stack you need: ")
        print("\n")
        nodesPick = int(nodesPick) - 1
        nodes_run = nodes_dict[nodes_keys[nodesPick]]
        #nodes_run = nodes_dict[nodesPick]
        nodes_keys = list(nodes_run.keys())

        print ("0 Select all")
        print ("Q Quit")
        print ("-1 Back one level\n")

        for i, nodesName in enumerate(nodes_keys):
            print(i+1, nodesName)

        print("\n")
        nodesPick = input("Choose the node you need: ")
        print("\n")
        if nodesPick.upper() == "Q":
            sys.exit(0)
        nodesPick = int(nodesPick)


    #When selecting all this if statement is used
    if (nodesPick == 0):
        for i in nodes_keys:
            #puts the domain at the end
            hosts = i+'.domain.com'
            print("Restarting services on " + hosts + "\n")
            if __name__=='__main__':
                sshCommand(hosts, 22, a[1], passWord, command_run)
    #when an individual node is selected, this one is taken in
    else:
        nodesPick = int(nodesPick) - 1
        nodes_run = nodes_run[nodes_keys[nodesPick]]
        print(nodes_run)
        hosts = nodes_run
        print("Restarting services on " + hosts + "\n")
        print(command_run)
        if __name__=='__main__':
            sshCommand(hosts, 22, a[1], passWord, command_run)


#keeps in loop till quit command is selected
while True:
    nodeStack()



