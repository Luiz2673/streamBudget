import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from services import services_list

st.set_page_config(page_title="⚙️Stream Budget", layout='wide')
st.markdown("<h1 style='text-align: center; color: white;'>📃💲Gerador de Orçamento Automático</h1>", unsafe_allow_html= True)
st.markdown("<p style='text-align: center; color: white;'>Preencha os campos abaixo e gere o orçamento em segundos!</p>", unsafe_allow_html= True)

font_client = ImageFont.truetype('./HankenGrotesk-Light.ttf',25) #Serve para as informações do Cliente e para o serviço incluíndo o valor
font_os = ImageFont.truetype('./HankenGrotesk-Light.ttf',67) # Serve para o número da Ordem de Serviço 
font_date = ImageFont.truetype('./HankenGrotesk-Light.ttf',50) # Serve para a data 

#Função que formata o telefone corretamente:
def phone_format(number):
    number = ''.join(filter(str.isdigit, number))
    if len(number) == 11:
        return f"({number[:2]}){number[2:6]}-{number[6:]}"
    elif len (number) ==10:
        return f"({number[:2]}) {number[2:6]}-{number[6:]}"
    else:
        return number
    
#Menu lateral:
with st.sidebar:
    st.header("✏️Formulário")
    customer = st.text_input('Nome do Cliente:', max_chars=35)
    email = st.text_input('Informe o E-mail do Cliente:', max_chars=35)
    phone = st.text_input('Celular', max_chars= 15)
    if phone and not phone.isdigit():
        st.warning("Digite apenas números no campo de Celular")
    phone_formated = phone_format(phone)
    
    #Lista de Serviços
    service_names = [s["serviceName"]for s in services_list]
    option = st.selectbox("Selecione o serviço", service_names)
    amount = st.number_input("Quantidade", min_value=1, value=1)
    selected_service = next(s for s in services_list if s["serviceName"] == option)
    unit_price = selected_service["price"]
    final_price = unit_price * amount



image = Image.open("./Modelo de Orçamento de T.I.png")
align = ImageDraw.Draw(image)

#Informações do Cliente:
align.text((250,727), "Luiz Fernando Gomessssssssssssssssss", fill='black', font=font_client, stroke_width= 0.1)
align.text((250,766), "luizfgomes42@gmail.com", fill='black', font=font_client, stroke_width= 0.1)
align.text((250,806), "(11) 97721-7225", fill='black', font=font_client, stroke_width= 0.1)

#Número da Ordem de Serviço:
align.text((1122,729), "01", fill='black', font=font_os, stroke_width= 0.1)

#Data do Orçamento:
align.text((1000,433), "01/06/2025", fill='black', font=font_date, stroke_width= 0.1)

#Informações do Serviço 1:
align.text((311,1033), "Formatação do Wndows", fill='black', font=font_client, stroke_width= 0.1)
align.text((818,1033), "R$ 280,00", fill='black', font=font_client, stroke_width= 0.1)
align.text((1012,1033), "9", fill='black', font=font_client, stroke_width= 0.1)
align.text((1122,1033), "R$ 280,00", fill='black', font=font_client, stroke_width= 0.1)

#Informações do Serviço 2:
align.text((311,1185), "Formatação do Wndows", fill='black', font=font_client, stroke_width= 0.1)
align.text((818,1185), "R$ 280,00", fill='black', font=font_client, stroke_width= 0.1)
align.text((1012,1185), "9", fill='black', font=font_client, stroke_width= 0.1)
align.text((1122,1185), "R$ 280,00", fill='black', font=font_client, stroke_width= 0.1)

#Informações do Serviço 3
align.text((311,1337), "Formatação do Wndows", fill='black', font=font_client, stroke_width= 0.1)
align.text((818,1337), "R$ 280,00", fill='black', font=font_client, stroke_width= 0.1)
align.text((1012,1337), "9", fill='black', font=font_client, stroke_width= 0.1)
align.text((1122,1337), "R$ 280,00", fill='black', font=font_client, stroke_width= 0.1)

#Valor Total do Serviço:
align.text((1122,1447), "R$ 280,00", fill='white', font=font_client, stroke_width= 0.1)

image.save('./tet.png')