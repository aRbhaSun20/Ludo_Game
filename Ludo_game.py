import pygame
import random
import time
https://firebasestorag.googleapis.com/v0/b/beaming-gadget-351716.appspot.com/o/ajrccm.160.2.9804094.pdf?alt=media&token=161e94da-080d-48ca-9eaa-1b4a4eaa9298
https://firebasestorage.googleapis.com/v0/b/beaming-gadget-351716.appspot.com/o/mbe-19-01-017.pdf?alt=media&token=6b99bd42-e1de-48bb-b312-de2e890ed19e
    
pygame.init()

height = 820
width = 820

screen = pygame.display.set_mode((width, height))
background = pygame.image.load('pics/bg.jpg')
pygame.display.set_caption('Ludo')

BLACK = (0, 0, 0)
BLUE = (255, 255, 0)


score_font = pygame.font.Font('freesansbold.ttf', 20)
die_font = pygame.font.Font('freesansbold.ttf', 50)
p1_icon = []
p2_icon = []
p3_icon = []
p4_icon = []

for i in range(4):
    p1_icon.append(pygame.image.load('pics/p1.jpg'))
for i in range(4):
    p2_icon.append(pygame.image.load('pics/p2.jpg'))
for i in range(4):
    p3_icon.append(pygame.image.load('pics/p3.jpg'))
for i in range(4):
    p4_icon.append(pygame.image.load('pics/p4.jpg'))

change = 110

initial_positions = [
    [190, height-88, 0], [190, height-202, 0],
    [130, height-145, 0], [250, height-145, 0],
    [190, 88+change, 0], [190, 202+change, 0],
    [130, 145+change, 0], [250, 145+change, 0],
    [width - 220, 88+change, 0], [width - 220, 202+change, 0],
    [width - 155, 145+change, 0], [width - 280, 145+change, 0],
    [width - 220, height-88, 0], [width - 220, height-202, 0],
    [width - 155, height-145, 0], [width - 280, height-145, 0]
]

current_positions = [
    [190, height-88, 0], [190, height-202, 0],
    [130, height-145, 0], [250, height-145, 0],
    [190, 88+change, 0], [190, 202+change, 0],
    [130, 145+change, 0], [250, 145+change, 0],
    [width - 220, 88+change, 0], [width - 220, 202+change, 0],
    [width - 155, 145+change, 0], [width - 280, 145+change, 0],
    [width - 220, height-88, 0], [width - 220, height-202, 0],
    [width - 155, height-145, 0], [width - 280, height-145, 0]
]

board_position_out = [
    [320, 725], [320, 675], [320, 625], [320, 575], [320, 525],
    [270, 525], [220, 525], [170, 525], [120, 525],
    [120, 470], [120, 420], [120, 360],
    [170, 360], [220, 360], [270, 360], [320, 360],
    [320, 310], [320, 260], [320, 210], [320, 160],
    [370, 160], [420, 160], [470, 160],
    [470, 210], [470, 260], [470, 310], [470, 360],
    [520, 360], [570, 360], [620, 360], [670, 360],
    [670, 420], [670, 470],
    [620, 530], [570, 530], [520, 530], [470, 530],
    [470, 580], [470, 630], [470, 680], [470, 725],
    [420, 725], [370, 725], [320, 725]
]

board_position_in = [
    [395, 675], [395, 615], [395, 555],
    [175, 465], [235, 465], [295, 465],
    [400, 235], [400, 295], [400, 355],
    [620, 445], [560, 445], [500, 445]
]


def show_icons():

    for i in range(4):
        # r
        screen.blit(p1_icon[i], (current_positions[i]
                                 [0], current_positions[i][1]))
    # g
        screen.blit(p2_icon[i], (current_positions[i+4]
                                 [0], current_positions[i+4][1]))
    # b
        screen.blit(p3_icon[i], (current_positions[i+8]
                                 [0], current_positions[i+8][1]))
    # y
        screen.blit(p4_icon[i], (current_positions[i+12]
                                 [0], current_positions[i+12][1]))


max_outside_square = 43
max_inside_square = 3
num = ''


def throw_dice(player):
    # time.sleep(1)
    global num
    print(num)
    num = random.randint(1, 6)
    change_position(player, key, num)
    show_icons()
    if num != 6:
        player += 1
        return player
    else:
        return player


counter_token = [0, 0, 0, 0]


def die_score():
    # print(num)
    die_num = die_font.render(str(num), True, BLUE)
    screen.blit(die_num, (700, 50))


def change_position(player_num, token_num, die_num):
    global current_positions
    if current_positions[token_num + (player_num*4)][2] == 0:
        if die_num == 6:

            current_positions[token_num + (player_num*4)
                              ][0] = board_position_in[die_num-1][0]
            current_positions[token_num + (player_num*4)
                              ][1] = board_position_in[die_num-1][1]
            current_positions[token_num + (player_num*4)][2] += die_num
        else:
            print('Try Again Next Time')

    elif current_positions[token_num + (player_num*4)][2] >= max_outside_square:

        if die_num <= max_inside_square:

            current_positions[token_num + (player_num*4)
                              ][0] = board_position_in[current_positions[token_num + (player_num*4)][2] + (die_num - 1)][0]
            current_positions[token_num + (player_num*4)
                              ][1] = board_position_in[current_positions[token_num + (player_num*4)][2] + (die_num-1)][1]
            current_positions[token_num + (player_num*4)][2] += die_num
        else:
            print('Tken is greater than needed')

    else:

        current_positions[token_num + (player_num*4)
                          ][0] = board_position_out[die_num-1][0]
        current_positions[token_num + (player_num*4)
                          ][1] = board_position_out[die_num-1][1]
        current_positions[token_num + (player_num*4)][2] += die_num

    if current_positions[token_num + (player_num*4)][2] == (max_inside_square+max_outside_square):
        current_positions[token_num + (player_num*4)
                          ][0] = 1000
        current_positions[token_num + (player_num*4)
                          ][1] = 1000
        counter_token[player_num] += 1


key = 0

current_player = 0

running = True

screen.fill(BLACK)

screen.blit(background, (10, 10))

text_pos = [[50, 630], [50, 220], [750, 220], [750, 630]]
show_icons()


def show_scores():

    for i in range(len(text_pos)):
        score = str(counter_token[i])
        score_text = score_font.render(score, True, BLUE)
        screen.blit(score_text, (text_pos[i][0], text_pos[i][1]))


while running:

    # pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type is pygame.KEYDOWN:
            # get dice
            if event.key == pygame.K_SPACE:
                print('curr = ' + str(current_player))
                current_player = throw_dice(current_player)
                if current_player >= 4:
                    current_player = 0

            if event.unicode.isalpha():

                if chr(event.key) is 'a':
                    key = 0
                elif chr(event.key) is 'd':
                    key = 1
                elif chr(event.key) is 's':
                    key = 2
                elif chr(event.key) is 'w':
                    key = 3
                else:
                    print('enter valid key')

    # show_icons()
    show_scores()
    die_score()
    pygame.display.update()
