import pytest
from fetch_weather import map_wind_direction

def test_north():
    assert map_wind_direction(10) == "North"
    assert map_wind_direction(22) == "North"
    assert map_wind_direction(337.5) == "North"
    assert map_wind_direction(0) == "North"

def test_north_east():
    assert map_wind_direction(22.5) == "North-East"
    assert map_wind_direction(45) == "North-East"
    assert map_wind_direction(67) == "North-East"
    assert map_wind_direction(30) == "North-East"

def test_east():
    assert map_wind_direction(90) == "East"
    assert map_wind_direction(67.5) == "East"
    assert map_wind_direction(112) == "East"
    assert map_wind_direction(100) == "East"

def test_south_east():
    assert map_wind_direction(112.5) == "South-East"
    assert map_wind_direction(135) == "South-East"
    assert map_wind_direction(157) == "South-East"
    assert map_wind_direction(150) == "South-East"

def test_south():
    assert map_wind_direction(157.5) == "South"
    assert map_wind_direction(180) == "South"
    assert map_wind_direction(202) == "South"
    assert map_wind_direction(200) == "South"

def test_south_west():
    assert map_wind_direction(202.5) == "South-West"
    assert map_wind_direction(225) == "South-West"
    assert map_wind_direction(247) == "South-West"
    assert map_wind_direction(240) == "South-West"

def test_west():
    assert map_wind_direction(247.5) == "West"
    assert map_wind_direction(270) == "West"
    assert map_wind_direction(292) == "West"
    assert map_wind_direction(290) == "West"

def test_north_west():
    assert map_wind_direction(292.5) == "North-West"
    assert map_wind_direction(315) == "North-West"
    assert map_wind_direction(337) == "North-West"
    assert map_wind_direction(330) == "North-West"

def test_wrong_value():
    assert map_wind_direction(-1) == "Unknown"
    assert map_wind_direction(361) == "Unknown"
    assert map_wind_direction('abc') == "Unknown"
    assert map_wind_direction(None) == "Unknown"
