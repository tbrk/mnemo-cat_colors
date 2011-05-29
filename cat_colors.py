##############################################################################
#
# cat_colors.py <tim@tbrk.org>
#
# Add a cat_colors dictionary to $HOME/.mnemosyne/config.py, that maps
# category names to X11 color names.
# (http://en.wikipedia.org/wiki/X11_color_names)
#
# e.g.
#   cat_colors = {"Dutch"  : "orange",
#		  "French" : "lightblue"}
#
##############################################################################

from mnemosyne.core import *
from mnemosyne.pyqt_ui.plugin import get_main_widget
from qt import *
import sys

##############################################################################
#
# Plugin to change the background color depending on the category.
#
##############################################################################

class CatColor(Plugin):
	version = "0.9.0"

	def warn(self, msg):
                status = QMessageBox.information(None,
		   self.main_dlg.trUtf8("Mnemosyne").append(": CatColor plugin"),
		   msg,
		   self.main_dlg.trUtf8("&OK"))

	def description(self):
		return ("Change the background color depending on the category. (v"
			+ version + ")")

	def load(self):
		self.main_dlg = get_main_widget()
		# TODO: read the default color from the widget
		self.default_color = QColor("gray")
		try: cat_colors = get_config("cat_colors")
		except KeyError:
		    self.warn("There is no cat_colors entry in config.py.")
		    cat_colors = {}

		    # TODO: This line works around an arguable limitation in
		    # mnemosyne.core.load_config() whereby only known config variables are
		    # imported from a users config.py. The plugin will not take effect, however,
		    # until the second time Mnemosyne is started after installation.
		    set_config("cat_colors", {})

		if type(cat_colors) != type({}):
		    self.warn("The cat_colors entry in config.py is not a dictionary.")
		    return

		self.cat_colors = {}
		for (cat, color) in cat_colors.iteritems():
		    self.cat_colors[cat] = QColor(color)

		register_function_hook("filter_q", self.set_color)

	def unload(self):
		self.main_dlg.setPaletteBackgroundColor(self.default_color)
		unregister_function_hook("filter_q", self.set_color)

	def set_color(self, text, card):
		cat = card.cat.name
		if self.cat_colors.has_key(cat):
		    self.main_dlg.setPaletteBackgroundColor(self.cat_colors[cat])
		else:
		    self.main_dlg.setPaletteBackgroundColor(self.default_color)
		return text

p = CatColor()
p.load()

