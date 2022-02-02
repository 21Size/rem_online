import phonenumbers

x = '+79137875414'

parse_phone = phonenumbers.parse(x, None)
national_phone = str(phonenumbers.format_number(parse_phone, phonenumbers.PhoneNumberFormat.NATIONAL))
phone = str('+7' + national_phone[1:])
phone = phone.replace(' ', '')

print(f'{parse_phone}, {national_phone}, {phone}, {type(phone)}')
