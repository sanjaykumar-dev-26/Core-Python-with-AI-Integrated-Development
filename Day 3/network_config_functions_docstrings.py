'''This is network configuration'''

import pprint


def f1():
    '''Return an empty dictionary'''
    network_params = {}
    return network_params


def f2(network_params):
    '''Receive a dictionary as an argument and
    load network configuration from a file'''
    with open('network.cfg', 'r') as fobj:
        for var in fobj.readlines():
            var = var.strip()
            K, V = var.split("=")
            network_params[K.strip()] = V.strip()

    return network_params


def f3(network_params):
    '''Display network parameters'''
    pprint.pprint(network_params)


def f4(network_params):
    '''Update dictionary with network settings'''
    network_params['Interface'] = 'eth1'
    network_params['bootproto'] = 'static'
    network_params['onboot'] = 'yes'
    network_params['IPADD'] = '192.168.1.10'
    network_params['PREFIX'] = 24
    network_params['DNS1'] = '122.33.344.555'

    return network_params


def f5(network_params):
    '''Write updated configuration to a new file'''
    with open('new_network.cfg', 'w') as wobj:
        for var in network_params:
            wobj.write(f'{var} = {network_params.get(var)}\n')