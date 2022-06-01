# The Wanda Magic teapot virtual version. Just like the original it has 5 options that will guide your future. Just think of a question and see.
import random
import time
(print("Hmmm, the answer to your question is... • Хммм, отговорът на твоя въпрос е:"))
time.sleep(2)
answer=random.randint(1,5)
if answer==1:
    print("Yes • Да")
if answer==2:
    print("No • Не")
if answer == 3:
        print("Maybe • Може би")
if answer == 4:
        print("Not today • Не и днес")
if answer == 5:
        print("Who knows • Кой знае")
