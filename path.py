import os

gallery_path = 'gallery/'

bg_images_path = gallery_path + 'background_images/'
bg_videos_path = gallery_path + 'background_videos/'
gif_images_path = gallery_path + 'gif/'
png_images_path = gallery_path + 'png/'
audio_path = gallery_path + 'audio/'
title_musiq = gallery_path + 'title_musiq/'

clips_bg_images = gallery_path + 'clips_bg_images/'

#------------data

data_file = 'data/data.xlsx'
completed_data_file = 'data/video_completed_data.xlsx'
quote_file = 'data/quotations.xlsx'

#----------- OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

#------------ COLOR codes


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