import traceback
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from tkinter import filedialog
import sys
import os
import midiutil
import mido
abs_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(abs_path)
sys.path.append(abs_path)
exec("from musicpy import *")
function_names = dir(__import__('musicpy')) + ['direct_play', 'print']
from io import BytesIO
import pygame
pygame.mixer.init(44100, -16, 1, 1024)
with open('config.py', encoding='utf-8-sig') as f:
    exec(f.read())
with open('musicpy editor for exe.py', encoding='utf-8-sig') as f:
    exec(f.read())