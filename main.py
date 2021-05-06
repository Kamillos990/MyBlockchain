from Blockchain import Blockchain

def show_menu():
    print("Welcome to your blockchain manager! \n"
          "What would you like to do? (Press number corresponding to action you would like to perform and confirm with "
          "Enter)")

    choice = input("1.Create new block \n"
                   "2.Perform new transaction \n"
                   "3.Display entire chain \n"
                   "4.Count blocks in the chain \n"
                   "5.Display block \n"
                   "6.Quit")
    print()
    return choice


blockchain = Blockchain()

while True:
    print()
    user_input = show_menu()
    if user_input == '1':
        proof = input("Provide block's proof")
        blockchain.new_block(proof)
        print("Block has been created successfully")
    elif user_input == '2':
        sender = input("Provide sender's name")
        recipient = input("Provide recipient's name")
        amount = input("Provide transaction amount")
        blockchain.new_transaction(sender, recipient, amount)
        print("Transaction has been performed successfully")
    elif user_input == '3':
        print(blockchain.chain)
    elif user_input == '4':
        print(blockchain.blocks_count())
    elif user_input == '5':
        index = int(input("Which block would you like to see"))
        print(blockchain.display_block(index))
    elif user_input == '6':
        break







# blockchain = Blockchain()
# t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
# t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
# t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
# blockchain.new_block(12345)
#
# t4 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
# t5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
# t6 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
# blockchain.new_block(6789)

# print("Genesis block: ", blockchain.chain)