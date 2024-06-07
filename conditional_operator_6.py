print("Любите ли вы котиков? (да/нет)")
answer1 = input()
print("Умеете ли вы программировать? (да/нет)")
answer2 = input()
if answer1.lower() == "да" and answer2.lower() == "да":
    print("Вы обладаете незаурядным умом")
elif answer1.lower() == "да" and answer2.lower() == "нет":
    print("Вам стоит чаще проводить время с котиками.")
elif answer1.lower() == "нет" and answer2.lower() == "да":
    print("Вас ждет блестящее будущее в мире технологий.")
elif answer1.lower() == "нет" and answer2.lower() == "нет":
    print("Вы обладаете незаурядным умом")
else:
    print("Пожалуйста, ответьте 'да' или 'нет'.")