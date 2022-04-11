#!/usr/bin/python
# -*- coding: utf-8 -*-


class PlayerDef(object):
    StatusAlive = "alive"
    StatusDie = "die"

    DirectionUp = "up"
    DirectionDown = "down"
    DirectionLeft = "left"
    DirectionRight = "right"


class WumpusDef(object):
    StatusAlive = "alive"
    StatusDie = "die"


class GoldDef(object):
    StatusUnMiss = "un_miss"
    StatusMiss = "miss"
