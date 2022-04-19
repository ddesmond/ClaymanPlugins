# Plugins core class

class ClaymanPluginCore(object):
    """Main ClaymanPluginCore class
    All Clayman context plugins needs to
    subclass this class"""

    def __init__(self):
        self.module_name = "ClaymanPluginCore"
        self.module_version = "1.0"
        self.plugin_name = "CorePlugin"

    def register(self):
        """Register you plugin here
        """
        self.plugin_name = "ClaymanPluginCore demo"

    def get_name(self):
        return self.plugin_name


    def process(self):
        """What you want to do with the asset package, do here.
        Example:
            You want to make maketx available for a package level,
            you would place your all logic here.
        Example:
            You want to make a "zip package" on right click.
            Do the logic here.
        """
        print("Processing {}".format(self.plugin_name))

        # acces the library data for the selected package as so:
        #packaged_asset_data = self.item.package_data
        #print(packaged_asset_data)
        return

    def cleanup(self):
        """Any cleanup stuff to be done here.
        If the process ends up as True, cleanup will be triggered
        """
        pass


def pass_plugin():
    return ClaymanPluginCore()


def load_plugin():
    ClaymanPluginCore().register()


def process_plugin():
    ClaymanPluginCore().process()


def cleanup_plugin():
    ClaymanPluginCore().cleanup()

