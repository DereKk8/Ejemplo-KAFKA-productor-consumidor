# Ejemplo-KAFKA-productor-consumidor


- Iniciar el broker en el puerto 9092 con la imgen Docker the Kafka 4.0.0
    ```sh
    docker run -p 9092:9092 apache/kafka-native:4.0.0
    ```


    ``` sh
    docker run -p 9092:9092 \
    -e CLUSTER_ID="5L6g3nShT-eMCtK--X86sw" \
    -e KAFKA_PROCESS_ROLES="broker,controller" \
    -e KAFKA_NODE_ID=1 \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS="1@localhost:9093" \
    -e KAFKA_LISTENERS="PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093" \
    -e KAFKA_ADVERTISED_LISTENERS="PLAINTEXT://192.168.5.171:9092" \
    -e KAFKA_CONTROLLER_LISTENER_NAMES="CONTROLLER" \
    -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP="CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT" \
    apache/kafka-native:4.0.0
    ```

    Note: Replace YOUR_MACHINE_IP with your actual machine's IP address. You can find it using:
    ```sh
    ipconfig getifaddr en0
    ```

- Crear el topico para la muestra del clima
    ```sh
    bin/kafka-topics.sh --create --topic weather_data_demo --bootstrap-server localhost:9092
    ```

    bin/kafka-topics.sh --create --topic weather_data_demo --bootstrap-server 192.168.5.171:9092

- Listar un topico
    ```sh
    bin/kafka-topics.sh --describe --topic weather_data_demo --bootstrap-server localhost:9092
    ```

- Publicar 'eventos' desde la consola
    ```sh
    bin/kafka-console-producer.sh --topic weather_data_demo --bootstrap-server localhost:9092
    ```
- Consumir los 'eventos' desde consola
    ```sh
    bin/kafka-console-consumer.sh --topic weather_data_demo --from-beginning --bootstrap-server localhost:9092
    ```