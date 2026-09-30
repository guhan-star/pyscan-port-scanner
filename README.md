# PyScan Port Scanner

A small Python TCP port scanner for checking which ports are open on the local machine.

## Features

- Scans ports `1` through `1024`
- Uses TCP connections over IPv4
- Scans ports concurrently with Python threads
- Reports the ports that accept a connection
- Uses only Python's standard library

## Requirements

- Python 3.8 or newer

No third-party packages are required.

## Usage

From the project directory, run:

```bash
python scanner.py
```

The scanner currently targets `127.0.0.1` and checks the well-known ports from `1` to `1024`.

Example output:

```text
--- PyScan Started against 127.0.0.1 ---
Scan complete in 0.42 seconds.
Open ports found: [135, 445]
```

The open ports in your output will depend on the services running on your computer.

## How It Works

For each port, PyScan attempts a TCP connection with a 0.5-second timeout. A successful connection means the port is reported as open. The program waits for all port checks to finish before printing the results.

## Limitations

- The target address is currently hardcoded to `127.0.0.1`.
- The port range is currently hardcoded to `1-1024`.
- Only IPv4 TCP ports are checked.
- Results may not be printed in numerical order.

## Legal and Ethical Use

Only scan systems and networks that you own or have explicit permission to test. Unauthorized port scanning may violate policies or local laws.
