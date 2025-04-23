# Screen dimensions
SCREEN_WIDTH = 1400
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
FEEDBACK_FONT_SIZE = 66
BUTTON_FONT_SIZE = 46

# Colors
BACKGROUND_COLOR = (219, 62, 177) 
CARD_BG_COLOR = (77, 77, 255)
CARD_FONT_COLOR = (219, 62, 177)
INSTRUCTION_FONT_COLOR = (77, 77, 255)
SUCCESS_FONT_COLOR = (219,62,177)
WRONG_FONT_COLOR = (255,173,0)
SUCCESS_BG_COLOR = (68,214,44) 
WRONG_BG_COLOR = (210,39,48)
GUESS_FONT_COLOR = (68,214,44)
SUCCESS_PADDING = 20
WRONG_PADDING = 20
BUTTON_BG_COLOR = (77, 77, 255)
BUTTON_FONT_COLOR =  (219, 62, 177) 

# Button dimensions
BUTTON_WIDTH = 1400
BUTTON_HEIGHT = 50
BUTTON_Y_OFFSET = 50

# Position constants
SEQUENCE_NUMBERS_Y = 200
NUMBER_SPACING = 80

# Calculated positions
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
# Sequence Y postition center of screen
SEQUENCE_Y = CENTER_Y - CARD_SIZE /2 
# Cat image Y in relation to the SEQUENCE
CAT_IMAGE_Y = SEQUENCE_Y - 100
# Cat image X in relation to the center of the screen
CAT_IMAGE_X = CENTER_X 
# Guessing numbers position
GUESS_NUMBERS_Y = SEQUENCE_Y + CARD_SIZE + 50  # Position below the cards
# Instruction text 1&2 Y in relation to the CAT_IMAGE_Y
INSTRUCTION_TEXT1_Y = CAT_IMAGE_Y - 50
INSTRUCTION_TEXT2_Y = CAT_IMAGE_Y+ 50
# Instruction text 1&2 X in relation to the CAT_IMAGE_X
INSTRUCTION_TEXT1_X = CAT_IMAGE_X
INSTRUCTION_TEXT2_X = CAT_IMAGE_X 
# Wrong text 1&2 Y in relation to the CENTER_Y
WRONG_TEXT1_Y = CENTER_Y - 50
WRONG_TEXT2_Y = CENTER_Y + 50
WRONG_TEXT1_X = CENTER_X
WRONG_TEXT2_X = CENTER_X
# Success text 1&2 Y in relation to the CENTER_Y
SUCCESS_TEXT1_Y = CENTER_Y - 50
SUCCESS_TEXT2_Y = CENTER_Y + 50
SUCCESS_TEXT1_X = CENTER_X
SUCCESS_TEXT2_X = CENTER_X

BUTTON_X = CENTER_X - BUTTON_WIDTH // 2
BUTTON_Y = SCREEN_HEIGHT - BUTTON_Y_OFFSET
# Text messages
INIT_TEXT1 = "GET"
INIT_TEXT2 = "READY!"
FIRST_TEXT1 = "MEMORIZE"
FIRST_TEXT2 = "IT!"
SECOND_TEXT1 = "Switching it around, "
SECOND_TEXT2 = "Try to not get confused!"
GUESS_TEXT1 = "Remember the 1st one?"
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
