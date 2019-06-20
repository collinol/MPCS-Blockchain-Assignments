from Block import Block
from BlockChain import BlockChain
from Header import Header
from Transaction import Transactions
if __name__ == '__main__':
    # generate transactions
    all_transactions = []
    for x in range(10):
        all_transactions.append(Transactions(["{}_input".format(x)], ["{}_output".format(x)]))
    # genesis header for genesis block - string of 0's for previousHash and 0 for input/output of transactions
    genesis_transactions = [Transactions(['0'], ['0'])]
    genesis_header = Header('0'*64, genesis_transactions)
    genesis_block = Block(0, genesis_header, genesis_transactions)
    # each block takes a header, which takes the previous block's hash, as well as new transactions for that block
    block1 = Block(1, Header(genesis_block.BlockHash, genesis_transactions), all_transactions[0:5])
    block2 = Block(2, Header(block1.BlockHash, block1.Transactions), all_transactions[5:])
    block_chain = BlockChain()
    block_chain.add_block(genesis_block)
    block_chain.add_block(block1)
    block_chain.add_block(block2)
    block_chain.print_blockchain()
    height = 2
    print("Find block located at height {}\n".format(height) + block_chain.find_block_by_height(height))
    search_transaction_hash = "cabf4e842bdb65c92dec16eb10d28ad2d1c566a227670d47dc3fe2d3a9eb4e86"
    print("Find transaction in block chain with transaction hash of {}".format(search_transaction_hash))
    print(block_chain.find_transaction_by_hash(search_transaction_hash))
    print("Find transaction in block chain with transaction hash of {}".
          format("48e440817635e525fdfbec3a5e14a7a7902b119d859859d2d2e318c0d08199d7"))
    print(block_chain.find_transaction_by_hash("48e440817635e525fdfbec3a5e14a7a7902b119d859859d2d2e318c0d08199d7"))
    print("details of block at height 1")
    print("Block size: ", block_chain.blocks[1].blocksize)
    print("Block hash: ", block_chain.blocks[1].BlockHash)
    print("Transactions Hashes: ")
    for x in [t.TransactionHash for t in block_chain.blocks[1].Transactions]:
        print(x)
