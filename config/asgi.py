import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chnl_expl_project.config.settings")
channel_layer = channels.asgi.get_channel_layer()
