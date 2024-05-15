import flet as ft

container = ft.Container

def main(page: ft.page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=numero.value))
        numero.value = ""
        page.update()

    numero = ft.TextField(hint_text="Ingrese el numero", expand=True)
    page.add(numero)
    binario = ft.ElevatedButton("Binario")
    octal = ft.ElevatedButton("Octal")
    hexa = ft.ElevatedButton("Hexadecimal")
    terna = ft.ElevatedButton("Ternario")
    cuat = ft.ElevatedButton("Cuaternario")
    botones = ft.Column()
    view=ft.Column(
        width=600,
        controls=[
            ft.Row(
                page.add(binario), page.add(octal), page.add(hexa), page.add(terna), page.add(cuat)
            ),
            botones,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

ft.app(target=main)
