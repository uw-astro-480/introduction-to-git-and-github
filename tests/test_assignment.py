#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Filename: test_assignment.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

from astropy.time import Time

from astr_480_intro.intro import get_moon_position


def test_get_moon_position_now():
    assert get_moon_position() is not None


def test_get_moon_position_date():
    date = Time("2023-06-01 00:00:00")
    assert get_moon_position(date=date) is not None
