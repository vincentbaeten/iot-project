# IoT project

The goal for this project is to deploy openremote and explore the various capabilities. It is divided into two parts. First there is the backend running openremote stack with an external EMQX broker. Then there is an IoT client or in this case a [Pynq-Z2](http://www.pynq.io/board.html) board running linux. The client runs a Python script to send some info to the MQTT broker.

## Usage

### Openremote

To deploy the openremote stack, first clone this repo. Follow below steps.

1. Clone the repo:

    ```bash
    git clone https://github.com/vincentbaeten/iot-project.git
    ```

2. Create a `.env` file
3. The `.env` needs to have the following environment variables:

    ```bash
    EMQX_COOKIE=super-secure-string
    OR_HOSTNAME=some-domain
    ```

4. Run the stack using docker compose using:

    ```bash
    docker compose up
    ```

5. Goto the domainname specified in `OR_HOSTNAME` or if left blank goto

    ```bash
    https://localhost
    ```

### Client

The client is built as a docker container and can be deployed as such.

1. Copy the `docker-compose.yml` in the client directory
2. Create an `.env` file with the following environment variables

    ```bash
    BASE_TOPIC=pynq
    ASSET_ID=<asset-id-from-openremote>
    MQTT_USERNAME=<mqtt-username>
    MQTT_PASSWORD=<super-secure-password>
    BROKER_HOST=<broker-endpoint>
    BROKER_PORT=<broker-port>
    ```

3. Run

    ```bash
    docker compose up -d
    ```

#### Alternative method

The alternative method runs the python script directly with no auto update.

1. Copy the `client` directory
2. Run

    ```bash
    python -m venv .venv
    ```

    To create a virtual environment and source it using

    ```bash
    source .venv/bin/activate
    ```

3. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Create an `.env` file with the following environment variables

    ```bash
    BASE_TOPIC=pynq
    ASSET_ID=<asset-id-from-openremote>
    MQTT_USERNAME=<mqtt-username>
    MQTT_PASSWORD=<super-secure-password>
    BROKER_HOST=<broker-endpoint>
    BROKER_PORT=<broker-port>
    ```

5. Run the script

    ```bash
    python main.py
    ```
