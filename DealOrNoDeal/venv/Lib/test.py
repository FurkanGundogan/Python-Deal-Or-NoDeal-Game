import pygame
import random
import time
import sys
import os


class Resim(pygame.sprite.Sprite):
# *** Class for image objects in my project***
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# *** All money card objects in a Dictionary ***
moneyList={
           "1":Resim('foto/1.png', [30, 100]), "10":Resim('foto/10.png', [30, 150]),
           "50":Resim('foto/50.png', [30, 200]), "100":Resim('foto/100.png', [30, 250]),
           "250":Resim('foto/250.png', [30, 300]), "500":Resim('foto/500.png', [30, 350]),
           "1000":Resim('foto/1000.png', [30, 400]), "5000":Resim('foto/5000.png', [30, 450]),
           "10000":Resim('foto/10000.png', [30, 500]), "25000":Resim('foto/25000.png', [30, 550]),
           "50000":Resim('foto/50000.png', [620, 100]), "75000":Resim('foto/75000.png', [620, 150]),
           "100000":Resim('foto/100000.png', [620, 200]),"150000":Resim('foto/150000.png', [620, 250]),
           "200000":Resim('foto/200000.png', [620, 300]),"200002":Resim('foto/200000.png', [620, 350]),
           "250000":Resim('foto/250000.png', [620, 400]), "250002":Resim('foto/250000.png', [620, 450]),
           "500000":Resim('foto/500000.png', [620, 500]), "500002":Resim('foto/500000.png', [620, 550])
           }
# *** All box objects in a Dictionary ***
boxList={"1":Resim('foto/bag.png', [190, 200]), "2":Resim('foto/bag.png', [275, 200]),
         "3":Resim('foto/bag.png', [360, 200]), "4":Resim('foto/bag.png', [445, 200]),
         "5":Resim('foto/bag.png', [530, 200]),"6":Resim('foto/bag.png', [190, 250]),
         "7":Resim('foto/bag.png', [275, 250]), "8":Resim('foto/bag.png', [360, 250]),
         "9":Resim('foto/bag.png', [445, 250]), "10":Resim('foto/bag.png', [530, 250]),
         "11":Resim('foto/bag.png', [190, 300]), "12":Resim('foto/bag.png', [275, 300]),
         "13":Resim('foto/bag.png', [360, 300]), "14":Resim('foto/bag.png', [445, 300]),
         "15":Resim('foto/bag.png', [530, 300]),"16":Resim('foto/bag.png', [190, 350]),
         "17":Resim('foto/bag.png', [275, 350]), "18":Resim('foto/bag.png', [360, 350]),
         "19":Resim('foto/bag.png', [445, 350]), "20":Resim('foto/bag.png', [530, 350])
         }
# *** My option images which will appear when it is offer time   ***
options={"Yes":Resim('foto/yes.png', [300, 300]),
            "No":Resim('foto/no.png', [410, 300])}



# *** i did these two because i need to map moneys and boxes randomly ***
userMoneyList=list(moneyList.keys())
# *** moneytoKutu have keys and values whiches are boxes and moneys ***
moneytoKutu={}


# *** Two methods to show boxes and money cards on screen ***
def ekranParalariGoster():
    for m in moneyList.values():
        screen.blit(m.image, m.rect)
def kutularıgGoster():
    for b in boxList.values():
        screen.blit(b.image, b.rect)


def getirMousePosition():
# *** i did a half turkish method to use  mouse.getpos function faster ***
    return pygame.mouse.get_pos()


def kutuMasayaTasima():
# *** This method move the box which player did select at the begining of game to top of Table***
# *** Then game will start with a warning message***
    x,y=getirMousePosition()
    print(x,"-",y)
    for a,b in boxList.items():
        en=b.rect[0]
        boy=b.rect[1]
        if x >=en and x <= en+79:
            if y >= boy and y <= boy+39:
                b.rect=[380,425]
                paraKutuDagitim()
                #Masadaki silinmesin diye kontrol ve key degerini sakladım.
                kutuMasaSecim[0]=True
                kutuMasaSecim[1] = a
                mesajGoster("Box", trq, 350, 150)
                mesajGoster("Selected", trq, 280, 225)
                mesajGoster("Game is", red, 300, 400)
                mesajGoster("Starting", red, 299, 475)
                pygame.display.update()
                time.sleep(2)



def kutuSecimi():
# *** This method moves box to unreachable coordinates***
# *** Then it calls paraSil(), paraSil() moves money cards to unreachable coordinates ***
# *** After all it remind how many selection remind to offer with a text ***
    x,y=getirMousePosition()
    for a,b in boxList.items():
        en=b.rect[0]
        boy=b.rect[1]
        if x >=en and x <= en+79 and a!=kutuMasaSecim[1]:
            if y >= boy and y <= boy+39:
                b.rect=[1000,1000]
                paraSil(a)
                showOfferRemineder()


def paraKutuDagitim():
# *** This method randomly adds boxnumber as keys and moneys as values to Dictionary moneytoKutu ***
    i=1
    size=20
    while size>0:
        x=random.randint(0,size)
        moneytoKutu[i]=userMoneyList[x-1]
        userMoneyList.remove((userMoneyList[x-1]))
        i+=1
        size-=1
    print(moneytoKutu)


