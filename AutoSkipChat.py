from time import sleep
from win32gui import FindWindow, GetWindowText, GetForegroundWindow, PostMessage
from win32con import WM_LBUTTONDOWN, WM_LBUTTONUP, MK_LBUTTON
from imagesearch import imagesearcharea
from pyautogui import moveTo
try:
    import vgamepad as vg
except Exception:
    print("Atención: No se encontró la API de los mandos virtuales, solo funcionará el modo de teclado y ratón")
    pass
from os import path

def mouse(hwnd, state):
    message = WM_LBUTTONDOWN if state else WM_LBUTTONUP
    PostMessage(hwnd, message, MK_LBUTTON, 0)

def PC_Mode(x1_izq, y1_sup, x1_der, y1_inf, x2_izq, y2_sup, x2_der, y2_inf, x, y, nombreAuto, nombreBurbuja):
    absolute_path = path.dirname(__file__)
    game = FindWindow("UnityWndClass", "Genshin Impact") # Conseguir el HWND
    print(game)
    posicionado = False  # Booleano para definir si el ratón está en su lugar
    comprobacionPos = 1  # Cada ciertas iteraciones nos aseguraremos que el ratón está bien posicionado
    iteraciones = 10  # Iteraciones de búsqueda rápida antes de pasar a búsqueda lenta si no se encuentra nada

    while True:  # Bucle infinito
        encontrado = False  # Por cada iteracion, definimos que no hemos encontrado nada

        ### Modo teclado y ratón
        # Buscamos el botón "Automático"
        # Si existe, hacer click en el lugar donde salen opciones
        pos = imagesearcharea(absolute_path + "\\" + nombreAuto + ".png", x1_izq, y1_sup, x1_der, y1_inf, 0.9948)
        if pos[0] != -1 and GetWindowText(GetForegroundWindow()) == "Genshin Impact":  # Si se encontró y estamos en Genshin Impact...
            if not posicionado:  # Se coloca el ratón cada ciertas iteraciones (y en la primera)...
                moveTo(x, y)  # En la posición genérica de opciones
                posicionado = True
                sleep(0.1)
            # Triple click
            mouse(game, True)
            sleep(0.1)
            mouse(game, False)
            mouse(game, True)
            sleep(0.1)
            mouse(game, False)
            mouse(game, True)
            sleep(0.1)
            mouse(game, False)
            encontrado = True
        else:
            # Buscamos la burbuja de selección de opciones
            # Si existe, hacer click en el lugar donde está la burbuja
            pos = imagesearcharea(absolute_path + "\\" + nombreBurbuja + ".png", x2_izq, y2_sup, x2_der, y2_inf, 0.994)
            if pos[0] != -1 and GetWindowText(GetForegroundWindow()) == "Genshin Impact":  # Si se encontró y estamos en Genshin Impact...
                if not posicionado:  # Se coloca el ratón cada ciertas iteraciones (y en la primera)...
                    moveTo(pos[0] + x2_izq, pos[1] + y2_sup)  # En el lugar donde aparezca la burbuja
                    posicionado = True
                    sleep(0.1)
                # Triple click
                mouse(game, True)
                sleep(0.1)
                mouse(game, False)
                mouse(game, True)
                sleep(0.1)
                mouse(game, False)
                mouse(game, True)
                sleep(0.1)
                mouse(game, False)
                encontrado = True

        if encontrado:  # Seguir el bucle de forma rápida
            sleep(0.001)
            iteraciones = 10  # Reiniciar iteraciones de búsqueda rápida
        else:  # Si no hay nada que skippear...
            if iteraciones > 0:  # Mientras la búsqueda rápida esté activada, hacer reinicio de bucle rápido
                sleep(0.1)
                iteraciones = iteraciones - 1
            else:  # Si se acabaron las iteraciones de búsqueda rápida, activar búsqueda lenta
                sleep(1.5)

        if comprobacionPos == 5:  # Cada ciertas iteraciones, reiniciamos el contador y reposicionamos el ratón (si está en modo skipear texto)
            comprobacionPos = 0
            if encontrado:
                posicionado = False
        comprobacionPos = comprobacionPos + 1

def DInput_Mode():
    absolute_path = path.dirname(__file__)
    game = FindWindow("UnityWndClass", "Genshin Impact") # Conseguir el HWND
    gamepad = vg.VDS4Gamepad() # Simulador de mando DS4/5
    print(game)
    iteraciones = 10 # Iteraciones de búsqueda rápida antes de pasar a búsqueda lenta si no se encuentra nada

    while True:  # Bucle infinito
        encontrado = False  # Por cada iteracion, definimos que no hemos encontrado nada
        ### Modo DInput
        # Buscamos el botón "Automático"
        # Si existe, simular botón X
        pos = imagesearcharea(absolute_path + "\\DInput_automatico.png", 1271, 996, 1609, 1021, 0.9948)
        if pos[0] != -1 and GetWindowText(GetForegroundWindow()) == "Genshin Impact": # Si se encontró y estamos en Genshin Impact...
            # Triple botón X
            gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            gamepad.update()
            sleep(0.1)
            gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            gamepad.update()
            gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            gamepad.update()
            sleep(0.1)
            gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            gamepad.update()
            gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            gamepad.update()
            sleep(0.1)
            gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            gamepad.update()
            encontrado = True
        else:
            # Buscamos la burbuja de selección de opciones
            # Si existe, hacer click en el lugar donde está la burbuja
            pos = imagesearcharea(absolute_path + "\\DInput_burbujaChat.png", 1283, 700, 1316, 798, 0.9948)
            if pos[0] != -1 and GetWindowText(GetForegroundWindow()) == "Genshin Impact": # Si se encontró y estamos en Genshin Impact...
                # Triple botón X
                gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
                gamepad.update()
                sleep(0.1)
                gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
                gamepad.update()
                gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
                gamepad.update()
                sleep(0.1)
                gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
                gamepad.update()
                gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
                gamepad.update()
                sleep(0.1)
                gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
                gamepad.update()
                encontrado = True

        if encontrado: # Seguir el bucle de forma rápida
            sleep(0.001)
            iteraciones = 10 # Reiniciar iteraciones de búsqueda rápida
        else: # Si no hay nada que skippear...
            if iteraciones > 0: # Mientras la búsqueda rápida esté activada, hacer reinicio de bucle rápido
                sleep(0.1)
                iteraciones = iteraciones - 1
            else: # Si se acabaron las iteraciones de búsqueda rápida, activar búsqueda lenta
                sleep(1.5)

if __name__ == "__main__":
    print("1 - Teclado y ratón (1080p)")
    print("2 - Mando PS4/5 [DInput] (1080p)")
    print("3 - Teclado y ratón (WXGA 85:48)")
    opcion = int(input("Escoge una opción: "))

    if opcion == 1:
        PC_Mode(50, 27, 92, 69, 1280, 712, 1318, 821, 1500, 700, "PC_automatico", "PC_burbujaChat")
        print("Asegúrate de ejecutar el programa en modo administrador para que funcione en modo teclado y ratón")
    elif opcion == 2:
        DInput_Mode()
    elif opcion == 3:
        PC_Mode(35, 19, 65, 49, 906, 507, 934, 585, 680, 384, "PC_automatico_alt", "PC_burbujaChat_alt")
        print("Asegúrate de ejecutar el programa en modo administrador para que funcione en modo teclado y ratón")