import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        ip = data['ip']
        return ip
    except requests.RequestException:
        return None

public_ip = get_public_ip()
if public_ip:
    print("Tu dirección IP pública es:", public_ip)
else:
    print("No se pudo obtener la dirección IP pública.")
