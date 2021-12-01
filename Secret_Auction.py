from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         
'''
bidders = {}
has_new_bidder = 'yes'
highest = ''
while has_new_bidder == 'yes':
    clear()
    print(logo)
    new_name = input("enter the bidder name : ")
    new_amount = int(input("enter the amount $: "))
    bidders[new_name] = new_amount
    has_new_bidder = input('have more bidders (yes/no) : ')

maximum = ''
highest = 0
for bidder in bidders:
    if bidders[bidder] > highest:
        maximum = bidder
        highest = bidders[bidder]
print(f"the bidder with highest bid is {maximum} and the bid is ${highest}")


