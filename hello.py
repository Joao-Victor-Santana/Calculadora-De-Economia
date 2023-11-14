import PySimpleGUI as sg

sg.theme('DarkBlue3')
sg.set_options(font=("Helvetica", 20))  

layout = [
    [sg.Text('Meta de Economia:', size=(20, 1)), sg.Input(key='meta', size=(10, 1))],
    [sg.Text('Economia por Mês:', size=(20, 1)), sg.Input(key='economia_por_mes', size=(10, 1))],
    [sg.Button('Calcular')],
    [sg.Text('', size=(30, 1), key='resultado')],
]


screen_width, screen_height = sg.Window.get_screen_size()
center_x, center_y = screen_width / 2, screen_height / 2

janela = sg.Window('Calculadora de Economia', layout, finalize=True, location=(center_x - 300, center_y - 220))  
janela.Maximize()

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        meta = float(valores['meta'])
        economia_por_mes = float(valores['economia_por_mes'])

        if economia_por_mes <= 0:
            janela['resultado'].update('Por favor, insira uma economia por mês válida.')
        else:
            meses_para_atingir_meta = meta / economia_por_mes
            janela['resultado'].update(f'Levará {int(meses_para_atingir_meta)} meses para atingir a meta.')

janela.close()
