from nicegui import ui

def greet():
    ui.notify(f'Hello, {name.value}!')

with ui.column().classes('w-full items-center p-8'):
    ui.label('My Desktop App').classes('text-3xl font-bold')

    name = ui.input('Enter your name')

    ui.button('Submit', on_click=greet)

if __name__ == '__main__':
    ui.run(
        native=True,
        window_size=(1000, 700),
        reload=False
    )