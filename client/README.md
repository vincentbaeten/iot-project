# Client

The client is a basic python script that uses the [Eclipse Paho](https://github.com/eclipse/paho.mqtt.python) library to send date using MQTT. [Psutil](https://github.com/giampaolo/psutil) is used to collect some system statistics.

The script expects an `.env` file with the following environment variables:

```bash
BASE_TOPIC=pynq

ASSET_ID=<asset-id-from-openremote>

MQTT_USERNAME=<mqtt-username>
MQTT_PASSWORD=<super-secure-password>

BROKER_HOST=<broker-endpoint>
BROKER_PORT=<broker-port>
```
