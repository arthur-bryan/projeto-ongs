from app.app import app
from app.config import config
import sys


def main(json):
    json = open(json, 'r')
    json.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
        app.run(config.IP_ADDR_SERVIDOR, config.PORTA_SERVIDOR)
        sys.exit(0)
    else:
        sys.exit(1)
