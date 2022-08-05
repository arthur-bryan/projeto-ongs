from views.interface import WebSite
import sys


def main(json):
    json = open(json, 'r')
    website = WebSite()
    website.listener_requisicoes(json.read())
    json.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
        sys.exit(0)
    else:
        sys.exit(1)
