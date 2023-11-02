cassio = {"eight": "1.78",
          "favorite color": "blue",
          "favorite team" : "Boca Juniors",
          "favorite fighter" : "Nick Diaz"
          }
question = input("What is your question about Cassio?")


if question in cassio:
    answer = cassio[question]
    print(answer)
else:
    print("Answer not found.")
