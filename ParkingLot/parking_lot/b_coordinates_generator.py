import cv2
import numpy as np

from colors import COLOR_WHITE
from drawing_utills_b import draw_contours_b


class Coordinates_b_Generator:
    KEY_RESET_B = ord("r")
    KEY_QUIT_B = ord("q")

    def __init__(self, images_b, output_b, color_b):
        self.caption_b = images_b
        self.output_b = output_b
        self.color_b = color_b

        self.images_b = cv2.imread(images_b).copy()
        self.click_count_b = 0
        self.ids_b = 0
        self.coordinates_b = []
        cv2.namedWindow(self.caption_b, cv2.WINDOW_GUI_EXPANDED)
        cv2.setMouseCallback(self.caption_b, self.__mouse_callback_b)

    def generate_b(self):
        while True:
            cv2.imshow(self.caption_b, self.images_b)
            key = cv2.waitKey(0)

            if key == Coordinates_b_Generator.KEY_RESET_B:
                self.images_b = self.images_b.copy()
            elif key == Coordinates_b_Generator.KEY_QUIT_B:
                break
        cv2.destroyWindow(self.caption_b)

    def __mouse_callback_b(self, event_b, x, y, flags, params):

        if event_b == cv2.EVENT_LBUTTONDOWN:
            self.coordinates_b.append((x, y))
            self.click_count_b += 1

            if self.click_count_b >= 4:
                self.__handle_done_b()

            elif self.click_count_b > 1:
                self.__handle_click_progress()

        cv2.imshow(self.caption_b, self.images_b)

    def __handle_click_progress(self):
        cv2.line(self.images_b, self.coordinates_b[-2], self.coordinates_b[-1], (255, 0, 0), 1)

    def __handle_done_b(self):
        cv2.line(self.images_b,
                 self.coordinates_b[2],
                 self.coordinates_b[3],
                 self.color_b,
                 1)
        cv2.line(self.images_b,
                 self.coordinates_b[3],
                 self.coordinates_b[0],
                 self.color_b,
                 1)

        self.click_count = 0

        coordinates_b = np.array(self.coordinates_b)

        self.output_b.write("-\n          id: " + str(self.ids_b) + "\n          coordinates: [" +
                            "[" + str(self.coordinates_b[0][0]) + "," + str(self.coordinates_b[0][1]) + "]," +
                            "[" + str(self.coordinates_b[1][0]) + "," + str(self.coordinates_b[1][1]) + "]," +
                            "[" + str(self.coordinates_b[2][0]) + "," + str(self.coordinates_b[2][1]) + "]," +
                            "[" + str(self.coordinates_b[3][0]) + "," + str(self.coordinates_b[3][1]) + "]]\n")

        draw_contours_b(self.images_b,
                        coordinates_b,
                        str(self.ids_b + 1),
                        COLOR_WHITE)

        for i in range(0, 4):
            self.coordinates_b.pop()

        self.ids_b += 1
