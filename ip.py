import socket

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Ejemplo de uso
my_ip = get_ip()
print(f"Mi dirección IP es: {my_ip}")
