Color Categories Plugin v1.0
----------------------------
Author: gbear605
Inspired by: T. Bourke 20080831

Change the window color depending on the current card's first tag.

This plugin is a prototype only. Feedback and suggestions are welcome.

INSTALLATION
------------
1. Copy cat_colors.py into the Mnemosyne plugins subdirectory.

2. Add a cat_colors declaration to the Mnemosyne config.py file, e.g.:
      cat_colors = {"German": 0xFFFF0000, "dates": 0xFF00FF00, \
  "world": 0xFF0000FF, "geography": 0xFFAABBCC}

   Tag names are given to the left of the colon (:), RGB hex values to the right.

3. Optionally add a cat_color_default declaration to set the default color for tags that don't have a set color. If you don't add one, the default color will be white. e.g.:
      cat_color_default = 0xFFFFFFFF

3. Start Mnemosyne.

4. Exit Mnemosyne.

5. Start Mnemosyne. The window should now change colour according to the
   current card's category.

TODO
----
* Improve configuration (GUI extensions?).
