import os

import httpx
from dotenv import load_dotenv
from godaddypy import Client, Account


def get_ip() -> str:
    response = httpx.get("https://api.ipify.org", params={"format": "json"})
    response.raise_for_status()
    return response.json()["ip"]


def set_ip(domain: str, ip: str) -> None:
    my_acct = Account(
        api_key=os.environ["GODADDY_PUBLIC"],
        api_secret=os.environ["GODADDY_SECRET"],
    )
    client = Client(my_acct)
    client.update_ip(ip, domains=[domain])


if __name__ == "__main__":
    load_dotenv()
    set_ip(os.environ["DOMAIN"], get_ip())