def paraSil(paraKey):
# *** Moves money card to an unreachable coordinates then show value of money on middle of screen***
# Parayı ekrandan uzağa taşıyarak silmiş gibi yapacak
    print(moneytoKutu[int(paraKey)])
    print(moneyList[str(moneytoKutu[int(paraKey)])])
    if int(paraKey) in moneytoKutu.keys():
        moneyList[str(moneytoKutu[int(paraKey)])].rect=[1000,1000]


        x=len(str(moneytoKutu[int(paraKey)]))
        # x is to write large numbers to middle of screen
        if x>3:
            x*=7
        mesajGoster(str(moneytoKutu[int(paraKey)])+"$", colorMoney, 353-x,260)
        pygame.display.update()
        time.sleep(1)

# *** Colors that i did use in my project***
colorMoney=(0,150,0)
black=(0,0,0)
red=(188,0,0)
trq=(0,128,128)


def mesajGoster(msg, color,x,y):
    # *** I made this method to use when i want to show a message on screen in my other methods***
    text = font.render(msg, True, color)
    screen.blit(text,[x,y])


def offerCalculator():
# *** this method has simple math to get an offer ***
    moneys = []
    for a,b in moneyList.items():
        if b.rect!=[1000,1000]:
            moneys.append(int(a))

    maxx=max(moneys)
    minn=min(moneys)
    length=len(moneys)

    if maxx-minn<=minn+2:
        offer=minn+(maxx-minn)/length
    else:
        offer=(maxx-minn)/length
    return offer


# # keys steps counts , values remind count
gameStep={1:3,
          2:3,
          3:3,
          4:2,
          5:1,
          6:0,}

def showOfferRemineder():
    # ***this method shows a text about how many selection remind to offer, it works with gameStep  ***
    for a,b in gameStep.items():
        if b>=0 and b!=-1:
            if b ==0:
                offerTime[0]=True
                gameStep[a]=-1
                break
            else:
                print("b=",b)
                mesajGoster(str(b)+" Step To Offer",red,202,130)
                pygame.display.update()
                time.sleep(1)
                gameStep[a] -= 1
                break

# *** Variable userSelection controls Deal or No Deal
userSelection = [False]
#*** offerTime controls that how many selection remind to get an offer
offerTime=[False]
#*** when it is time to show offer and get an answer offerSelectin controls it.
offerSelection=[False]
#*** i could not reach these 3 variable when they were normal boolean,then
#*** i changed them as a list with 1 variable


def showOffer():
#   *** Method for showing offer on screen ***
    for o in options.values():
        screen.blit(o.image, o.rect)
    x=str(int(offerCalculator()))
    mesajGoster("! Offer !",red,300,170)
    mesajGoster(x+" $",colorMoney,300,230)
    pygame.display.update()


def endGame(offerCount):
#   *** This method shows prize and Restarts game automatically ***
    restart = Resim("foto/restart.png", [250, 320])
    screen.blit(restart.image, restart.rect)
    prize = str(int(offerCalculator()))
    if offerCount==6:
        for x,y in boxList.items():
            if y.rect==[380,425]:
                prize=(moneytoKutu[int(x)])

    mesajGoster("!!! Your Prize !!!", red, 200, 200)
    mesajGoster(prize+" $", colorMoney, 300, 260)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    os.system('python "test.py"')


def exitControl():
#   *** If mouse clicks on power button.png Game will close ***
    x,y=getirMousePosition()
    if x>75 and x<125 and y>25 and y<75:
        sys.exit(1)


def showPowerButton():
#   *** These method shows power button.png at left top ***
    btn=Resim("foto/power.png", [75, 25])
    screen.blit(btn.image, btn.rect)



pygame.init()
font=pygame.font.SysFont('Hursheys',80)


BackGround = Resim('foto/background.png', [0, 0])

# These list with 2 variables provides only one box selection which is on table and box's number
kutuMasaSecim=[False,0]

# There are max 6 offers in game, if it is 6 game, game must end
offerCounter = 0

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Deal or No Deal")
done = False



# I Solved "surface quit error" by try-except
try:
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                exitControl()
                if kutuMasaSecim[0] == False:
                    kutuMasayaTasima()
                else:
                    kutuSecimi()



            if userSelection[0] == True or offerCounter==6:
                endGame(offerCounter)



        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        ekranParalariGoster()
        kutularıgGoster()
        showPowerButton()
        pygame.display.update()

        # Boolean Control to show offer on screen
        if offerTime[0]==True:
            # loop to show offer on screen
            while offerSelection[0]==False:
                x,y=getirMousePosition()
                showOffer()
                for event in pygame.event.get():
                    # 'Deal' or 'NoDeal' selection
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if x>=300 and x<=403 and y>=300 and y<=400:
                            print('yes')
                            offerSelection[0]=True
                            userSelection[0]=True
                            offerCounter+=1
                            break
                        elif x>=410 and x<=513 and y>300 and y<400:
                            print('no')
                            offerSelection[0] = True
                            offerCounter+=1
                            break
        offerTime[0] = False
        offerSelection[0]=False



except:
    print("Çıkış Yapıldı")

