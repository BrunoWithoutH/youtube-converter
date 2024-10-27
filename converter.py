from pytubefix import YouTube
import os
import json
import requests

video_url = input("Insira o link do vídeo: ")

escolha = input("Deseja baixar como mp4 ou mp3? ('1' para mp4, '2' para mp3): ")
if escolha == '1':
    print("Baixando vídeo em mp4...")
    try:
        response = requests.get(f"https://www.youtube.com/oembed?url={video_url}&format=json")
        video_info = response.json()

        print("Título:", video_info['title'])
        
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()

        print("Download concluído! Áudio salvo como:", stream.default_filename)
        
    except KeyError as e:
        print("Erro ao acessar o título do vídeo.")
        print("Erro específico:", e)
    except Exception as e:
        print("Ocorreu um erro:", e)
if escolha == '2':
    print("Baixando como mp3...")
    try:
        response = requests.get(f"https://www.youtube.com/oembed?url={video_url}&format=json")
        video_info = response.json()

        print("Título:", video_info['title'])
        
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        out_file = stream.download()
        
        base, ext = os.path.splitext(out_file)
        new_file = f"{base}.mp3"
        os.rename(out_file, new_file)
        
        print("Download concluído! Áudio salvo como:", new_file)
        
    except KeyError as e:
        print("Erro ao acessar o título do vídeo.")
        print("Erro específico:", e)
    except Exception as e:
        print("Ocorreu um erro:", e)