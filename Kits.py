import streamlit as st

# Function to display biography with image
def display_bio(name, title, location, education, skills, philosophy, mission, vision, image_url):
    st.title(f"**{name}**")
    st.header(f"**{title}**")
    
    # Display the image as 1x1 (square)
    st.image(image_url, caption=f"Photo of {name}", width=300, height=300)  # Adjust width and height as needed
    
    st.subheader("Location:")
    st.write(location)

    st.subheader("Education:")
    st.write(education)

    st.subheader("Professional Skills:")
    for skill in skills:
        st.write(f"- {skill}")

    st.subheader("Content Philosophy:")
    st.write(philosophy)

    st.subheader("Mission:")
    st.write(mission)

    st.subheader("Vision:")
    st.write(vision)

# Biography details
bio_data = {
    "name": "Paquito Jr. V. Binongo",
    "title": "Freshman Student | YouTube Scriptwriter | Copywriter",
    "location": "Philippines",
    "education": "Freshman, currently exploring and adapting to the grading system in the Philippines.",
    "skills": [
        "YouTube Scriptwriting: Expert in creating engaging long-form and short-form scripts.",
        "Copywriting: Skilled in crafting persuasive and compelling copy for diverse clients.",
        "Freelance Expertise: Developing a robust profile on Upwork to showcase writing skills and services.",
    ],
    "philosop
