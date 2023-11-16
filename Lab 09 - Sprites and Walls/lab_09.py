import arcade
import random

# --Constants--
SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Sprites and Walls"

NUMBER_OF_COINS = 10

MOVEMENT_SPEED = 5


class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        self.wall_list = None
        self.coin_list = None


def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()

    # Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/brickBrown.png",
                                 SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite(":resources:images/tiles/brickBrown.png",
                                     SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in range(157, 800, 64):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 480
        room.wall_list.append(wall)

    for x in range(285, 800, 64):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 415
        room.wall_list.append(wall)

    for x in range(285, 800, 64):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 96
        room.wall_list.append(wall)

    for x in range(350, 650, 64):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 225
        room.wall_list.append(wall)

    for x in range(735, 820, 64):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 225
        room.wall_list.append(wall)

    for y in range(64, 350, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.left = 125
        wall.bottom = y
        room.wall_list.append(wall)

    for y in range(64, 159, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.left = 190
        wall.bottom = y
        room.wall_list.append(wall)

    for y in range(255, 500, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.left = 255
        wall.bottom = y
        room.wall_list.append(wall)

    for y in range(255, 500, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.left = 320
        wall.bottom = y
        room.wall_list.append(wall)

    # Create the coins
    for coins in range(NUMBER_OF_COINS):

        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

        # Boolean variable if we successfully placed the coin
        coin_placed_successfully = False

        # Keep trying until success
        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)

            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                coin_placed_successfully = True

        # Add the coin to the lists
        room.coin_list.append(coin)

    # Load the background image for this level.
    room.background = arcade.load_texture(":resources:images/backgrounds/"
                                          "abstract_1.jpg")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    # Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

    for x in range(735, 820, 64):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 225
        room.wall_list.append(wall)

    for x in range(95, 300, 64):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 415
        room.wall_list.append(wall)

    for x in range(352, 600, 64):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 160
        room.wall_list.append(wall)

    for x in range(671, 790, 64):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 162
        room.wall_list.append(wall)

    for x in range(608, 650, 64):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 285
        room.wall_list.append(wall)

    for x in range(608, 800, 64):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 349
        room.wall_list.append(wall)

    for y in range(128, 500, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.left = 320
        wall.bottom = y
        room.wall_list.append(wall)

    for y in range(64, 200, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.left = 190
        wall.bottom = y
        room.wall_list.append(wall)

    for y in range(190, 450, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.left = 512
        wall.bottom = y
        room.wall_list.append(wall)

    for y in range(380, 500, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
        wall.left = 703
        wall.bottom = y
        room.wall_list.append(wall)

    # Create the coins
    for coins in range(NUMBER_OF_COINS):

        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

        # Boolean variable if we successfully placed the coin
        coin_placed_successfully = False

        # Keep trying until success
        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)

            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                coin_placed_successfully = True

        # Add the coin to the lists
        room.coin_list.append(coin)

    return room


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING

    def update(self):
        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        self.coin_sound = arcade.load_sound("smw_coin.wav")

        # Sprite lists
        self.total_coins = 0
        self.current_room = 0
        self.game_over = False

        # Set up the player
        self.rooms = None
        self.coin_list = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("cfefc63c-3610-4768-a547-d7f18137094f.png", 3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.coin_list = arcade.SpriteList()

        # Our list of rooms
        self.rooms = []

        # Create the rooms.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        # Starting room number
        self.current_room = 0
        
        # Starting coin count
        self.total_coins = 0

        self.game_over = False

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.rooms[self.current_room].wall_list)

    def on_draw(self):
        self.clear()

        if not self.game_over:
            # Draw the background texture
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                SCREEN_WIDTH, SCREEN_HEIGHT,
                                                self.rooms[self.current_room].background)

            # Draw all the walls in this room
            self.rooms[self.current_room].wall_list.draw()
            self.rooms[self.current_room].coin_list.draw()
            self.player_list.draw()

            # Draw UI for total coins collected
            total_coins_text = f"Coins Collected: {self.total_coins}"
            arcade.draw_text(total_coins_text, 10, 10, arcade.color.WHITE, 14)
        else:
            output = f"{self.total_coins}"
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED,
                             font_size=50, anchor_x="center")
            arcade.draw_text("Final Score", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, arcade.color.RED,
                             font_size=30, anchor_x="center")
            arcade.draw_text(text=output, start_x=SCREEN_WIDTH // 2 - 25, start_y=SCREEN_HEIGHT // 2 - 150,
                             color=arcade.color.WHITE, font_size=25)

    def update_player_speed(self):
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        # Check for collisions between player and coins in the current room
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.rooms[self.current_room].coin_list)

        # Handle coin collection logic
        for coin in coin_hit_list:
            arcade.play_sound(self.coin_sound)
            coin.remove_from_sprite_lists()
            self.total_coins += 1  # Increase total coins when a coin is collected

        # Check if the coin list is empty
        if self.total_coins == 20:
            self.game_over = True

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
