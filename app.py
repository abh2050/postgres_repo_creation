import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the University class based on the univ table
class University(Base):
    __tablename__ = 'univ'
    id = Column(Integer, primary_key=True, autoincrement=True)  # This is important
    university_name = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    founded = Column(Integer)
    number_of_students = Column(Integer)
    tuition_fee = Column(Float)
    academic_programs = Column(String)
    rankings = Column(Integer)

# Database connection string
DATABASE_URL = "postgresql://postgres:abhi@localhost/abhi_db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Form to add a new university
with st.form("university_form", clear_on_submit=True):
    st.write("### Add New University")
    #Add a photo on the header
    st.image('https://cdn.britannica.com/85/13085-050-C2E88389/Corpus-Christi-College-University-of-Cambridge-England.jpg', width=300)
    university_name = st.text_input("University Name")
    city = st.text_input("City")
    state = st.text_input("State")
    country = st.text_input("Country")
    founded = st.number_input("Founded", step=1, format="%d")
    number_of_students = st.number_input("Number of Students", step=1, format="%d")
    tuition_fee = st.number_input("Tuition Fee", step=0.01, format="%f")
    academic_programs = st.text_input("Academic Programs")
    rankings = st.number_input("Rankings", step=1, format="%d")
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        try:
            university = University(
                university_name=university_name,
                city=city,
                state=state,
                country=country,
                founded=founded,
                number_of_students=number_of_students,
                tuition_fee=tuition_fee,
                academic_programs=academic_programs,
                rankings=rankings
            )
            session.add(university)
            session.commit()
            st.success("University added successfully!")
        except Exception as e:
            session.rollback()
            st.error(f"Failed to add university. Error: {e}")
        finally:
            session.close()

