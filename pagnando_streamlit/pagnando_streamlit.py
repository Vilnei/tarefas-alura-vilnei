import streamlit as st


lista_qrcode = ['qra000','qra001', 'qra002', 'qra003', 'qra004', 'qra005', 'qra006', 'qra007', 'qra008', 'qra009',
         'qra010','qra011', 'qra012', 'qra013', 'qra014', 'qra015', 'qra016', 'qra017', 'qra018', 'qra019',
         'qra020','qra021', 'qra022', 'qra023', 'qra024', 'qra025', 'qra026', 'qra027', 'qra028', 'qra029',
         'qra030','qra031', 'qra032', 'qra033', 'qra034', 'qra035', 'qra036', 'qra037', 'qra038', 'qra039',
         'qra040','qra041', 'qra042', 'qra043', 'qra044', 'qra045', 'qra046', 'qra047', 'qra048', 'qra049',
         'qra050','qra051', 'qra052', 'qra053', 'qra054', 'qra055', 'qra056', 'qra057', 'qra058', 'qra059',
         'qra060','qra061', 'qra062', 'qra063', 'qra064', 'qra065', 'qra066', 'qra067', 'qra068', 'qra069',
         'qra070','qra071', 'qra072', 'qra073', 'qra074', 'qra075', 'qra076', 'qra077', 'qra078', 'qra079',
         'qra080','qra081', 'qra082', 'qra083', 'qra084', 'qra085', 'qra086', 'qra087', 'qra088', 'qra089',
         'qra090','qra091', 'qra092', 'qra093', 'qra094', 'qra095', 'qra096', 'qra097', 'qra098', 'qra099'
        ]

def main():

    # menu = ["Home", "Login"]
    # choice = st.sidebar.selectbox("Opções", menu)


    # if choice == "Home":
    #     st.subheader("Pagina Principal")


    # if menu == "Login":
    #     st.subheader("Acesso Principal")

    #     username = st.sidebar.text_input("Nome de usuario")
    #     password = st.sidebar.text_input("Senha de usuario", type='password')
    #     if st.sidebar.checkbox("login"):
    #         if password == "Deussejalouvado":
    #             st.success("Acesso liberado para {}".format(username))
    #         else:
    #             st.warning("Cadastro de usuario não encontrado")       



    with st.form(key="login"):
        username = st.text_input(label="Insira o seu login")
        password = st.text_input(label="Insira seu password", type="password")
        st.form_submit_button(label="Logar")

        if password == "Deussej@louvad0":
            st.success("Acesso liberado para {}".format(username))

            choice = st.sidebar.selectbox("Opções", lista_qrcode)

            if choice == "Home":
                st.subheader("Pagina Principal")

        else:
            st.warning("Acesso NEGADO, Procure pelo Administrador")

    # with st.subheader("QRCode"):
    #     st.write(lista_qrcode)


if __name__ == "__main__":
    main()
