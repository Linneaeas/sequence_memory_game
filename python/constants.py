# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Game settings
SEQUENCE_LENGTH = 4
CARD_SHOW_TIME = 1.0
SEQUENCE_SHOW_TIME = 2.0
INIT_TIME = 1.0
BREAK_TIME = 1.0
WRONG_TEXT_DURATION = 1.0

# Visual elements
CARD_SIZE = 180
MARGIN = 10
CARD_FONT_SIZE = 96
INSTRUCTION_FONT_SIZE = 46
FEEDBACK_FONT_SIZE = 46
BUTTON_FONT_SIZE = 32

# Colors
BACKGROUND_COLOR = (219, 62, 177)
CARD_BG_COLOR = (77, 77, 255)
CARD_FONT_COLOR = (219, 62, 177)
INSTRUCTION_FONT_COLOR = (199, 36, 177)
FEEDBACK_FONT_COLOR = (77, 77, 255)
BUTTON_BG_COLOR = (77, 77, 255)
BUTTON_FONT_COLOR = (0, 0, 0)

# Button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_Y_OFFSET = 80

# Position constants
INSTRUCTION_TEXT_X = 50
INSTRUCTION_TEXT_Y = 100
SEQUENCE_NUMBERS_Y = 200
NUMBER_SPACING = 80

# Calculated positions
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
BUTTON_X = CENTER_X - BUTTON_WIDTH // 2
BUTTON_Y = SCREEN_HEIGHT - BUTTON_Y_OFFSET
SEQUENCE_Y = CENTER_Y - CARD_SIZE // 2
SUCCESS_TEXT_Y = CENTER_Y - CARD_SIZE - 50
INSTRUCTION_TEXT1_Y = CENTER_Y - CARD_SIZE - 90
INSTRUCTION_TEXT2_Y = CENTER_Y - CARD_SIZE + 50
INSTRUCTION_TEXT1_X = CENTER_X - 150
INSTRUCTION_TEXT2_X = CENTER_X + 190
FEEDBACK_TEXT_Y = CENTER_Y + CARD_SIZE + 50

# Text messages
INIT_TEXT1 = "Get"
INIT_TEXT2 = "ready!"
FIRST_TEXT1 = "Memorize"
FIRST_TEXT2 = "it!"
SECOND_TEXT1 = "Switching it around, "
SECOND_TEXT2 = "try to not get confused!"
GUESS_TEXT1 = "Do you remember the first sequence?"
GUESS_TEXT2 = "Type to guess"
SUCCESS_TEXT1 = "Congratulations!"
SUCCESS_TEXT2 = "You won!"
WRONG_TEXT1 = "Sorry, that was wrong."
WRONG_TEXT2 = "Try again!"
BUTTON_TEXT = "Restart Game"

# Game states
STATE_INIT = "init"  # All cards are facing down
# Each card flips one by one until all cards are shown
STATE_FIRST_SEQUENCE = "first_sequence"
STATE_BREAK = "break"  # All cards are facing down
# Each card flips one by one until all cards are shown
STATE_SECOND_SEQUENCE = "second_sequence"
# All cards are facing down. User guesses the sequence, that is typed above each card.
STATE_GUESS = "guess"
# All cards are shown. User guessed the sequence correctly.
STATE_SUCCESS = "success"
STATE_WRONG = "wrong"  # Wrong text is shown and the user can guess again.
