from typing import List, Tuple
import numpy as np


class DataTransformer:
    """Library for removing pixel offset variance."""

    def centre_canvas(
        canvas: List[int], tile_x_amount: int, tile_y_amount: int
    ) -> List[int]:
        """
        Generates a new list of pixels that are translated towards the centre
        of the canvas to eliminate offset variance.
        """
        # Do nothing if canvas is empty
        if np.sum(canvas) == 0:
            return canvas

        centre_x, centre_y = DataTransformer._find_centre_pixel(
            canvas, tile_x_amount
        )
        # Get the centre tile index as if there is no pixel drawing
        canvas_centre_x = (tile_x_amount - 1) // 2
        canvas_centre_y = (tile_y_amount - 1) // 2
        off_set = (
            canvas_centre_x - centre_x,
            canvas_centre_y - centre_y,
        )
        # Shift the pixels towards the centre of the canvas
        new_pixels = DataTransformer._shift_pixels(
            canvas, off_set, tile_x_amount, tile_y_amount
        )
        return new_pixels

    def _find_centre_pixel(
        canvas: List[int], tile_x_amount: int
    ) -> Tuple[int, int]:
        """
        Get the centre tile index location of the pixel drawing on the
        canvas.
        """
        sum_xdx = sum_ydy = dx = pixel_count = 0
        dy = -1
        # Find the centre of the drawn pixels using the centre of gravity
        # formula
        for i in range(len(canvas)):
            if i % tile_x_amount == 0:
                dx = 0
                dy += 1
            if canvas[i]:
                pixel_count += 1
                sum_xdx += dx
                sum_ydy += dy
            dx += 1

        centre = sum_xdx // pixel_count, sum_ydy // pixel_count
        return centre

    def _shift_pixels(
        canvas: List[int],
        off_set: Tuple[int, int],
        tile_x_amount: int,
        tile_y_amount: int,
    ) -> List[int]:
        """
        Shift the pixel centre of the drawing towards to centre of the
        canvas.
        """
        new_canvas = [0] * len(canvas)
        for i in range(len(canvas)):
            if canvas[i]:
                new_location = i + off_set[0] + off_set[1] * tile_x_amount
                # Ignore if out of bounds
                tile_amount = tile_x_amount * tile_y_amount
                if 0 <= new_location < tile_amount:
                    new_canvas[new_location] = 1
        return new_canvas
