from services.DataBase import DB

phrases = {
    "menu": {
        "ru": "Меню",
        "eng": "Menu"
    },
    "shop_map": {
        "ru": "Показать карту магазина",
        "eng": "Show the store map"
    },
    "call_admin": {
        "ru": "️Позвать администратора",
        "eng": "Call store administrator"
    },
    "call_cashier": {
        "ru": "Позвать кассира",
        "eng": "Call cashier"
    },
    "staff_request_sent": {
        "ru": "Запрос отправлен",
        "eng": "Request has been sent"
    },
    "cancel": {
        "ru": "Отменить",
        "eng": "Cancel"
    },
    "who_to_call": {
        "ru": "Кого вы хотите позвать?",
        "eng": "Who do you want to call"
    },
    "write_feedback": {
        "ru": "Напишите отзыв о боте",
        "eng": "Send feedback about this bot"
    },
    "thank_you_feedback": {
        "ru": "Спасибо за отзыв! Мы ценим ваше мнение",
        "eng": "Thanks for the feedback! We appreciate your feedback"
    },
    "send_name": {
        "ru": "Отправить название",
        "eng": "Send the product name"
    },
    "call_staff": {
        "ru": "‍Позвать сотрудника магазина",
        "eng": "Call a store employee"
    },
    "leave_feedback": {
        "ru": "Оставить отзыв о боте",
        "eng": "Leave feedback about bot"
    },
    "request_information_about_product": {
        "ru": "Узнать о наличии товара у сотрудников",
        "eng": "Request information about presence of a product"
    },
    "place_order": {
        "ru": "Заказать отсутствующую продукцию",
        "eng": "Order absent product"
    },
    "wrong_tag": {
        "ru": "Сообщить о неправильном ценнике",
        "eng": "Inform about the wrong price tag"
    },
    "select_menu": {
        "ru": "Что вас интересует?",
        "eng": "Select an option"
    },
    "greeting": {
        "ru": 'Привет! Я чат бот магазина "Пятёрочка" в г. Иннополис',
        "eng": 'Hello! I am the chat bot of "Pyaterochka" shop in the Innopolis city'
    },
    "send_name_and_photo": {
        "ru": "Отправить фото и название",
        "eng": "Send photo and the product name"
    },
    "select_option": {
        "ru": "Выберите опцию",
        "eng": "Select an option"
    },
    "enter_product_name": {
        "ru": "Напишите название продукта",
        "eng": "What is the product name?"
    },
    "enter_product_photo": {
        "ru": "Отправте фотографию продукта",
        "eng": "Send a picture of a product"
    },
    "request_sent": {
        "ru": "Ваш запрос отправлен сотрудникам магазина",
        "eng": "Your request was sent to the store"
    },
    "absent_product": {
        "ru": "Данного товара сейчас нет в наличии",
        "eng": "This product isn't currently in the shop"
    },
    "present_product": {
        "ru": "Данный товар есть в наличии\nЖдём вас в пятёрочке!",
        "eng": "This product is in the shop\nWaiting for you in Pyaterochka!"
    },
    "can_not_order": {
        "ru": "Мы приняли ваш заказ",
        "eng": "Your order was confirmed"
    },
    "can_order": {
        "ru": "Ваш заказ подтвердили, ожидайте поступления в ближайшее время",
        "eng": "Your order was accepted\nIt will be delivered to the shop as soon as possible!"
    },
    "thank_fix_tag": {
        "ru": "Спасибо за отзыв! Мы решим проблему с ценником в ближайшее время",
        "eng": "Thank you for your feedback! We will fix this issue as soon as possible"
    },
    "send_wrong_tag": {
        "ru": "Пожалуйста, пришлите фотографию неправильного ценника",
        "eng": "Please, send the picture of a wrong tag"
    },
    "send_name_and_barcode": {
        "ru": "Отправить штрих код и название",
        "eng": "Send barcode and the product name"
    },
    "enter_product_barcode": {
        "ru": "Отправьте фото штрих кода продукта",
        "eng": "Send a photo of a barcode of the product"
    }
}


def translate(key: str, language: str):
    return phrases[key][language]


def extract_language_and_update_if_not_present(update, context):
    if "language" not in context.user_data:
        language_preference = DB('language_selection', chat_id="TEXT", language="TEXT")
        language = language_preference.get_items(chat_id=update.message.chat_id)
        if len(language) == 0:
            language_preference.add_item(chat_id=update.message.chat_id, language="ru")
            context.user_data["language"] = "ru"
        else:
            context.user_data["language"] = language[0][1]

    return context.user_data["language"]
