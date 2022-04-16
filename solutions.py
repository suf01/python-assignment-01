  n = int(input("Enter limit "))
  if(n <= 2):
      print("2")
  else:
      print("2 ")
      for i in range (2, n):
          if(i%2 != 0):
              print(f"{i} ")

#################################

  m = input("Enter a number ")
  size = len(m)

  for j in range (0, size):
      if m[j] == "1":
          print("one ")
      elif m[j] == '2':
          print("two ")
      elif m[j] == '3':
          print("three ")
      elif m[j] == '4':
          print("four ")
      elif(m[j] == "5"):
          print("five ")
      elif (m[j] == "6"):
          print("six ")
      elif (m[j] == "7"):
          print("seven ")
      elif (m[j] == "8"):
          print("eight ")
      elif (m[j] == "9"):
          print("nine ")
      elif (m[j] == "0"):
          print("zero ")

 #####################################

  one = int(input("Enter 1st number "))
  two = int(input("Enter 2st number "))
  three = int(input("Enter 3st number "))
  four = int(input("Enter 4st number "))
  five = int(input("Enter 5st number "))

  if(one+1 == two or one+1 == three or one+1 == four or one+1 == five):
      print("consective")
  elif(two+1 == one or two+1 == three or two+1 == four or two+1 == five):
      print("consective")
  elif(three+1 == one or three+1 == two or three+1 == four or three+1 == five):
      print("consective")
  elif(four+1 == one or four+1 == two or four+1 == three or four+1 == five):
      print("consective")
  elif(five+1 == two or five+1 == three or five+1 == four or five+1 == one):
      print("consective")
  else:
      print("not consective")

##########################################

  import random
  a = ['a', '1', 'E', 'r', '2']
  b = ['T', '5', 'w', 'W', '1']
  c = ['A', 'v', 'Y', 'q', '7']
  d = ['a', '2', 'w', 'n', '4']
  e = ['4', '9', 'h', 'L', 'i']
  f = ['k', 'J', 'T', 'n', '7']
  passs = ""
  for i in range (0, 6):
      num = random.randint(1,6)
      if(num == 1):
          passs+=random.choice(a)
      elif(num == 2):
          passs+=random.choice(b)
      elif(num == 3):
          passs+=random.choice(c)
      elif(num == 4):
          passs+=random.choice(d)
      elif(num == 5):
          passs+=random.choice(e)
      elif(num == 6):
          passs+=random.choice(f)

  print(passs)

#################################################

  nt = int(input("Enter a number "))

  n1 = 0
  n2 = 1
  cnt = 0

  if nt <= 0:
      print("not valid")
  elif nt == 1:
      print(n1)
  else:
      while cnt < nt:
          print(n1)
          nth = n1 + n2
          n1 = n2
          n2 = nth
          cnt += 1

##############################################

  x = int(input("Enter a number "))
  up = x//10
  lo = x%10
  ans = 0
  if(up%lo==0):
      while (x > 0):
          rem = x % 10
          ans = (ans * 10) + rem
          x = x // 10
      print(ans)
  else:
      print(x)

#####################################################

 one  = int(input("enter a number "))
 lar = one
 two  = int(input("enter a number "))
 if(two > lar):
     lar = two
 three  = int(input("enter a number "))
 if(three > lar):
     lar = three
 four = int(input("enter a number "))
 if(four > lar):
     lar = four
 five  = int(input("enter a number "))
 if(five > lar):
     lar = five

 slar = one
 if(two > slar and two != lar):
     slar = two
 if(three > slar and three != lar):
     slar = three
 if(four > slar and four != lar):
     slar = four
 if(five > slar and five != lar):
     slar = five

 print(slar)
 if(slar == one):
     print("position 1")
 elif(slar == two):
     print("position 2")
 elif(slar == three):
     print("position 3")
 elif(slar == four):
     print("position 4")
 elif(slar == five):
     print("position 5")

#################################################

one = int(input("enter a number "))
two = int(input("enter a number "))
three = int(input("enter a number "))
four = int(input("enter a number "))
five = int(input("enter a number "))

avg = one+two+three+four+five

avg/=5

if(one > avg):
    print(one)
if(two > avg):
    print(two)
if(three > avg):
    print(three)
if(four > avg):
    print(four)
if(five > avg):
    print(five)

