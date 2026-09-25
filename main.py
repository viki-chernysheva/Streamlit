import streamlit as st
import pandas as pd
import base64

# выбор места
# бюджет
# отели и маршрут
# тип отдыха (тур)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


try:
    bin_str = get_base64_of_bin_file('fly.png')

    st.html(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .st-key-booking {{
        background-color: #ffffff !important;
        padding: 40px !important;
        border-radius: 24px !important;
        box-shadow: 0px 12px 40px rgba(0,0,0,0.25) !important;
        max-width: 600px !important;
        margin: 40px auto !important;
        border: none !important;
    }}

    .st-key-booking p,
    .st-key-booking label,
    .st-key-booking h1,
    .st-key-booking h2,
    .st-key-booking h3 {{
        color: #111827 !important;
        font-weight: 500 !important;
    }}
    </style>
    """)

except FileNotFoundError:
    st.warning("Файл с фоновым изображением не найден. Проверь имя файла.")

with st.container(border=True, key="booking"):

    st.title("🌏 Собери свое путешествие")
    country = st.selectbox(
        "Куда поедем?",
        [
            "Франция",
            "Италия",
            "Россия"
        ]
    )

    # Города для каждой страны
    cities = {
        "Франция": [
            [48.8566, 2.3522],  # Париж
        ],

        "Италия": [
            [41.8919, 12.5113],  # Рим
        ],

        "Россия": [
            [55.7558, 37.6173],  # Москва
        ]
    }

    map_data = pd.DataFrame(
        cities[country],
        columns=["lat", "lon"]
    )

    st.map(map_data)

    budget = st.slider(
        "Какой бюджет?",
        10000,
        500000,
        100000,
        5000
    )

    type_of_trip = st.selectbox(
        "Кукой тип отдыха предпочитаешь?",
        [
            "Море",
            "История",
            "Еда"
        ]
    )

    button = st.button("Предложить путешествие")

    if button:
        if budget < 100000:
            level = "Эконом"
        elif budget > 300000:
            level = "Люкс"
        else:
            level = "Стандарт"
        st.info(f"{country} | {type_of_trip} | {level}")
        if country == "Франция":

            if type_of_trip == "Еда":
                st.success(
                    "🥐 Французская кухня: луковый суп, "
                    "утиная ножка конфи, киш Лорен, крем-брюле."
                )

            elif type_of_trip == "Море":
                st.success(
                    "🌊 Морской отдых: Ницца, Канны, "
                    "Лазурный берег и Биарриц."
                )

            elif type_of_trip == "История":
                st.success(
                    "🏰 Исторический отдых: замки Луары, "
                    "Мон-Сен-Мишель и музеи Парижа."
                )

        elif country == "Италия":

            if type_of_trip == "Еда":
                st.success(
                    "🍕 Итальянская кухня: пицца, паста "
                    "карбонара, лазанья и джелато."
                )

            elif type_of_trip == "Море":
                st.success(
                    "🌊 Морской отдых: Амальфитанское побережье, "
                    "Лигурия и пляжи Сардинии."
                )

            elif type_of_trip == "История":
                st.success(
                    "🏛️ Исторический отдых: Рим, Колизей "
                    "и Флоренция."
                )

        elif country == "Россия":

            if type_of_trip == "Еда":
                st.success(
                    "🥞 Русская кухня: блины с икрой, "
                    "пельмени, борщ и бефстроганов."
                )

            elif type_of_trip == "Море":
                st.success(
                    "🌊 Морской отдых: Сочи, Анапа "
                    "и побережье Калининграда."
                )

            elif type_of_trip == "История":
                st.success(
                    "🏛️ Исторический отдых: Эрмитаж, "
                    "Москва и города Золотого кольца."
            )
        st.subheader("🌟 Что дальше?")

        col1, col2 = st.columns(2)

        with col1:
            st.link_button(
                "🏨 Подобрать отель",
                "https://ostrovok.ru/hotel/",
                use_container_width=True
            )

        with col2:
            st.link_button(
                "✈️ Подобрать маршрут",
                "https://www.aviasales.ru/",
                use_container_width=True
            )