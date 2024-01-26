import random
import turtle
import tests


a = 0 
givers = []
names = []
print('*   sssss              *                       *                 *                     *          *')
print('  ssssssssss    *             *          ccccc         rrr  *                *             ttttt *')
print('*ssss      ss    * eeeeeee        *    cccc   *       rrrrrrrr  *       eeeeeee           *ttttt  ')
print(' ssss             eeeeeeeeeee         cccc           rrrr    rrrr*     eeeeeeeeeee         *ttttt  ')
print('*  ssssss       eeee    *  eeee      ccc   *         rrrr       *    eeee    *  eee      tttttttttt')
print('    sssssss  *  eeee        eee     cc        *      rrrr            eeee    *   ee      tttttttttt')
print('   *   sssss    eeeeeeeeeeeeee  *   cc         *     rrrr     *      eeeeeeeeeeeee       *  ttttt  ')
print('        sssss   eeeee               ccc              rrrr            eeee                   ttttt  ')
print('ssss    sssss    eeeee                ccc            rrrr            eeee                   ttttt  ')
print('  ssssssssss      eeeee                 cccc         rrrr             eeee                  ttttt  ')
print('    ssssss          eeeeeeeeee            ccccc      rrrr              eeeeeeeeeee          ttttt  ')
print('')
print('*   sssss              *                       *                 *                     *          *')
print('  sssssssssss    *             *                          ttttt                                   * ')
print('*ssss       ss    * aaaaaa        *    nn                 ttttt          aaaaaa                     ')
print(' ssss             aaaaaaaaaa          nnnnnnnnnnn         ttttt        aaaaaaaaaa                   ')
print('*  ssssss        aaaa     * eee       nnnnn   nnnnn     ttttttttt     aaaa     * eee                ')
print('    sssssss  *  aaaa        eee       nnn      nnnn     ttttttttt    aaaa        eee                ')
print('   *   sssss   aaa          aae  *    nnn       nnn       ttttt     aaa          aae                ')
print('        sssss   aaaa        aaa       nnn       nnn       ttttt     aaaa         aaa                ')
print('ssss    sssss   aaa         aaa       nnn       nnn       ttttt      aaa         aaa                ')
print('  ssssssssss     aaa        aaaa      nnn       nnn       ttttt       aaa        aaaa               ')
print('    ssssss        aaaaaaaaaaaaaaa     nnn       nnn       ttttt        aaaaaaaaaaaaaaa             ')
print('')
print('')
print('')
print('Limit of people is 10')
while True: 
    number_of_people = int(input('Enter amount of people doing secret santa: '))
    if number_of_people > 10:
        print('We apologize but our limit is only 10 people per usage')
        continue
    else:
        if number_of_people > 0:
             print('Let\'s get started')
             break
        else: 
            continue
while a != number_of_people:
    people_participating = input("Who is doing secret santa: ")
    names.append(people_participating)
    a = a+1
givers.extend(names)
#if they forgot people 
more = input("Is there more people (Y/N):")
if more.upper() == 'Y' or more.upper() == 'YES':
    Extra_people = int(input('How many more are doing secret santa?: '))
    number_of_people = number_of_people+Extra_people
    while True:
        if number_of_people > 10:
            print('We have a limit of ten people per usage')
            number_of_people = number_of_people-Extra_people
        Extra_people = int(input('How many more are doing secret santa?: '))
        number_of_people = number_of_people+Extra_people
        if number_of_people <= 10:
            break
        else:
            continue
    while a != number_of_people:
        people_participating = input("Who is doing secret santa: ")
        names.append(people_participating)
        a = a+1
        givers.append(people_participating)
    ab = 130
    cb = -250
    tests.backround()
    tests.cube()
    tests.redraw()
    tests.relid()
    tests.lid()
    for i in range(a):
        gifter = random.choice(givers)
        receiver = random.choice(names)
        while gifter == receiver:
                reciver = random.choice(names)
                if gifter != receiver:
                    break
                else:
                    continue
        tests.k.pendown()
        tests.k.write(f'{gifter} got {receiver}', font=("Roboto", 25, "bold"))
        tests.k.penup()
        ab = ab+75
        tests.k.goto(cb, ab)
        if ab >= 400:
             cb = cb-375
             ab = 75
        names.remove(receiver)
        givers.remove(gifter)
    tests.letters.write(f'Merry Christmas', font=("Times New Roman", 35, "italic"))
else:
    ab = 130
    cb = -250
    tests.backround()
    tests.cube()
    tests.redraw()
    tests.relid()
    tests.lid()
    for i in range(a):
        for k in range(1):
            gifter = random.choice(givers)
            receiver = random.choice(names)
            while gifter == receiver:
                receiver = random.choice(names)
                if gifter != receiver:
                     break
                else:
                     continue
        tests.k.pendown()
        tests.k.write(f'{gifter} got {receiver}', font=("Roboto", 20, "bold"))
        tests.k.penup()
        ab = ab+75
        tests.k.goto(cb, ab)
        if ab >= 400:
             cb = cb-375
             ab = 75
        names.remove(receiver)
        givers.remove(gifter)
    tests.letters.write(f'Merry Christmas', font=("Times New Roman", 35, "italic"))
turtle.Screen().exitonclick()



