# Import libraries
import numpy as np 
import pandas as pd 
import streamlit as st 
import time
import random 
from random import sample


# Define Functions

# Quiz
def show_question(question_idx):
    domandine = [
        'Per iniziare...',
        'OK vediamo come risponderesti adesso...',
        'Siamo a metà...',
        "Quest'altra invece?...",
        'Last but not Least...'
    ]
    question = st.session_state.questions_sample[question_idx]
    st.subheader(domandine[question_idx])
    # st.subheader(f"Question {question_idx + 1}:")
    st.title(f"{question['question']}")
    # Display options as buttons in a single row
    col1, col2 = st.columns(2)
    with col1:
        if st.button(question["options"][0], key=f"left_{question_idx}"):
            check_answer(question, 0)
    with col2:
        if st.button(question["options"][1], key=f"right_{question_idx}"):
            check_answer(question, 1)

def check_answer(question, selected_option):
    if st.session_state.answered:
        return
    correct_answer = question["correct_answer"]
    selected_answer = question["options"][selected_option]
    
    if selected_answer == correct_answer:
        st.write("Correct!")
        st.session_state.score += 1
    else:
        st.write(f"Sorry, the correct answer was: {correct_answer}")
    
    st.session_state.answered = True
    # Wait for 1 second to show the feedback
    time.sleep(1)

    # Move to the next question
    st.session_state.current_question += 1
    st.session_state.answered = False

    # Rerun the script to show the next question
    st.experimental_rerun()

def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.questions_sample = random.sample(questions, 5)
    st.experimental_rerun()

# Rock Paper Scissors
def get_computer_choice():
    # Simulating computer's thinking process
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f'Calcolando Mossa Vincente... {i+1}')
        bar.progress(i + 1)
        time.sleep(0.03)  # Adjust sleep time for desired speed

    # After thinking process, determine computer's choice
    choices = ["🗿", "🧻", "✂️"]
    computer_choice = random.choice(choices)

    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        st.header(' ')
        time.sleep(0.7)
        return "Pareggio!"
    elif    (user_choice == "🗿" and computer_choice == "🧻") or \
            (user_choice == "🧻" and computer_choice == "✂️") or \
            (user_choice == "✂️" and computer_choice == "🗿"):
        st.header(' ')
        time.sleep(0.7)
        return "🤖: Easy Win!"
    else:
        st.header(' ')
        time.sleep(0.7)
        return "Hai Vintooo!"

# Personality Test
def determine_personality_type(average_score):
    # Example function to determine personality type based on average score
    if average_score <= 10:
        return "Type 1"
    elif average_score <= 20:
        return "Type 2"
    elif average_score <= 30:
        return "Type 3"
    elif average_score <= 40:
        return "Type 4"
    elif average_score <= 50:
        return "Type 5"
    elif average_score <= 60:
        return "Type 6"
    elif average_score <= 70:
        return "Type 7"
    elif average_score <= 80:
        return "Type 8"
    elif average_score <= 90:
        return "Type 9"
    else:
        return "Type 10"


# Main page configuration
st.set_page_config(
    page_title = '佳欣爱睡觉',
    page_icon = "🐰💤",
    layout = "wide",
    initial_sidebar_state = "expanded",
    menu_items = {
        'Get Help': 'https://www.instagram.com/angelozhang_?igsh=cXd5eG1mNHgzeDFu&utm_source=qr',
        'Report a bug': "https://bere.al/casafeng",
        'About': "# 尊嘟假嘟!"
    }
)


# Build Dashboard 
add_sidebar = st.sidebar.selectbox(
    'Scegli un gioco 🎮',
    (' ', '比大小 📊', '石头剪刀布 🆚', 'Quanto conosci bene 阿烽 🧐', 'Test della personalità 💭', '秘密'))


## Total Picture 
if add_sidebar == ' ':

    # st.title('_早上好老婆_ 🌹')
    # st.header('睡得好吗？')
    st.subheader('一起玩游戏吧 👻', divider='grey')
    # st.title('_Streamlit_ is :blue[cool] :sunglasses:')

    st.markdown(

        """
        👈 Usa la barra laterale
        """
    )

