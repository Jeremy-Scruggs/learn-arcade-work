import random
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Python Blackjack"

CARD_SCALE = 0.6
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

BOTTOM_Y = CARD_HEIGHT / 2 + CARD_HEIGHT * VERTICAL_MARGIN_PERCENT
START_X = CARD_WIDTH / 2 + CARD_WIDTH * HORIZONTAL_MARGIN_PERCENT

# Constants for card values and suits
CARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
# Face down image
FACE_DOWN_IMAGE = ":resources:images/cards/cardBack_red2.png"


def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card[0] in ["K", "Q", "J"]:
            value += 10
        elif card[0] == "A":
            num_aces += 1
        elif card[0] == "1":  # Only way to make "10" work
            value += 10
        else:
            value += int(card[0])

    for ace in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value


def deal_card():
    value = random.choice(CARD_VALUES)
    suit = random.choice(CARD_SUITS)
    return f"{value} of {suit}"


class Main_Menu(arcade.View):
    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        # Picture from Google Images
        self.texture = arcade.load_texture("hjciyalf_screen.jpg")

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = InstructionView()
        self.window.show_view(game_view)


class InstructionView(arcade.View):
    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.color.RED_DEVIL)

        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("Hit until you think you can beat the Dealer", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("The magic number is 21", self.window.width / 2, self.window.height / 2 - 50,
                         arcade.color.BLACK,
                         font_size=30, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2 - 90,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.player_hand = []
        self.dealer_hand = []
        self.player_wins = 0
        self.dealer_wins = 0

        self.game_over = False

        # Load card images
        self.card_images = {}
        for suit in CARD_SUITS:
            for value in CARD_VALUES:
                cards = f":resources:images/cards/card{suit}{value}.png"
                self.card_images[f"{value} of {suit}"] = arcade.load_texture(cards)

        # Button dimensions
        self.button_width = 100
        self.button_height = 40

        # Button positions
        self.hit_button_pos = (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT // 2)
        self.stand_button_pos = (SCREEN_WIDTH * 0.8, SCREEN_HEIGHT // 2)
        self.new_hand_pos = (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT // 2)

        # Load the background ambiance
        # Sound clip from Pixabay
        self.background_ambiance = arcade.load_sound("casino-ambiance-19130.mp3")
        arcade.play_sound(self.background_ambiance)

        arcade.set_background_color(arcade.color.RED_DEVIL)

    def setup(self):
        # Initialize player and dealer hands
        self.player_hand = [deal_card(), deal_card()]
        self.dealer_hand = [deal_card(), deal_card()]

    def display_hand(self, hand, center_x, center_y, hide_second_card=False):
        total_hand_width = max(len(hand) * (CARD_WIDTH + 10) - 10, CARD_WIDTH)  # Ensure it starts centered
        start_x = center_x - total_hand_width / 2

        for i, card in enumerate(hand):
            texture = self.card_images[card]
            x_position = int(start_x + i * (CARD_WIDTH + 10))

            # Hide the dealer's second card
            if hide_second_card and center_y == SCREEN_HEIGHT - CARD_HEIGHT and i == 1 and not self.game_over:
                texture = arcade.load_texture(FACE_DOWN_IMAGE)

            arcade.draw_texture_rectangle(x_position, center_y, CARD_WIDTH, CARD_HEIGHT, texture)

    def check_for_blackjack(self):
        if not self.game_over:
            player_value = calculate_hand_value(self.player_hand)
            if player_value == 21 and len(self.player_hand) == 2:
                # Blackjack!
                print("Blackjack! You win!")
                self.player_wins += 1
                self.game_over = True

    def check_for_dealer_blackjack(self):
        if not self.game_over:
            dealer_value = calculate_hand_value(self.dealer_hand)
            if dealer_value == 21 and len(self.dealer_hand) == 2:
                print("Dealer has Blackjack! You lose.")
                self.dealer_wins += 1
                self.game_over = True

    def draw_button(self, label, pos, button_color=arcade.color.LIGHT_GRAY):
        # Draw button background
        arcade.draw_rectangle_filled(pos[0], pos[1], self.button_width, self.button_height, button_color)

        # Draw button label
        arcade.draw_text(label, pos[0], pos[1], arcade.color.BLACK, font_size=14,
                         anchor_x="center", anchor_y="center", width=self.button_width)

    def on_draw(self):
        arcade.start_render()

        # Display player's and dealer's hands
        self.display_hand(self.player_hand, SCREEN_WIDTH // 2 + 50, BOTTOM_Y)
        self.display_hand(self.dealer_hand, SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - CARD_HEIGHT, hide_second_card=True)

        # Draw buttons
        if not self.game_over:
            self.draw_button("Hit", self.hit_button_pos)
            self.draw_button("Stand", self.stand_button_pos)
        if self.game_over:
            self.draw_button("New Hand", self.new_hand_pos)

        # Display text
        self.display_text()

        # Check for blackjack
        self.check_for_blackjack()
        self.check_for_dealer_blackjack()

    def on_mouse_press(self, x, y, button, key_modifiers):
        if (self.new_hand_pos[0] - self.button_width / 2 < x < self.new_hand_pos[0] + self.button_width / 2 and
                self.new_hand_pos[1] - self.button_height / 2 < y < self.new_hand_pos[1] + self.button_height / 2):
            self.reset_game()

        if not self.game_over:
            # Check if the mouse click is within the hit button bounds
            if (self.hit_button_pos[0] - self.button_width / 2 < x < self.hit_button_pos[0] + self.button_width / 2 and
                    self.hit_button_pos[1] - self.button_height / 2 < y < self.hit_button_pos[1] +
                    self.button_height / 2):
                self.on_hit_button_click()

            # Check if the mouse click is within the stand button bounds
            elif (self.stand_button_pos[0] - self.button_width / 2 < x < self.stand_button_pos[
                0] + self.button_width / 2 and
                  self.stand_button_pos[1] - self.button_height / 2 < y < self.stand_button_pos[
                      1] + self.button_height / 2):
                self.on_stand_button_click()

    def display_text(self):
        # Display text for player's hand value
        player_value = calculate_hand_value(self.player_hand)
        arcade.draw_text(f"Your hand value: {player_value}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 165,
                         arcade.color.BLACK, font_size=16, anchor_x="center")
        # Display text for dealer's potential or actual hand value
        dealer_known_value = calculate_hand_value([self.dealer_hand[0]])
        dealer_potential_value = dealer_known_value + 10

        if not self.game_over:
            # Display potential value if the game is not over
            arcade.draw_text(f"Dealer's potential value: {dealer_potential_value}",
                             SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, arcade.color.BLACK, font_size=16,
                             anchor_x="center")
        else:
            # Display actual value underneath the dealer's hand after the game is over
            dealer_actual_value = calculate_hand_value(self.dealer_hand)
            arcade.draw_text(f"Dealer's actual value: {dealer_actual_value}",
                             SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, arcade.color.BLACK, font_size=16,
                             anchor_x="center")

        # Display total wins counter
        arcade.draw_text(f"Player Wins: {self.player_wins}", 10, 10, arcade.color.BLACK, font_size=16)
        arcade.draw_text(f"Dealer Wins: {self.dealer_wins}", 635, 10, arcade.color.BLACK,
                         font_size=16)

    def on_hit_button_click(self):
        # Handle hit button click
        self.player_hand.append(deal_card())

        # Check for bust
        if calculate_hand_value(self.player_hand) > 21:
            print("Bust! You lose.")
            self.dealer_wins += 1

        # Set game_over to True after the player busts
        if calculate_hand_value(self.player_hand) > 21:
            self.game_over = True

    def on_stand_button_click(self):
        # Handle stand button click
        # Dealer's turn
        while calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(deal_card())

        # Display final hands
        self.display_hand(self.player_hand, START_X, BOTTOM_Y)
        self.display_hand(self.dealer_hand, START_X, SCREEN_HEIGHT - BOTTOM_Y - CARD_HEIGHT)

        # Determine the winner
        player_value = calculate_hand_value(self.player_hand)
        dealer_value = calculate_hand_value(self.dealer_hand)

        if dealer_value > 21:
            print("Dealer bust! You win!")
            self.player_wins += 1
        elif player_value > 21:
            print("You bust! You lose!")
            self.dealer_wins += 1
        elif player_value > dealer_value:
            print("You win!")
            self.player_wins += 1
        elif player_value < dealer_value:
            print("You lose.")
            self.dealer_wins += 1
        else:
            print("It's a tie.")

        # Set game_over to True after the player stands
        self.game_over = True

    def reset_game(self):
        # Store hand values before clearing hands
        player_value = calculate_hand_value(self.player_hand)
        dealer_value = calculate_hand_value(self.dealer_hand)

        # Clear hands
        self.player_hand = []
        self.dealer_hand = []

        # Display hand values before reset
        print(f"Player's hand value: {player_value}")
        print(f"Dealer's hand value: {dealer_value}")

        print("Next Deal!")

        # Set up a new game
        self.setup()

        # Reset the game_over flag to False
        self.game_over = False


def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT - 50, SCREEN_TITLE)
    start_view = Main_Menu()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
