from cassandra.cluster import Cluster

machine_name = 'localhost'
keyspace = "Stock"
port = 9042

cluster = Cluster([machine_name], port=port)
session = cluster.connect(keyspace)

# hostname --ip-address | sudo sed -i 's/^listen_address:.*/listen_address: \1/' /etc/cassandra/cassandra.yaml


1. no good
listen_address: 192.168.2.121
broadcast_rpc_address: 192.168.2.121
rpc_address: 0.0.0.0


import sys
import yaml

def rewrite_cassandra_yaml(local_address):
    fname = "/etc/cassandra/cassandra.yaml"
    with open(fname) as f:
        cassandra = yaml.load(f)
    
    seed_provider = cassandra["seed_provider"]
    for sp in seed_provider:
        if sp['class_name'] == 'org.apache.cassandra.locator.SimpleSeedProvider':
            for parameter in sp['parameters']
                if 'seeds' in parameter:
                    parameter['seeds'] = local_address
    
    cassandra.update({
        "listen_address": local_address,
        "broadcast_rpc_address": local_address,
        "rpc_address": "0.0.0.0",
        "seed_provider": seed_provider,
    })
    
    with open(fname, "w") as f:
        cassandra = yaml.dump(cassandra, stream=f)


def main():
    # local_address = "192.168.2.121"
    try:
        local_address = sys.argv[1]
        rewrite_cassandra_yaml(local_address)
        sys.exit(0)
    except:
        sys.exit(1)


if __name__ == '__main__':
    return main()
