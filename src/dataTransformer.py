import numpy as np
import src.constants as c


class DataTransformer:

    # Moves the pixels towards the centre of the canvas (offset invariance)
    @staticmethod
    def centre_canvas(canvas):
        # Do nothing if canvas is empty
        if np.sum(canvas) == 0:
            return canvas

        pixel_centre = DataTransformer._find_centre_pixel(canvas)
        canvas_centre = (c.TILE_X_AMOUNT - 1) // 2, (c.TILE_Y_AMOUNT - 1) // 2
        off_set = (canvas_centre[0] - pixel_centre[0], canvas_centre[1] - pixel_centre[1])
        new_pixels = DataTransformer._shift_pixels(canvas, off_set)
        return new_pixels

    @staticmethod
    def _find_centre_pixel(canvas):
        sum_xdx = sum_ydy = dx = pixel_count = 0
        dy = -1
        # Find the centre of the drawn pixels
        for i in range(len(canvas)):
            if i % c.TILE_X_AMOUNT == 0:
                dx = 0
                dy += 1
            if canvas[i]:
                pixel_count += 1
                sum_xdx += dx
                sum_ydy += dy
            dx += 1
        
        centre = sum_xdx // pixel_count, sum_ydy // pixel_count
        return centre

    @staticmethod
    def _shift_pixels(canvas, off_set):
        new_canvas = [0] * len(canvas)
        for i in range(len(canvas)):
            if canvas[i]:
                new_location = i + off_set[0] + off_set[1] * c.TILE_X_AMOUNT
                # Ignore if out of bounds
                if 0 <= new_location < c.TILE_AMOUNT:
                    new_canvas[new_location] = 1
        return new_canvas
