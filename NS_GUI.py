from tkinter import *


def show_application():
    """Toon de GUI.

    Deze functie maakt een root-window. Daarna worden twee frames gemaakt. Deze worden exact op
    dezelfde plaats gepositioneerd met behulp van een grid en de sticky-parameter. Op het frame_start
    (het startscherm) staat één button: 'Toon vertrektijden'. Als je daarop klikt, wordt functie
    'frame_departures_tkraise' aangeroepen waarmee het andere frame (frame_departures) op de
    voorgrond komt te staan.
    """
    root = Tk()

    frame_start = Frame(master=root, pady=30, padx=30)
    frame_departures = create_departures_frame(root, frame_start)

    frame_start.grid(column=0, row=0, sticky="nsew")
    frame_departures.grid(column=0, row=0, sticky="nsew")

    btn_show_departures = Button(master=frame_start, text='Toon Vertrektijden', command=frame_departures.tkraise)
    btn_show_departures.pack()

    frame_start.tkraise()
    root.mainloop()


def create_departures_frame(root, frame_previous):
    """Deze functie maakt het 'vertrektijden'-frame.

    Breid de functie uit, en maak:
        Entry: invoer stationscode
        Button: toon de vertrektijden van het station met de ingevoerde code!
        Text: textarea om alle gevonden vertrektijden in te plaatsen
        Button: terug naar hoofdscherm

    De functie heeft twee parameters; root: de master waarop het frame geplaatst moet worden, en
    frame_previous: het frame wat op de voorgrond moet komen als je 'terug' gaat naar het vorige
    scherm (frame). Deze functie moet niet alles zelf, doen, maar maak ook gebruik van de (volgende)
    functie: 'show_departures'.
    """
    frame_departures = Frame(master=root, pady=40, padx=40)

    return frame_departures


def show_departures(txt_output, departure):
    """Deze functie vult het Text-widget.

    De functie heeft twee parameters:
        txt_output: de widget waar de vertrektijden in moeten komen
        departure: string voor de stationscode waarvan de vertrektijden getoond moeten worden

    Haal met behulp van de (volgende) functie, 'load_departures_NS' een lijst met vertrektijden op.
    Doorloop vervolgens deze lijst, en plaats alle vertrektijden in de Text-widget. leeg de widget
    voordat je nieuwe data plaatst, en zorg dat de applicatie niet crashed als er een niet bestaande
    stationscode invoert!
    """
    pass


def load_departures_NS(station):
    """Deze functie haal de vertrektijden op bij de NS-API.

    De functie heeft één parameter; de string voor de stationscode. Op basis hiervan moet je
    de URL van een NS-API aanroepen, waarbij je deze code meegeeft. Return een LIJST met
    vertrektijden!
    """
    pass