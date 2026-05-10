#1.1 - A hotel wants to calculate the number of rooms needed for a group of guests. The group of guests intend to save money but sharing rooms, and each room can occupy a maximum of 3 people. Provide code for a python 3 function that returns the minimum number of rooms needed for the guests, (5 marks)

def min_rooms(guests):
    # Each room can hold up to 3 guests
    capacity = 3
    
    # Divide guests by capacity
    # Use integer division and remainder to check if extra room is needed
    rooms = guests // capacity   # full rooms
    if guests % capacity != 0:   # if there are leftover guests
        rooms += 1               # add one more room
    
    return rooms

# Example:
print(min_rooms(10))  # 4 rooms (3+3+3+1)
print(min_rooms(6))   # 2 rooms (3+3)
print(min_rooms(2))   # 1 room


#1.2 - A network administrator wants to subnet a network with the IP address 192.168.1.0/24. If they want to create subnets with a maximum of 30 hosts each, how many subnets can they create? (5 marks)

def subnet_count():
    # Original network is /24 → 256 addresses
    # We need max 30 hosts per subnet
    
    # Hosts formula: 2^h - 2
    # Find h = 5 (since 2^5 - 2 = 30)
    host_bits = 5
    
    # Network bits = 32 - host_bits
    network_bits = 32 - host_bits
    
    # Subnets = 2^(network_bits - original_network_bits)
    subnets = 2 ** (network_bits - 24)
    
    return subnets

# Example:
print(subnet_count())  # 8
