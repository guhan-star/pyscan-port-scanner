import socket
import threading
import time

target = "127.0.0.1" # Localhost (safe to scan)
active_ports = []

def scan_port(port):
    # Create a network socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        # connect_ex returns 0 if the connection is successful (port is open)
        if s.connect_ex((target, port)) == 0:
            active_ports.append(port)
        s.close()
    except:
        pass

def run_scanner(start_port, end_port):
    threads = []
    # Dispatch a thread for every port to scan them simultaneously
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish before moving on
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print(f"--- PyScan Started against {target} ---")
    start_time = time.time()
    
    # Scanning the 1024 "well-known" system ports
    run_scanner(1, 1024)
    
    print(f"Scan complete in {time.time() - start_time:.2f} seconds.")
    print(f"Open ports found: {active_ports}")