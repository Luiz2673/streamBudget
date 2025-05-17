import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from services import services_list
from io import BytesIO
from datetime import datetime
import os


image = Image.open("./Modelo de Orçamento Stream Budget.png")
align = ImageDraw.Draw(image)

st.set_page_config(page_title="⚙️Stream Budget", layout='wide')
st.markdown("<h1 style='text-align: center; color: white;'>Bem Vindo(a) ao Stream Budget📌</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white;'>Preencha os Campos no Formulário e Gere um Orçamento em Segundos❗</h6>", unsafe_allow_html=True)

font_client = ImageFont.truetype('./HankenGrotesk-Light.ttf', 25)
font_os = ImageFont.truetype('./HankenGrotesk-Light.ttf', 67)
font_date = ImageFont.truetype('./HankenGrotesk-Light.ttf', 50)

def phone_format(number):
    number = ''.join(filter(str.isdigit, number))
    if len(number) == 11:
        return f"({number[:2]}) {number[2:6]}-{number[6:]}"
    elif len(number) == 10:
        return f"({number[:2]}) {number[2:6]}-{number[6:]}"
    elif len(number) == 9:
        return f"(11) {number[:5]}-{number[5:]}"
    else:
        return number

def replace_void(option, quantity):
    if option == placeholder:
        return "***********************************", 1
    return option, quantity

def get_service_data(service_name, quantity):
    for service in services_list:
        if service["serviceName"] == service_name:
            unit_price = service["price"]
            return service_name, f"R$ {unit_price:.2f}", str(quantity), f"R$ {unit_price * quantity:.2f}"
    return service_name, "R$ 0.00", str(quantity), "R$ 0.00"

def get_next_os_number(file_path="os_counter.txt"):
    # Se o arquivo não existir, cria com valor 1
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("1")
        return 1

    with open(file_path, "r") as f:
        number = int(f.read().strip())

    # Incrementa e salva de volta
    next_number = number + 1
    with open(file_path, "w") as f:
        f.write(str(next_number))

    return number



with st.sidebar:
    st.header("✏️Formulário")
    customer = st.text_input('Nome do Cliente:', max_chars=35)
    email = st.text_input('E-mail do Cliente:', max_chars=35)
    phone = st.text_input('Celular do Cliente:', max_chars=15)
    if phone and not phone.isdigit():
        st.warning("Digite apenas números no campo de Celular")
    phone_formated = phone_format(phone)

    align.text((250, 727), customer, fill='black', font=font_client, stroke_width=0.1)
    align.text((250, 766), email, fill='black', font=font_client, stroke_width=0.1)
    align.text((250, 806), phone_formated, fill='black', font=font_client, stroke_width=0.1)

    service_names = [s["serviceName"] for s in services_list]
    placeholder = "Selecione um Serviço"
    select_options = [placeholder] + service_names
    st.sidebar.subheader("Selecione até 3 Serviços:")

    option1 = st.selectbox("Serviço 1", select_options, key="serv1")
    quant1 = st.number_input("Quantidade", min_value=1, value=1, key="qtd1")

    option2 = None
    quant2 = None
    option3 = None
    quant3 = None

    work1, unit1, qtd1, total1 = get_service_data(*replace_void(option1, quant1))

    if option1 != placeholder:
        option2 = st.selectbox("Serviço 2", select_options, key="serv2")
        quant2 = st.number_input("Quantidade", min_value=1, value=1, key="qtd2")
        work2, unit2, qtd2, total2 = get_service_data(*replace_void(option2, quant2))

        if option2 != placeholder:
            option3 = st.selectbox("Serviço 3", select_options, key="serv3")
            quant3 = st.number_input("Quantidade", min_value=1, value=1, key="qtd3")
            work3, unit3, qtd3, total3 = get_service_data(*replace_void(option3, quant3))
        else:
            work3, unit3, qtd3, total3 = "***********************************", "R$ 0.00", "0", "R$ 0.00"
    else:
        work2, unit2, qtd2, total2 = "***********************************", "R$ 0.00", "0", "R$ 0.00"
        work3, unit3, qtd3, total3 = "***********************************", "R$ 0.00", "0", "R$ 0.00"
    processar = st.button("Processar Orçamento ✅")
if processar:
    # Preencher os dados dos serviços
    align.text((311, 1033), work1, fill='black', font=font_client, stroke_width=0.1)
    align.text((818, 1033), unit1, fill='black', font=font_client, stroke_width=0.1)
    align.text((1012, 1033), qtd1, fill='black', font=font_client, stroke_width=0.1)
    align.text((1122, 1033), total1, fill='black', font=font_client, stroke_width=0.1)
    align.text((311, 1185), work2, fill='black', font=font_client, stroke_width=0.1)
    align.text((818, 1185), unit2, fill='black', font=font_client, stroke_width=0.1)
    align.text((1012, 1185), qtd2, fill='black', font=font_client, stroke_width=0.1)
    align.text((1122, 1185), total2, fill='black', font=font_client, stroke_width=0.1)
    align.text((311, 1337), work3, fill='black', font=font_client, stroke_width=0.1)
    align.text((818, 1337), unit3, fill='black', font=font_client, stroke_width=0.1)
    align.text((1012, 1337), qtd3, fill='black', font=font_client, stroke_width=0.1)
    align.text((1122, 1337), total3, fill='black', font=font_client, stroke_width=0.1)
    # Número da Ordem de Serviço:
    os_number = get_next_os_number()
    align.text((1122, 729), f"{os_number:02}", fill='black', font=font_os, stroke_width=0.1)

    # Data do Orçamento:
    current_date = datetime.now().strftime("%d/%m/%Y")
    align.text((1000, 433), current_date, fill='black', font=font_date, stroke_width=0.1)

    # Calcular valor total de todos os serviços
    def convert_to_float(value):
        return float(value.replace("R$ ", ""))
    total_value = convert_to_float(total1) + convert_to_float(total2) + convert_to_float(total3)
    total_str = f"R$ {total_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    # Escreve o valor total
    align.text((1122,1447), total_str, fill='white', font=font_client, stroke_width=0.1)


    with st.spinner("Processando..."):
        try:
            img_buffer = BytesIO()
            image.save(img_buffer, format="PNG")
            img_buffer.seek(0)

            import base64
            img_base64 = base64.b64encode(img_buffer.read()).decode("utf-8")

           
            st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{img_base64}" width="900"/>
            </div>
            """,
            unsafe_allow_html=True
            )
            left, middle, right = st.columns([8.5, 3, 8.5], gap="small",)  # coluna do meio é o dobro das outras

            with middle: 
                st.markdown("")
                st.download_button(
                    label="⬇️ Download",
                    data=img_buffer.getvalue(),
                    file_name=f"Orçamento de {customer} - OS {os_number:02}.png",
                    mime="image/png"
                )
        except Exception as e:
            st.error(f"Erro ao processar orçamento: {e}")
        