init:
    default skin_color = 1
    default hairstyle = 1
    default hair_color = 1
    default eyes = 1
    default eye_color = 1
    default top_choice = 1
    default bottom_choice = 1
    default top_style = 1
    default top_style_max = 6
    default bottom_style = 1
    default bottom_style_max = 6

init python:
    def keri_sprite(st, at):
        return LiveComposite(
            (467, 946),
            (0, 0), "Create_Character/Base/base{}.png".format(skin_color),
            (0, 0), "Create_character/Bottoms/bottom{}_{}.png".format(bottom_choice, bottom_style),
            (0, 0), "Create_character/Tops/top{}_{}.png".format(top_choice, top_style),
            (0, 0), "Create_character/Eyebrows/eyebrows{}_1.png".format(skin_color),
            (0, 0), "Create_character/Eyes/eyes{}_{}.png".format(eyes, eye_color),
            (0, 0), "Create_character/Mouth/mouth{}_1.png".format(skin_color),
            (0, 0), "Create_character/Hair/hair{}_{}.png".format(hairstyle, hair_color),
        ),.1

screen dress_keri():
    modal True

    imagemap:
        ground "Dressup_Screen/background.png"
        idle "Dressup_Screen/idle.png"
        hover "Dressup_Screen/hover.png"
        selected_idle "Dressup_Screen/selected.png"
        selected_hover "Dressup_Screen/selected.png"

        ##Skin Color##
        hotspot(267, 112, 80, 80) action SetVariable("skin_color", 1)
        hotspot(364, 112, 80, 80) action SetVariable("skin_color", 2)
        hotspot(461, 112, 80, 80) action SetVariable("skin_color", 3)
        hotspot(558, 112, 80, 80) action SetVariable("skin_color", 4)
        hotspot(655, 112, 80, 80) action SetVariable("skin_color", 5)

        ##Hairstyle##
        hotspot(267, 233, 80, 80) action SetVariable("hairstyle", 1)
        hotspot(364, 233, 80, 80) action SetVariable("hairstyle", 2)
        hotspot(461, 233, 80, 80) action SetVariable("hairstyle", 3)
        hotspot(558, 233, 80, 80) action SetVariable("hairstyle", 4)
        hotspot(655, 233, 80, 80) action SetVariable("hairstyle", 5)

        ##Hair Color##
        hotspot(267, 352, 80, 80) action SetVariable("hair_color", 1)
        hotspot(364, 352, 80, 80) action SetVariable("hair_color", 2)
        hotspot(461, 352, 80, 80) action SetVariable("hair_color", 3)
        hotspot(558, 352, 80, 80) action SetVariable("hair_color", 4)
        hotspot(655, 352, 80, 80) action SetVariable("hair_color", 5)
        hotspot(267, 445, 80, 80) action SetVariable("hair_color", 6)
        hotspot(364, 445, 80, 80) action SetVariable("hair_color", 7)
        hotspot(461, 445, 80, 80) action SetVariable("hair_color", 8)
        hotspot(558, 445, 80, 80) action SetVariable("hair_color", 9)
        hotspot(655, 445, 80, 80) action SetVariable("hair_color", 10)
        hotspot(267, 538, 80, 80) action SetVariable("hair_color", 11)
        hotspot(364, 538, 80, 80) action SetVariable("hair_color", 12)
        hotspot(461, 538, 80, 80) action SetVariable("hair_color", 13)
        hotspot(558, 538, 80, 80) action SetVariable("hair_color", 14)
        hotspot(655, 538, 80, 80) action SetVariable("hair_color", 15)

        ##Eyes##
        hotspot(267, 675, 80, 80) action SetVariable("eyes", 1)
        hotspot(364, 675, 80, 80) action SetVariable("eyes", 2)
        hotspot(461, 675, 80, 80) action SetVariable("eyes", 3)

        ##Eye Color##
        hotspot(267, 794, 80, 80) action SetVariable("eye_color", 1)
        hotspot(364, 794, 80, 80) action SetVariable("eye_color", 2)
        hotspot(461, 794, 80, 80) action SetVariable("eye_color", 3)
        hotspot(558, 794, 80, 80) action SetVariable("eye_color", 4)
        hotspot(655, 794, 80, 80) action SetVariable("eye_color", 5)
        hotspot(267, 887, 80, 80) action SetVariable("eye_color", 6)
        hotspot(364, 887, 80, 80) action SetVariable("eye_color", 7)
        hotspot(461, 887, 80, 80) action SetVariable("eye_color", 8)
        hotspot(558, 887, 80, 80) action SetVariable("eye_color", 9)
        hotspot(655, 887, 80, 80) action SetVariable("eye_color", 10)

        ##Top Choice##
        hotspot(952, 112, 80, 80) action SetVariable("top_choice", 1)
        hotspot(1050, 112, 80, 80) action SetVariable("top_choice", 2)
        hotspot(1146, 112, 80, 80) action SetVariable("top_choice", 3)
        hotspot(1243, 112, 80, 80) action SetVariable("top_choice", 4)
        hotspot(1340, 112, 80, 80) action SetVariable("top_choice", 5)

        ##Bottom Choice##
        hotspot(952, 233, 80, 80) action SetVariable("bottom_choice", 1)
        hotspot(1050, 233, 80, 80) action SetVariable("bottom_choice", 2)
        hotspot(1146, 233, 80, 80) action SetVariable("bottom_choice", 3)
        #hotspot(1243, 233, 80, 80) action SetVariable("bottom_choice", 4)
        #hotspot(1340, 233, 80, 80) action SetVariable("bottom_choice", 5)

        ##Top Style##
        hotspot(1231, 522, 88, 77) action If(top_style > 1, SetVariable("top_style", top_style - 1), SetVariable("top_style", 1))
        hotspot(1800, 522, 88, 77) action If(top_style < top_style_max, SetVariable("top_style", top_style + 1), SetVariable("top_style", top_style_max))

        ##Bottom Style##
        hotspot(1231, 853, 88, 77) action If(bottom_style > 1, SetVariable("bottom_style", bottom_style - 1), SetVariable("bottom_style", 1))
        hotspot(1800, 853, 88, 77) action If(bottom_style < bottom_style_max, SetVariable("bottom_style", bottom_style + 1), SetVariable("bottom_style", bottom_style_max))

        ##Continue##
        hotspot(1661, 14, 236, 80) action Return()

    add "keri":
        pos(1300, 120)
        zoom 0.5
