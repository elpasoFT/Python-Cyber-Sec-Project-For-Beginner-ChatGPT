import random
import string

whitelist = []
for i in range(100):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
    whitelist.append(password)

with open('whitelist.txt', 'w') as f:
    f.write('\n'.join(whitelist))
