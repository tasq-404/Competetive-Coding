username = input().strip().lower()
username = set(username)

if len(username) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")