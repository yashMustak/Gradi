# Gradi
Graph digitizing python script 
---------------------------------------------------------------------------------------------------------------------------------------
### ```About```
This script helps to create a csv file for data points of any graph image provided. Follow the instructions below to use it.
GUI is yet to exist...

### ```Introducing Gradi```

**Let's take a dive to its working.**

**```1. Prerequisites:```** 
  * OpenCV (Python library)
  * numpy (Python library)
  * cvs (Python library)

**```2. Setup:```**
```
  Step 1 Download the script from github.
  Step 2 Make 2 new folders at same path where the script is present. 
         First named as "plotDataFiles" and second named as "plots".
  Step 3 Paste the image of graph which has to be digitized into the "graphs" folder.
  Step 4 Run the script using either IDLE (Text editor come along python) or command line.
```

**```3. How to use:```**
  1. First of all it will ask the name of graph image with its extension.
  2. Now the graph image is open (if not poped up watch it somewhere behind the open windows).
    ***```CAUTION: DO NOT CLICK TWICE ON THE POPED UP IMAGE BEFORE ANSWERING THE INPUT.```***
  3. Now **PRESS 'o' to select origin** of the graph.
  4. After selecting origin **PRESS 'x' to select any point on x-axis** (just one click).
  5. It will ask the distance between origin and the point on x-axis which has just been selected.
  6. Following this it will ask if there is any zero offset i.e. if the origin represent 0 on the x-axis.
  7. After answering the length of line segment selected, zero offset and pressing enter **PRESS 'y' for y-axis** and follow the same procedure.
  8. After completion of caliberation, now **PRESS 'p' to select data point** on graph for which coordinates has to be studied.
  9. **PRESS 's' to save** the image of graph with selected points.
  10. **PRESS 'f' to finish**.
  11. Check "plotDataFiles" folder for .csv file generated and "plots" folder for the saved map image.
