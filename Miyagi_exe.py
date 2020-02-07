from Miyagi_core_func import  *

while True:
    user_input = input("Say something")
    if sensei(user_input):
        print('You are smart, but not wise - address me as Sensei please')
    elif block_blocking(user_input):
        print('Remember, best block, not to be there..')
    elif question(user_input):
        print('questions are wise, but for now. Wax on, and Wax off!')
    elif exit_(user_input):
        print("Sometimes, what heart know, head forget")
        break
    else:
        print('do not lose focus. Wax on. Wax off.')

