code = input()
while True:
    if code == 'csboltpnfi':
        print('BHA')
        break
    if code == 'noejcinwpm':
        print('SJA')
        break
    if code == 'northlondo':
        print('NLCS')
        break
    if code == 'koreainter':
        print('KIS')
        break
    new_code = ''
    for c in code:
        n = ord(c)
        n += 1
        if n == 123:
            n = 97
        new_code += chr(n)
    code = new_code