from plugins.plugins_core import ClaymanPluginCore

class HelloWorld(ClaymanPluginCore):
    def __init__(self):
        super(HelloWorld, self).__init__()
        self.module_name = "HelloWorld"
        self.module_version = "1.0"
        self.plugin_name = "HelloWorld Print"

    def register(self):
        """Register you plugin here
        """
        print("Registering {}".format(self.module_name))
        self.plugin_name = "Hello world"


    def process(self):
        """Do your logic here
        """
        print("HEEEELOOOO WOOORLLLD")


# Do not remove those lines since those are needed to run your logic
def pass_plugin():
    return HelloWorld()

def load_plugin():
    HelloWorld().register()

def process_plugin():
    HelloWorld().process()

def cleanup_plugin():
    HelloWorld().cleanup()