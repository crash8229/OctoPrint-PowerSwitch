# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin


class PowerswitchPlugin(octoprint.plugin.StartupPlugin,
						octoprint.plugin.SettingsPlugin,
						octoprint.plugin.AssetPlugin,
						octoprint.plugin.TemplatePlugin,
						octoprint.plugin.SimpleApiPlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(state="limegreen")

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/powerswitch.js"],
			css=["css/powerswitch.css"],
			less=["less/powerswitch.less"]
		)

	def get_template_vars(self):
		return dict(state=self._settings.get(["state"]))

	def get_api_commands(self):
		self._logger.info("Manually triggered get_api")
		return dict(flip=[])

	def on_api_command(self, command, data):
		if command == 'flip':
			self._logger.info("World")

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			powerswitch=dict(
				displayName="Powerswitch Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="crash8229",
				repo="OctoPrint-PowerSwitch",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/crash8229/OctoPrint-PowerSwitch/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Power Switch"


def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = PowerswitchPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
