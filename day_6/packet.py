with open("packet.txt") as f: 
    packet = [line for line in f][0]
    # set to 4 for part 1 and 14 for part 2
    num_unique_elements = 4
    subpackets = [len(set(packet[i:i+num_unique_elements])) for i in range(0, len(packet))]
    print("the first unique sec ends at index: " + str(subpackets.index(num_unique_elements) + num_unique_elements))
