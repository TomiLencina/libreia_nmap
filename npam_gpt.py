import nmap

def scan_network():
    # Reemplaza 'C:\\ruta\\a\\nmap.exe' con la ruta de acceso correcta a tu archivo nmap.exe
    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap',))

    ip_range = "192.168.0.114"
    nm.scan(hosts=ip_range, arguments='-sn')
    
    for host in nm.all_hosts():
        if 'ipv4' in nm[host]['addresses']:
            ip = nm[host]['addresses']['ipv4']
            mac = nm[host]['addresses']['mac']
            
            print("IP: ", ip)
            print("Mac: ", mac)

scan_network()

