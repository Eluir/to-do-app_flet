from flet import *


def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    categories_card = Row(
        scroll='auto'

    )
    categories = ['trampo', 'familia','amigos']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
            border_radius=20,
            padding=15,
            bgcolor=BG,
            height=110,
            width=170,
            content=Column(
                controls=[
                    Text('40 Tasks'),
                    Text(category),
                    Container(
                        width=160,
                        height=5,
                        bgcolor='white12',
                        padding=padding.only(right=i*30),
                        content=Container(
                            bgcolor=PINK
                        )
                    )
                ]
            )
            )
        )

    first_page_contents=Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(
                                icons.MENU
                            )
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                            ]
                        )
                    ]
                ),
            Container(height=20),
            Text(
                value='E aí, meu chapa!'
            ),
            Text(
                value='CATEGORIAS'
            ),
            Container(
                padding=padding.only(bottom=20, top=10),
                content=categories_card
            )
            ]
            
        )
    )
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=5
                ),
                content=Column(
                    controls=[first_page_contents]
                )
            )
        ]
    )

    container = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    page.add(container)


app(target=main)
