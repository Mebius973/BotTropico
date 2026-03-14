from readMoney import read_money

previous_money = None

def compute_reward():

    global previous_money

    current_money = read_money()

    if previous_money is None:
        previous_money = current_money
        return 0

    reward = (current_money - previous_money) / 1000

    previous_money = current_money

    return reward