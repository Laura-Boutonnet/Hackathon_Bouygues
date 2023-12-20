import streamlit as st
from fonctions import logo
from streamlit_chat import message
import typer
import time


# Affichage du logo
logo()

# Affichage du titre
st.title("Better Call Paul")

# Création des colonnes
col1, col2 = st.columns(2)

# Création fonction qui écrit au ralentit
def type_text_slowly(text, speed=0.01):
    text_container = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        text_container.text(typed_text)
        time.sleep(speed)

# Colonne 1
with col1:
    st.subheader('Discussion')
    def on_input_change():
        user_input = st.session_state.user_input
        st.session_state.past.append(user_input)
        st.session_state.generated.append("The messages from Bot\nWith new line")

    def on_btn_click():
        del st.session_state.past[:]
        del st.session_state.generated[:]

    st.session_state.setdefault(
        'past', 
        ['bonjour je suis Paul',
        'Voici votre réponse']
    )
    st.session_state.setdefault(
        'generated', 
        ["bonjour, j'ai besoin de X",
         ""]
    )

    chat_placeholder = st.empty()

    with chat_placeholder.container():    
        for i in range(len(st.session_state['past'])):                
            message(st.session_state['past'][i])
            if st.session_state['generated'][i]:
                message(st.session_state['generated'][i], is_user=True, key=f"{i}_user")

# Colonne 2 
with col2:
   st.subheader("Résumé")
   type_text_slowly('Voici le résumé de la conversation : \nJe suis content')


st.markdown(
    '<div style="font-size: 20px; background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; cursor: pointer;">Prendre l\'appel</div>',
    unsafe_allow_html=True
)

