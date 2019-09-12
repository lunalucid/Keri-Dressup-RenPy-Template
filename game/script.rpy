image keri = DynamicDisplayable(keri_sprite)
image school = "Modern_School.png"
label start:
    call screen dress_keri
    scene school
    $ quick_menu = True
    show keri:
        pos(800, 120)
        zoom 0.5
    "You've created your look!"
    return
