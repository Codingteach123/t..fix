import json
import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="T..fixer", page_icon=":wrench:", layout="wide")

#....path_settings...
current_dir = Path(__file__).parent if "__file__"in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
profie_pic = current_dir / "photos" / "profile-pic.png"
projects_pic = current_dir / "photos" / "pic1.png"
projects_pic2 = current_dir / "photos" / "pic2.png"
projects_pic3 = current_dir / "photos" / "pic3.png"
projects_pic4 = current_dir / "photos" / "pic4.png"

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope",],
       #orientation="horizontal",
        default_index=0
  )


if selected ==  "Home":


#...add_emoji..
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    lottie_coding = load_lottiefile("lottiefile/coding.json")        

#...add_photos...
    profie_pic = Image.open(profie_pic)
    coli,col2 = st.columns(2, gap="small")
    with col2:
        st.image(profie_pic, width=280)
       # with col2:
          #  st.download_button("Download", data="profile-pic.png")

#...adding infro
    with coli:
        st.markdown(" # _Hi, i am Kelvin Kambalame :wave:_")
        st.write("")
        st.markdown("_✅ I am a Programer 3 Years expereince._")
        st.write("_✅Strong hands on experience and knowledge in Python._") 
        with st.expander("_Click to read more_"):
            st.markdown("_and i aiso fix and build a lot of things see some of them in my projects. I lives in Malawi, and If U are interested with my services please get in touch with me._")

       #...adding_links
    #social_media ={"Github": "https://github.com"}
    st.write("#")
   #cols = st.columns(len(social_media))
   #for index, (platfom, link) in enumerate(social_media.items()):
        #cols[index].write(f"[{platfom}]({link})")




    st.title(" _A Software and Hardware Engineer_")

    with st.container():
        st.write("___")
        col1, col2, col3 = st.columns([5,10,5,])


    st.subheader(" _This Is What I Do, (Software)_")
    st.write("#")
    st.write("_I create webpages like this._")
    st.write("_Fixing software  programs in computer._")


    left_column, right_column = st.columns(2)
    st.write("#")

    with st.container():
        st.write("___")
        st.header(" _Hardware_")
        st.write("#")
        st.write("_Building Computers._")
        st.write("_Building Amplifiers._")
        st.write("_Building Sensors Using Arduino._")
        st.write("_Instaling Security System._")

        st.write("✅ AND I aiso Fix all Electronic things.")

    st.write("___")

    
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#....adding emoji
    with right_column:
        st_lottie(
            lottie_coding,
            speed=1,
            height= 250,
           #width= 100,
        )    

elif selected == "Projects":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with st.container():
        st.write(" # _How I Made My Things._ ")
        st.write("#")
        st.write("___")
        col1, col2 = st.columns(2)
        projects_pic = Image.open(projects_pic)
        with col1:
            st.image(projects_pic, width=500)
            st.write(" #### Transform a broken laptop into a stunning desktop media PC")

        projects_pic2 = Image.open(projects_pic2)
        with col2:
            st.image(projects_pic2, width=500)
            st.write(" #### Transforming broken Laptop into a All in One PC + Upgrades")

        st.write("#")

        col11, col22 = st.columns(2)
        projects_pic3 = Image.open(projects_pic3)
        with col11:
            st.image(projects_pic3, width=500)
            st.write(" #### Transforming old desktop Box into a good looking Box ")

        projects_pic4 = Image.open(projects_pic4)
        with col22:
            st.image(projects_pic4, width=500)
            st.write(" #### Transforming old desktop Box into a Gaming Box") 



        


elif selected == "Contact":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    with st.container():
        st.write(" # 📬 Get In Touch with me! ")
        st.write("___")
        st.write("##")
        contact_form = """
       <form action="https://formsubmit.co/kkambalame@yahoo.com" method="POST">
       <input type="hidden" name="_captcha" value="false">
       <input type="text" name="name" placeholder="Your name" required>
       <input type="email" name="email"placeholder="Your email" required>
       <textarea name="message" placeholder="Your message here" required></textarea>
       <button type="submit">Send</button>
  </form>
      """

    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

    #...add_css file
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</contact form.css", unsafe_allow_html=True)
    local_css("style/contact form.css")

    st.write("##")
    st.write("___")
    st.write(" # _☎  + 265 993 171 257_ ")


