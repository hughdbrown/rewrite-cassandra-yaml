# Description
Short python script to rewrite a `/etc/cassandra/cassandra.yaml` file to allow remote access.

# Installation
Run the following command to get a local command installed:
    `python setup.py install_scripts`

# Usage
Make the cassandra server accessible at 192.168.1.100:
```
rewrite-cassandra-yaml 192.168.1.100
```

# Caveat
Running this command will strip comments from the YAML file.
