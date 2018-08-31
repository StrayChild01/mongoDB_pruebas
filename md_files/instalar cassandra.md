# How to install Cassandra 3.0.16 from source

### Prerequisites

For this guide to work you **must have** Java JDK installed.

### Get it from the source
    wget "http://archive.apache.org/dist/cassandra/3.0.16/apache-cassandra-3.0.16-bin.tar.gz"
    
If you are unable to get it directly from the server, transfer it from your machine, for example:

    scp apache-cassandra-3.0.16-bin.tar.gz myUser@192.168.1.111:/home/myUser/
    
### After you downloaded it
Decompress it to the desired folder:

    tar -xvzf apache-cassandra-3.0.16-bin.tar.gz -C /usr/local/

Test the installation:

    cd /usr/local/apache-cassandra-3.0.16/bin
    ./cassandra
    #This will throw a lot of java text

### Change cluster name
If no errors were shown on the last stage, change the cluster name:

    ./cqlsh
    #Connected to Test Cluster at 127.0.0.1:9042.
    #[cqlsh 5.0.1 | Cassandra 3.0.16 | CQL spec 3.4.0 | Native protocol v4]
    cqlsh> update system.local set cluster_name = 'my_cluster' where key = 'local';
    cqlsh> exit;

Flush the system tables to persist the update. Note: The following instruction will wipe all the system data to default, **do *NOT* use when in prod**

    ./nodetool flush system
    
Change the configuration file:

    cd /usr/local/apache-cassandra-3.0.16/conf
    vi cassandra.yaml

Change the cluster name (originally Test Cluster):

    cluster_name: 'my_cluster'

Restart the server:

    ps -ef | grep root | grep -vE grep | grep -i cass | awk '{print $2}' | xargs kill -9
    cd /usr/local/apache-cassandra-3.0.16/bin
    ./cassandra

### After changing cluster name
If the server started correctly, check the cluster name:

    ./cqlsh
    #Connected to my_cluster at 127.0.0.1:9042.
    #[cqlsh 5.0.1 | Cassandra 3.0.16 | CQL spec 3.4.0 | Native protocol v4]
    #Use HELP for help.

Notice how the cluster name is now *my_cluster*

Test the cluster

    cqlsh> CREATE KEYSPACE test WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};
    cqlsh> use test;
    cqlsh> CREATE TABLE test (id uuid PRIMARY KEY, name text);
    cqlsh> insert into test.test(id, name) values (uuid(), 'The Dark Side of the Moon');
    cqlsh> insert into test.test(id, name) values (uuid(), 'This is a test');
    cqlsh> select * from test.test;
    cqlsh> /* delete a random record, the id might not match */
    cqlsh> delete from test.test where id = 80c26089-e5c4-4f3e-b56e-333bcb1416b7
    cqlsh> /* check it was really deleted */
    cqlsh> select * from test.test;

You can also select what you have created to doublecheck:

    cqlsh> select * from system_schema.keyspaces;
    cqlsh> /* to select all keyspaces */
    
Output:

    keyspace_name      | durable_writes | replication
    --------------------+----------------+-------------------------------------------------------------------------------------
           system_auth |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'}
         system_schema |           True |                             {'class': 'org.apache.cassandra.locator.LocalStrategy'}
             mi_prueba |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'}
    system_distributed |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
                system |           True |                             {'class': 'org.apache.cassandra.locator.LocalStrategy'}
         system_traces |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '2'}

To show all tables in a keyspace:

    cqlsh> use my_keyspace;
    cqlsh> describe tables;   

### Add Cassandra binaries to PATH

Edit the profile:

    vi $HOME/.bash_profile
    
Add Cassandra to path:

    CASSANDRA_HOME=/usr/local/apache-cassandra-3.0.16
    CASSANDRA_BIN=$CASSANDRA_HOME/bin
    
    PATH=$PATH:$HOME/.local/bin:$HOME/bin:$CASSANDRA_BIN

### To enable remote access
By default, Cassandra does not enable remote access. To achieve this, we need to set it on the configuration file **cassandra.yaml**
    
    start_rpc: true
    
    #rpc_address: [node-ip]
    #NOT BOTH
    rpc_interface: eth0   
    
    #listen_address:
    #NOT BOTH
    listen_interface: eth0
    
    seed_provider:    
    - class_name: org.apache...
      parameters:          
          - seeds: "[node-ip]"

Another way

    start_rpc: true
    rpc_address: 0.0.0.0
    broadcast_rpc_address: [node-ip]
    listen_address: [node-ip]
    seed_provider:
      - class_name: ...
        - seeds: "[node-ip]"


    
### Notes
If you try to connect to the server with *./cqlsh* and you get an error message
    
    ./cqlsh
    Connection error: ('Unable to connect to any servers', {'127.0.0.1': error(111, "Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused")})

Try the following *./cqlsh* __ip-address__

    ./cqlsh 192.168.1.111
    # Connected to my_cluster at 192.168.1.111:9042.
    # [cqlsh 5.0.1 | Cassandra 3.0.16 | CQL spec 3.4.0 | Native protocol v4]
    # Use HELP for help.

Done.
