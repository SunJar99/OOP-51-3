import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "My new app!"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    
    greeting_text = ft.Text("Hello!") 
    
    
    greeting_history = []
    
    history_text = ft.Text("Greeting history: ", style='bodyMedium')
    
    
    def on_button_click(e):
        name = name_input.value.strip()
        now = datetime.now()
        hour = now.hour
        if name:
            if 5 <= hour <= 12:
                greeting_text.value = f"Good morning, {name}!"
            elif 12 <= hour <= 18:
                greeting_text.value = f"Good afternoon, {name}!"
            elif 18 <= hour <= 21:
                greeting_text.value = f"Good evening, {name}!"
            else:
                greeting_text.value = f"Good night, {name}!"
            greet_button.text = 'Greet again'
            name_input.value = ''
            
            timestamp = datetime.now().strftime("Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp}: {name}")
            history_text.value = "Greeting history:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Please, type out your name!"
        page.update()
    
    name_input = ft.TextField(label="Type your name: ", autofocus=True, on_submit=on_button_click)
    
    def clear_history(e):
        greeting_history.clear()
        history_text.value = "Greeting history: "
        page.update()
        
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        
        page.update()
    
    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Change theme", on_click=toggle_theme)
    
    clear_button = ft.TextButton("delete the history", on_click=clear_history)
    
    greet_button = ft.ElevatedButton("greet", on_click=on_button_click)
    
    page.add(ft.Row([theme_button], alignment=ft.MainAxisAlignment.CENTER),
             greeting_text,
             name_input,
             greet_button,
             clear_button,
             history_text
    )
    
ft.app(target=main)

# ft.app(target=main, view=ft.WEB_BROWSER)



