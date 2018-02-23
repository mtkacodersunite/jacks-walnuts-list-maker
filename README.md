# jacks-walnuts-list-maker
Makes lists of books for Walnuts on the Sidewalk; see eado/BookList-Walnuts

## Using Walnuts List Maker

1. Visit the [spreadsheet](https://docs.google.com/spreadsheets/d/1SX_T2RpBbNN1LgalLx_8yzkGiiXCZNT0Ayj57fKLthU/edit#gid=0)
2. Go to the File menu > Download as > Tab-seperated values (.tsv, current sheet)
3. Rename the file to `walnuts.tsv`
4. Download `walnuts.py` and put it in the same folder as `walnuts.tsv`
5. On macOS and Linux, open a Terminal window and `cd` to the directory that contains the files. Then run `python walnuts.txt`. On Windows, you'll need to install Python, then open the folder in Explorer, then right-click `walnuts.py` and click Run with Python (or similar, depending on your version of Python and/or Windows). 
6. If you need to copy the output for putting it in WordPress, simply send the output to a text file like this: `python walnuts.py > walnuts.txt`. If it would be easier, you can also just copy the text directly from your Terminal window or from `cmd.exe`. 
7. Post it on the WordPress page titled "Looking for a Book?"

If you need help, make an Issue in GitHub. 
