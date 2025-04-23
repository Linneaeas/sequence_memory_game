import pygame
import random
import time
from constants import *


class Game:
    """Main game class for the Sequence Memory game."""

    def __init__(self, window, font, button_font, feedback_font, card_font):
        """Initialize the game with default values."""
        self.window = window
        self.font = font
        self.button_font = button_font
        self.feedback_font = feedback_font
        self.card_font = card_font
        self.sequence = []
        self.shuffled_sequence = []
        self.player_sequence = []
        self.state = STATE_INIT
        self.show_time = 0
        self.wrong_message = ""
        self.wrong_time = 0
        self.current_card_index = 0
        self.is_flipping_back = False
        self.flip_back_time = 0
        self.guess_result = None  # None, "correct", or "wrong"

        # Load card back image
        self.card_back = pygame.image.load("./shared/card_image.jpg")
        self.card_back = pygame.transform.scale(
            self.card_back, (CARD_SIZE, CARD_SIZE))

        # Load state images
        self.state_images = {
            "one": pygame.transform.scale(pygame.image.load("./shared/one.png"), (CARD_SIZE, CARD_SIZE)),
            "two": pygame.transform.scale(pygame.image.load("./shared/two.png"), (CARD_SIZE, CARD_SIZE)),
            "three": pygame.transform.scale(pygame.image.load("./shared/three.png"), (CARD_SIZE, CARD_SIZE)),
            "four": pygame.transform.scale(pygame.image.load("./shared/four.png"), (CARD_SIZE, CARD_SIZE)),
            "five": pygame.transform.scale(pygame.image.load("./shared/five.png"), (CARD_SIZE, CARD_SIZE)),
            "six": pygame.transform.scale(pygame.image.load("./shared/six.png"), (CARD_SIZE, CARD_SIZE)),
            "seven": pygame.transform.scale(pygame.image.load("./shared/seven.png"), (CARD_SIZE, CARD_SIZE)),
            "eight": pygame.transform.scale(pygame.image.load("./shared/eight.png"), (CARD_SIZE, CARD_SIZE))
        }

        # Map states to images (you can change these mappings as needed)
        self.state_to_image = {
            STATE_INIT: "one",
            STATE_FIRST_SEQUENCE: "two",
            STATE_BREAK: "three",
            STATE_SECOND_SEQUENCE: "four",
            STATE_GUESS: "five",
            STATE_SUCCESS: "six"
        }

        # Map guess results to images
        self.guess_result_to_image = {
            "correct": "seven",
            "wrong": "eight"
        }

        self.generate_sequence()

    def generate_sequence(self) -> None:
        """Generate a new random sequence and reset game state."""
        self.sequence = [random.randint(0, 9) for _ in range(SEQUENCE_LENGTH)]
        self.shuffled_sequence = self.sequence.copy()
        random.shuffle(self.shuffled_sequence)
        self.player_sequence = []
        self.state = STATE_INIT
        self.show_time = time.time() + INIT_TIME
        self.wrong_message = ""
        self.current_card_index = 0
        self.is_flipping_back = False
        self.guess_result = None

    def draw_sequence(self) -> None:
        """Draw the current game state on the screen."""
        self.window.fill(BACKGROUND_COLOR)

        # Draw state image above the cards
        if self.guess_result is not None:
            # Show guess result image if there's a result
            image_name = self.guess_result_to_image[self.guess_result]
            if image_name in self.state_images:
                image = self.state_images[image_name]
                image_rect = image.get_rect(center=(CAT_IMAGE_X, CAT_IMAGE_Y))
                self.window.blit(image, image_rect)
        elif self.state in self.state_to_image:
            # Show normal state image
            image_name = self.state_to_image[self.state]
            if image_name in self.state_images:
                image = self.state_images[image_name]
                image_rect = image.get_rect(center=(CAT_IMAGE_X, CAT_IMAGE_Y))
                self.window.blit(image, image_rect)

        if self.state == STATE_SUCCESS:
            # Draw cards first
            self._draw_cards(self.sequence, SEQUENCE_Y, show_all=True)
            self._draw_restart_button()

            # Draw success text in two parts (after cards)
            success_text1 = self.feedback_font.render(
                SUCCESS_TEXT1, True, SUCCESS_FONT_COLOR)
            success_text2 = self.feedback_font.render(
                SUCCESS_TEXT2, True, SUCCESS_FONT_COLOR)
            success_rect1 = success_text1.get_rect(
                center=(SUCCESS_TEXT1_X, SUCCESS_TEXT1_Y))
            success_rect2 = success_text2.get_rect(
                center=(SUCCESS_TEXT2_X, SUCCESS_TEXT2_Y))
            
            # Add padding around the text
            bg_rect1 = pygame.Rect(
                success_rect1.x - SUCCESS_PADDING,
                success_rect1.y - SUCCESS_PADDING,
                success_rect1.width + SUCCESS_PADDING * 2,
                success_rect1.height + SUCCESS_PADDING * 2
            )
            bg_rect2 = pygame.Rect(
                success_rect2.x - SUCCESS_PADDING,
                success_rect2.y - SUCCESS_PADDING,
                success_rect2.width + SUCCESS_PADDING * 2,
                success_rect2.height + SUCCESS_PADDING * 2
            )
            
            # Draw background rectangles
            pygame.draw.rect(self.window, SUCCESS_BG_COLOR, bg_rect1)
            pygame.draw.rect(self.window, SUCCESS_BG_COLOR, bg_rect2)
            
            # Draw text on top of backgrounds
            self.window.blit(success_text1, success_rect1)
            self.window.blit(success_text2, success_rect2)
            return

        current_sequence = {
            STATE_FIRST_SEQUENCE: self.sequence,
            STATE_SECOND_SEQUENCE: self.shuffled_sequence,
            STATE_GUESS: self.sequence,
            STATE_INIT: self.sequence,
            STATE_BREAK: self.shuffled_sequence
        }.get(self.state, self.player_sequence)

        if self.state == STATE_GUESS:
            self._draw_cards(current_sequence, SEQUENCE_Y, show_all=False)
            self._draw_guesses(self.player_sequence, SEQUENCE_Y - CARD_SIZE - 10)
        else:
            show_all = (
                self.state == STATE_FIRST_SEQUENCE and self.current_card_index >= SEQUENCE_LENGTH)
            self._draw_cards(current_sequence, SEQUENCE_Y, show_all=show_all)

        # Draw instruction text in two parts
        instruction_texts = {
            STATE_INIT: (INIT_TEXT1, INIT_TEXT2),
            STATE_FIRST_SEQUENCE: (FIRST_TEXT1, FIRST_TEXT2),
            STATE_BREAK: (SECOND_TEXT1, SECOND_TEXT2),
            STATE_SECOND_SEQUENCE: (SECOND_TEXT1, SECOND_TEXT2),
            STATE_GUESS: (GUESS_TEXT1, GUESS_TEXT2)
        }.get(self.state, (GUESS_TEXT1, GUESS_TEXT2))

        instruction_text1 = self.font.render(
            instruction_texts[0], True, INSTRUCTION_FONT_COLOR)
        instruction_text2 = self.font.render(
            instruction_texts[1], True, INSTRUCTION_FONT_COLOR)
        
        # Calculate dynamic positions based on text width
        cat_image = self.state_images[self.state_to_image[self.state]]
        cat_width = cat_image.get_width()
        
        # Position first text to end at cat's left edge
        instruction_rect1 = instruction_text1.get_rect(
            right=CAT_IMAGE_X - cat_width//2 - 15,  # 15 pixels gap
            centery=INSTRUCTION_TEXT1_Y)
        
        # Position second text to start at cat's right edge
        instruction_rect2 = instruction_text2.get_rect(
            left=CAT_IMAGE_X + cat_width//2 + 15,  # 15 pixels gap
            centery=INSTRUCTION_TEXT2_Y)
        
        self.window.blit(instruction_text1, instruction_rect1)
        self.window.blit(instruction_text2, instruction_rect2)

        if self.wrong_message:
            # Draw wrong message in two parts
            wrong_text1 = self.feedback_font.render(
                WRONG_TEXT1, True, WRONG_FONT_COLOR)
            wrong_text2 = self.feedback_font.render(
                WRONG_TEXT2, True, WRONG_FONT_COLOR)
            wrong_rect1 = wrong_text1.get_rect(
                center=(WRONG_TEXT1_X, WRONG_TEXT1_Y))
            wrong_rect2 = wrong_text2.get_rect(
                center=(WRONG_TEXT2_X, WRONG_TEXT2_Y))
            
            # Add padding around the text
            bg_rect1 = pygame.Rect(
                wrong_rect1.x - WRONG_PADDING,
                wrong_rect1.y - WRONG_PADDING,
                wrong_rect1.width + WRONG_PADDING * 2,
                wrong_rect1.height + WRONG_PADDING * 2
            )
            bg_rect2 = pygame.Rect(
                wrong_rect2.x - WRONG_PADDING,
                wrong_rect2.y - WRONG_PADDING,
                wrong_rect2.width + WRONG_PADDING * 2,
                wrong_rect2.height + WRONG_PADDING * 2
            )
            
            # Draw background rectangles
            pygame.draw.rect(self.window, WRONG_BG_COLOR, bg_rect2)
            pygame.draw.rect(self.window, WRONG_BG_COLOR, bg_rect1)
            
            # Draw text on top of backgrounds
            self.window.blit(wrong_text1, wrong_rect1)
            self.window.blit(wrong_text2, wrong_rect2)

        if self.state == STATE_GUESS:
            self._draw_restart_button()

    def _draw_cards(self, sequence, y, show_all=False):
        total_width = (CARD_SIZE * SEQUENCE_LENGTH) + \
            (MARGIN * (SEQUENCE_LENGTH - 1))
        start_x = CENTER_X - total_width // 2

        for i, number in enumerate(sequence):
            x = start_x + (i * (CARD_SIZE + MARGIN))

            self.window.blit(self.card_back, (x, y))

            should_show = (
                show_all or
                (self.state == STATE_FIRST_SEQUENCE and i <= self.current_card_index) or
                (self.state == STATE_SECOND_SEQUENCE and i <= self.current_card_index)
            ) and self.state not in [STATE_INIT, STATE_BREAK]

            if should_show:
                pygame.draw.rect(self.window, CARD_BG_COLOR,
                                 (x, y, CARD_SIZE, CARD_SIZE))
                number_text = self.card_font.render(
                    str(number), True, CARD_FONT_COLOR)
                number_rect = number_text.get_rect(
                    center=(x + CARD_SIZE//2, y + CARD_SIZE//2))
                self.window.blit(number_text, number_rect)

    def _draw_guesses(self, sequence, y):
        """Draw the player's guesses below the cards."""
        total_width = (CARD_SIZE * SEQUENCE_LENGTH) + \
            (MARGIN * (SEQUENCE_LENGTH - 1))
        start_x = CENTER_X - total_width // 2

        for i, number in enumerate(sequence):
            x = start_x + (i * (CARD_SIZE + MARGIN))

            # Render and draw the guess number
            guess_text = self.font.render(str(number), True, GUESS_FONT_COLOR)
            guess_rect = guess_text.get_rect(
                center=(x + CARD_SIZE//2, GUESS_NUMBERS_Y))
            self.window.blit(guess_text, guess_rect)

    def _draw_empty_slot(self, sequence, y):
        total_width = (CARD_SIZE * SEQUENCE_LENGTH) + \
            (MARGIN * (SEQUENCE_LENGTH - 1))
        start_x = CENTER_X - total_width // 2

        for i in range(SEQUENCE_LENGTH):
            x = start_x + (i * (CARD_SIZE + MARGIN))
            self.window.blit(self.card_back, (x, y))

    def _draw_restart_button(self):
        button_rect = pygame.Rect(
            BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(self.window, BUTTON_BG_COLOR, button_rect)
        restart_text = self.button_font.render(
            BUTTON_TEXT, True, BUTTON_FONT_COLOR)
        restart_rect = restart_text.get_rect(center=button_rect.center)
        self.window.blit(restart_text, restart_rect)
        return button_rect

    def is_restart_clicked(self, pos):
        button_rect = pygame.Rect(
            BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
        return button_rect.collidepoint(pos)

    def check_sequence(self) -> bool:
        """Check if the player's sequence matches the original sequence."""
        is_correct = self.player_sequence == self.sequence
        self.guess_result = "correct" if is_correct else "wrong"
        return is_correct
