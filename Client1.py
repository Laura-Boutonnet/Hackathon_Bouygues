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
        ["Bonjour je suis Paul, l'agent téléphonique de Bouygues Telecom. Comment puis-je vous aider?",
        "Je vais regarder. Quel est le numéro téléphonique fixe relié à la box",
        "Merci, êtes-vous bien Pierre Hamoir?",
        "Parfait, je vais vous poser quelques questions pour mieux comprendre votre problème.\n Est-ce que les voyants de votre box sont correctement allumés",
        "Est-ce que vous avez redémarrer votre box?",
        "Merci pour ces informations, je lance l'appel vers l'un de nos conseillers spécialisés.\n Y'a t-il eu de grosses intempéries ou orage récemment?",
        "Est-ce qu'il y a eu recemment des travaux dans votre quartier ?",
        "Très bien, j'ai envoyé un récapitulatif à Laura, notre conseillère clientèle. Elle est en train de prendre connaissance de votre dossier et va récupérer l'appel de suite"]
    )
    st.session_state.setdefault(
        'generated', 
        ["J'ai un problème wifi",
         "0183643718",
         "Oui, tout à fait",
         "Oui ils le sont",
         "Oui tout à fait",
         "Non, il n'y en a pas eu",
         "Je ne sais pas",
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
   type_text_slowly("Le client signale un problème de wifi.\nLe client s'apelle Monsieur Pierre Hamoir,\nson numéro est le 0683643718.\nLes voyants de la box sont bien allumés\net malgré un redémarrage, la box ne\nfonctionne toujours pas. Le client a\nindiqué qu'il n'y avait pas de problèmes\ndans sa rue ni d'orages.")


st.markdown(
    '<div style="font-size: 20px; background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; cursor: pointer;">Prendre l\'appel</div>',
    unsafe_allow_html=True
)

