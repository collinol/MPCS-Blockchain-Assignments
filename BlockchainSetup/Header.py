import math
import datetime as date
import merkle
from BlockChain import double_hash, encode_and_concenate
class Header:
    def __init__(self, previoushash, list_of_transactions):
        self.version = 1
        self.previousHash = previoushash
        self.hashPreviousBlock = double_hash(encode_and_concenate(previoushash))
        self.hashMerkleRoot = merkle.MerkleTreeHash([transaction.TransactionHash for transaction in  list_of_transactions],
                                                    math.ceil(math.log2(len(list_of_transactions))))
        self.TimeStamp = date.datetime.now()
        self.bits = 0
        self.nonce = 0
