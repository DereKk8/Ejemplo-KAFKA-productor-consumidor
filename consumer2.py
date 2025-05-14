from quixstreams import Application
import json


def main():
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        consumer_group="weather_reader2",
        auto_offset_reset="earliest",
    )

    with app.get_consumer() as consumer:
        consumer.subscribe(["weather_data_demo"])

        while True:
            msg = consumer.poll(1)

            if msg is None:
                print("Waiting...")
            elif msg.error() is not None:
                raise Exception(msg.error())
            else:
                key = msg.key().decode("utf8") if msg.key() else "null"
                try:
                    # Try to parse as JSON first
                    value = json.loads(msg.value())
                except json.JSONDecodeError:
                    # If not JSON, treat as plain text
                    value = msg.value().decode("utf8")
                offset = msg.offset()

                print(f"{offset} {key} {value}")
                consumer.store_offsets(msg)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
