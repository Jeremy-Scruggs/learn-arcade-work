import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 2
SPRITE_SCALING_COIN = .25
SPRITE_SCALING_BAD_COIN = .05
COIN_COUNT = 50
BAD_COIN_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Dodge and Collect"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.coin_sound = arcade.load_sound("smw_coin.wav")
        self.bad_coin_sound = arcade.load_sound("smw_blargg_no_echo.wav")

        self.player_list = None
        self.coin_list = None
        self.bad_coin_list = None

        self.player_sprite = None
        self.score = 0
        self.game_over = False

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()

        # Score
        self.score = 0
        self.game_over = False

        # Set up the player
        self.player_sprite = arcade.Sprite("cfefc63c-3610-4768-a547-d7f18137094f.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for Coins in range(COIN_COUNT):
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Set initial velocity for the coin
            coin.change_x = 3
            coin.change_y = 0

            # Add the coins to the list
            self.coin_list.append(coin)

        for Bad_coins in range(BAD_COIN_COUNT):
            bad_coin = arcade.Sprite("evil_coin__png__by_elementerused_dfb00c3-375w-2x.png", SPRITE_SCALING_BAD_COIN)

            bad_coin.center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Set initial velocity for the bad coin
            bad_coin.change_x = 0
            bad_coin.change_y = random.choice([-2, 2])  # Moves up or down randomly

            self.bad_coin_list.append(bad_coin)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.player_list.draw()

        if not self.game_over:
            self.coin_list.draw()
            self.bad_coin_list.draw()

            # Put the score on the screen
            output = f"Score: {self.score}"
            arcade.draw_text(text=output, start_x=10, start_y=20, color=arcade.color.WHITE, font_size=14)
        else:
            output = f"{self.score}"
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED,
                             font_size=50, anchor_x="center")
            arcade.draw_text("Final Score", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, arcade.color.RED,
                             font_size=30, anchor_x="center")
            arcade.draw_text(text=output, start_x=SCREEN_WIDTH // 2 - 25, start_y=SCREEN_HEIGHT // 2 - 150,
                             color=arcade.color.WHITE, font_size=25)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if not self.game_over:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """
        if not self.game_over:
            self.coin_list.update()
            self.bad_coin_list.update()

        # Check for collisions with player
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        bad_coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_coin_list)

        # Handle coin collisions
        for coin in coins_hit_list:
            arcade.play_sound(self.coin_sound)
            coin.remove_from_sprite_lists()
            self.score += 1

        # Handle bad coin collisions
        for bad_coin in bad_coins_hit_list:
            arcade.play_sound(self.bad_coin_sound)
            bad_coin.remove_from_sprite_lists()
            self.score -= 1

        # Check for coins reaching the screen edges and bounce
        for coin in self.coin_list:
            if coin.right > SCREEN_WIDTH or coin.left < 0:
                coin.change_x *= -1

        # Check for bad coins reaching the screen edges and bounce
        for bad_coin in self.bad_coin_list:
            if bad_coin.top > SCREEN_HEIGHT or bad_coin.bottom < 0:
                bad_coin.change_y *= -1

        # Check if the coin list is empty
        if len(self.coin_list) == 0:
            self.game_over = True


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
