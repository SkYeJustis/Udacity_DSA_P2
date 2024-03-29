import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash, index=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

        self.previous_block = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{str(self.index)}: {self.timestamp} - Encode this string of data.".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:

    def __init__(self, initial_data = "Some information"):
        self.genesis_block = self._genesis_block(initial_data)
        self.latest_block = self.genesis_block
        self.size = 1

    def _genesis_block(self, data):
        return Block(time.strftime("%-H:%M %-m/%-d/%Y", time.gmtime()), data, 0)

    def add_block(self, new_data="Default new data"):
        timestamp = time.strftime("%-H:%M %-m/%-d/%Y", time.gmtime())
        data = new_data
        hash = self.latest_block.hash
        index = self.latest_block.index + 1
        new_block = Block(timestamp, data, hash, index)

        new_block.previous_block = self.latest_block
        self.latest_block = new_block
        self.size += 1

        return new_block

"""
References:
    Udacity: Data Structures and Nanodegree Program - 2. Data Structures
    https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
"""

if __name__ == '__main__':

    def test_case_1():
        blockchain = BlockChain("Starting info")

        for _ in range(5):
            blockchain.add_block("New information")

        print("Check that the previous_hash is the same as the previous block's hash.")
        # Solution: The previous_hash is the same as the previous block's hash
        current_block = blockchain.latest_block
        for i in range(blockchain.size):
            previous_hash = current_block.previous_hash
            if previous_hash != 0:
                current_block = current_block.previous_block
                print(f" {previous_hash} == {current_block.hash} ")
                assert current_block.hash == previous_hash

    def test_case_2():
        blockchain = BlockChain("Starting info")

        blockchain.add_block("Info 1")
        blockchain.add_block(None)
        blockchain.add_block("Info 2")
        blockchain.add_block(None)

        print("Check that the previous_hash is the same as the previous block's hash.")
        # Solution: The previous_hash is the same as the previous block's hash
        current_block = blockchain.latest_block
        for i in range(blockchain.size):
            previous_hash = current_block.previous_hash
            if previous_hash != 0:
                current_block = current_block.previous_block
                print(f" {previous_hash} == {current_block.hash} ")
                assert current_block.hash == previous_hash


    def test_case_3():
        blockchain = BlockChain("Starting info")

        blockchain.add_block(1)
        blockchain.add_block(2)
        blockchain.add_block(3)
        blockchain.add_block(4)
        blockchain.add_block(5)

        print("Check that the hashes are different per block.")
        # Solution: All hash values in the of the current block should be different from hash of the previous block
        current_block = blockchain.latest_block
        while current_block.previous_block:
            print(f" {current_block.hash} <> {current_block.previous_block.hash} ")
            assert current_block.hash != current_block.previous_block.hash
            current_block = current_block.previous_block



    test_case_1()
    test_case_2()
    test_case_3()