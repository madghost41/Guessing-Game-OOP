class GuessingGame():
    def __init__(self, answer, answer_number=0):
        self.answer_number = answer_number
        self.answer = answer

    def guess(self, user_guess, answer_number=0):
        user_guess = int(user_guess)
        answer_number += 1
      
        if user_guess > self.answer:
            print('high')
            print(user_input)
            
        if user_guess == self.answer:
            print("correct")

        if user_guess < self.answer:
            print("low")
            print(user_input)
        return self.answer_number

    def solved(self, user_guess):
        if user_guess == self.answer:
            print("True") 

game = GuessingGame(10)
user_input = input("guess a number ")
game.guess(user_input)



# game.solved()   # => False

# game.guess(5)  # => 'low'
# game.guess(20) # => 'high'
# game.solved()   # => False

# game.guess(10) # => 'correct'
# game.solved()   # => True


