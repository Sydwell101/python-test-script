import os
from netmiko import ConnectHandler
from getpass import getpass

host = {
   'device_type': 'cisco_ios',
   'host': input('Enter host IP Address: '),
   'username': input('Enter username: '),
   'password': getpass('Enter password: '),
   'port': 22,
   'secret': input('Enter enable password: ')
}

print('-----------------------')
print('Ping host...')
print('-----------------------')
print()
response = os.system('ping -c 1 {}'.format(host['host']))

print()
output = ''

if response == 0:
   print('{} is reachable.'.format(host['host']))

   connect = ConnectHandler(**host)
   output = connect.send_command('sh int des | e customername|pw|Lo|Vi')
   
   print('----------------------')
   print('List of interfaces:')
   print('----------------------')
   print(output + '\n')
   
   output = connect.send_command('sh int des | i up')
   print('-------------------')
   print('Active links:')
   print('-------------------')
   print(output + '\n')
   output = connect.send_command('sh int des | i down')
   print('---------------')
   print('Down links')
   print('---------------' + '\n')
   print(output)

   output = connect.send_command('sh ver | i uptime')
   print('Device uptime: {}'.format(output))

else:
   print('Host unreachable.')
