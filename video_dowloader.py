import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def download_video():
    url = url_entry.get()
    # Diretório de saída
    output_dir = "videos_baixados"
    try:
        # Comando para baixar vídeo usando yt-dlp
        result = subprocess.run(['yt-dlp', '-o', f'{output_dir}/%(title)s.%(ext)s', url], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", "Video downloaded successfully!")
        else:
            messagebox.showerror("Error", f"Failed to download video:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Criando a pasta "videos_baixados" se não existir
os.makedirs("videos_baixados", exist_ok=True)

# Criando a janela principal
root = tk.Tk()
root.title("Twitter Video Downloader")

# Criando e posicionando widgets
url_label = tk.Label(root, text="Video URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

# Iniciando o loop principal
root.mainloop()