elif add_sidebar == 'Quanto conosci bene 阿烽 🧐':

    # Define the questions list
    questions = [
        {
            "question": "Coffee☕️ OR Hot Chocolate🍫",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Halloween🎃 OR Christmas🎄",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Music🎶 OR Movies🎬",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "Talking🗣️ OR Texting🤳🏻",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "Blue🔵 OR Red🔴",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "Spring🌷 OR Summer🍉",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "Autumn🍁 OR Winter❄️",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "Baths🛁 OR Showers🚿",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Pizza🍕 OR Hamburger🍔",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "Cake🍰 OR Ice cream🍦",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Sunrise🌅 OR Sunset🌄",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Coke🥤 OR Fanta🍊",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "KFC🍗 OR MC🍟",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Cats🐈 OR Dogs🐕",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Passenger👸🏻 OR Driver🧑🏻‍✈️",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Early Morning🌆 OR Late Night🌃",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Sweet🍬 OR Salty🌯",
            "options": ["👈", "👉"],
            "correct_answer": "👉"
        },
        {
            "question": "Home Cooking🧑🏻‍🍳 OR Eating Out🥡",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "Sand🏖️ OR Snow❄️",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
        {
            "question": "Rice🍚 OR Pasta🍝",
            "options": ["👈", "👉"],
            "correct_answer": "👈"
        },
    ]

    # Initialize session state variables with default values
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "questions_sample" not in st.session_state:
        st.session_state.questions_sample = random.sample(questions, 5)  # Sample 5 questions
    if "answered" not in st.session_state:
        st.session_state.answered = False


    st.title("Cosa Farebbe 阿烽?")
    # st.write("Welcome to the Game!", divider = 'grey')

    if st.session_state.current_question < len(st.session_state.questions_sample):
        show_question(st.session_state.current_question)
    else:
        # st.write(f"You scored {st.session_state.score} out of {len(st.session_state.questions_sample)}!")

        rispostine = [
            'Bro non mi conosci?',
            'Almeno sai che mi chiamo Angelo',
            'Not Bad',
            "Quasi",
            'Mamma?'
        ]
        st.subheader(rispostine[st.session_state.score - 1] + f'    {st.session_state.score}/{len(st.session_state.questions_sample)}')
        # st.write()

        if st.button("Restart Quiz"):
            restart_quiz()


elif add_sidebar == 'Test della personalità 💭':

    st.title('Work in Progress 🚧')

elif add_sidebar == '比大小 📊':

    st.title('Work in Progress 🔜')
    st.subheader('我的 criceti 累了')

elif add_sidebar == '石头剪刀布 🆚':

    if 'user_choice' not in st.session_state:
        st.session_state.user_choice = None
        st.session_state.computer_choice = None
        st.session_state.result = None
        st.session_state.play_again = False

    st.title("Il Gioco del Sasso rompe Forbice ma muore per Carta")

    if st.session_state.user_choice is None and not st.session_state.play_again:
        st.subheader("Scegli la tua mossa:")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Rock🗿"):
                st.session_state.user_choice = "🗿"
        with col2:
            if st.button("Paper🧻"):
                st.session_state.user_choice = "🧻"
        with col3:
            if st.button("Scissors✂️"):
                st.session_state.user_choice = "✂️"

    if st.session_state.user_choice is not None and not st.session_state.play_again:
        # st.subheader("🤖 is deciding...")
        st.session_state.computer_choice = get_computer_choice()
        st.write("🤖: Io gioco ", st.session_state.computer_choice)
        st.session_state.result = determine_winner(st.session_state.user_choice, st.session_state.computer_choice)
        st.subheader(st.session_state.result)
        st.session_state.play_again = True

    if st.session_state.play_again:
        if st.button("Play Again"):
            st.session_state.user_choice = None
            st.session_state.computer_choice = None
            st.session_state.result = None
            st.session_state.play_again = False
            st.experimental_rerun()  # Ensure the game restarts with one click


elif add_sidebar == '秘密':

    time.sleep(1)
    # st.write('READY!')
    time.sleep(1)
    # You can use a column just like st.sidebar:
    if st.button('Clicca'):
        st.write('你是傻逼 🐸')


#    st.title('Work in Progress 🚧')
#    st.title('Work in Progress 🏗️')

