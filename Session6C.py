"""
Another Brick in the wall

john
jack
harry: 11 bricks

        total
john:1   1
jack:2   3
john:2   5
jack:4   9
john:3   12

john:2   11
"""

bricks_by_customer = int(input("Enter Number of bricks:"))

print('wall must be constructed with', bricks_by_customer, 'bricks')

total_bricks = 0

# John starts with 1 brick
# Then John increases by 1 in every round
for bricks in range(1, bricks_by_customer + 1):

    # John places bricks
    john = bricks
    total_bricks += john

    # Check if John crossed the required number
    if total_bricks > bricks_by_customer:
        extra_bricks = total_bricks - bricks_by_customer
        last_bricks = john - extra_bricks

        print('john placed last bricks', last_bricks)
        break

    # Jack places double the bricks John placed
    jack = john * 2
    total_bricks += jack

    # Check if Jack crossed the required number
    if total_bricks > bricks_by_customer:
        extra_bricks = total_bricks - bricks_by_customer
        last_bricks = jack - extra_bricks

        print('jack placed last bricks', last_bricks)
        break