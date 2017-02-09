"""
Implementation for rewriting cassandra.yaml to allow
remote access to server
"""
from __future__ import print_function

import sys
import yaml

SEED = 'org.apache.cassandra.locator.SimpleSeedProvider'


def rewrite_cassandra_yaml(local_address):
    """
    Operative code
    - open file, read into memory
    - manipulate memory representation
    - write back to disk
    """
    fname = "/etc/cassandra/cassandra.yaml"
    with open(fname) as handle:
        cassandra = yaml.load(handle)

    new_cassandra = {
        "listen_address": local_address,
        "broadcast_rpc_address": local_address,
        "rpc_address": "0.0.0.0",
    }

    # A list of seed_providers
    seed_providers = cassandra.get("seed_provider")
    if seed_providers:
        new_cassandra["seed_provider"] = seed_providers
        for seed_provider in seed_providers:
            # A seed_provider is a dict
            if seed_provider['class_name'] == SEED:
                # parameters is a list of dicts
                for parameter in seed_provider.get('parameters', []):
                    if 'seeds' in parameter:
                        parameter['seeds'] = local_address

    cassandra.update(new_cassandra)

    with open(fname, "w") as handle:
        cassandra = yaml.dump(cassandra, stream=handle)


def main():
    """ Entry point for console script """
    try:
        local_address = sys.argv[1]
    except IndexError:
        print("Require argument for local address of cassandra server",
              file=sys.stderr)
        sys.exit(1)
    else:
        try:
            rewrite_cassandra_yaml(local_address)
            sys.exit(0)
        except Exception as exc:  # pylint: disable=broad-except
            print(exc, file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
