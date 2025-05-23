import requests
import time
import json
import logging
from quixstreams import Application


def get_weather():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params = {
            "latitude": 4.6097,
            "longitude": -74.0817,
            "start_date": "2025-05-15",
            "end_date": "2025-05-15",
            "hourly": "temperature_2m"
        }
    )

    return response.json()


def main():
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
    )

    with app.get_producer() as producer:
        while True:
            weather = get_weather()
            logging.debug("Got weather: %s", weather)
            producer.produce(
                topic="weather_data_demo",
                key="Bogota",
                value=json.dumps(weather),
            )
            logging.info("Produced. Sleeping...")
            time.sleep(300)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
