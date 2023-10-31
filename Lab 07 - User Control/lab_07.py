import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_road():
    # Draw the highway
    arcade.draw_rectangle_filled(400, 300, 300, SCREEN_HEIGHT, arcade.color.GRAY)


def draw_road_lines():
    # Draw the yellow road lines
    line_width = 10
    num_lines = 10
    gap = SCREEN_HEIGHT // num_lines

    for num_lines in range(num_lines + 1):
        y = num_lines * gap
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, y, line_width, gap - 10, arcade.color.YELLOW)


def draw_car(car):
    """ Draw the cars with the instance variables we have. """
    car_width = 40
    car_height = 100

    # Draw the car wheels (circles)
    wheel_radius = 10
    wheel_offset = 23
    arcade.draw_circle_filled(car.position_x - wheel_offset, car.position_y - wheel_offset, wheel_radius,
                              arcade.color.BLACK)
    arcade.draw_circle_filled(car.position_x + wheel_offset, car.position_y - wheel_offset, wheel_radius,
                              arcade.color.BLACK)
    arcade.draw_circle_filled(car.position_x - wheel_offset, car.position_y + wheel_offset, wheel_radius,
                              arcade.color.BLACK)
    arcade.draw_circle_filled(car.position_x + wheel_offset, car.position_y + wheel_offset, wheel_radius,
                              arcade.color.BLACK)

    # Draw the car body (rectangle)
    arcade.draw_rectangle_filled(car.position_x, car.position_y, car_width, car_height, arcade.color.RED)
    arcade.draw_rectangle_filled(car.position_x, car.position_y + 35, car_width - 10, car_height // 2, arcade.color.RED)
    arcade.draw_rectangle_filled(car.position_x, car.position_y + 25, car_width - 10, car_height // 3,
                                 arcade.color.BLACK)


def draw_car2(car2):
    # Draw the second car
    car2_width = 40
    car2_height = 100

    # Draw the car wheels (circles)
    wheel_radius = 10
    wheel_offset = 23
    arcade.draw_circle_filled(car2.position_x - wheel_offset, car2.position_y - wheel_offset, wheel_radius,
                              arcade.color.BLACK)
    arcade.draw_circle_filled(car2.position_x + wheel_offset, car2.position_y - wheel_offset, wheel_radius,
                              arcade.color.BLACK)
    arcade.draw_circle_filled(car2.position_x - wheel_offset, car2.position_y + wheel_offset, wheel_radius,
                              arcade.color.BLACK)
    arcade.draw_circle_filled(car2.position_x + wheel_offset, car2.position_y + wheel_offset, wheel_radius,
                              arcade.color.BLACK)

    # Draw the car body (rectangle)
    arcade.draw_rectangle_filled(car2.position_x, car2.position_y, car2_width, car2_height, arcade.color.BLUE)
    arcade.draw_rectangle_filled(car2.position_x, car2.position_y - 35, car2_width - 10, car2_height // 2,
                                 arcade.color.BLUE)
    arcade.draw_rectangle_filled(car2.position_x, car2.position_y - 25, car2_width - 10, car2_height // 3,
                                 arcade.color.BLACK)


class Car:
    def __init__(self, position_x, position_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius


class Car2:
    def __init__(self, position_x, position_y, change_x, change_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

    def move_up(self):
        self.position_y += MOVEMENT_SPEED

    def move_down(self):
        self.position_y -= MOVEMENT_SPEED

    def move_left(self):
        self.position_x -= MOVEMENT_SPEED

    def move_right(self):
        self.position_x += MOVEMENT_SPEED


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        self.horn_sound = arcade.load_sound("car-horn-beep-beep-two-beeps-honk-honk-6188.mp3")
        self.crash_sound = arcade.load_sound("clank-car-crash-collision-6206.mp3")

        arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)

        # Create the cars
        self.car = Car(475, 50, 15)
        self.car2 = Car2(325, 550, 0, 0, 15)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        draw_road()
        draw_road_lines()
        draw_car(self.car)
        draw_car2(self.car2)

    def update(self, delta_time):
        self.car2.update()
        if self.car2.position_x < 0 or self.car2.position_x > SCREEN_WIDTH or \
                self.car2.position_y < 0 or self.car2.position_y > SCREEN_HEIGHT:
            arcade.play_sound(self.crash_sound)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.car.position_x = x
        self.car.position_y = y

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """
        if key == arcade.key.W:
            self.car2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.car2.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.car2.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.car2.change_x = MOVEMENT_SPEED
        if key == arcade.key.SPACE:
            arcade.play_sound(self.horn_sound)

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.car2.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.car2.change_y = 0


def main():
    window = MyGame(800, 600, "Controllable Cars")
    arcade.run()


main()
