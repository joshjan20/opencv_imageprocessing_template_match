```markdown
# Template Matching with OpenCV

This Python project demonstrates template matching using OpenCV. Template matching is a technique in computer vision to find the location of a template image within a larger image. The script matches a small image (template) to a larger image using multiple matching methods provided by OpenCV.

## Features

- **Template Matching**: Matches a template image (e.g., an object) to a larger image (e.g., a scene).
- **Different Matching Methods**: Uses six different template matching methods from OpenCV to compare results.
- **Visualization**: Draws rectangles around the best match for each method and displays the result.

## Requirements

- Python 3.x
- OpenCV
- NumPy

You can install the required packages using `pip`:

```bash
pip install opencv-python numpy
```

## How to Run

1. Clone this repository or download the script.
2. Provide the paths to your main image and the template image in the code (`soccer_practice.jpg` and `shoe2.PNG`).
3. Run the script using Python:

```bash
python main.py
```

4. The result will be displayed in a window showing the detected match for each method. Press any key to close the window and proceed to the next method.

## Code Breakdown

### Template Matching

```python
import numpy as np
import cv2

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('assets/shoe2.PNG', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

### Explanation

1. **Image Loading and Resizing**:
   - The script loads the main image (`soccer_practice.jpg`) and the template image (`shoe2.PNG`), then resizes both to 80% of their original size.

2. **Template Matching Methods**:
   - The script uses six different OpenCV template matching methods:
     - `cv2.TM_CCOEFF`
     - `cv2.TM_CCOEFF_NORMED`
     - `cv2.TM_CCORR`
     - `cv2.TM_CCORR_NORMED`
     - `cv2.TM_SQDIFF`
     - `cv2.TM_SQDIFF_NORMED`

3. **Matching and Drawing**:
   - For each method, the script matches the template to the image and draws a rectangle around the best match location.

4. **Result Display**:
   - The result for each method is displayed in a window. Press any key to close the current match window and continue to the next method.

## Example Output

The output window will display the main image with a rectangle drawn around the area where the template matches, using each method in sequence.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
