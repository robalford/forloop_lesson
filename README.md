## **Exercise Title:** Too many friends

**Exercise Description:** You have way too many followers on social media and it's just too much to keep up with.
Generate random compliments for friends using for-each loops with this handy Python program.

The code for this lesson is in `forloop_lesson.py`. To view the outputs for the code below, run the program from the 
command line with `python forloop_lesson.py`.

To get started we'll need a list of your followers and a list of compliments to send them.

```
followers = ['Jo Jo', 'Randy', 'Lee', 'Becky', 'Jamal']

compliments = [
    "you have a really nice smile :)",
    "you are on FIRE",
    "I like you more than puppies and rainbows",
]
```

Let's start by using a for-each loop to generate a different compliment to send your best friend Randy every day. A 
for-each loop in Python allows us to repeat the same block of code for each item in a list.

```
print("Send Randy compliments\n")

for compliment in compliments:
    print("Hey " + followers[1] + "! It's been too long. Just wanted to tell you that " + compliment)
```

Cool, now let's generate random compliments for every single one of your friends (remember to import the random module
from the Python Standard Library at the top of your file).

```
print("\nSend random compliments to all your friends\n")

for friend in followers:
    print("Hey " + friend + "! How's it going? Just reaching out to say that " + random.choice(compliments))
```

Today you're feeling extra nice so you're going to use a nested for loop to generate every compliment you can think of
for every one of your friends. Go ahead and add some more compliments to the list if you'd like.

```
print("\nSend all the compliments to all your friends\n")

for friend in followers:
    print("Hey " + friend + "! I have a few things I've been meaning to tell you.")
    for num, compliment in enumerate(compliments):
        print(str(num + 1) + "): " + compliment)
```

Whoa, what the heck is that `enumerate` thing? It's a special built-in Python function that gives you the current for 
loop item's list index as well as the item itself. The enumerate function returns two values (`list_index`, `item`) 
for each item that you can use inside your loop block. 

In the example, we have named these values `num` and `compliment`. In the `print` statement, 
we change the item's list index `num` from an integer to a string and add 1 to it because list indexes begin 
with 0, but your friends would think it was weird if you started counting with 0 and that might blow our cover.

Your automated complimenting has been going great. All of your followers feel very appreciated. But today you want
to send an extra special compliment only to your friends that you are following, and just a normal compliment to your
many followers who you can't be bothered to follow. Let's use conditionals inside a for loop to do just that.

```
following = ["Lee", "Becky"]
special_compliment = "You're my favorite!"
normal_compliment = "I like your shoes!"

print("\nSend special compliments to friends you are following and normal compliments to your other followers\n")

for friend in followers:
    if friend in following:
        print("Hey " + friend + "! " + special_compliment)
    else:
        print("Hey " + friend + "! " + normal_compliment)
```

You and Jo Jo are in a fight so today you're sending a random compliment to every one of your followers except her. To
do this you can use a `continue` statement which tells the for loop to skip the rest of the loop block and move to the
next item in the list.

```
print("\nSend a random compliment to everyone but JoJo\n")

for friend in followers:
    if friend == "Jo Jo":
        continue
    print("Hey " + friend + "! " + random.choice(compliments))
```

Today you only want to send a compliment to one random friend. Use a break statement to stop your for loop after
sending your message to just that friend.

```
random_friend = random.choice(followers)

print("\nSend a random compliment to your random friend: " + random_friend + "\n")

for friend in followers:
    if friend == random_friend:
        print("Hey " + friend + "! " + random.choice(compliments))
        break
```
