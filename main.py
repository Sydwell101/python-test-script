from netmiko import ConnectHandler
from ping3 import ping, verbose_ping


def check_host_availability(host: str):
    delay = ping(host)

    if not delay:
        print('Destination unreachable.')
    else:
        return True


def connect_to_device(host, username, password, secret):
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
        'port': 8022,
        'secret': secret

    }

    net_connect = ConnectHandler(**device)

    return net_connect


def main():
    host = input("Enter host: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    secret = input("Enter secret: ")

    if check_host_availability(host):
        print(verbose_ping(host))
        print('----------------------')
        print(f'Connecting to {host}...')
        connect = connect_to_device(host, username, password, secret)

        connect.send_command('show version | inc uptime')
    else:
        print('Connection failed.')


if __name__ == '__main__':

    try:
        main()
    except OSError:
        print('Destination unreachable.')