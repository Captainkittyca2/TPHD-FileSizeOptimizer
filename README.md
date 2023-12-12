# TPHD-FileSizeOptimizer
A tool that adjusts the FileSizeList.txt and DecompressedSizeList.txt of Twilight Princess HD to have proper sizes for the files in the game.

## Usage
* Place the tool in the folder that contains **code**, **content**, and **meta** folders.
* Execute the tool.
* You will be asked whether you want to:
    Adjust the filesize for all files aside from files located in **Stage** folder.
    or
    Adjust the filesize for files located inside of a folder in **Stage** folder (such as **F_SP104**).
* Input 0 if you want to adjust the filesize for all files aside from **Stage** folder files.
* Once it finishes, press `ENTER` to exit the tool.
* Input 1 if you want to adjust the filesize for files inside a specific folder within **Stage** folder.
## Notes
* When adjusting filesize for a specific stage within **Stage** folder, make sure that the stage you choose is a pre-existing stage in the game that still has the same amount of rooms (or perhaps less) and same room number as unmodified version of the stage.
* So in other words: make sure the stage you adjust filesize for, is simply a replacement of a pre-existing stage in the game, and has same amount of rooms as before you modified it.
* **However, if you would like to adjust the filesize of a new stage that doesn't replace a pre-existing stage or if you would like to adjust the filesize of a modified pre-existing stage with more rooms than unmodified version, use a hex editor and add the extra stage/rooms in `FileSizeist.txt` and `DecompressedSizeList.txt`, with any random numbers for the filesize values and percentages. Then execute the tool.**
