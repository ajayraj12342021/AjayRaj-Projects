Questions = [
    ["What is the capital city of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", 3],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2],
    ["Who wrote Hamlet?", "Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain", 3],
    ["What is the largest ocean on Earth?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["In which country are the Pyramids of Giza located?", "Greece", "Mexico", "Egypt", "Sudan", 3],
    ["What is the chemical symbol for Gold?", "Ag", "Au", "Gd", "Go", 2],
    ["Who was the first person to walk on the Moon?", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins", "Neil Armstrong", 4],
    ["How many continents are there on Earth?", "5", "6", "7", "8", 3],
    ["Which is the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", 2],
    ["What is the national currency of Japan?", "Won", "Yuan", "Ringgit", "Yen", 4]
]


for question in Questions:
    print(question[0])
    print(f"A. {question[1]}")
    print(f"B. {question[2]}")
    print(f"C. {question[3]}")
    print(f"D. {question[4]}")

    try:
        ans = int(input("Enter your answer:\n1 for A, 2 for B, 3 for C, 4 for D: "))
    except ValueError:
        print("Invalid input.")
        break

    if (ans==question[5]):
        print("Correct Answer.")
    else:
        correct = question[question[5]]
        print(f"Incorrect Answer.\nThe correct answer is: {correct}")
        print("Better luck next time.")
        break






