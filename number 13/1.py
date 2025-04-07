# from ipaddress import *
# net = ip_network('136.36.240.16/255.255.255.248',0)
# counter = 0
# for ip in net:
#     if f'{ip:b}'.count('101') == 0:
#         counter += 1
# print(counter)
#4   № 12922


# from ipaddress import *
# net = ip_network('192.168.32.48/255.255.255.240', 0)
# counter = 0
# for ip in net:
#     if f'{ip:b}'.count('1') % 2 != 0:
#         counter += 1
# print(counter)
# 8 № 12245


# from ipaddress import *
# net = ip_network('129.128.0.0/255.128.0.0', 0)
# print(min(f'{ip:b}'.count('0') for ip in net))
# 6 № 11782


# from ipaddress import *
# count = 0
# net = ip_network('192.168.32.160/255.255.255.240', 0)
# for ip in net:
#     if f'{ip:b}'.count('1') % 2 == 0:
#         count += 1
# print(count)


# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'215.181.200.27/{m}', 0)
#     if str(net.network_address) == '215.181.192.0':
#         print(net.netmask)


# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'148.195.140.28/{m}', 0)
#     if str(net.network_address) == '148.195.140.0':
#         print(m)


# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'241.185.253.57/{m}', 0)
#     if str(net.network_address) == '241.185.252.0':
#         print(32 - m)


# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'208.207.230.65/{m}', 0)
#     if str(net.network_address) == '208.207.224.0':
#         print('Йоу')



# from ipaddress import *
# net = ip_network('156.132.15.138/255.255.252.0', 0)
# for n, ip in enumerate(net.hosts()):
#     print(n + 1, ip)



# from ipaddress import *
# for m in range(33):
#     net1 = ip_network(f'157.127.182.76/{m}', 0)
#     net2 = ip_network(f'157.127.190.80/{m}', 0)
#     if net1.network_address != net2.network_address:
#         print(m)


# from ipaddress import *
# count = 0
# net = ip_network('192.168.240.0/255.255.255.0', 0)
# for ip in net:
#     if f'{ip:b}'.count('1') == f'{ip:b}'.count('0'):
#         count += 1
# print(count)



# from ipaddress import *
# count = 0
# net = ip_network('112.154.133.208/255.255.252.0', 0)
# for ip in net:
#     if f'{ip:b}'[:16].count('1') <= f'{ip:b}'[16:].count('0') and f'{ip:b}'[16:].count('0') % 2 != 0:
#         count += 1
# print(count)



# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'145.192.94.230/{m}', 0)
#     if str(net.network_address) == '145.192.80.0':
#         print(net.netmask)


# from ipaddress import *
# count = 0
# net = ip_network('192.168.240.0/255.255.255.0', 0)
# for ip in net:
#     if f'{ip:b}'.count('1') == f'{ip:b}'.count('0'):
#         count += 1
# print(count)



# from ipaddress import *
# count = 0
# net = ip_network('115.192.0.0/255.192.0.0', 0)
# for ip in net:
#     if f'{ip:b}'.count('1') % 3 != 0:
#         count += 1
# print(count)



#17710

# from ipaddress import *
# count = 0
# net = ip_network('214.187.224.0/255.255.224.0', 0)
# for ip in net:
#     if f'{ip:b}'.count("1") % 6 != 0 and f'{ip:b}'[-4:] == '1000':
#         count += 1
# print(count)

#16260
# from ipaddress import *
# for m in range(33):
#     net1 = ip_network(f'123.20.103.136/{m}', 0)
#     net2 = ip_network(f'123.20.103.151/{m}', 0)
#     if str(net1.network_address) != str(net2.network_address):
#         print(net1.netmask)
#какая-то фигня, джобс решает без библиотеки вообще

#13885 шастин хрень придумал
# from ipaddress import *
# for A in (128, 192, 224, 240, 248, 252, 254, 255):
#     net = ip_network(f'238.51.1.202/255.255.{A}.0', 0)
#     if all(f'{ip:b}'[:16].count('1') >= f'{ip:b}'[16:].count('1') for ip in net):
#         print(A)
#         break

#10569
# from ipaddress import *
# net = ip_network('10.8.248.131/255.255.224.0', 0)
# print(net.network_address)

#10575
# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'118.193.30.139/{m}', 0)
#     print(net.network_address, net.netmask)

#10570
# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'154.201.208.17/{m}', 0)
#     print(net.network_address, net.netmask)

#10571
# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'122.21.49.91/{m}', 0)
#     print(net)

#10572
# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'173.103.25.118/{m}', 0)
#     print(net)

#10574
# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'158.116.11.146/{m}', 0)
#     print(net)

#10573
# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'191.173.145.240/{m}', 0)
#     print(net, net.num_addresses)

#10576
# from ipaddress import *
# net = ip_network('0.0.0.0/255.255.240.0', 0)
# print(net.num_addresses)

#10577
# from ipaddress import *
# for m in range(33):
#     net1 = ip_network(f'165.112.200.70/{m}', 0)
#     net2 = ip_network(f'165.112.175.80/{m}', 0)
#     if net1 == net2:
#         print(net1)

#10578
# from ipaddress import *
# for m in range(33):
#     net1 = ip_network(f'10.96.180.231/{m}', 0)
#     net2 = ip_network(f'10.96.140.118/{m}', 0)
#     if net1 != net2:
#         print(net1)

#10579
# from ipaddress import *
# count = 0
# net = ip_network('192.168.240.0/255.255.255.0', 0)
# for ip in net:
#     if f'{ip:b}'.count('0') == f'{ip:b}'.count('1'):
#         count += 1
# print(count)

#10580
# from ipaddress import *
# count = 0
# net = ip_network('10.48.96.0/255.255.240.0', 0)
# for ip in net:
#     ip_binary = bin(int(ip))[2:].zfill(32)
#     if ip_binary.count('1') > ip_binary.count('0'):
#         count += 1
# print(count)

#	№ 1755
# from ipaddress import *
# count=0
# net = ip_network('112.160.0.0/255.240.0.0', 0)
# for ip in net:
#     ip_binary = bin(int(ip))[2:].zfill(32)
#     if ip_binary.count('1')%5==0:
#         count+=1
# print(count)

# from ipaddress import *
# count=0
# net = ip_network('172.16.128.0/255.255.192.0', 0)
# for ip in net:
#     ip_binary = bin(int(ip))[2:].zfill(32)
#     if ip_binary.count('1')%2!=0:
#         count+=1
# print(count)

# from ipaddress import *
# count=0
# net = ip_network('112.160.0.0/255.240.0.0', 0)
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin.count('1')%3!=0:
#         count+=1
# print(count)

# from ipaddress import *
# count=0
# net = ip_network('115.192.0.0/255.192.0.0', 0)
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin.count('1')%3!=0:
#         count+=1
# print(count)

# from ipaddress import *
# count = 0
# net = ip_network('123.222.111.192/255.255.255.248', 0)
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)  это новый родин метод, чтобы обхоиться без f"{ip:b}", который не везде работает
#     if ip_bin[25:].count('0')%3!=0: count += 1
# print(count)

# from ipaddress import *
# net = ip_network('119.68.84.200/255.255.240.0', 0)
# print(str(bin(int(net.network_address))[2:].zfill(32)).count('1'), bin(int(net.network_address))[2:].zfill(32))



# from ipaddress import *
# for m in range(33):
#     net1 = ip_network(f'200.154.190.12/{m}', 0)
#     net2 = ip_network(f'200.154.184.0/{m}', 0)
#     if net1==net2:
#         print(m)



















































