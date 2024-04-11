import flet

def main(page: flet.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    page.add(flet.Text("Hola, esto es una demo Flet para la asignatura de SI"))

    txt_number = flet.TextField(value="0", text_align=flet.TextAlign.RIGHT, width=100)

    def boton_menos(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def boton_mas(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        flet.Row(
            [
                flet.IconButton(flet.icons.REMOVE, on_click=boton_menos),
                txt_number,
                flet.IconButton(flet.icons.ADD, on_click=boton_mas),
            ],
            alignment=flet.MainAxisAlignment.CENTER,
        )
    )

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(flet.Text(f"Hello, {name}!"))

    txt_name = flet.TextField(label="Your name")
    page.add(txt_name, flet.ElevatedButton("Say hello!", on_click=btn_click))

#flet.app(main)
#flet.app(main,view=flet.WEB_BROWSER)