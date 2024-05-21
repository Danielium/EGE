from ipaddress import *
net = ip_network('112.154.133.208/255.255.252.0', 0)
k = 0
for ip in net.hosts():
    if f'{ip:b}'[:16].count('1') <= f'{ip:b}'[16:].count('0') and f'{ip:b}'[16:].count('0') % 2 != 0:
        k += 1
print(k)

# 502  № 12088

