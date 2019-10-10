##############################################################################
#
# cat_colors.py 
#
# Plugin to change the background color depending on the tag.
# Based on filter.py by <Peter.Bienstman@UGent.be>
#
# Add a cat_colors dictionary to $HOME/.mnemosyne/config.py, that maps
# category names to RGB hex colors. They should all be in the form 0xFFRRGGBB
# With RR GG and BB replaced with the hexedecimal numbers for those colors
#
# You can also add a default color "cat_color_default", or it will default
# to 0xFFFFFFFF
#
# e.g.
#   cat_colors = {"Dutch"  : 0xFFAA00BB, "French" : 0xFFAA00BB}
#   cat_color_default = 0xFFAABBCC
##############################################################################

from PyQt5 import QtGui

from mnemosyne.libmnemosyne.plugin import Plugin
from mnemosyne.libmnemosyne.filter import Filter

class CatColorReplacer(Filter):

    def __init__(self, component_manager):
        Filter.__init__(self, component_manager)
        print(self.config().keys())
        if(self.config()["cat_colors"] == None):
            self.config()["cat_colors"] = {}
        if(self.config()["cat_color_default"] == None):
            self.config()["cat_color_default"] = 0xFFFFFFFF
        self.cat_colors = self.config()["cat_colors"]
        self.default_cat_color = self.config()["cat_color_default"]
        print(self.cat_colors)

    def run(self, text, card, fact_key, **render_args):
        print(self.config().card_type_property(\
            "background_colour", card.card_type))
        # Choose a random tag to use for the color
        tag = card.tag_string()
        if(tag.find(":") != -1):
          tag = tag[:tag.find(":")]
        print(tag)
        if(tag in self.cat_colors):
          self.config().set_card_type_property(\
            "background_colour", self.cat_colors[tag], card.card_type)
        else:
          self.config().set_card_type_property(\
            "background_colour", self.default_cat_color, card.card_type)


        for render_chain in self.component_manager.all("render_chain"):
            render_chain.renderer_for_card_type(card.card_type).\
                update(card.card_type)
        return text


class CatColorPlugin(Plugin):

    name = "Category Colors"
    description = "Change the background color depending on the category"
    components = [CatColorReplacer]
    supported_API_level = 2

    def __init__(self, component_manager):
        Plugin.__init__(self, component_manager)
        #self.config()["cat_color_default"] = ""
    
    def activate(self):
        Plugin.activate(self)
        #print("test")
        #self.config()["cat_color_default"] = ""
        self.render_chain("default").\
            register_filter(CatColorReplacer, in_front=True)

    def deactivate(self):
        Plugin.deactivate(self)
        self.render_chain("default").\
            unregister_filter(CatColorReplacer)

# Register plugin.

from mnemosyne.libmnemosyne.plugin import register_user_plugin
register_user_plugin(CatColorPlugin)
