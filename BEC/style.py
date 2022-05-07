# текст всплывающего окна
alert_text = "Некоторые разделы находятся в разработке.\n Приновим извинения за неудобства!"
info_text = "Версия проекта: 2.3 \nПоследнее обновление: 07.05.2022 \n Чтобы оставить отзыв, пишите на почту: \n " \
            "                 zintaise@gmail.com \n Список обновлений: changelog.txt"

db_ex = [[2, '04.05.2022 21:44', 'Nevskogo 15 B', 'img\\trans_2.jpg',
          'Kovalevski A.P.'],
         [1, '30.04.2022 9:36', 'Gukova 3', 'img\\lep_1.jpg',
          'Anastasyan B.V.'],
         [12, '06.03.2021 13:25', 'Nevskogo 374 A', 'img\\el_12.jpg',
          'Kovalevski A.P.'],
         [31, '01.02.2022', 'Pushkina 133', 'img\\el_31.jpg', 'Dulova M.D.']]
# ----------------------------------------------------------------
# фон главного окна (+ кнопки данных)
background = "background-color: rgb(240, 250, 255);"

# заголовок title heading
logo = "QLabel{font-size: 20pt;" \
       "font-weight: bold;}"

# данные должностного лица
label_info = "QLabel{font-size: 14pt;}"

# заголовок
q_text_style = "QLabel{font-size: 15pt;" \
               "background-color: rgb(210, 230, 255);}"

# кнопка входа
enter_button = "QPushButton{" \
               "background-color:rgb(220, 220, 220);" \
               "font-size:30pt;" \
               "background-color:rgb(0, 128, 255);" \
               "font-weight:bold;}"

# кнопки сортировки данных
sort_button = "QPushButton{" \
               "background-color:rgb(220, 220, 220);" \
               "font-size:10pt;" \
               "background-color:rgb(0, 128, 255);" \
               "font-weight:bold;}"

# ----------------------------------------------------------------------
# кнопки главного экрана
logo_sign = "QLabel{font-size: 15pt;}"

main_buttons = "QPushButton{font-size: 13pt;" \
               "background-color: rgb(129,195,250);" \
               "font-weight: bold;}" \
               "QPushButton:hover{background-color: rgb(1,138,190);}" \
               "QPushButton:onclick{background-color: rgb(135, 206, 200);}"

# кнопка инфо
info_button = "QPushButton{font-weight: bold;" \
              "background-color: rgb(63,168,255);" \
              "width: 50px;" \
              "height: 20px;}"

# главное окно
main_window = "background: rgb(254,245,238);"
