# Elasticsearch Tutorial

This tutorial is meant for introduction to elastisearch for beginers. The content is taken from ElasticSearch official documentation. I have worked on examples and scenerios for the tutorial. The elasticsearch version supported by this tutorial is 5.6.3.

This tutorial assume that your have installed elasticsearch and kibana (only for dev tools for querying elasticsearch). It is fairly simple, just download the elasticsearch zip file and run the elasticsearch command. Do same for kibana. If you do not want that or if you are familiar with docker, you can follow an alternate route.

1. [Install docker](https://docs.docker.com/engine/installation/)
2. [Install docker compose](https://docs.docker.com/compose/install/)
3. Clone this repository in you computer and browse to the repository folder.
4. Modify the esdata settings under volume key if you are using windows and put any folder of your choice.
4. Run commmand `docker-compose up` and your single node elasticsearh container along with kibana will be up in minutes.

It will take a while to run docker for the first time becuase docker will download the elasticsearch and kibana images. After that, next time you do docker-compose, it will use the cached images for spawning containers.

# Table of contents

[Introduction](./docs/introduction.md)

[Getting Started](./docs/getting_started.md)