# CEAM-TASK-PHASE-PART-1-IMAGE-PROCESSOR-5X5-MATRIX-
NAME-Zayaan Husain Azad
261580050488
My CEAM task phase image processor takes a 5x5 grid as an input and can perform one of 6 functions upon it:
1. **Image inversion**- the values of the 5x5 grid range from 0 to 255 so the inversion works by adjusting each pixel to become 255- its original value.
   example- input image:
[38, 97, 131, 0, 251]

[146, 130, 6, 108, 191]

[206, 126, 71, 185, 39]

[40, 181, 21, 46, 139]

[167, 12, 181, 86, 36]

inverted list:

[217, 158, 124, 255, 4]

[109, 125, 249, 147, 64]

[49, 129, 184, 70, 216]

[215, 74, 234, 209, 116]

[88, 243, 74, 169, 219]

3. **Image brightnening/darkening**- Works by adjusting the value of the grid by a flat value, positivee or negative, whilst staying in the 0 to 255 limit.
   input image:
[230, 163, 149, 144, 61]

[217, 76, 153, 229, 21]

[76, 226, 116, 253, 237]

[112, 44, 86, 19, 166]

[195, 93, 180, 101, 4]

Do you want to darken or brighten[D/B]:D 

Darken by how many units?200

Changed image:
[30, 0, 0, 0, 0]

[17, 0, 0, 29, 0]

[0, 26, 0, 53, 37]

[0, 0, 0, 0, 0]

[0, 0, 0, 0, 0]

5. **Image thresholding**- The user will input a threshold value and then the values of the grid above and equal to that value become brightest and all that do not qualify become darkest.
   input image:
[191, 243, 210, 136, 41]

[190, 60, 230, 215, 89]

[208, 179, 16, 79, 170]

[254, 115, 114, 46, 248]

[171, 68, 244, 104, 9]

Enter threshold value:155

Image with threshold applied:

[255, 255, 255, 0, 0]

[255, 0, 255, 255, 0]

[255, 255, 0, 0, 255]

[255, 0, 0, 0, 255]

[255, 0, 255, 0, 0]

7. **Image blurring**- utilises a 3x3 kernel to create a mean blurring effect where all numbers within the 3x3 grid are averaged out with equal weight, and the mean value is then applied to the origin, which is the center of the 3x3 grid. This is repeated for all elements of the image.
  input image:            

[26, 242, 177, 118, 129]

[213, 219, 66, 55, 112]

[21, 47, 113, 42, 223]

[244, 85, 250, 168, 86]

[251, 4, 205, 240, 247]

Blurred list:

[201, 160, 135, 98, 89]

[141, 124, 119, 115, 99]

[131, 139, 116, 123, 105]

[87, 135, 128, 174, 161]

[120, 179, 161, 188, 174]

**Edge detection of image:** A mirrroring method was used for edge detection, when the kernel requires a pixel which is, for example, 1 pixel out of bounds, then the pixel which is 1 unit in bounds is mirrored. This maeks the edges have a much smoother gradient as apposed to applying a boundary of zeroes at edges which can give harsh black lines at the edges.
9. **Image rotation**- Clockwise rotation is achieved by taking the transpose of the matrix aand then horizontally reversing each row. the process is done in reverse for anti-clockwise rotation.
    input image:

[42, 0, 75, 211, 125]

[175, 128, 5, 225, 97]

[50, 54, 91, 249, 240]

[252, 67, 246, 84, 77]

[5, 147, 225, 64, 103]

Rotate Anti-Clockwise or Clockwise [1/2]1

rotated image:

[125, 211, 75, 0, 42]

[97, 225, 5, 128, 175]

[240, 249, 91, 54, 50]

[77, 84, 246, 67, 252]

[103, 64, 225, 147, 5]

11. **Image Flip**- horizontal flipping is achieved via the inbuilt reverse(0 function, the vertical flip is achieved via swapping of corresponding horizontal elements
    input image:

[151, 62, 128, 37, 77]

[114, 51, 143, 12, 113]

[202, 23, 89, 49, 236]

[169, 163, 81, 177, 179]

[173, 102, 4, 166, 155]

Do you want vertical or horizontal flip?[1/2]1

Vertically rotated image:

[173, 102, 4, 166, 155]

[169, 163, 81, 177, 179]

[202, 23, 89, 49, 236]

[114, 51, 143, 12, 113]
[151, 62, 128, 37, 77]
