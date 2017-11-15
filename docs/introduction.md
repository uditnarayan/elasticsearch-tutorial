## Elasticsearch

- Near Realtime search and analytics engine.
- Distributed and scalable by design.
- Fail Safe and resilient.
- Flexible in nature, supports multiple use cases like search, log analysis with variety of data.
- Bigdata support, integrates with Hadoop.
- Provide security with auth plugins.

## Terminology

- **Cluster** is a collection of one or more nodes (servers) that together holds your entire data and provides federated indexing and search capabilities across all nodes.

- **Node** is a single server that is part of your cluster, stores your data, and participates in the cluster’s indexing and search capabilities. Just like a cluster, a node is identified by a name which by default is a random Universally Unique IDentifier (UUID) that is assigned to the node at startup. 

- **Index** is a collection of documents that have somewhat similar characteristics. For example, you can have an index for customer data, another index for a product catalog, and yet another index for order data. 

- **Type** is a logical category/partition of your index whose semantics is completely up to you. In general, a type is defined for documents that have a set of common fields.

- **Document** is a basic unit of information that can be indexed.

- **Shards and Replicas** An index can potentially store a large amount of data that can exceed the hardware limits of a single node. To solve this problem, Elasticsearch provides the ability to subdivide your index into multiple pieces called shards. When you create an index, you can simply define the number of shards that you want. Each shard is in itself a fully-functional and independent "index" that can be hosted on any node in the cluster.

    Sharding is important for two primary reasons:

    * It allows you to horizontally split/scale your content volume.
    * It allows you to distribute and parallelize operations across shards (potentially on multiple nodes) thus increasing performance/throughput.

    In a network/cloud environment where failures can be expected anytime, it is very useful and highly recommended to have a failover mechanism in case a shard/node somehow goes offline or disappears for whatever reason. To this end, Elasticsearch allows you to make one or more copies of your index’s shards into what are called replica shards, or replicas for short.

    Replication is important for two primary reasons:

    * It provides high availability in case a shard/node fails. For this reason, it is important to note that a replica shard is never allocated on the same node as the original/primary shard that it was copied from.
    * It allows you to scale out your search volume/throughput since searches can be executed on all replicas in parallel.

    To summarize, each index can be split into multiple shards. An index can also be replicated zero (meaning no replicas) or more times. Once replicated, each index will have primary shards (the original shards that were replicated from) and replica shards (the copies of the primary shards). The number of shards and replicas can be defined per index at the time the index is created. After the index is created, you may change the number of replicas dynamically anytime but you cannot change the number of shards after-the-fact.

    By default, each index in Elasticsearch is allocated 5 primary shards and 1 replica which means that if you have at least two nodes in your cluster, your index will have 5 primary shards and another 5 replica shards (1 complete replica) for a total of 10 shards per index.

    **Note:** Each Elasticsearch shard is a Lucene index. There is a maximum number of documents you can have in a single Lucene index. As of LUCENE-5843, the limit is 2,147,483,519 (= Integer.MAX_VALUE - 128) documents. You can monitor shard sizes using the _cat/shards API.