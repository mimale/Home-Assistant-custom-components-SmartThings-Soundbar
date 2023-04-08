import logging
import voluptuous as vol

from .api import SoundbarApiSwitch

from homeassistant.components.switch import (
    SwitchEntity,
    PLATFORM_SCHEMA,
)
from homeassistant.const import (
    CONF_NAME, CONF_API_KEY, CONF_DEVICE_ID
)
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "night_mode"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_DEVICE_ID): cv.string,
    }
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    api_key = config.get(CONF_API_KEY)
    device_id = config.get(CONF_DEVICE_ID)
    add_entities([SmartThingsSoundbarMediaPlayer(name, api_key, device_id )])

class SmartThingsSoundbarMediaPlayer(SwitchEntity):

    def __init__(self, name, api_key, device_id ):
        self._name = name
        self._device_id = device_id
        self._api_key = api_key
        self._state = "off"
        self._night_mode = False

    def update(self):
        SoundbarApiSwitch.device_update(self)

    def turn_off(self):
        arg = ""
        cmdtype = "switch_off"
        SoundbarApiSwitch.send_command(self, arg, cmdtype)

    def turn_on(self):
        arg = ""
        cmdtype = "switch_on"
        SoundbarApiSwitch.send_command(self, arg, cmdtype)

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state


