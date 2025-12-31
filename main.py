import random, time

def main():
    bot_name = "Bot"
    user_name = "You"
    end = ["end", "stop", "no", "n"]

    secret_num = random.sample(range(1, 20),3)
    Secret = secret_num
    print(Secret)

    print("Welcome here for Mystery Box — Number Mind Game", flush=True)
    time.sleep(1)

    # It's for how many numbers are correct
    def is_correct(Secret, user_guess):
        correct_num = 0
        for r in Secret:
            if r in user_guess:
                correct_num += 1
        return correct_num
    
    # It's for how many numbers are correct and for correct poistion also
    def correct_position(Secret, user_guess):
        correct_pos = 0
        for r in range(min(len(Secret), len(user_guess))):
            if Secret[r] == user_guess[r]:
                correct_pos += 1
        return correct_pos
    
    # It's for how many numbers are correct, butin wrong position
    def correct_wrong_position(Secret, user_guess):
        any_pos = is_correct(Secret, user_guess)
        c_pos = correct_position(Secret, user_guess)
        return any_pos - c_pos


    while True:
        user_input = input(f"{bot_name}: Would you like to play this Game (Yes/No): ").strip().lower()

        if user_input == ("Yes").lower() or user_input == ("Y").lower():

            while True:
                user_guess = input(f"{user_name}: Enter any 3 Numbers (between 1 to 20): ").strip().lower()

                if user_guess in end:
                    print(f"{bot_name}: Ok, ending this round.")
                    break 

                try:
                    user_guess = list(map(int, user_guess.replace(",", " ").split()))
                except ValueError:
                    print(f"{bot_name}: Please enter valid numbers only.")
                    continue

                # If user enter less than 3 numbers
                total_input = len(user_guess)
                if total_input != len(Secret):
                    print(f"{bot_name}: Please enter exactly 3 numbers.")
                    continue

                if user_guess == Secret:
                    print(f"{bot_name}: Congrats, You guessed the number correctly!")
                    break
                else:
                    # print(f"{bot_name}: Sorry, You can't guess it Correctly!")
                    print(f"{bot_name}: Sorry, that's not correct. Try again!")


                # Using Function here
                # 1. It's for how many numbers are correct 
                any_pos = is_correct(Secret, user_guess)
                if any_pos:
                        print(f"{bot_name}: Correct numbers (any position): {any_pos}")

                # 2. For correct poistion and it's not done by me
                c_pos = correct_position(Secret, user_guess)
                if c_pos:
                    print(f"{bot_name}: Correct numbers (correct position): {c_pos}")
                        
                # 3. For Correct but wrong position
                w_pos = correct_wrong_position(Secret, user_guess)
                if w_pos:
                    print(f"{bot_name}: Correct number (wrong position): {w_pos}")


        elif user_input in end:
            print(f"{bot_name}: Ok Thank you, We will try next time.")
            break             

        elif user_input == "":
            print(f"{bot_name}: Input cannot be empty. Please type 'Yes' or 'No'.")    

        else:
            print(f"{bot_name}: Please type Yes or No.")

main()
