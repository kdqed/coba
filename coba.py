import random

c1 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
c2 = ['a','e','i','o','u','r','y','t']
c3 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
c4 = ['a','e','i','o','u','r','y','t','s','k','q']
print('{}{}{}{}'.format(random.choice(c1),random.choice(c2),random.choice(c3),random.choice(c4)))
