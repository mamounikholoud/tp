
class Question():
   
        questions=("ما هي الدولة التي تمتلك أكبر تعداد سكاني في العالم؟",
        "ما هي أكبر دولة في العالم؟",
        "ما هو متوسط عمر خلايا الدم الحمراء في أجسامنا؟",
        "كم عدد الخلايا العصبية في الدماغ البشري؟")
        options=(("a_الصين","b_الولايات المتحدة","c_كوريا الجنوبية","d_"),
        ("a_الجزائر","b_المكسيك","c_روسيا","d_الولايات المتحدة"),
        ("a_120يوما","b_200يوما","c_60يوما","d_300يوما"),
        ("a_100","b_90","c_59","d_86") )
        answaers=("a","c","a","d")
        guesses=[]
        score=0
        questionum=()
        for question in questions:
            print("--------------------------")
            print(question)
            for option in options:
                   print(option)
            guss=input("enter (A,B,C,D):").upper()
            guesses.append(guss)
            if guss ==answaers[questionum]:
                 score +=1
                 print("CORRECT!")
            else:
                  print("INCORRECT!")
                  print(f"{answaers[questionum]}is the corrct answer")