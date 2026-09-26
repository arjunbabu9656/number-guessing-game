import random
import streamlit as st


st.write("welcome to the number gussing program!!")
st.write("iam thinking of number 1 to 100")


# Create the computer number only once
if "computer" not in st.session_state:
    st.session_state.computer = random.randint(1, 100)


easy_or_hard = st.selectbox(
    "Choose a difficulty:",
    ["easy", "hard"]
)


def easy(text, computer_number):

    if text == "easy":

        if "count" not in st.session_state:
            st.session_state.count = 10

        if "won" not in st.session_state:
            st.session_state.won = False

        st.write(
            f"You have {st.session_state.count} attempts remaining"
        )

        user_number = st.number_input(
            "Enter your guess:",
            min_value=1,
            max_value=100,
            step=1
        )

        if st.button(
            "Guess",
            disabled=st.session_state.won or st.session_state.count == 0
        ):

            st.session_state.count = st.session_state.count - 1

            if computer_number > user_number:
                st.write("too low")

            elif computer_number < user_number:
                st.write("too high")

            else:
                st.write("You got it!")
                st.session_state.won = True

            if st.session_state.count == 0 and not st.session_state.won:
                st.write(
                    f"your attempts are over, you lose! "
                    f"and computer number is {computer_number}"
                )


def hard(text, computer_number):

    if text == "hard":

        if "hard_count" not in st.session_state:
            st.session_state.hard_count = 5

        if "hard_won" not in st.session_state:
            st.session_state.hard_won = False

        st.write(
            f"You have {st.session_state.hard_count} attempts remaining"
        )

        user_number = st.number_input(
            "Enter your guess:",
            min_value=1,
            max_value=100,
            step=1
        )

        if st.button(
            "Guess",
            disabled=st.session_state.hard_won or st.session_state.hard_count == 0
        ):

            st.session_state.hard_count = st.session_state.hard_count - 1

            if computer_number > user_number:
                st.write("too low")

            elif computer_number < user_number:
                st.write("too high")

            else:
                st.write("You got it!")
                st.session_state.hard_won = True

            if st.session_state.hard_count == 0 and not st.session_state.hard_won:
                st.write(
                    f"your attempts are over, you lose! "
                    f"and computer number is {computer_number}"
                )


easy(
    text=easy_or_hard,
    computer_number=st.session_state.computer
)

hard(
    text=easy_or_hard,
    computer_number=st.session_state.computer
)