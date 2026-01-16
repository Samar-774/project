import socket
import threading
from cryptography.fernet import Fernet

# Generate a Key (In a real app, this would be shared beforehand)
key = Fernet.generate_key()
cipher = Fernet(key)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    print(f"[*] Server listening on Port 9999 (AES Encrypted)")
    
    client, addr = server.accept()
    print(f"[*] Connection from {addr}")
    
    # Receive encrypted data
    encrypted_msg = client.recv(1024)
    print(f"[RAW ENCRYPTED BYTES]: {encrypted_msg}")
    
    # Decrypt
    decrypted_msg = cipher.decrypt(encrypted_msg).decode()
    print(f"[DECRYPTED MESSAGE]: {decrypted_msg}")
    client.close()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    
    message = "Confidential_Data_Packet"
    encrypted_msg = cipher.encrypt(message.encode())
    
    client.send(encrypted_msg)
    print("[*] Data Encrypted and Sent.")

# Run both for demonstration
if __name__ == "__main__":
    # Start server in background thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    
    import time
    time.sleep(1) # Wait for server to start
    
    start_client()