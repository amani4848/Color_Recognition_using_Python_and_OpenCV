This is a simple Python project that uses OpenCV to recognize colors in a video. When you run the program, a video will open. You can click anywhere on the video, and it will show you the RGB color of the pixel you clicked. The color will appear in a rectangle with its red, green, and blue values.

**Files**

- `color_recognition.py` the main Python file
- `red_flower.mp4` video file (you can use any video with a different name)
- `launch.json` optional, for running the project easily from VS Code

**How to Run**

1. Make sure Python is installed.
2. Install OpenCV with this command:
  ```
   pip install opencv-python
   ```
3. Put the video file in the same folder as the Python file.
4. Open a terminal in the project folder.
5. Run the code:
  ```
   python color_recognition.py
   ```
**What Happens**

- The video plays in a new window.
- Click anywhere inside the video.
- A rectangle appears with the color you clicked.
- RGB values (like R=255 G=0 B=0) are shown on the screen.

**Notes**

- Run the code from the terminal, not the Run button in VS Code.
- If the video doesn't load, make sure the filename is correct and it's in the same folder as the Python file.

**Skills You Learn**

- Using OpenCV with Python  
- Reading and displaying video files  
- Handling mouse click events  
- Getting pixel color values (RGB)  

*This project is great for beginners to learn how to use OpenCV for color detection.* *

**Demo Video**
![Demo Video](https://github.com/user-attachments/assets/046dd535-62fb-46e6-8abf-ca119885e9f6)
