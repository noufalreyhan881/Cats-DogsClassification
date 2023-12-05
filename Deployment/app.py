import streamlit as st
from PIL import Image
import eda
import model

st.sidebar.title("Menu")
page = st.sidebar.selectbox(label='Select Page', options=['Home Page', 'EDA', 'Model'])

if page == 'Home Page':
    st.header('Cats and Dogs Image Classification')
    img = Image.open('Cat&Dog.jpeg')
    st.image(img)
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Noufal Rifata Reyhan')
    st.write('Batch     : HCK - 009')
    st.write("Objective : Graded Challenge 7 ini dibuat untuk:")
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>Mampu mengimplementasikan CNN untuk tugas klasifikasi gambar. Ini melibatkan pelatihan model untuk mengenali dan mengategorikan objek-objek dalam gambar.</li>
            <li>Memahami konsep deteksi objek menggunakan CNN, di mana model tidak hanya mengenali kelas objek tetapi juga mengidentifikasi lokasi atau batas objek dalam gambar.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
    st.write('')
    with st.expander("Problem Statement"):
        st.caption('Bisakah Saya memprediksi gambar Cats and Dogs secara benar?')

    with st.expander("Kesimpulan"):
        st.caption('Dengan model CNN keakuratan yang didapatkan yaitu hanya 78% oleh karena itu saya melakukan improvment model dengan transfer learning menggunakan VGG16 dan didapatkan imprvement keakuratan menjadi 89%.')

elif page == 'EDA':
    eda.run()
else:
    model.run()