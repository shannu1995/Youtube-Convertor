import pyautogui as pgui
import subprocess as sp
import re
input_url = pgui.prompt(text="Please enter the original URL", title="URL Shortener")
if not re.match(r"^https://www.youtube.com/shorts/", input_url):
    pgui.alert(text="The URL is not a valid YouTube Shorts URL", title="URL Shortener")
else:   
    video_id = input_url.split("/")[-1]
    if re.match(r"\?feture=share$", video_id):
        video_id = video_id.split("?")[0]
    new_url = f"https://www.youtube.com/watch?v={video_id}"
    pgui.alert(text="The new URL is has been copied to the clipboard.\n Please enjoy!", title="URL Shortener")
    sp.run(['clip.exe'], input=new_url.encode('UTF-16LE'), check=True)