import nmap 
import sys
tg = str(sys.argv[1])
ports = [21,22,80,139,443,8080]
scan_v = nmap.PortScanner()

print(f"Scanning {tg} for ports {str(ports)}")

for port in ports: 
  portscan  = scan_v.scan(tg, str(port))
  print(f"Port {port} is {portscan['scan'][tg]['tcp'][port]['state']}")

print(f"Host {tg} is {portscan['scan'][tg]['status']['state']}")
