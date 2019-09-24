# Keri-Dressup-RenPy-Template
<<<<<<< HEAD
Images and code for a character creation screen based off of the sprite **Keri** created by **Konett**.
=======
Images and code for a character creation screen based off of the sprite 'Keri' created by Konett. Image modifications, interface, and code created by LunaLucid/Namastaii. If you use this sprite, please credit Konett.
>>>>>>> 9e8eb0d35b941ffbdec47fa7017f1a2d0ebc8381

_Modifications created by LunaLucid/Namastaii. If you use this sprite, please credit Konett._

Konett: https://konett.itch.io/

Konett's Lemma Soft thread: https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=28840&hilit=konett


**Keri is CC-BY license**

You are not required to credit me for the code template or manipulated images but if you'd like to do so you can credit LunaLucid https://lunalucid.itch.io/

This template was created with the Ren'Py Engine

_Note: Not all Keri assets were included. You can download the original PSD at the Lemma Soft link above._
___
In **dressup.rpy**, there is a Ren'Py language version of the character live composite and a Python version just so you can see how each one works. In this case, they're almost the same.

The images for the sprite layers are quite large so you'll need to factorscale the layers in livecomposite or continue to display with **zoom**.

#### Default variables:
```python
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
```

#### LiveComposite of the character:

```python
image keri = LiveComposite(
    (467, 946),
    (0, 0), "Create_Character/Base/base[skin_color].png",
    (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
    (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
    (0, 0), "Create_character/Eyebrows/eyebrows[skin_color]_1.png",
    (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
    (0, 0), "Create_character/Mouth/mouth[skin_color]_1.png",
    (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
)
```

When we name our image paths like this, we allow a variable to change the file according to which items we choose.

In this line:

`"Create_character/Hair/hair[hairstyle]_[hair_color].png"`

We are passing two variables to the path. **hairstyle** and **hair_color**
By default, the game should be displaying the image located at **"Create_character/Hair/hair1_1.png"**

The file will change when we interact with buttons that increase, decrease, or assign the variable a new value.

Pressing a button/hotspot associated with this action:

`action SetVariable("hairstyle", 2)`

will change the path to **"Create_character/Hair/hair2_1.png"** etc

During game, you can also change these variables in the script with the following syntax:
`$ top_choice = 3`
