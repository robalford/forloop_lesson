import random

followers = ['Jo Jo', 'Randy', 'Lee', 'Becky', 'Jamal', ]

compliments = ["you have a really nice smile :)", "you are on FIRE", "I like you more than puppies and rainbows", ]

print("Send Randy compliments\n")

for compliment in compliments:
    print("Hey " + followers[1] + "! It's been too long. Just wanted to tell you that " + compliment)

print("\nSend random compliments to all your friends\n")

for friend in followers:
    print("Hey " + friend + "! How's it going? Just reaching out to say that " + random.choice(compliments))

print("\nSend all the compliments to all your friends\n")

for friend in followers:
    print("Hey " + friend + "! I have a few things I've been meaning to tell you.")
    for num, compliment in enumerate(compliments):
        print(str(num + 1) + "): " + compliment)

following = ["Lee", "Becky"]
special_compliment = "You're my favorite!"
normal_compliment = "I like your shoes!"

print("\nSend special compliments to friends you are following and normal compliments to your other followers\n")

for friend in followers:
    if friend in following:
        print("Hey " + friend + "! " + special_compliment)
    else:
        print("Hey " + friend + "! " + normal_compliment)

print("\nSend a random compliment to everyone but JoJo\n")

for friend in followers:
    if friend == "Jo Jo":
        continue
    print("Hey " + friend + "! " + random.choice(compliments))

random_friend = random.choice(followers)

print("\nSend a random compliment to your random friend: " + random_friend + "\n")

for friend in followers:
    if friend == random_friend:
        print("Hey " + friend + "! " + random.choice(compliments))
        break
