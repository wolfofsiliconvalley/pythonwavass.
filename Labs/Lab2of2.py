verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

print('The length of the string is: {}'.format(len(verse)))
print("\nThe index of the first occurences of the word 'and' is: {}".format(verse.find('and')))
print("\nThe index of the last occurences of the word 'you' is: {}".format(verse.rfind("you")))
print("\nThe count of occurences of the word 'you' in the verse is: {}".format(verse.count("you")))
