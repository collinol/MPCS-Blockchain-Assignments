from BlockChain import encode_and_concenate, double_hash
class Transactions:
    def __init__(self, inputs=None, outputs=None):
        self.version = 1
        self.ListOfInputs = ['input1', 'input2', 'other'] if inputs is None else inputs
        self.ListOfOutputs = ['output', 'output_second', 'other2'] if outputs is None else outputs
        self.InCounter = len(self.ListOfInputs)
        self.OutCounter = len(self.ListOfOutputs)
        self._string_to_hash = encode_and_concenate([self.version, self.InCounter,
                                                     self.OutCounter]
                                                    + self.ListOfOutputs + self.ListOfInputs)
        self.TransactionHash = double_hash(self._string_to_hash)
