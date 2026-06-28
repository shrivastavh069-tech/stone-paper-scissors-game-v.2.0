import time 
def computer_choise():
    import random
    gond=random.choice(["scissor","stone","paper"])
    return gond 
    
def checking():
    if(user == "stone"):
        return user
    elif(user == "paper"):
        return user
    elif(user == "scissor"):
        return user
    else:
        print("❌ Invalid Syntax")
        print("Points Goes to Bot 🤖")
        return ("❌ Invalid Syntax")

def winning():
    if(user == "stone" and bot=="stone"):
        return("==DRAW==")
    elif(user =="paper" and bot =="paper"):
        return("==DRAW==")
    elif(user == "scissor" and bot=="scissor"):
        return("==DRAW==")
    elif(user == "paper" and bot == "stone"):
        return("==USER WINS==")
    elif(bot == "paper" and user == "stone"):
        return("==BOT WINS==")
    elif(user == "paper" and bot =="scissor"):
        return("==BOT WINS==")
    elif(bot == "scissor" and user == "paper"):
        return("==BOT WINS==")
    elif(user =="stone" and bot=="scissor"):
        return("==USER WINS==")
    elif(bot =="stone" and user=="scissor"):
        return("==BOT WINS==")
    elif(user =="scissor" and bot =="paper"):
        return("==USER WINS==") 
    elif(user== "❌ Invalid Syntax"):
        return("==BOT WINS==")
    
        
        
def winner(): #for level 3 
    if(user == "stone" and bot1=="stone" and bot2=="stone"):
        return("==DRAW==")
    elif(user == "scissor" and bot1=="scissor" and bot2=="scissor"):
        return("==DRAW==")
    elif(user == "paper" and bot1=="paper" and bot2=="paper"):        
        return("==Draw==")
    elif(user=="paper" and bot1== "stone" and bot2 =="stone"):
        return("==USER WINS==")
    elif(user =="stone" and bot1=="paper" and bot2=="paper"):
        return("==☠️The Deadly Twins Wins☠️==")
    elif(user =="scissor" and bot1=="stone" and bot2=="stone"):
        return("==☠️The Deadly Twins Wins☠️==")
    elif(user =="stone" and bot1=="stone" and bot2=="scissor"):
        return("==USER WINS==")
    elif(user =="scissor" and bot1=="stone" and bot2=="paper"):
        return("==DRAW==") 
    elif(user =="scissor" and bot1=="paper" and bot2=="stone"):
        return("==DRAW==") 
    elif(user =="paper" and bot1=="paper" and bot2=="stone"):
        return("==☠️The Deadly Twins Wins☠️==") 
    elif(user =="stone" and bot1=="paper" and bot2=="scissor"):
        return("==DRAW==")
    elif(user =="stone" and bot1=="scissor" and bot2=="paper"):
        return("==DRAW==")
    elif(user =="paper" and bot1=="scissor" and bot2=="stone"):
        return("==DRAW==")
    elif(user =="stone" and bot1=="paper" and bot2=="stone"):
        return("==☠️The Deadly Twins Wins☠️==")
    elif(user =="stone" and bot1=="scissor" and bot2=="stone"):
        return("==USER WINS==")
    elif(user =="stone" and bot1=="scissor" and bot2=="scissor"):
        return("==USER WINS==")
    elif(user =="paper" and bot1=="stone" and bot2=="paper"):
        return("==USER WINS==")
    elif(user =="paper" and bot1=="scissor" and bot2=="paper"):
        return("==☠️The Deadly Twins Wins☠️==")
    elif(user =="paper" and bot1=="scissor" and bot2=="scissor"):
        return("==☠️The Deadly Twins Wins☠️==")
    elif(user =="scissor" and bot1=="paper" and bot2=="paper"):
        return("==USER WINS==")
    elif(user =="scissor" and bot1=="paper" and bot2=="scissor"):
        return("==USER WINS==")
    elif(user =="scissor" and bot1=="stone" and bot2=="scissor"):
        return("==☠️The Deadly Twins Wins☠️==")
    elif(user =="paper" and bot1=="paper" and bot2=="scissor"):
        return("==☠️The Deadly Twins Wins☠️==")
    elif(user =="scissor" and bot1=="scissor" and bot2=="stone"):
        return("==☠️The Deadly Twins Wins☠️==")
    elif(user == "❌ Invalid Syntax"):
        return("=☠️The Deadly Twins Wins☠️=")
        
