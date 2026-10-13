# COMAND LINE PROMPS:
RABBITMQ IMAGE PULLING AND RUNNING: docker run -d -e RABBITMQ_NODENAME=my-rabbit --name some-rabbit -p 8080:15672 rabbitmq:3-management
PRODUCER IMAGE BUILDING (ON /producer): docker build -t producer .
PRODUCER IMAGE BUILDING (ON /consumer): docker build -t consumer .
RABBITMQ NETWORK CONNECTION: docker network connect middleware-network-network some-rabbit
PRODUCER CONTAINER DEPLOYMENT: docker run producer --network middleware-network
CONSUMER CONTAINER DEPLOYMENT: docker run conumer --network middleware-network
