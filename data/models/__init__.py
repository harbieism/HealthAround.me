from .census import Census
from .dartmouth import Dartmouth
from .ers import Ers
from .fast_food import FastFood

assert all((Census, Dartmouth, Ers, FastFood))  # pyflakes be quiet
