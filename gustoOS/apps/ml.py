import pygame
import time
import random


def game():
    pygame.init()

    rijen = 18
    kolommen = 20
    vakgrootte = 30
    moeilijkheidsgraad = 20
    scherm = pygame.display.set_mode((kolommen * vakgrootte, rijen * vakgrootte))

    titel_font = pygame.font.SysFont(None, 44)
    uitleg_font = pygame.font.SysFont(None, 28)
    start_font = pygame.font.SysFont(None, 36)
    start_knop = pygame.Rect(190, 470, 220, 55)

    uitleg = (
        "Use the arrow keys to move the red square.",
        "Paint as many squares red as possible.",
        "Green moves randomly and tries to paint them green.",
        "Press SPACE to become an eraser.",
        "Green cannot pass through blue squares.",
        "Paint more red squares than green squares.",
        "scoreboard is in making.",
    )

    wacht_op_start = True
    while wacht_op_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                wacht_op_start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_knop.collidepoint(event.pos):
                    wacht_op_start = False

        scherm.fill((255, 255, 255))
        titel = titel_font.render("PAINTER - How to play", True, (0, 0, 0))
        scherm.blit(titel, titel.get_rect(center=(scherm.get_width() // 2, 55)))

        for index, regel in enumerate(uitleg):
            tekst = uitleg_font.render(regel, True, (0, 0, 0))
            scherm.blit(tekst, tekst.get_rect(center=(scherm.get_width() // 2, 115 + index * 42)))

        pygame.draw.rect(scherm, (0, 170, 0), start_knop)
        tekst = start_font.render("START", True, (255, 255, 255))
        scherm.blit(tekst, tekst.get_rect(center=start_knop.center))
        pygame.display.flip()

    veld = [[0 for k in range(kolommen)] for r in range(rijen)]


    sleep = time.sleep

    rij = 1
    kolom = 1
    veld[rij][kolom] = 1
    rijmonster = random.randint(0, rijen - 1)
    kolommonster = random.randint(0, kolommen - 1)
    veld[rijmonster][kolommonster] = 2
    laatstebeweging = 0
    running = True
    geel = False
    score = 0
    for i in range(moeilijkheidsgraad):
            mogelijkepositiesy = len(veld[rij]) - 2
            mogelijkepositiesx = len(veld) - 2
            generateintx = random.randint(2, mogelijkepositiesy)
            generatinty = random.randint(2, mogelijkepositiesx)
            veld[generatinty][generateintx] = 4
            
            veld[generatinty][generateintx + 1] = 4
            veld[generatinty][generateintx - 1] = 4
            veld[generatinty + 1][generateintx] = 4
            veld[generatinty - 1][generateintx] = 4
            veld[generatinty + 1][generateintx + 1] = 4
            veld[generatinty - 1][generateintx - 1] = 4
            veld[generatinty + 1][generateintx - 1] = 4
            veld[generatinty - 1][generateintx + 1] = 4
            for r in range(len(veld)):
                for k in range(len(veld[r])):
                    if veld[r][k] == 4:
                        pygame.draw.rect(scherm, (0, 0, 255), (k * vakgrootte, r * vakgrootte, vakgrootte, vakgrootte))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False

        
        

        toetsen = pygame.key.get_pressed()
        if pygame.time.get_ticks() - laatstebeweging > 300:
            if toetsen[pygame.K_LEFT]:
                    
                kolom -= 1
                if kolom < 0:
                    kolom = 0
                laatstebeweging = pygame.time.get_ticks()

            if toetsen[pygame.K_RIGHT]:
                    
                kolom += 1
                huidigekolom = None
                for k in range(len(veld[rij])):
                    if veld[rij][k] == 1:
                        huidigekolom = k
                if kolom > len(veld[rij]) - 1:
                    kolom = len(veld[rij]) - 1
                laatstebeweging = pygame.time.get_ticks()
                        

            if toetsen[pygame.K_UP]:
                    
                rij -= 1
                huidigekolom = None
                    
                if rij < 0: 
                    rij = 0
                laatstebeweging = pygame.time.get_ticks()
            if toetsen[pygame.K_DOWN]:
                    
                    
                rij += 1
                if rij > rijen - 1:
                    rij -= 1
                laatstebeweging = pygame.time.get_ticks()
            
            
        veld[rij][kolom] = 1
        veld[rijmonster][kolommonster] = 2
            
        for r in range(len(veld)):
            for k in range(len(veld[r])):
                if veld[r][k] == 1:
                    pygame.draw.rect(scherm, (255, 0, 0), (k * vakgrootte, r * vakgrootte, vakgrootte, vakgrootte))
                    
                elif veld[r][k] == 4:
                    pygame.draw.rect(scherm, (0, 0, 255), (k * vakgrootte, r * vakgrootte, vakgrootte, vakgrootte))
                    

                else:
                    pygame.draw.rect(scherm, (255, 255, 255), (k * vakgrootte, r * vakgrootte, vakgrootte, vakgrootte))

            
        if toetsen[pygame.K_SPACE]:
            veld[rij][kolom] = 3
            geel = True

            for r in range(len(veld)):
                for k in range(len(veld[r])):
                    if veld[r][k] == 3:
                        pygame.draw.rect(scherm, (255, 255, 0), (k * vakgrootte, r * vakgrootte, vakgrootte, vakgrootte))
                        veld[rij][kolom] = 0    
        oude_rij = rijmonster
        oude_kolom = kolommonster
        rgetal = random.randint(0, 3)
        if rgetal == 0:
            rijmonster -= 1
            if rijmonster < 0:
                rijmonster = 0
        elif rgetal == 1:
            rijmonster += 1
            if rijmonster > rijen - 1:
                rijmonster = rijen - 1
        elif rgetal == 2:
            kolommonster -= 1
            if kolommonster < 0:
                kolommonster = 0
        elif rgetal == 3:
            kolommonster += 1
            if kolommonster > kolommen - 1:
                kolommonster = kolommen - 1
        if veld[rijmonster][kolommonster] == 4:
            rijmonster = oude_rij
            kolommonster = oude_kolom
        veld[rijmonster][kolommonster] = 2
        for rm in range(len(veld)):
                for km in range(len(veld[rm])):
                    if veld[rm][km] == 2:
                        
                        pygame.draw.rect(scherm, (0, 255, 0), (km * vakgrootte, rm * vakgrootte, vakgrootte, vakgrootte))
                    

        pygame.display.flip()
        if geel:
            pygame.time.delay(300)
            geel = False
        else:
            pygame.time.delay(75)

    pygame.quit()


if __name__ == "__main__":
    game()
