/*
 * View model for OctoPrint-PowerSwitch
 *
 * Author: Mike Umana
 * License: AGPLv3
 */
$(function() {
    function PowerswitchViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
        self.switcher = function () {
            OctoPrint.logger.info("Hello");
            OctoPrint.simpleApiCommand("powerswitch", "flip");
        };
    }


    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: PowerswitchViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ /* "loginStateViewModel", "settingsViewModel" */ ],
        // Elements to bind to, e.g. #settings_plugin_powerswitch, #tab_plugin_powerswitch, ...
        elements: [ /* ... */ ]
    });
});
