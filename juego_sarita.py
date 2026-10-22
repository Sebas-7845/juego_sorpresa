import streamlit as st

st.set_page_config(page_title="Sorpresa", page_icon="💌", layout="centered")

if 'etapa' not in st.session_state:
    st.session_state.etapa = 1
if 'intentos_jb' not in st.session_state:
    st.session_state.intentos_jb = 0

def avanzar(nueva_etapa):
    st.session_state.etapa = nueva_etapa

st.title("💌 Un pequeño juego...")

corazon = """
   ♥♥♥     ♥♥♥   
  ♥♥♥♥♥   ♥♥♥♥♥  
 ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥ 
 ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ 
  ♥♥♥♥♥♥♥♥♥♥♥♥♥  
   ♥♥♥♥♥♥♥♥♥♥♥   
    ♥♥♥♥♥♥♥♥♥    
     ♥♥♥♥♥♥♥     
      ♥♥♥♥♥      
       ♥♥♥       
        ♥        
"""

flores = """
      _ 
    _(_)_ 
   (_)@(_) 
     (_)\\ 
        \\|/ 
         | 
        \\|/ 
"""

if st.session_state.etapa == 1:
    st.markdown(f"<div style='color:#ff4b4b; text-align:center; font-family:monospace; font-size:16px; white-space:pre;'>{corazon}</div>", unsafe_allow_html=True)
    st.write("¿Quieres jugar a un juego?")
    col1, col2 = st.columns(2)
    if col1.button("Sí", use_container_width=True):
        avanzar(2)
        st.rerun()
    if col2.button("No", use_container_width=True):
        st.error("¡Oh! Vamos, inténtalo de nuevo...")

elif st.session_state.etapa == 2:
    st.write("¿Tú me quieres?")
    col1, col2 = st.columns(2)
    if col1.button("Sí", use_container_width=True):
        avanzar(21)
        st.rerun()
    if col2.button("No", use_container_width=True):
        avanzar(3)
        st.rerun()

elif st.session_state.etapa == 21:
    st.warning("Embustera vale 😭")
    if st.button("Continuar"):
        avanzar(7)
        st.rerun()

elif st.session_state.etapa == 3:
    st.write("¿Estas segura?")
    col1, col2 = st.columns(2)
    if col1.button("Sí, segura", use_container_width=True):
        avanzar(6)
        st.rerun()
    if col2.button("No", use_container_width=True):
        avanzar(4)
        st.rerun()

elif st.session_state.etapa == 4:
    st.write("¿Estas muuuy muy segura?")
    col1, col2 = st.columns(2)
    if col1.button("Sí, muy segura", use_container_width=True):
        avanzar(6)
        st.rerun()
    if col2.button("No", use_container_width=True):
        avanzar(5)
        st.rerun()

elif st.session_state.etapa == 5:
    st.write("¿Ni un poquito enserio?")
    col1, col2 = st.columns(2)
    if col1.button("Sí...", use_container_width=True):
        avanzar(6)
        st.rerun()
    if col2.button("No", use_container_width=True):
        st.error("Error: yo sé que mientes.")

elif st.session_state.etapa == 6:
    st.write("¿Enserio??")
    col1, col2 = st.columns(2)
    if col1.button("Sí, enserio", use_container_width=True):
        avanzar(7)
        st.rerun()
    if col2.button("No", use_container_width=True):
        st.error("Ahh no juegues así conmigo vale")

elif st.session_state.etapa == 7:
    st.write("¿Mas que a el tal Ross?")
    col1, col2 = st.columns(2)
    if col1.button("Sí", use_container_width=True):
        avanzar(71)
        st.rerun()
    if col2.button("No", use_container_width=True):
        st.error("Error: intenta de nuevo")

elif st.session_state.etapa == 71:
    st.success("¡Yo sabíaa valee JAJAJA!")
    if st.button("Continuar... ¿sí?"):
        avanzar(8)
        st.rerun()

elif st.session_state.etapa == 8:
    st.write("Y... ¿mas que a Justin Bieber?")
    col1, col2 = st.columns(2)
    if col1.button("Sí", use_container_width=True):
        avanzar(81)
        st.rerun()
    if col2.button("No", use_container_width=True):
        if st.session_state.intentos_jb == 0:
            st.warning("Porfa no seas asii sarita")
            st.session_state.intentos_jb += 1
        else:
            st.error("Mmm respuesta incorrecta")

elif st.session_state.etapa == 81:
    st.success("¡Enserioo? Me vas a hacer llorar vale")
    if st.button("Siguiente"):
        avanzar(9)
        st.rerun()

elif st.session_state.etapa == 9:
    st.write("¿Quieres un obsequio?")
    if st.button("Sí"):
        avanzar(10)
        st.rerun()

elif st.session_state.etapa == 10:
    st.markdown(f"<div style='color:#2e8b57; text-align:center; font-family:monospace; font-size:16px; white-space:pre;'>{flores}</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Gracias por jugar, yo también te quiero muchoo</h3>", unsafe_allow_html=True)
    st.write("**De:** Sebas.")
    st.write("**Para:** Ti ❤️")