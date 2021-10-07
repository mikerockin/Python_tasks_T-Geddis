import matplotlib.pyplot as plt
def main():
    infile = open('expenses', 'r')
    expences = infile.readlines()
    for i in range(len(expences)):
        expences[i] = expences[i].rstrip('\n')
    slice_labels = ['Аренда', 'Топливо', 'Еда', 'Одежда', 'Техобслуживание авто', 'Прочее']
    plt.pie(expences, labels=slice_labels)
    plt.title('Расходы за месяц')
    plt.show()

main()