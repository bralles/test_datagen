import elizabeth

en = elizabeth.Business('en')
per = elizabeth.Personal('en')
path1 = elizabeth.Path()

f = open("test_data.txt", 'a+', encoding='utf-8')
count = 1
quantity = int(input('How many records do you want to generate?: '))

for i in range(1, quantity + 1):

    f.write('Record #: ' + str(count) + '\n',)
    f.write('Company Name: ' + en.company() + '\n')
    f.write('Name: ' + per.full_name() + '\n')
    f.write('Social Media Profile: ' + per.social_media_profile() + '\n')
    f.write('Computer IP Address: ' + elizabeth.core.Internet.ip_v4() + '\n')
    f.write('Username: ' + per.username() + '\n')
    f.write('Password: ' + per.password(8) + '\n')
    f.write('Credit Card #: ' + per.credit_card_number() + '\n')
    f.write('Expiration Date: ' + per.credit_card_expiration_date() + '\n')
    f.write('CVV: ' + str(per.cvv()) + '\n')
    f.write('SSN: ' + per.identifier(mask='###-##-####') + '\n')
    f.write('Company Value: ' + en.price(100000.0, 100000000.0) + '\n\n')
    count += 1

f.close()

