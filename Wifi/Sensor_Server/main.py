
import network
import binascii
import time
import machine
import urequests as requests
import socket

ssid = 'CE_STD_2_4G_2' 
password = 'CE@STDKSU'
i = 0

def connect_wifi():
    i = 0 
    if_config = ["IP", "NETMASK", "GATEWAY", "DNS"]
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi!')
    for i in range(4):
        print("{:<10} {:<20}".format(if_config[i],wlan.ifconfig()[i]))
    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
    return html

def html_response():
    global request
    global i
    conn, addr = s.accept()
    print('Got a connection from', addr)
    request = conn.recv(1024)
    request = str(request)
    print('Request content = %s' % request)
    i = i+1
    response = get_html('index.html')
    response = response.replace('counter', str(i))
    conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    conn.send(response)
    conn.close()

def html_socket():
    global s
    global addr
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen()
    print('listening on', addr)

def _start():
    connect_wifi()
    html_socket()
    while True:
        try:
            html_response()
        except KeyboardInterrupt:
            conn.close()
            print("html_sv_exception")
            
if __name__ == "__main__":
    try:
        _start()
    except KeyboardInterrupt:
        machine.reset()
        print("Exception")

