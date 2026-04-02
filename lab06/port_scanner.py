from scapy.all import *
import socket

# Danh sách các port phổ biến theo hình mẫu trong đề
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

def scan_common_ports(target_domain, timeout=2):
    open_ports = []
    # Phân giải domain thành IP
    target_ip = socket.gethostbyname(target_domain)
    
    for port in COMMON_PORTS:
        # Gửi gói tin TCP SYN
        response = sr1(IP(dst=target_ip)/TCP(dport=port, flags="S"), timeout=timeout, verbose=0)
        
        # Nếu nhận được cờ SYN-ACK (0x12) thì port mở
        if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
            open_ports.append(port)
            # Gửi gói tin RST để đóng nửa kết nối
            send(IP(dst=target_ip)/TCP(dport=port, flags="R"), verbose=0)
            
    return open_ports

if __name__ == "__main__":
    target = input("Enter the target domain: ")
    ports = scan_common_ports(target)
    print(f"Open ports: {ports}")