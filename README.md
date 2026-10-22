# CEAM-TASK-PHASE-PART-1-IMAGE-PROCESSOR-5X5-MATRIX-
NAME-Zayaan Husain Azad
261580050488
My CEAM task phase image processor takes a 5x5 grid as an input and can perform one of 6 functions upon it:
1. Image inversion- the values of the 5x5 grid range from 0 to 255 so the inversion works by adjusting each pixel to become 255- its original value.
2. Image brightnening/darkening- Works by adjusting the value of the grid by a flat value, positivee or negative, whilst staying in the 0 to 255 limit.
3. Image thresholding- The user will input a threshold value and then the values of the grid above and equal to that value become brightest and all that do not qualify become darkest.
4. Image blurring- utilises a 3x3 kernel to create a mean blurring effect where all numbers within the 3x3 grid are averaged out with equal weight, and the mean value is then applied to the origin, which is the center of the 3x3 grid. This is repeated for all elements of the image.
Edge detection of image: A mirrroring method was used for edge detection, when the kernel requires a pixel which is, for example, 1 pixel out of bounds, then the pixel which is 1 unit in bounds is mirrored. This maeks the edges have a much smoother gradient as apposed to applying a boundary of zeroes at edges which can give harsh black lines at the edges.
5. Image rotation- Clockwise rotation is achieved by taking the transpose of the matrix aand then horizontally reversing each row. the process is done in reverse for anti-clockwise rotation.
6. Image Flip- horizontal flipping is achieved via the inbuilt reverse(0 function, the vertical flip is achieved via swapping of corresponding horizontal elements
