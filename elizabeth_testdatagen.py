import elizabeth

en = elizabeth.Business('en')
per = elizabeth.Personal('en')
path1 = elizabeth.Path()

for i in range(1, 5):
    print('Company Name: ' + en.company() + '\t')
    print('Name: ' + per.full_name() + '\t')
    print('Social Media Profile: ' + per.social_media_profile() + '\t')
    print('Where are passwords stored?: ' + path1.project_dir() + '\t')
    print('Computer IP Address: ' + elizabeth.core.Internet.ip_v4() + '\t')
    print('Username: ' + per.username() + '\t')
    print('Password: ' + per.password(8) + '\t')
    print('Credit Card #: ' + per.credit_card_number() + '\t')
    print('Expiration Date: ' + per.credit_card_expiration_date() + '\t')
    print('CVV: ' + str(per.cvv()) + '\t')
    print('SSN: ' + per.identifier(mask='###-##-####') + '\t')
    print('Company Value: ' + en.price(100000.0, 100000000.0) + '\n')