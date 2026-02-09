questions = [
    {"q": "What is the output?", "code": "print(2+3 * 4)", "a": "14"},
    {"q": "Is 15 odd?", "code": "15 % 2 == 1", "a": "True"},
    {"q": "How many items in ['a','b'}?", "code": "len(['a', 'b'])", "a": "2"},
    {"q": "What is the first number printed?", "code": "for i in range(5): print(i)", "a": "0"},
    {"q": "What is the value of x['a']?", "code": "x = {'a': 10, 'b': 20}", "a": "10"} 
    ]

def ask_question(item):
    print("\n" + item["q"])
    print("Code:")
    print(item["code"])
    answer = input("Your answer: ").strip()
    return answer == item["a"]

highscore = 0

play_again = "yes"
while play_again == "yes":
    
    score = 0
    for q in questions:
        if ask_question(q):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    # logic to calculate high score
    
    if score > highscore:
        highscore = score
        
    print(f"\nFinal Score: {score}/{len(questions)}|High Score: {highscore}")  

    play_again = input("\nPlay again? (yes/no): ").lower()
print("Thanks for reviewing!")
