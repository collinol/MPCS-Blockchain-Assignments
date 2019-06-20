from BlockChain import encode_and_concenate, double_hash
class Block:
    def __init__(self, index, header, list_of_transactions):
        self.MagicNumber = 0xD9B4BEF9
        self.blocksize = self.__sizeof__()
        self.BlockHeader = header
        self.index = index
        self.TransactionCounter = len(list_of_transactions)
        self.Transactions = list_of_transactions
        self.to_dsha = encode_and_concenate([self.BlockHeader.hashPreviousBlock, self.BlockHeader.TimeStamp,
                                           self.BlockHeader.bits, self.BlockHeader.nonce,
                                            self.BlockHeader.hashMerkleRoot])
        self.BlockHash = double_hash(self.to_dsha)

