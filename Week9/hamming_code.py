import numpy as np

class Hamming74:
    def __init__(self):
        # Generator matrix G
        self.G = np.array([
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        
        # Parity check matrix H
        self.H = np.array([
            [1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1]
        ])

    def encode(self, data):
        # data should be a vector of 4 bits
        codeword = np.dot(self.G, data) % 2
        return codeword

    def decode(self, received):
        # received should be a vector of 7 bits
        syndrome = np.dot(self.H, received) % 2
        syndrome_val = syndrome[0] + syndrome[1]*2 + syndrome[2]*4
        
        corrected = np.copy(received)
        if syndrome_val > 0:
            # Error index is syndrome_val - 1
            idx = int(syndrome_val - 1)
            print(f"   [Error detected at bit {idx+1}. Correcting...]")
            corrected[idx] = 1 - corrected[idx]
            
        # Extract original 4 data bits from indices 2, 4, 5, 6 (1-indexed: 3, 5, 6, 7)
        return corrected[[2, 4, 5, 6]]

if __name__ == "__main__":
    hamming = Hamming74()
    
    # Original data
    data = np.array([1, 0, 1, 1])
    print(f"--- Hamming (7,4) Code Demonstration ---\n")
    print(f"Original Data: {data}")
    
    # Encoding
    encoded = hamming.encode(data)
    print(f"Encoded Codeword: {encoded}")
    
    # Simulating a single bit error
    received = np.copy(encoded)
    error_bit = 2 # Bit index 2 (0-indexed)
    received[error_bit] = 1 - received[error_bit]
    print(f"Received with error at bit {error_bit+1}: {received}")
    
    # Decoding and correcting
    decoded = hamming.decode(received)
    print(f"Decoded Data (Corrected): {decoded}")
    
    if np.array_equal(data, decoded):
        print("\nSuccess: Data recovered correctly!")
