import random

def quiz(option):
    if option != "yes":
        pass
    else:
        print("\nOk lets go...")
        
        count = 0
        
        for i in range(10):
            print(f"\nQuestion no {i+1} :\n{questions[i]}")
            answer = input("\nAnswer : ").lower()
            if questions == questions_one:
                if answer == answers_one[i]:
                    print(f"\nCorrect !")
                    count+=1
                else:
                    print(f"\nWrong !\nThe Answer is {answers_one[i]}")
            elif questions == questions_two:
                if answer == answers_two[i]:
                    print(f"\nCorrect !")
                    count+=1
                else:
                    print(f"\nWrong !\nThe Answer is {answers_two[i]}")
            elif questions == questions_three:
                if answer == answers_three[i]:
                    print(f"\nCorrect !")
                    count+=1
                else:
                    print(f"\nWrong !\nThe Answer is {answers_three[i]}")
        print(f"\nYour score is {count}/10")
        
questions_one = [
    "What is the only bird that can fly backwards?\nA)Parrot\nB)Hummingbird\nC)Eagle",
    "What is the world's largest waterfall, by volume of water?\nA)Victoria Falls\nB)Niagara Falls\nC)Inga Falls",
    "What is the name of the first web browser?\nA)Internet Explorer\nB)WorldWideWeb\nC)Mozilla Firefox",
    "Who created the Marvel Comics Universe?\nA)Steve Ditko\nB)Stan Lee\nC)Jack Kirby",
    "What is the largest mammal on Earth?\nA)Blue whale\nB)Elephant\nC)Lion",
    "Who was the first president of the United States?\nA)Thoams Jefferson\nB)Abraham Lincoln\nC)George Washington",
    "What is the name of the famous american muscle car?\nA)Ford Mustang\nB)Dodge Charger\nC)Chevrolet Camaro",
    "Which planet has the most moons?\nA)Saturn\nB)Jupiter\nC)Uranus",
    "Which programming language is commonly used for game development?\nA)Python\nB)Java\nC)C++",
    "What is the highest-grossing film of all time?\nA)Avatar\nB)Avengers:Endgame\nC)Titanic"]

questions_two = [
    "What is the capital of France?\nA)Madrid\nB)Paris\nC)Berlin",
    "Which planet is known as the Red Planet?\nA)Mars\nB)Mercury\nC)Venus",
    "Who wrote the play 'Romeo and Juliet'?\nA)William Shakespeare\nB)Jane Austen\nC)Mark Twain",
    "What is the largest ocean on Earth?\nA)Atlantic Ocean\nB)Indian Ocean\nC)Pacific Ocean",
    "What is the chemical symbol for gold?\nA)Go\nB)Au\nC)Ag",
    "How many continents are there on Earth?\nA)6\nB)7\nC)8",
    "Which animal is known as the 'King of the Jungle'?\nA)Tiger\nB)Lion\nC)Elephant",
    "What is the boiling point of water at sea level in Celsius?\nA)90 degree C\nB)100 degree C\nC)110 degree C",
    "Which language has the most native speakers in the world?\nA)Mandarin Chinese\nB)English\nC)Spanish",
    "In which year did the Titanic sink?\nA)1910\nB)1912\nC)1920"]

questions_three = [
    "Who painted the Mona Lisa?\nA)Pablo Picasso\nB)Leonardo da Vinci\nC)Vincent van Gogh",
    "Which is the smallest prime number?\nA)1\nB)2\nC)3",
    "What is the tallest mountain in the world?\nA)Mount Everest\nB)K2\nC)Mount Fuji",
    "What currency is used in Japan?\nA)Won\nB)yuan\nC)Yen",
    "Which planet is closest to the Sun?\nA)Mercury\nB)Venus\nC)Earth",
    "Who is the author of the 'Harry Potter' series?\nA)Suzanne Collins\nB)Stephen King\nC)JK Rowling",
    "In which country were the Olympic Games invented?\nA)Italy\nB)France\nC)Greece",
    "What is the hardest natural substance on Earth?\nA)Diamond\nB)Gold\nC)Iron",
    "Which gas do plants absorb from the atmosphere?\nA)Oxygen\nB)Carbondioxide\nC)Nitrogen",
    "How many legs does a spider have?\nA)8\nB)10\nC)6"]


answers_one = [
    "hummingbird",
    "inga falls",
    "worldwideweb",
    "stan lee",
    "blue whale",
    "george washington",
    "ford mustang",
    "saturn",
    "c++",
    "avengers:endgame"]

answers_two = [
    "paris",
    "mars",
    "william shakespeare",
    "pacific ocean",
    "au",
    "7",
    "lion",
    "100 degree c",
    "mandarin chinese",
    "1912"]

answers_three = [
    "leonardo da vinci",
    "2",
    "mount everest",
    "yen",
    "mercury",
    "jk rowling",
    "greece",
    "diamond",
    "carbondioxide",
    "8"]

question_options = [questions_one,questions_two,questions_three]
questions = random.choice(question_options)

print("Quiz Game !\n\nWarning! : Spelling mistake may leads to wrong answer !")
  
user = input("\nDo you want to play ? : ").lower()
quiz(user)

print("\nThank You !")
