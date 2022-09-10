from hashlib import sha256

# Mini code snippet for understanding sha256 function
"""
hash = sha256(("yOuR_TxT").encode("ASCII")).hexdigest()
print(hash)
"""

# SHA256 function for input text
def SHA256(text):
 return sha256(text.encode("ASCII")).hexdigest()

# find function for finding the hash of the block
# This function iterates infinitely until hash contains prefix_zeros according to our difficulty level
def find(block_number,transactions,previous_hash,prefix_zeros):
 nonce = 1
 while(True):    
    text = str(block_number) + transactions + previous_hash + str(nonce)
    if SHA256(text)[:prefix_zeros] == "0"*prefix_zeros:
        print("nonce",nonce)
        print("HASH MATCHED NOW")
        print(SHA256(text))
        return "Congrats"
    else :
        print("nonce=",nonce,",prefix_zeros for Hash=", SHA256(text)[:prefix_zeros])
        nonce += 1
        
# Entry point of python file
if __name__ == "__main__":
    transactions = """
    Bob -> Marley -> 20,
    Tom -> Jerry -> 10
    """
    difficulty = 4
    newHash = find(5,transactions,"b2cf7e6c7ee8758035cbc2bc9f7e75a98c601f95bd328110d6c94cf32ba8c2eb",difficulty)
    print("The HASH is",newHash)
