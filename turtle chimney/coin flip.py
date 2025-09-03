import random
headscounter = 0
tailscounter = 0
for i in range(10000):
 x = random.randint(0, 1)
 if x == 0:
    print('heads')
    headscounter = headscounter + 1
 elif x == 1:
    print('tails')
    tailscounter = tailscounter + 1
print(f"the amount of heads you got is {headscounter}")
print(f"the amount of tails you got is {tailscounter}")
print(f'heads percentage: {int(round((headscounter/i)*100))}%')
print(f'tails percentage: {int(round((tailscounter/i)*100))}%')