cost_ed_sem = 45000
up_paid = 0.03 / 2
for x in range(1,6):
    cost_ed_sem = cost_ed_sem * up_paid + cost_ed_sem
    print(x, '\t', format(cost_ed_sem, '.2f'))