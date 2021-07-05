"""Schemas for data about lights."""
from datetime import datetime
from typing import Any, List, Optional, Tuple, Union

from pydantic import BaseModel, Field


class LightState(BaseModel):
    """The State of a light."""

    on: Optional[bool]
    reachable: Optional[bool]

    alert: Optional[str]
    bri: Optional[int]
    color_mode: Optional[str]
    ct: Optional[int]
    effect: Optional[str]
    hue: Optional[int]
    mode: Optional[str]
    sat: Optional[int]
    xy: Optional[Tuple[int, int]]
    transitiontime: Optional[str]


class LightInfo(BaseModel):
    """Information about a light."""

    id: int
    name: str
    uniqueid: str
    state: Optional[LightState]

    manufacturername: str
    modelid: str
    productname: str
    type: str

    swversion: str


class GroupState(BaseModel):
    """The state of lights in a group."""

    all_on: bool
    any_on: bool


class GroupInfo(BaseModel):
    """Information about a light group."""

    id: int
    name: str
    lights: List[int]
    sensors: List[int]
    type: str
    state: GroupState

    group_class: str = Field(..., alias="class")

    action: LightState


class GenericSensorState(BaseModel):
    """Information about the state of a sensor."""

    lastupdated: datetime


class PresenceSensorState(GenericSensorState):
    """Information about the state of a sensor."""

    presence: bool


class RotarySensorState(GenericSensorState):
    """Information about the state of a sensor."""

    rotaryevent: str
    expectedrotation: str
    expectedeventduration: str


class SwitchSensorState(GenericSensorState):
    """Information about the state of a sensor."""

    buttonevent: int


class LightLevelSensorState(GenericSensorState):
    """Information about the state of a sensor."""

    dark: bool
    daylight: bool
    lightlevel: int


class TemperatureSensorState(GenericSensorState):
    """Information about the state of a sensor."""

    temperature: int


class HumiditySensorState(GenericSensorState):
    """Information about the state of a sensor."""

    humidity: int


class OpenCloseSensorState(GenericSensorState):
    """Information about the state of a sensor."""

    open: str


SensorState = Union[
    PresenceSensorState,
    RotarySensorState,
    SwitchSensorState,
    LightLevelSensorState,
    TemperatureSensorState,
    HumiditySensorState,
    OpenCloseSensorState,
]


class SensorInfo(BaseModel):
    """Information about a sensor."""

    id: int
    name: str
    type: str
    modelid: str
    manufacturername: str

    productname: str
    uniqueid: str
    swversion: Optional[str]

    state: SensorState
    capabilities: Any