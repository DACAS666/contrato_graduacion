import sys
import os

# Agregar el directorio de la aplicación al sys.path
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application
