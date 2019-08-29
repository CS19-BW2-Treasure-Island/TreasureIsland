import hashlib
import requests
import json
import sys
import random
def proof_of_work(last_block):
    
    block_string = json.dumps(last_block, sort_keys=True).encode()
    proof = 18000000000
    while not valid_proof(last_block, proof):
        proof += 1
    return proof
def valid_proof(block_string, proof):
    
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?
    """
    guess = f'{block_string}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    # TODO:  CHANGE BACK TO SIX!!!!!!!!!
    return guess_hash[:6] == '000000'
if __name__ == '__main__':
    # What node are we interacting with?
    node = "https://lambda-treasure-hunt.herokuapp.com/api/bc"
    coins_mined = 0
    # Run forever until interrupted
    while True:
        headers ={"Authorization":"Token 8462b8d16624f572bdc0d8402680ae5245449f4d"}
        r = requests.get(url=node + "/last_proof/", headers=headers, timeout=2)
        data = r.json()
        print(data)
        last_block = data['proof']
        diff = data['difficulty']
        print("Last block is:")
        print(last_block)
        print(diff)
        new_proof = proof_of_work(last_block)
        print(f"found a proof: {new_proof}")
        post_data = {
            "proof": new_proof
        }
        r = requests.post(url=node + "/mine/", headers=headers, data=post_data, timeout=2)
        post_data = r.json()
        # print(post_data)
        if data['messages']:
            # keep track of the coins we've mined
            print(data['messages'])
        else:
            print("handle failure message")