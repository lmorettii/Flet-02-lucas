import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    is_dark = True  # Inicializa o estado do tema

    # Campos
    peso = ft.TextField(label="Peso (kg)", width=200, keyboard_type=ft.KeyboardType.NUMBER)
    altura = ft.TextField(label="Altura (m)", width=200, keyboard_type=ft.KeyboardType.NUMBER)

    resultado = ft.Text(
        "Resultado aparecerá aqui",
        size=20,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREY_600,
    )

    titulo = ft.Text("🧮 Calculadora de IMC", size=24, weight=ft.FontWeight.BOLD)

    def calcular(e):
        try:
            p, h = float(peso.value), float(altura.value)

            if h == 0:  # evitar divisão por zero
                resultado.value, resultado.color = "❌ Altura não pode ser zero!", ft.Colors.RED
            else:
                imc = p / (h ** 2)

                if imc < 18.5:
                    resultado.value, resultado.color = f"Seu IMC é {imc:.2f}. Abaixo do peso.", ft.Colors.RED
                    if is_dark == False:
                        resultado.color = ft.Colors.RED_600
                    else:
                        resultado.color = ft.Colors.RED_200
                elif 18.5 <= imc <= 24.9:
                    resultado.value, resultado.color = f"Seu IMC é {imc:.2f}. Peso normal.", ft.Colors.GREEN
                    if is_dark == False:
                        resultado.color = ft.Colors.GREEN_600
                    else:
                        resultado.color = ft.Colors.GREEN_200
                elif 25 <= imc <= 29.9:
                    resultado.value, resultado.color = f"Seu IMC é {imc:.2f}. Acima do peso.", ft.Colors.YELLOW
                    if is_dark == False:
                        resultado.color = ft.Colors.ORANGE
                    else:
                        resultado.color = ft.Colors.YELLOW_200
                else:
                    resultado.value, resultado.color = f"Seu IMC é {imc:.2f}. Obesidade.", ft.Colors.RED
                    if is_dark == False:
                        resultado.color = ft.Colors.RED_600
                    else:
                        resultado.color = ft.Colors.RED_200

        except ValueError:
            resultado.value, resultado.color = "⚠️ Digite números válidos!", ft.Colors.RED

        page.update()

    def limpar(e):
        peso.value = altura.value = ""
        resultado.value, resultado.color = "Campos limpos! ✨", ft.Colors.BLUE
        page.update()

    def toggle_theme(e):
        nonlocal is_dark
        is_dark = not is_dark
        if is_dark:
            page.bgcolor = ft.Colors.BLACK
            toggle.icon = ft.Icons.WB_SUNNY_OUTLINED
            titulo.color = ft.Colors.WHITE
            peso.color = ft.Colors.WHITE
            altura.color = ft.Colors.WHITE
            peso.label_style = ft.TextStyle(color=ft.Colors.WHITE)
            altura.label_style = ft.TextStyle(color=ft.Colors.WHITE)
        else:
            page.bgcolor = ft.Colors.WHITE
            toggle.icon = ft.Icons.DARK_MODE
            titulo.color = ft.Colors.BLACK
            peso.color = ft.Colors.BLACK
            altura.color = ft.Colors.BLACK
            peso.label_style = ft.TextStyle(color=ft.Colors.BLACK)
            altura.label_style = ft.TextStyle(color=ft.Colors.BLACK)
        page.update()

    toggle = ft.IconButton(icon=ft.Icons.DARK_MODE, on_click=toggle_theme)

    # Interface
    page.add(
        ft.Column(
            [
                ft.Row([titulo, toggle], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                peso, altura,
                ft.Row(
                    [
                        ft.ElevatedButton("🧮 Calcular", on_click=calcular, width=150, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
                        ft.ElevatedButton("🧹 Limpar", on_click=limpar, width=150, bgcolor=ft.Colors.GREY, color=ft.Colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER, spacing=20,
                ),
                ft.Divider(),
                resultado
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)