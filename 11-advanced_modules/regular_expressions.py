if __name__ == '__main__':

    text = "The phone number is 123-456-789654"
    text2 = "The phone number number is 123-456-789654"
    print('phone' in text)

    import re

    pattern = 'phone'
    print(re.search(pattern, text))

    new_pattern = 'unknown text'
    print(re.search(new_pattern, text))

    match = re.search(pattern, text2)  # returns always the first occurrence
    print(match.span())
    print(match.start())
    print(match.end())

    matches = re.findall("number", text2)
    print(len(matches))

    for item in re.finditer("number", text2):
        print(item.span())
        print(item.start())
        print(item.end())
        print(item.group())


    regex = r'\d\d\d-\d\d\d-\d\d\d\d\d\d'
    phone = re.search(regex, text)
    print(phone)
    print(phone.group())
    print(phone.span())

    regex_optimized = r'\d{3}-\d{3}-\d{6}'
    phone_optimized = re.search(regex_optimized, text)
    print(phone_optimized)
    print(phone_optimized.group())
    print(phone_optimized.span())

    phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{6})')
    phone_optimized_2 = re.search(phone_pattern, text)
    print(phone_optimized_2)
    print(phone_optimized_2.group())
    print(phone_optimized_2.span())
    print(phone_optimized_2.group(1))
    print(phone_optimized_2.group(2))
    print(phone_optimized_2.group(3))

    search1 = re.search(r'cat|dog', "The dog is here")
    search2 = re.search(r'cat|dog', "The dog and the cat are here") # first result only
    print(search1)
    print(search2)

    findall_res = re.findall(r'.at', 'The cat in the hat went splat')
    print(findall_res)

    findall_res2 = re.findall(r'^\d', "1 is a number")  # verifies if a string starts with a number, otherwise return nothing
    print(findall_res2)

    findall_res3 = re.findall(r'\d$', "1 is a number inferior to 2")  # verifies if a string ends with a number, otherwise return nothing
    print(findall_res3)

    findall_res4 = re.findall(r'[^\d]+', "There are 3 numbers maybe 5 or 6, but sometimes yes indeed")  # excludes any digits
    print(findall_res4)

    findall_res5 = re.findall(r'[^!.? ]+', "There are 3 ! numbers ? .... maybe 5 or 6, but sometimes yes indeed")  # excludes specific ponctuation marks and whitespaces
    print(findall_res5)
    print(' '.join(findall_res5))

    findall_res6 = re.findall(r'[\w]+-[\w]+', "find hyphen-words or long-ish or anything you-want")  # excludes any digits
    print(findall_res6)