import openai


openai.api_key = open('key.txt', 'r').read().strip('\n')


def get_start(starting_choice):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user',
                   'content': f'This is the first start of a text-based RPG game you will take the user through,'
                              f' please provide numerical options for all options. The user has chosen these to start '
                              f'the game: {starting_choice}'}]
    )

    start = completion['choices'][0]['message']['content']
    return start

def start_game():
    starting_choice = user_starting_choices()
    start = get_start(starting_choice)
    return start


def get_instruction(user_input):

    openai.api_key = open('key.txt', 'r').read().strip('\n')

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': f'The user has chosen option: {user_input}. please continue'}]
    )

    instruction = completion['choices'][0]['message']['content']
    return instruction

def get_user_choice():
    choice = input('Please enter a choice: ')
    return choice


def user_starting_choices():
    starting_choice = input()
    return starting_choice

def main():
    choice = get_user_choice()
    instruction = get_instruction(choice)



if __name__ == '__main__':
    start = start_game()
    print(start)
    while True:
        main()
