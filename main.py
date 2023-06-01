import pyautogui
import keyboard  # using module keyboard
from fpdf import FPDF
pdf = FPDF()
screenshot_num = 0
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shownq
        if keyboard.is_pressed('s'):  # if key 'q' is pressed 
            print('You made a screenshot!')
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(rf"C:\Users\desa01\1Projects\3utils\screenshots2prezi\pics\screenshot_{screenshot_num}.png")
            screenshot_num += 1
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('Quitting!')
            # imagelist is the list with all sqimage filenames
            for i in range(screenshot_num):
                pdf.add_page()
                image = f"pics\screenshot_{i}.png"
                pdf.image(image,x=0,y=0,w=210)
                # pdf.image(image)
            pdf.output("yourfile.pdf", "F")
            break
    except:
        break  # if user pressed a key other than the given key the loop will break
