doska = list(range(1,10))
combination = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
def doska_paint():
     print("*************")
     for i in range(3):
          print('*', doska[0 + i *3],'*', doska[1 + i *3],'*', doska[2 + i *3],'*')
     print("*************")
def hod(playar_token):
     while True:
          a = input("какой твой ход " + playar_token + " ?")
          if not (a in '123456789'):
              print('так не пойдет. Повтори')
              continue
          a = int(a)
          if str(doska[a -1]) in 'XO':
               print('глаза разуй. Занято!')
               continue
          doska[a - 1] = playar_token
          break
def proverka():
     for e in combination:
          if doska[e[0]-1] == doska[e[1]-1] == doska[e[2]-1]:
               return doska[e[1]-1]
     else:
          return False
def main():
     ch = 0
     while True:
          doska_paint()
          if ch % 2 == 0:
               hod("X")
          else:
               hod("O")
          if ch > 3:
               pob = proverka()
               if pob:
                    doska_paint()
                    print(pob, 'КрасавчеГ!')
                    break
          ch += 1
          if ch > 8:
               doska_paint()
               print('оба лохи, фу')
               break
main()


