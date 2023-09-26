import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Highway Between The Trees"

# Initialize car_y and y_direction
car_y = 300
y_direction = 1

# Initialize car variables for the second car
car2_x = 325  # Adjust the initial x-coordinate for the second car
car2_y = 300  # Adjust the initial y-coordinate for the second car
car2_y_direction = -1  # Car 2 moves in the opposite direction


def draw_road():
    # Draw the highway
    arcade.draw_rectangle_filled(400, 300, 300, SCREEN_HEIGHT, arcade.color.GRAY)


def draw_car(x, y):
    car_x = 475
    car_width = 40
    car_height = 100

    # Draw the car wheels (circles)
    wheel_radius = 10
    wheel_offset = 23
    arcade.draw_circle_filled(car_x - wheel_offset + x, car_y - wheel_offset + y, wheel_radius, arcade.color.BLACK)
    arcade.draw_circle_filled(car_x + wheel_offset + x, car_y - wheel_offset + y, wheel_radius, arcade.color.BLACK)
    arcade.draw_circle_filled(car_x - wheel_offset + x, car_y + wheel_offset + y, wheel_radius, arcade.color.BLACK)
    arcade.draw_circle_filled(car_x + wheel_offset + x, car_y + wheel_offset + y, wheel_radius, arcade.color.BLACK)

    # Draw the car body (rectangle)
    arcade.draw_rectangle_filled(car_x + x, car_y + y, car_width, car_height, arcade.color.RED)
    arcade.draw_rectangle_filled(car_x + x, car_y + 35, car_width - 10, car_height // 2, arcade.color.RED)
    arcade.draw_rectangle_filled(car_x + x, car_y + 25, car_width - 10, car_height // 3, arcade.color.BLACK)


def draw_second_car(x, y):
    # Draw the second car
    car2_x = 325  # Adjust the x-coordinate for the second car
    car2_width = 40
    car2_height = 100

    # Draw the car wheels (circles)
    wheel_radius = 10
    wheel_offset = 23
    arcade.draw_circle_filled(car2_x - wheel_offset + x, car2_y - wheel_offset + y, wheel_radius, arcade.color.BLACK)
    arcade.draw_circle_filled(car2_x + wheel_offset + x, car2_y - wheel_offset + y, wheel_radius, arcade.color.BLACK)
    arcade.draw_circle_filled(car2_x - wheel_offset + x, car2_y + wheel_offset + y, wheel_radius, arcade.color.BLACK)
    arcade.draw_circle_filled(car2_x + wheel_offset + x, car2_y + wheel_offset + y, wheel_radius, arcade.color.BLACK)

    # Draw the car body (rectangle)
    arcade.draw_rectangle_filled(car2_x + x, car2_y + y, car2_width, car2_height, arcade.color.BLUE)
    arcade.draw_rectangle_filled(car2_x + x, car2_y - 35, car2_width - 10, car2_height // 2, arcade.color.BLUE)
    arcade.draw_rectangle_filled(car2_x + x, car2_y - 25, car2_width - 10, car2_height // 3, arcade.color.BLACK)


def draw_road_lines():
    # Draw the yellow road lines
    line_width = 10
    num_lines = 10
    gap = SCREEN_HEIGHT // num_lines

    for num_lines in range(num_lines + 1):
        y = num_lines * gap
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, y, line_width, gap - 10, arcade.color.YELLOW)


def draw_trees():
    # Draw tree tops on the sides of the highway
    tree_top_radius = 45
    tree_spacing = 150

    # Draw tree tops on the left side
    for trees in range(0, SCREEN_HEIGHT + tree_spacing, tree_spacing):
        arcade.draw_circle_filled(50, trees, tree_top_radius, arcade.color.DARK_GREEN)
        arcade.draw_circle_filled(175, trees, tree_top_radius, arcade.color.DARK_GREEN)
        arcade.draw_circle_filled(115, trees + 75, tree_top_radius, arcade.color.DARK_GREEN)

    # Draw tree tops on the right side
    for trees in range(0, SCREEN_HEIGHT + tree_spacing, tree_spacing):
        arcade.draw_circle_filled(750, trees, tree_top_radius, arcade.color.DARK_GREEN)
        arcade.draw_circle_filled(625, trees, tree_top_radius, arcade.color.DARK_GREEN)
        arcade.draw_circle_filled(690, trees + 75, tree_top_radius, arcade.color.DARK_GREEN)


def on_draw(delta_time):
    """ Draw everything """
    global car_y, car2_y, y_direction

    arcade.start_render()

    draw_road()
    draw_car(0, 0)
    draw_second_car(0, 0)
    draw_road_lines()
    draw_trees()

    # Update car's vertical position
    car_y += y_direction * 3
    car2_y += car2_y_direction * 3

    # Check if the car has gone off the screen
    if car_y > 800:
        # Reset the car's position to the bottom
        car_y = SCREEN_HEIGHT - 700
    if car2_y < -100:
        car2_y = SCREEN_HEIGHT + 700


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)
    # Load the audio file
    background_music = arcade.Sound("249707-2a0a97d4-58d6-48e7-9c62-775443cbd4f5.mp3")

    arcade.schedule(on_draw, 1 / 60)

    arcade.play_sound(background_music)
    arcade.run()


main()