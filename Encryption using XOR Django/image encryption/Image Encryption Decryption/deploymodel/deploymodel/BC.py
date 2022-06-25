import hashlib
from datetime import datetime
from . import settings


class Block:
    def __init__(self, index, productId, productQuantity, ownerId, timestamp, previousHash):
        self.index = index
        self.productId = productId
        self.productQuantity = productQuantity
        self.ownerId = ownerId
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        transaction = str(self.index) + str(self.productId) + str(self.productQuantity) + \
            str(self.ownerId) + str(self.timestamp) + str(self.previousHash)
        return hashlib.sha256(transaction.encode()).hexdigest()


def getLatestBlock():
    return blockchain[-1]


def generateNextBlock(nextBlock):
    previousBlock = getLatestBlock()
    nextIndex = previousBlock.index + 1
    productId = nextBlock[0]
    productQuantity = nextBlock[1]
    ownerId = nextBlock[2]
    nextTimestamp = datetime.now()
    blockchain.append(Block(nextIndex, productId, productQuantity,
                    ownerId, nextTimestamp, previousBlock.hash))


def getGenesisBlock():
    return Block(0, 0, 0, 0, datetime.now(), 0)


def getBlockDetails(index=-1):
    # ans==list of list of string
    ans = []
    if index != -1:
        a = []
        a.append(str(blockchain[index].productId))
        a.append(str(blockchain[index].productQuantity))
        a.append(str(blockchain[index].ownerId))
        a.append(str(blockchain[index].timestamp))
        a.append(str(blockchain[index].previousHash))
        a.append(str(blockchain[index].hash))
        ans.append(a) 
    else:
        for index in range(0, len(blockchain)):
            a = []
            a.append(str(blockchain[index].productId))
            a.append(str(blockchain[index].productQuantity))
            a.append(str(blockchain[index].ownerId))
            a.append(str(blockchain[index].timestamp))
            a.append(str(blockchain[index].previousHash))
            a.append(str(blockchain[index].hash))
            ans.append(a)
    return ans



blockchain=[getGenesisBlock(), ]

menu={}
menu['1']="Add Block."
menu['2']="Get Block Details."
menu['3']="Exit"
while False:
    options=menu.keys()
    for entry in options:
        print(entry, menu[entry])

    selection=int(input("Please Select: "))
    if selection == 1:
        blockchain.append(generateNextBlock())
        print()
    elif selection == 2:
        index=int(input("Enter Desired Block Index: "))
        if(0 <= index and index < len(blockchain)):
            print(getBlockDetails(index))
    elif selection == 3:
        break
    else:
        print("Unknown Option Selected!")
