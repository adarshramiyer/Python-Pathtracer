#!/usr/bin/env python
"""Main Raytracer"""
import argparse
import importlib
import os

from color import Color
from engine import RenderEngine
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector
from light import Light
from material import Material, CheckeredMaterial
import math

WIDTH = 1920
HEIGHT = 1080
RENDERED_IMG = "2balls.ppm"
CAMERA = Vector(0, -0.035, -1)
OBJECTS = [
    #Ground Plane
    Sphere(Point(0, 10000.5, 1), 10000.0,
           CheckeredMaterial(color1=Color.from_hex("#f5dec9"), color2=Color.from_hex("#542406"),
                             ambient = 0.2, reflection = 0.2, )),
    #Ball 1
    Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#0b8ee6"))),
    #Ball 2
    Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#f08e32")))]

LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6"))]

def main():
    '''parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to finished file")
    args = parser.parse_args()'''
    #mod = importlib.import_module(args.scene)

    scene = Scene(CAMERA, OBJECTS, LIGHTS, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    #os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open("test2.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
