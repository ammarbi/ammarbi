
from flet import *
import webbrowser

def main(page:Page):
    page.window.width =  390
    page.window.height = 720
    page.window.top = 5
    page.window.left = 960
    page.bgcolor = 'red'

    def pro(r):
        webbrowser.open('https://www.googel.com/search?q=' + g.value)


    g = TextField(label='ابحث عن اي شي في جوجل', icon=icons.SEARCH)
    page.add(
        AppBar(
            bgcolor='black',
            title= Text('Ammar_Bi [1v.0] Welcome....'),
            center_title= True,
            color= 'red',
        ),
        Row([
            Image(src='gog.jpeg',border_radius=10)
        ],alignment=MainAxisAlignment.CENTER),
        Row([

            Text('اكتب اي شي للتصفح', rtl=True, color=colors.BLACK, size=22)
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Text('بحث',rtl=True, color=colors.BLACK, size=22),
            g
        ], alignment=MainAxisAlignment.CENTER,rtl=True),

        Row([
            ElevatedButton(text='بحث',icon=icons.SEARCH_OFF_SHARP,bgcolor='red',on_click=pro)
        ],alignment=MainAxisAlignment.CENTER)

    )
    page.update()
app(main)