print("""
=========================================
||   🎮|WELCOME TO THE WORLD OF|🎮     ||
||⚔️ [STONE  PAPER  AND  SCISSOR] ⚔️   ||
=========================================
""")

time.sleep(1)

print("🤖 INITIALISING DATA")
time.sleep(1)

print("🤖 INITIALISING JARVIS")
time.sleep(1)

print("🤖 INITIALISING TROJIS")
time.sleep(1)

print("📡CONTACTING TO ☠️DEADLY TWINS☠️")
time.sleep(1)

print("🔗Connection Accomplished")
time.sleep(1)

print("✅SYSTEM READY")
time.sleep(1)

print("⚔️ BATTLE BEGINS ⚔️")
time.sleep(1)

print("===========[LEVELS]===========")
print("""
---->LEVEL 1<----
>>🥸Easy🥸
>>Contains Single Bot🤖
>>3 Matches🎯
---->LEVEL 2<----
>>🔥MEDIUM🔥
>>Contains TWO Advanced Bots🤖 [Jarvis and Trojis] 
>>PLay One by One
>>Each Bot [3 Match]
---->LEVEL 3<----
>>☠️HARD☠️
>>Contains A Single Advanced AI Bot 👾
>>Single FINAL MATCH💀""")
print("THE APPONENT WHO PASS THESE LEVEL SHOULD BE HIGHLY REWARDED🎁")
time.sleep(4)
print("__________________________________________")
while True:
    print("""
------📢🔴IMPORTANT INSTRUCTION🔴📢-----
TYPE LOWERCASE IN THS GAME LIKE---
1.stone
2.paper
3.scissor
if type uppercase or another alphabets points goes to ☠️The Deadly Twins☠️
🔹If You loose In Any Level The Game Restarts From Level 1.
---------------------------------""")
    time.sleep(2)
    start=int(input("""🤖:-TO \n=========================================\nSTART THE MATCH [PLEASE Type:1]\n For Exit [Please Press 2]:\n=========================================\nTYPE HERE:-"""))
    if(start == 1):
        comp_po=0
        user_po=0
        print("==========[🥸LEVEL 1,EASY🥸]==========")
        for i in range (1,4,1):
            user=input("I choose:")
            check=checking()
            user=check
            print("🤖 Choose:-\a")
            bot=computer_choise()
            print(bot)
            chunk=winning()
            print(chunk)
            if(chunk == "==USER WINS=="):
                user_po+=1
            elif(chunk == "==BOT WINS=="):
                comp_po+=1
            elif(chunk == "❌ Invalid Syntax"):
                comp_po+=1
        print("=================")
        print("📊SCORE BOARD📊")
        print("-----------------")
        print("👤:USER POINTS-->",user_po)
        print("🤖:BOT POINTS-->",comp_po)
        print("==================")
        time.sleep(1)
        if(comp_po == user_po):
            print("🤖:-Nobody Wins!!\nbut see you on next match")
        elif(comp_po<user_po):
            print("🤖:- I will see you on the next match!!\a")
            time.sleep(1)
        else:
            print("🤖:- aah!! I won !!\n!!retry!!\a")
            continue

        print("==========[😈LEVEL 2,MEDIUM😈]==========")
        time.sleep(1)
        
        print("🤖:- Now Two Bots is participating Tackel the 1st Bot:JARVIS")
        time.sleep(2)
        print("🤖 BOT:- RESETTING SCORE BOARD📊")
        time.sleep(1)
        print("🤖:-MEET JARVIS")
        time.sleep(1)
        print("Hii!!\nThis is JARVIS 😁\nlet's play\n1st you start")
        time.sleep(1)
        comp_po=0
        user_po=0
        print("------------++++++++++++++--------------")
        for i in range (1,4,1):
            user=input("I choose:")
            check=checking()
            user=check
            print("JARVIS Choose:-\a")
            bot=computer_choise()
            print(bot)
            win=winning()
            chunk=win
            print(chunk)
            if(chunk == "==USER WINS=="):
                user_po+=1
            elif(chunk == "==BOT WINS=="):
                comp_po+=1
            elif(chunk == "❌ Invalid Syntax"):
                comp_po+=1
        print("=================")
        print("📊SCORE BOARD📊")
        print("-----------------")
        print("👤:USER POINTS-->",user_po)
        print("😁:JARVIS POINTS-->",comp_po)
        print("=================")
        time.sleep(1)
        if(comp_po == user_po):
            print("JARVIS:-Nobody Wins!!\nbut see you on next match")
        elif(comp_po<user_po):
            print("JARVIS:- NICE MY BROTHER IS LEFT DON'T BE HAPPY!!😤\a")
            time.sleep(1)
        else:
            print("JARVIS:-I won !!\n Come again Another Time\a")
            continue
        print("------------++++++++++++++--------------")
        comp_po=0
        user_po=0
        print("😁 JARVIS:-RESETTING SCORE BOARD 📊")
        print("😁 JARVIS:- USER Meet my brother")
        time.sleep(1)
        time.sleep(1)
        print("Hi!!!,Iam Trojis🤓\n let's play the winning game 🎯")
        for i in range (1,4,1):
            user=input("I choose:")
            check=checking()
            user=check
            print("TROJIS Choose:-\a")
            bot=computer_choise()
            print(bot)
            win=winning()
            chunk=win
            print(chunk)
            if(chunk == "==USER WINS=="):
                user_po+=1
            elif(chunk == "==BOT WINS=="):
                comp_po+=1
            elif(chunk == "==❌ Invalid Syntax=="):
                comp_po+=1
        print("=================")
        print("📊SCORE BOARD📊")
        print("-----------------")
        print("👤:USER POINTS-->",user_po)
        print("🤓:TROJIS POINTS-->",comp_po)
        print("=================")
        time.sleep(1)
        if(comp_po == user_po):
            print("TROJIS:-Nobody Wins!!\nready for next match🤨!")
        elif(comp_po<user_po):
            print("TROJIS:-Appreciating You Wins🎉\a")
            time.sleep(1)
        else:
            print("TROJIS:-I won !!\n Come again Another Time😆\a")
            break
        print("------------++++++++++++++--------------")         
        print("==========[☠️LEVEL 3,HARD☠️]==========")
        time.sleep(1)
        print("===⚠️ !WARNING! ⚠️===")
        time.sleep(1)
        print("--🔥You Have Entered The Final Level🔥--")
        time.sleep(1)
        print("-[The Ultimate BotS Has Arrived......]-")
        time.sleep(1)
        print("  |       🔥_________________🔥   |")
        print("  |--------|The DEADLY TWINS☠️|----|")
        print("          🔥-----------------🔥    ")
        time.sleep(1)
        print("☠️The Deadly Twins:- User I Always Win ")
        time.sleep(1)
        print("Let's Play The Winning Game 🎯 ")
        time.sleep(1)
        print("☠️The Deadly Twins :-1st Chance Is Yours")
        for i in range (1,2,1):
            user=input("I choose:")
            check=checking()
            user=check
            print("Jarvis choose-")
            bot1=computer_choise()
            print(bot1)
            print("Trojis choose-")
            bot2=computer_choise()
            print(bot2)
            sukkon=winner()
            sakhu=sukkon
            print(sakhu)
            print("Processing 🌍")
            time.sleep(1)
            if(sakhu == "==☠️The Deadly Twins Wins☠️=="):
                print("YAY!!! , I Know That I Always Winner😎")
                time.sleep(1)
                print("come again On Another Day😆 ")
                continue
            elif(sakhu == "=☠️The Deadly Twins Wins☠️="):
                print("""
                ☠️THE DEADLY TWINS☠️

                ⚠️Invalid Move Detected.....

                We Don't fight Players Who Don't Know The Rules.

                Point Awarded✨ To ☠️The Deadly Twins☠️! 😈

                Come Again After Remembering 🔴Important Instructions 🔴""")
                continue
                
            elif(sakhu == "==USER WINS=="):
                print("☠️THE DEADLY TWINS☠️:- CONGRATULATIONS 🎉 Very Few Comes At This Step")
                print("☠️THE DEADLY TWINS☠️:- According To Menu\n --:YOUR REWARD IS:")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("--EMPTY 🪣--")
                print("☠️THE DEADLY TWINS☠️:- 😂😂\n Hamko Haraoge\n Kase Laga Gift 🤣?")
                input("YOUR RESPONSE:-")
                continue
            elif(sakhu =="==DRAW=="):
                print("☠️The Deadly Twins Wins☠️ :- Your Fortune Is Bright That Match Is Draw \nWanna I Win !😎")
                continue
            
    elif(start== 2):
        print("Thank You For Using")
        break
        
    