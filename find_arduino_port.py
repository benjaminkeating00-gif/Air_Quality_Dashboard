import serial.tools.list_ports

def find_arduino_ports():
    """Find potential Arduino COM ports"""
    ports = serial.tools.list_ports.comports() #function that scans for all available COM ports
    arduino_ports = []
    
    print("Available COM ports:")
    print("-" * 40)
    
    for port in ports:
        print(f"Port: {port.device}")
        print(f"Description: {port.description}")
        print(f"Hardware ID: {port.hwid}")
        
        # Check if it might be an Arduino
        if any(keyword in port.description.lower() for keyword in ['arduino', 'usb', 'serial']):
            arduino_ports.append(port.device)
            print("  -> Potential Arduino port!")
        
        print("-" * 40)
    
    if arduino_ports:
        print(f"\nPotential Arduino ports: {arduino_ports}")
        print(f"Try using: {arduino_ports[0]}")
    else:
        print("\nNo obvious Arduino ports found.")
        print("Make sure your Arduino is connected and drivers are installed.")
    
    return arduino_ports

if __name__ == "__main__":
    find_arduino_ports()