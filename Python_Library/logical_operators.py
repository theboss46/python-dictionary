# AND operator(Both must be true)
hight_income = True
good_credit = True
criminal_record = False

if hight_income and good_credit:
    print('Elegible for loan 1 ')


# Or operator(only one has to be true)
if hight_income or good_credit:
    print('Elegible for loan 2')

# Not opertator(turns true to false and turns false to true)
if hight_income and not criminal_record or good_credit and not criminal_record:
    print('Elegible for loan 3')
