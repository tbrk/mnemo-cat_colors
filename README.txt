Color Categories Plugin v0.9
----------------------------
Author: T. Bourke 20080831

Change the window color depending on the current card's category.

This plugin is a prototype only. Feedback and suggestions are welcome.

INSTALLATION
------------
1. Copy cat_colors.py into the Mnemosyne plugins subdirectory.

2. Add a cat_colors declaration to the Mnemosyne config.py file, e.g.:
      cat_colors = { 'French' : 'lightblue',
		     'Dutch'  : 'orange',
		     'English': 'red' }

   Category names are given to the left of the colon (:), CSS/HTML colour
   names (http://en.wikipedia.org/wiki/X11_colors) to the right.

3. Start Mnemosyne. It will warn that a cat_colors variable does not exist.

4. Exit Mnemosyne.

5. Start Mnemosyne. The window should now change colour according to the
   current card's category.

TODO
----
* Fix storage and retrieval of original background color.
* Color buttons properly
  - calculate a lighter color for the 3D shadows.
  - change the foreground text/line color if necessary
* Improve configuration (GUI extensions?).

