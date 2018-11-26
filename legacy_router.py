#!/usr/bin/python
#Eli Manzo
#Alejandro Ruvalcaba
from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
    defaultIP = '10.0.1.1/24' # IP addr for r1-eth0
    #sets up the mininet network with the base ip that all hosts need to connect to as well as not letting it build off a topology
    net = Mininet( topo=None, build=False, ipBase=defaultIP)
#adds the router as the host r1
    r1 = net.addHost('r1', cls=Node, ip=defaultIP)
    #   Enables IP forwarding by setting it equal to 1
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')
				  
    info( '*** Add hosts\n')
#adding hosts to the network as well as an ip with a default route 
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.2/24', defaultRoute='via 10.0.1.1')
    h2 = net.addHost('h2', cls=Host, ip='10.0.2.2/24', defaultRoute='via 10.0.2.1')

#adds the links between the router r1 and the multiple hosts h1 and h2
    info( '*** Add links\n')
    net.addLink(h1, r1, intfName2='r1-eth0', params2={ 'ip' : defaultIP } )
    net.addLink(h2, r1, intfName2='r1-eth1', params2={ 'ip' : '10.0.2.1/24' } )
#begins building the network
    info( '*** Starting network\n')
    net.build()

    info( '*** Routing Table on Router:\n' )
    print net[ 'r1' ].cmd( 'route' )
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

