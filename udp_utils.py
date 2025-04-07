import socket
import threading

class UDPReceiver(threading.Thread):
    def __init__(self, port=7501, callback=None):
        super().__init__(daemon=True)
        self.port = port
        self.callback = callback
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", self.port))

    def run(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
                message = data.decode().strip()
                if self.callback:
                    self.callback(message)
            except Exception as e:
                print(f"UDP Receiver error: {e}")
                break

    def stop(self):
        self.running = False
        self.sock.close()

def send_udp_message(message, ip="127.0.0.1", port=7500):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(str(message).encode(), (ip, port))
    sock.close()

_target_ip = "127.0.0.1"

def set_target_ip(ip):
    global _target_ip
    _target_ip = ip
    print(f"[INFO] Target IP set to {_target_ip}")

def get_target_ip():
    return _target_ip

