import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import os
from pathlib import Path

#############################################################
# QUALITY You can change this. Default: 1  Range: 0 - 1     #
#############################################################
quality = 1
#############################################################



def optimizar_video(input_path, output_path, quality):
    # Cargar el video
    video = VideoFileClip(input_path)
    
    # Obtener la nueva resolución del video
    new_width = int(video.size[0] * quality)
    new_height = int(video.size[1] * quality)
    
    # Redimensionar el video
    video = video.resize((new_width, new_height))
    
    # Guardar el video optimizado
    video.write_videofile(output_path)

# Crear una ventana de Tkinter
root = tk.Tk()
root.withdraw()

# Solicitar al usuario la ubicación del archivo de entrada
input_path = filedialog.askopenfilename(title="Seleccionar archivo de video", filetypes=[("Videos", "*.mp4")])

# Verificar si se seleccionó un archivo
if input_path:
    # Obtener la carpeta del archivo de entrada
    folder_path = os.path.dirname(input_path)
    
    # Obtener la ruta del escritorio del usuario
    desktop_path = Path.home() / "Downloads"
    
    # Ruta del video de salida optimizado (en el escritorio del usuario)
    output_path = os.path.join(desktop_path, 'video_optimizado.mp4')
    
    
    # Optimizar el video
    optimizar_video(input_path, output_path, quality)
    print("Video optimizado guardado en:", output_path)
else:
    print("No se seleccionó ningún archivo.")
