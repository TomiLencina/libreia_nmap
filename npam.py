import nmap

def scan_network():
    ip_range = 'ip'
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')

    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print('Host: %s' % host)

scan_network()