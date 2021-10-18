import random
def main():
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
                'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
                'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover',
                'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
                'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
                'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
                'Maine': 'Augusta', 'Maryland': 'Annapolis',
                'Massachusetts': 'Boston', 'Michigan': 'Lansing',
                'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
                'Missouri': 'Jefferson City', 'Montana': 'Helena',
                'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
                'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                'New Mexico': 'Santa Fe', 'New York': 'Albany',
                'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
                'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
                'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
                'Texas': 'Austin', 'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier', 'Virginia': 'Richmond',
                'Washington': 'Olympia', 'West Virginia': 'Charleston',
                'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    correct = 0
    wrong = 0
    next_question = True
    index = 0
    user_solution = ''
    while next_question:
        state_iterator = iter(capitals)
        index = (random.randint(1, 50) - 1)
        for i in range(index-1):
            temp = state_iterator.__next__()
        current_state = str(state_iterator.__next__())
        user_solution = input('Назовите столицу штата ' + \
                              current_state + \
                              ' (либо введите 0, чтобы выйти): ')
        if user_solution == '0':
            next_question = False
            print('Вы дали', correct, 'правильных и', \
                  wrong, 'неправильных ответов.')
        elif user_solution == capitals[current_state]:
            correct = correct + 1
            print('Правильно.')
        else:
            wrong = wrong + 1
            print('Неправильно.')

main()
