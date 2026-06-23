import streamlit as st

st.set_page_config(
    page_title="Walker Prime RH",
    page_icon="👑",
    layout="centered"
)

st.title("👑 Walker Prime RH")
st.subheader("🚀 Contratamos mais que o São Vicente")

st.sidebar.image("logo.png")



nome = st.text_input("👤 Nome do funcionário")
idade = st.text_input("🎂 Idade do funcionário")
email = st.text_input("📧 E-mail do funcionário")
salario = st.text_input("💰 Salário do funcionário")
cargo = st.text_input("💼 Cargo do funcionário")

if st.button("✅ Cadastrar Funcionário"):
    st.warning(f"🎉 Funcionário {nome} cadastrado com sucesso!")
    st.balloons()
    st.image('https://thispersondoesnotexist.com/')


