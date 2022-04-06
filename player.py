from gameManager import GameManager
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)

        self.name = 'Hunter'
        self.state = StateMachine()
        self.speed = 3
    
        self.images = {
            'idle': {
                'left': pg.image.load('Assets/Player/BoxLeft.png').convert_alpha(),
                'right': pg.image.load('Assets/Player/BoxRight.png').convert_alpha(),
                'up': pg.image.load('Assets/Player/BoxUp.png').convert_alpha(),
                'down': pg.image.load('Assets/Player/BoxDown.png').convert_alpha()
            },
            'walking': {
                'left': pg.image.load('Assets/Player/BoxLeft.png').convert_alpha(),
                'right': pg.image.load('Assets/Player/BoxRight.png').convert_alpha(),
                'up': pg.image.load('Assets/Player/BoxUp.png').convert_alpha(),
                'down': pg.image.load('Assets/Player/BoxDown.png').convert_alpha()
            },
            'running': {
                'left': pg.image.load('Assets/Player/BoxLeft.png').convert_alpha(),
                'right': pg.image.load('Assets/Player/BoxRight.png').convert_alpha(),
                'up': pg.image.load('Assets/Player/BoxUp.png').convert_alpha(),
                'down': pg.image.load('Assets/Player/BoxDown.png').convert_alpha()
            },
            'rolling': {
                'left': pg.image.load('Assets/Player/BoxLeft.png').convert_alpha(),
                'right': pg.image.load('Assets/Player/BoxRight.png').convert_alpha(),
                'up': pg.image.load('Assets/Player/BoxUp.png').convert_alpha(),
                'down': pg.image.load('Assets/Player/BoxDown.png').convert_alpha()
            }
        }

        self.image = self.images['idle']['down']
        self.rect = self.image.get_rect(topleft = [x*64, y*64])
        self.hitbox = self.rect.inflate(-12,-12)
        self.direction = pg.math.Vector2()
        self.iFrame = False

        self.rollTime = 0

        self.prevTick = 0
    
    def update(self):
        state = self.state.currentState.split()
        self.image = self.images[state[0]][state[1]]
        
        if state[0] == 'rolling':
            print(self.state.currentState, self.rollTime)
            if self.rollTime < 8:
                
                self.hitbox.x += (self.direction.x * 8)
                self.collision('horizontal')
                self.hitbox.y += (self.direction.y * 8)
                self.collision('vertical')
                self.iFrame = True  
                self.rollTime += 1
                
            elif self.rollTime == 8:
                
                self.rollTime = 0
                self.iFrame = False
                self.prevTick = pg.time.get_ticks()
                self.state.changeState('running', state[1])
        else:
            self.input()
            
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
    
            if state[0] == 'walking':
                self.hitbox.x += self.direction.x * self.speed
                self.collision('horizontal')
                self.hitbox.y += self.direction.y * self.speed
                self.collision('vertical')     
            elif state[0] == 'running':
                self.hitbox.x += self.direction.x * (self.speed* 1.5)
                self.collision('horizontal')
                self.hitbox.y += self.direction.y * (self.speed* 1.5)
                self.collision('vertical')    
        

        self.rect.x = self.hitbox.x-6
        self.rect.y = self.hitbox.y-6

    def collision(self, direction):                        
        
        if direction == "horizontal":
            for object in GameManager.obstacleSprites:
                if object.hitbox.colliderect(self.hitbox) and object != self:

                        
                    if self.direction.x > 0:
                        self.hitbox.right = object.hitbox.left
                        
                    if self.direction.x < 0:
                        self.hitbox.left = object.hitbox.right
                        
                        

        if direction == "vertical":
            for object in GameManager.obstacleSprites:
                if object.hitbox.colliderect(self.hitbox) and object != self:

                    if self.direction.y > 0:
                        self.hitbox.bottom = object.hitbox.top
                        
                    if self.direction.y < 0:
                        self.hitbox.top = object.hitbox.bottom
    
    def input(self):
        keys = pg.key.get_pressed()

        notMoving = True

        if keys[pg.K_a]:
            
            self.direction.x = -1
            self.state.changeState('walking', 'left')
            notMoving = False
            
        elif keys[pg.K_d]:
            
            self.direction.x = 1
            self.state.changeState('walking', 'right')
            notMoving = False
        else:
            notMoving = True
            self.direction.x = 0

        if keys[pg.K_w]:
            
            self.direction.y = -1
            self.state.changeState('walking', 'up')
            notMoving = False
            
        elif keys[pg.K_s]:
            
            self.direction.y = 1
            self.state.changeState('walking', 'down')
            notMoving = False
        elif notMoving == True:
            notMoving = True
            self.direction.y = 0
        
        if keys[pg.K_LSHIFT]:
            prevState = self.state.currentState.split()
            self.state.changeState('running', prevState[1])
        
        prevState = self.state.currentState.split()
        
        if keys[pg.K_SPACE] and (prevState[0] == 'walking' or prevState[0] == 'running') and pg.time.get_ticks() - self.prevTick >= 200:
            self.state.changeState('rolling', prevState[1])

        if notMoving == True:
            prevState = self.state.currentState.split()
            self.state.changeState('idle', prevState[1])
            


class StateMachine():
    def __init__(self):
        self.currentState = 'idle down'
        self.states = {
            'idle': {
                'left': 'idle left',
                'right': 'idle right',
                'up': 'idle up',
                'down': 'idle down',
            },
            'walking': {
                'left': 'walking left',
                'right': 'walking right',
                'up': 'walking up',
                'down': 'walking down',
            },
            'running': {
                'left': 'running left',
                'right': 'running right',
                'up': 'running up',
                'down': 'running down',
            },
            'rolling': {
                'left': 'rolling left',
                'right': 'rolling right',
                'up': 'rolling up',
                'down': 'rolling down',
            },
        }

    def changeState(self, toState, direction):
        self.currentState = self.states[toState][direction]
        