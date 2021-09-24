import pygame
import sys
import random

from pygame.constants import KEYDOWN, K_ESCAPE, K_SPACE
pygame.display.set_caption("Flappy Bird by Samiul")
icon= pygame.image.load("images/Flappy.PNG")
pygame.display.set_icon(icon)

def rotate_bird(bird):
    new_bird=pygame.transform.rotozoom(bird,-bird_mov*4,1)
    return new_bird
def create_pipe():
    randomPipePos= random.choice(pipe_height)
    bottom_Pipe= pipesur.get_rect(midtop=(1470,randomPipePos))
    top_pipe= pipesur.get_rect(midbottom=(1470,randomPipePos-200))
    return bottom_Pipe,top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    visible_pipes=[pipe for pipe in pipes if pipe.right>-100]
    return visible_pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 720:
          screen.blit(pipesur,pipe)
        else:
            flipe_pipe= pygame.transform.flip(pipesur,False,True)
            screen.blit(flipe_pipe,pipe)
def check_collision(pipes):
    
    for pipe in pipes:
        bird_mov=0
        gravity=20
        if bird_surf.colliderect(pipe):
            hit_sound.play()
           



            return False
    if bird_surf.top <=-18  or bird_surf.bottom >= 720:
        die_sound.play()
        return False
    return True
def update_score(score,highscore):
    with open('highscore.txt','r') as f:
        highscore=float(f.read())
    if score > highscore:
        with open('highscore.txt','w') as f:
          f.write(str(score))
    return highscore
def pipescore():
    global score
    if pipe_list:
        for pipe in pipe_list:
            if  pipe.centerx==300:
                score +=0.5
                score_sound.play()

  
def score_display(game_state):
    if game_state== "main_game":
        score_surf= game_font.render("Score=" + str(int(score)),True,(0,0,0))
        score_rect= score_surf.get_rect(center=(1100,100))
        screen.blit(score_surf,score_rect)
    elif game_state=="game_over":
         score_surf= game_font.render("Score=" + str(int(score)),True,(0,0,0))
         score_rect= score_surf.get_rect(center=(1100,100))
         screen.blit(score_surf,score_rect)

         highscore_surf= game_font.render("Highscore=" + str(int(highscore)),True,(0,0,0))
         highscore_rect= score_surf.get_rect(center=(1000,200))
         screen.blit(highscore_surf,highscore_rect)

    

    

pygame.init()
game_font=pygame.font.SysFont('goudystout',20)
gravity= 0.25
bird_mov=0
fps=120
Game_act=True
score= 0
highscore=0






screen= pygame.display.set_mode((1270,720))
clock= pygame.time.Clock()
background=pygame.image.load('images/background.png').convert()
bird=pygame.image.load('images/bird.png').convert_alpha()
bird_surf=bird.get_rect(center=(300,360))
pipee =pygame.image.load("images/pipe.png")
pipesur=pygame.transform.scale2x(pipee)
game_over_surf= pygame.image.load("images/message.png")
game_over_rect= game_over_surf.get_rect(center=(635,360))
flap_sound=pygame.mixer.Sound('sounds/wing.mp3')
hit_sound= pygame.mixer.Sound("sounds/hit.mp3")
die_sound=pygame.mixer.Sound('sounds/die.mp3')
score_sound=pygame.mixer.Sound('sounds/point.mp3')
pipe_list=[]
SPAWNPIPE= pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height=[360,270,470,580 ]






while True:
    for event in pygame.event.get():

        if event.type ==pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Game_act:
                bird_mov=0
                bird_mov-=6
                flap_sound.play()
            if event.key== pygame.K_TAB and Game_act== False:
                Game_act= True
                pipe_list.clear()
                bird_surf.center=(300,360)
                bird_mov=0
                
                score=0

        if event.type== SPAWNPIPE:
            pipe_list.extend(create_pipe())

            
    screen.blit(background,(0,0))         
    if Game_act:
        bird_mov += gravity
        bird_surf.centery += bird_mov
        rotated_bird= rotate_bird(bird)
        screen.blit(rotated_bird,bird_surf)
        pipe_list=move_pipe(pipe_list)
        draw_pipes(pipe_list)
        Game_act = check_collision(pipe_list)
        pipescore()
    
        score_display('main_game')
    else:
         
         screen.blit(game_over_surf,game_over_rect)
        
         highscore=update_score(score,highscore)
         score_display('game_over')
         
        



    
    
    

    pygame.display.update()
    clock.tick(fps)