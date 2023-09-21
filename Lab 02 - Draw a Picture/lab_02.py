"""
This is a picture of a highway surrounded by trees on either side
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Highway Between The Trees"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)

arcade.start_render()

# Draw the highway
arcade.draw_rectangle_filled(400, 300, 300, SCREEN_HEIGHT, arcade.color.GRAY)

# Draw the yellow road lines
line_width = 10
num_lines = 10
gap = SCREEN_HEIGHT // num_lines

for num_lines in range(num_lines + 1):
    y = num_lines * gap
    arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, y, line_width, gap - 10, arcade.color.YELLOW)

# Draw tree tops on the sides of the highway
tree_top_radius = 45
tree_spacing: int = 150

# Draw tree tops on the left side
for trees in range(0, SCREEN_HEIGHT + tree_spacing, tree_spacing):
    arcade.draw_circle_filled(50, trees, tree_top_radius, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(175, trees, tree_top_radius, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(115, trees + 75, tree_top_radius, arcade.color.DARK_GREEN)
# Draw tree tops on the right side
    arcade.draw_circle_filled(750, trees, tree_top_radius, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(625, trees, tree_top_radius, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(690, trees + 75, tree_top_radius, arcade.color.DARK_GREEN)

arcade.finish_render()
arcade.run()