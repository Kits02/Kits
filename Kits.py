import streamlit as st

# Function to display biography with image
def display_bio(name, title, location, education, skills, philosophy, mission, vision, image_path):
    st.title(f"**{name}**")
    st.header(f"**{title}**")
    
    # Display the image
    st.image(image_path, caption=f"Photo of {https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/461971567_526586080318564_4016883153565424525_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeGmcIZOJD3AHDAiYPYA4qVAf1ZpL3kXZsl_VmkveRdmyVZ4Nc84RsDJaW8BmunSKQXP07-N9Q7FpV_oves5ONms&_nc_ohc=GUKKYBmRSU0Q7kNvgEEjBc7&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=AoSXPKF8uLxZF_CKRnqAkW9&oh=00_AYCPOuIEBdfxMDM6MIpJJZr-PfSzEd0DCUCvm6Q4V_DqNg&oe=674B6CC1}", use_column_width=True)
    
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
    "philosophy": (
        "Believes in providing in-depth yet easy-to-understand explanations to enhance "
        "the viewer’s learning experience. Passionate about dismantling myths around intelligence "
        "and promoting strategies for self-improvement."
    ),
    "mission": (
        "To excel in scriptwriting, storytelling, and helping audiences find clarity and value "
        "in the content they consume."
    ),
    "vision": (
        "Becoming a sought-after creative professional while balancing academic growth and "
        "practical experience."
    ),
    "image_path": "path_to_your_image.jpg",  # Update this with the path to your image
}

# Streamlit app
def main():
    display_bio(
        bio_data["name"],
        bio_data["title"],
        bio_data["location"],
        bio_data["education"],
        bio_data["skills"],
        bio_data["philosophy"],
        bio_data["mission"],
        bio_data["vision"],
        bio_data["image_path"]  # Provide the image path
    )

if __name__ == "__main__":
    main()
