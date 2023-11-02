qtn = input("What is your name? ")
answer = qtn
for answer in qtn:
    with open("resposta.txt", "w") as answer:
        answer.write(qtn)

answer = input("What is your favorite color?")
with open("fav_color.txt", "w") as f:
    f.write(answer)
