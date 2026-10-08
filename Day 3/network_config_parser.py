import pprint

network_params = {}  # Empty dictionary

# Read configuration from file
with open('network.cfg', 'r') as fobj:
    for var in fobj.readlines():
        var = var.strip()  # Remove newline and surrounding whitespace
        K, V = var.split("=")
        network_params[K.strip()] = V.strip()

# Display original configuration
pprint.pprint(network_params)

# Update dictionary with new network settings
network_params['Interface'] = 'eth1'
network_params['bootproto'] = 'static'
network_params['onboot'] = 'yes'
network_params['IPADD'] = '192.168.1.10'
network_params['PREFIX'] = 24
network_params['DNS1'] = '122.33.344.555'

print('\nUpdated Dict details:-')
pprint.pprint(network_params)

# Write updated configuration to a new file
with open('new_network.cfg', 'w') as wobj:
    for var in network_params:
        wobj.write(f'{var} = {network_params.get(var)}\n')

print('\nUpdated configuration saved to new_network.cfg')