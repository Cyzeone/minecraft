from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
window.size = (1280, 720)  # largura x altura
app = Ursina()
player = FirstPersonController()
Sky()

pause_text = Text(
    text='',
    origin=(0,0),
    scale=2,
    color=color.azure,
    background=False,
)

game_paused = False

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j,0,i),
            texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

def input(key):
    global game_paused

    if key == 'p':
        if not game_paused:
            game_paused = True
            player.enabled = False
            pause_text.text = 'Jogo Pausado\nPressione P para continuar'
        else:
            game_paused = False
            player.enabled = True
            pause_text.text = 'Jogo Retomado'
            invoke(setattr, pause_text, 'text', '', delay=2)

    if key == 'f':
        if not window.fullscreen:
            window.fullscreen = True
        else:
            window.fullscreen = False

    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='grass.png', parent=scene, origin_y=0.5)
                boxes.append(new)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)

app.run()
    
    