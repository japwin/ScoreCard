SCard1 = []
SCard2 = []

def FighterName1():
    global fighter1

    fighter1 = input('Enter Fighter 1 Name:')

    print('Hello' + ' ' + str(fighter1))

def FighterName2():
    global fighter2
    fighter2 = input('Enter Fighter 2 Name:')

    print('Hello' + ' ' + str(fighter2))

def Round1():
    global Round1F1
    global Round1F2
    while True:
        print('Round 1')
        Round1F1 = input(str(fighter1) + ' ' )
        Round1F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round1F1))
        SCard2.append(int(Round1F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))      
        resumeend = input('Continue?' + ' ')

        if resumeend == 'yes':
            print('Round 2')
            Round2()
            break
        elif resumeend == 'no':
            Results()
            break
            finishednow()

def Round2():
    global Round2F1
    global Round2F2
    while True:
        Round2F1 = input(str(fighter1) + ' ' )
        Round2F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round2F1))
        SCard2.append(int(Round2F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))
        resumeend = input('Continue?' + ' ')

        if resumeend == 'yes':
            print('Round 3')
            Round3()
            break
            
        elif resumeend == 'no':
            Results()
            break
def Round3():
    global Round3F1
    global Round3F2
    while True:
        Round3F1 = input(str(fighter1) + ' ' )
        Round3F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round3F1))
        SCard2.append(int(Round3F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))
        resumeend = input('Continue?' + ' ')  
        if resumeend == 'yes':
            print('Round 4')
            Round4()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round4():
    global Round4F1
    global Round4F2
    while True:
        Round4F1 = input(str(fighter1) + ' ' )
        Round4F2 = input(str(fighter2) + ' ' )        
        SCard1.append(int(Round4F1))
        SCard2.append(int(Round4F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))
        resumeend = input('Continue?' + ' ')  
        if resumeend == 'yes':
            print('Round 5')
            Round5()
            break

        elif resumeend == 'no':
            Results()
            break

def Round5():
    global Round5F1
    global Round5F2
    while True:
        Round5F1 = input(str(fighter1) + ' ' )
        Round5F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round5F1))
        SCard2.append(int(Round5F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))
        resumeend = input('Continue?' + ' ')  
        if resumeend == 'yes':
            print('Round 6')
            Round6()
            break
        
        elif resumeend == 'no':
            Results()
            break

def Round6():
    global Round6F1
    global Round6F2
    while True:
        Round6F1 = input(str(fighter1) + ' ' )
        Round6F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round6F1))
        SCard2.append(int(Round6F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))
        resumeend = input('Continue?' + ' ')  
        if resumeend == 'yes':
            print('Round 7')
            Round7()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round7():
    global Round7F1
    global Round7F2
    while True:
        Round7F1 = input(str(fighter1) + ' ' )
        Round7F2 = input(str(fighter2) + ' ' )       
        SCard1.append(int(Round7F1))
        SCard2.append(int(Round7F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))
        resumeend = input('Continue?' + ' ') 
        if resumeend == 'yes':
            print('Round 8')
            Round8()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round8():
    global Round8F1
    global Round8F2
    while True:
        Round8F1 = input(str(fighter1) + ' ' )
        Round8F2 = input(str(fighter2) + ' ' )       
        SCard1.append(int(Round8F1))
        SCard2.append(int(Round8F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))  
        resumeend = input('Continue?' + ' ')
        if resumeend == 'yes':
            print('Round 9')
            Round9()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round9():
    global Round9F1
    global Round9F2
    while True:
        Round9F1 = input(str(fighter1) + ' ' )
        Round9F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round9F1))
        SCard2.append(int(Round9F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))         
        resumeend = input('Continue?' + ' ')
        if resumeend == 'yes':
            print('Round 10')
            Round10()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round10():
    global Round10F1
    global Round10F2
    while True:
        Round10F1 = input(str(fighter1) + ' ' )
        Round10F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round10F1))
        SCard2.append(int(Round10F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))        
        resumeend = input('Continue?' + ' ')
        if resumeend == 'yes':
            print('Round 11')
            Round11()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round11():
    global Round11F1
    global Round11F2
    while True:
        Round11F1 = input(str(fighter1) + ' ' )
        Round11F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round11F1))
        SCard2.append(int(Round11F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2)) 
        resumeend = input('Continue?' + ' ')
        if resumeend == 'yes':
            print('Round 12')
            Round12()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round12():
    global Round12F1
    global Round12F2
    while True:
        Round12F1 = input(str(fighter1) + ' ' )
        Round12F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round12F1))
        SCard2.append(int(Round12F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2)) 
        resumeend = input('Continue?' + ' ')
        if resumeend == 'yes':
            print('Round 13')
            Round13()
            break
        
        elif resumeend == 'no':
            Results()
            break

def Round13():
    global Round13F1
    global Round13F2
    while True:
        Round13F1 = input(str(fighter1) + ' ' )
        Round13F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round13F1))
        SCard2.append(int(Round13F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2)) 
        resumeend = input('Continue?' + ' ')

        if resumeend == 'yes':
            print('Round 14')
            Round14()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round14():
    global Round14F1
    global Round14F2
    while True:
        Round14F1 = input(str(fighter1) + ' ' )
        Round14F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round14F1))
        SCard2.append(int(Round14F2))
        overall1 = sum(SCard1)
        overall2 = sum(SCard2)
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))         
        resumeend = input('Continue?' + ' ')
        if resumeend == 'yes':
            print('Round 15')
            Round15()
            break
            
        elif resumeend == 'no':
            Results()
            break

def Round15():
    global Round15F1
    global Round15F2
    while True:
        Round15F1 = input(str(fighter1) + ' ' )
        Round15F2 = input(str(fighter2) + ' ' )
        SCard1.append(int(Round15F1))
        SCard2.append(int(Round15F2))
        print('Fight goes to Scorecards')
        ScoreCards()
        break

def Results():
    while True:
        print ('How did it end? 1=KO, 2=No Contest, 3=Scorecards, 4=DQ')
        ending = input('Enter Here: ')
        if ending == '1':
            KnockOut()
            break
        elif ending == '2':
            print('No Contest')
            overall1 = sum(SCard1)
            overall2 = sum(SCard2)
            print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
            print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))            
            finishednow()
        elif ending == '3':
            ScoreCards()
            break

        elif ending == '4':
            print('under Construction')
            finishednow()
def KnockOut():
    global overall1
    global overall2

    overall1 = sum(SCard1)
    overall2 = sum(SCard2)
    print('Who Won' + '1='+ str(fighter1) + '2=' + str(fighter2))
    KOWinner = input('Enter Number: ')
    if KOWinner == '1':
        print('Winner by KO ' + str(fighter1))
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))
    elif KOWinner == '2':
        print('Winner by KO ' + str(fighter2))
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(overall1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(overall2))        
    else:
        print('You Drunk?!')

def ScoreCards():
    Scorecard1 = sum(SCard1)
    Scorecard2 = sum(SCard2)
    print(sum(SCard1))
    if Scorecard1 > Scorecard2:
        print('Winner by Decision' + ' ' + str(fighter1))
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(Scorecard1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(Scorecard2))  

    elif Scorecard2 > Scorecard1:
        print('Winner by Decision' + ' ' + str(fighter2))
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(Scorecard1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(Scorecard2))

    else:
        print('Draw')
        print(str(fighter1) + ' ' + str(SCard1) + ' ' + str(Scorecard1))
        print(str(fighter2) + ' ' + str(SCard2) + ' ' + str(Scorecard2)) 

def finishednow():
    print('Bye')

FighterName1()
FighterName2()
Round1()


finishednow()
