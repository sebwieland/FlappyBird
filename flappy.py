import bird
import pipe

pipes = []

def setup():
    size(800, 600)
    background(200)
    # global mybir d
    global score
    score = 0
    global mybird
    mybird = bird.Bird()
    mybird.show()


def draw():
    background(0)
    global score
    mybird.show()
    mybird.update()
    for i in reversed(range(len(pipes))):
        pipes[i].update()
        pipes[i].show()

        if pipes[i].passes(mybird):
            score += 1

        if pipes[i].hits(mybird):
            gameover()

        if pipes[i].offscreen():
            pipes.remove(pipes[i])

    if (frameCount) % 80 == 0:
        pipes.append(pipe.Pipe())

    if mybird.offscreen():
        gameover()

    showScores(score)

    # // touches is an list that contains the positions of all
    # // current touch points positions and IDs
    # // here we check if touches' length is bigger than one
    # // and set it to the touched var
    # touched = (touches.length > 0);

    # // if user has touched then make bird jump
    # // also checks if not touched before
    # if (touched && !prevTouched) {
    # bird.up();
    # }

    # // updates prevTouched
    # prevTouched = touched;


def keyPressed(event):
    if key == ' ':
            # print("key pressed")
        mybird.up()
    if key == ENTER:
        reset()
        print("reset game")


def gameover():
    print("GAMEOVER")
    # maxScore = max(score, maxScore);
    isOver = False
    noLoop()


def reset():
    del pipes[:]
    global score
    score=0
    mybird.reset()
    background(0)
    loop()


def showScores(score):
    textSize(32)
    text('score: ' + str(score), 1, 32)
    # text('record: ' + str(maxScore), 1, 64)
