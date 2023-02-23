from netmiko import ConnectHandler
#define the device information
device={
    'device_type':'linux',
    'ip':'192.168.149.129',
    'username':'himasree',
    'password':'1234',
}
#cretae Netmiko SSH connection to the device
connection=ConnectHandler(**device)
cpu_output=connection.send_command('cat /proc/cpuinfo')
mem_output=connection.send_command('free -h')
connection.disconnect()
print('CPU Information:')
print(cpu_output)
print('\nMemory Information:')
print(mem_output)
