# Read 2 string input from user, whether it is raining and lightning, then do not go out. If it is only raining then either go out with umbrella or play in water. If it is not raining, user may go out with out umbrella.

input_raining = input('Íf it is raining, type raining or else input anything else')
input_lightning = input('Íf it is lightning, type lightning or else input anything else').lower()

if input_raining.lower() == 'raining':
    if input_lightning == 'lightning':
        print("Do not go out")
    else:
        print("Go out with umbrella or you may wish to play in water")
else:
    print("Go out without Umbrella")