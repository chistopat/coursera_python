from solution import Client
from config import Config


def main():
    client = Client(Config.address, Config.port, Config.timeout)
    # client.get()
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    print(client.get('*'))


if __name__ == '__main__':
    main()


