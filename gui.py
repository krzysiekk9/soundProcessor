import PySimpleGUI as sg
import soundProcessor

sg.theme('DarkTeal1')

file_choose = [
    [
        sg.Text("Choose file *.wav"),
        sg.In(size=(35,1), enable_events=True, key="-FILE_"),
        sg.FileBrowse(),
        sg.Button(button_text="Load")
    ]
]

pitch_slider = [
    [
        sg.Text("Change pitch"),
        sg.Slider(range=(-10,10), orientation='vertical', size=(5,20), default_value=0, key="-PITCH-"),
        sg.Button(button_text="Change pitch")
    ]
]

trim_slider = [
    [
        sg.Text('trim'),
        sg.Slider(range=(0,20), orientation='vertical', size=(5,20), default_value=0, key="-TRIM-"),
        sg.Button(button_text="Trim")
    ]
]

filter_choise = [
    [
        sg.Text('Choose filter'),
        sg.Button(button_text="High-pass"),
        sg.Button(button_text="Low-pass")
    ]
]

layout = [
    [
        [
            sg.Column(file_choose),
        ],
        [
            sg.Column(pitch_slider),
            sg.Column(trim_slider),
        ],
        [
            sg.Column(filter_choise),
        ],
        sg.Button(button_text="Exit")
    ]
]

window = sg.Window("Sound processor", layout, element_justification='c')
event, values = window.Read()

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    elif event == "Load":
        a = window.read()
        b = a[1]
        c = str(b).split("'")
        path = c[3]
        y, sr = soundProcessor.load_file(path)

    elif event == "Change pitch":
        pitch_value = values["-PITCH-"]
        soundProcessor.shift_pitch(y, sr, pitch_value)

    elif event == "Trim":
        trim_value = values["-TRIM-"]
        soundProcessor.trim(y, sr, trim_value)

    elif event == "High-pass":
        soundProcessor.f_high(y, sr)

    elif event == "Low-pass":
        soundProcessor.f_low(y, sr)

window.close()