import cv2
from colors import COLOR_RED


def draw_contours_b(image,
                  coordinates,
                  label,
                  font_color,
                  border_color=COLOR_RED,
                  line_thickness=1,
                  font=cv2.FONT_HERSHEY_SIMPLEX,
                  font_scale=0.5):
    cv2.drawContours(image,
                     [coordinates],
                     contourIdx=-1,
                     color=border_color,
                     thickness=2,
                     lineType=cv2.LINE_8)
    moments = cv2.moments(coordinates)

    center = (int(moments["m10"] / moments["m00"]) - 3,
              int(moments["m01"] / moments["m00"]) + 3)

    cv2.putText(image,
                label,
                center,
                font,
                font_scale,
                font_color,
                line_thickness,
                cv2.LINE_AA)
