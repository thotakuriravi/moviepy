import os
import random
import textwrap
from moviepy.editor import *
from gtts import gTTS

color_codes = [
                '#d81e5b', '#ed45bd', '#fbc93d', '#b65fcf', '#13cbe7', '#10e5aa', '#bb1116', '#000051' ,'#be29ec',
                '#d40b8d', '#882dbb', '#06e4d1', '#8806ce', '#ee5c42', '#003366', '#40c060', '#9d1039', '#ffd700',
                '#bada55', '#f08080', '#20b2aa', '#ffc3a0', '#660066', '#f6546a' , '#00ced1', '#daa520', '#088da5',
                '#420420', '#ff1493'
               ]

stroke_colors = [    
                '#2e0101', '#2e011d', '#2e012e', '#1e012e', '#1c0139', '#010238', '#011c38', 
                '#013138', '#013835', '#01381e', '#043801', '#203801', '#2d3801', '#383301', 
                '#382501', '#381701' 
                ]


def title_intro(topic:str):
    
    text = '\n'.join(textwrap.wrap(topic.upper(), width=30))
    text = text.title()
    
    #  -bg video
    bg_videos_path = 'gallery\\background_videos\\'
    video_path =  bg_videos_path + random.choice(os.listdir(bg_videos_path))
    video = VideoFileClip(video_path)
    
    
    font_color = random.choice(color_codes)
    font_stroke_color = random.choice(stroke_colors)
    
    
    txt_clip = TextClip(txt=text, 
                        fontsize= 130, 
                        font='melton',
                        color= font_color, 
                        stroke_color= font_stroke_color, 
                        stroke_width=2).set_position('center', 'center')
    
    txt_clip1 = TextClip(txt=text, 
                        fontsize= 45, 
                        font='melton',
                        color= random.choice(color_codes), 
                        stroke_color= font_stroke_color,  
                        stroke_width=2).set_duration(1).set_position('center', 'center')
    
    txt_clip2 = TextClip(txt=text, 
                        fontsize= 90, 
                        font='melton',
                        color= random.choice(color_codes), 
                        stroke_color= font_stroke_color,  
                        stroke_width=2).set_duration(1).set_position('center', 'center')
    
    txt_clip3 = TextClip(txt=text, 
                        fontsize= 130, 
                        font='melton',
                        color= random.choice(color_codes), 
                        stroke_color= font_stroke_color,  
                        stroke_width=2).set_duration(1).set_position('center', 'center')
    
    
    def get_txt_color(t):
        if t < 0.5:
            return random.choice(color_codes)
        elif t < 1:
            return '#a32372'
        elif t < 1.5:
            return random.choice(color_codes)
        elif t < 2:
            return '#008080'
        elif t < 2.5:
            return random.choice(color_codes)
        elif t < 3:
            return 'red'
        else:
            return random.choice(color_codes)
    
    def modified_text_clip(get_frame, t):
        # print(t)
        modified_clip = TextClip(txt=text, 
                        fontsize= 130, 
                        font='melton',
                        color= get_txt_color(t), 
                        stroke_color= font_stroke_color, 
                        stroke_width=2).set_duration(1).set_position('center', 'center')
        
        return modified_clip.get_frame(t)    
    
    modified_txt_clip = txt_clip.fl(modified_text_clip)
    
    tts = gTTS(topic)
    topic_audio = 'output/' + topic + '.mp3'
    tts.save(topic_audio)
    topic_audio_clip = AudioFileClip(topic_audio)

    modified_txt_clip = modified_txt_clip.set_audio(topic_audio_clip)
    
    duration = 3 + topic_audio_clip.duration + 1
    
    audio_path = os.path.join('gallery\\title_musiq\\' ,  random.choice(os.listdir('gallery\\title_musiq\\')))
    bg_audio = AudioFileClip(audio_path).set_duration(3)
    
    video = video.set_duration(duration).set_audio(bg_audio)
    final_video = CompositeVideoClip([video, txt_clip1, txt_clip2.set_start(1), txt_clip3.set_start(2), modified_txt_clip.set_start(3)]).set_duration(duration)
    
    final_video.write_videofile('output/title_intro.mp4', fps=30, codec = 'libx264', logger= None)
    
    
title_intro("Time is more important than money")
