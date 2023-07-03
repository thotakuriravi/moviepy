from moviepy.editor import *
import functions as func
import random
import path
import openpyxl as xl

def main():
    #------------------Generating uniq id
    id = func.uniq_id() 
    #------------------Picking the Topic from the Data File
    index, quote, quote_author = func.quote_pick()
    print(quote)

    video = ImageClip('gallery\\rose.jpg').set_duration(5).resize((1920, 1080))
    
    effect = VideoFileClip('gallery\\transition.gif').set_opacity(0.2).resize((1920, 1080))
    
    quote_icon_1 =ImageClip("gallery\\quote_icon_1.png")
    quote_icon_1 = quote_icon_1.resize(( quote_icon_1.w//2, quote_icon_1.h // 2   ))
    
    quote_icon_2 =ImageClip("gallery\\quote_icon_2.png")
    quote_icon_2 = quote_icon_2.resize(( quote_icon_2.w//2, quote_icon_2.h // 2   ))
    
    quote_audio = func.gtts_audio(txt=quote, id = id)
    
    audio = AudioFileClip(quote_audio)
    
    quote_clip = TextClip(txt=quote, 
                          font='morris',
                          fontsize= 100,
                          color= random.choice(path.color_codes), 
                          stroke_color= random.choice(path.stroke_colors)).set_audio(audio)
    
    quote_author_clip = TextClip(txt=quote_author, 
                          font='morris',
                          fontsize= 100,
                          color= random.choice(path.color_codes), 
                          stroke_color= random.choice(path.stroke_colors))
    
    final_video = CompositeVideoClip([video, 
                                      effect, 
                                      quote_icon_1.set_position((150, 150)), 
                                      quote_icon_2.set_position((1500, 750)), 
                                      quote_clip.set_position(('center', 'center')), 
                                      quote_author_clip.set_position(('center', 800))]).set_duration(5)
    
    file_name = 'final_videos/' + quote.replace(' ', '_').replace('\'', '') + '.mp4'
    final_video.write_videofile(file_name, fps= 30, codec='libx264', logger = None)
    
    try:
        # func.data_manger(topic=topic, index=index)
        
        #------data Deletion from Main Data file
    
        workbook = xl.load_workbook(path.quote_file)
        workbook_active = workbook.active
        workbook_active.delete_rows(index, 1)
        workbook.save(path.quote_file)
        workbook.close()

        for file in os.listdir('output/'):
            if file.startswith(id):
                os.unlink('output/'+ file )
    except:
        pass
    print(file_name)
    
    
# main()

def manual_quote(quote, quote_author):
    #------------------Generating uniq id
    id = func.uniq_id() 
    #------------------Picking the Topic from the Data File
    
    print(quote)

    video = ImageClip('gallery\\rose.jpg').set_duration(5).resize((1920, 1080))
    
    effect = VideoFileClip('gallery\\transition.gif').set_opacity(0.2).resize((1920, 1080))
    
    quote_icon_1 =ImageClip("gallery\\quote_icon_1.png")
    quote_icon_1 = quote_icon_1.resize(( quote_icon_1.w//2, quote_icon_1.h // 2   ))
    
    quote_icon_2 =ImageClip("gallery\\quote_icon_2.png")
    quote_icon_2 = quote_icon_2.resize(( quote_icon_2.w//2, quote_icon_2.h // 2   ))
    
    quote_audio = func.gtts_audio(txt=quote, id = id)
    
    audio = AudioFileClip(quote_audio)
    
    quote_clip = TextClip(txt=quote, 
                          font='morris',
                          fontsize= 100,
                          color= random.choice(path.color_codes), 
                          stroke_color= random.choice(path.stroke_colors)).set_audio(audio)
    
    quote_author_clip = TextClip(txt=quote_author, 
                          font='morris',
                          fontsize= 100,
                          color= random.choice(path.color_codes), 
                          stroke_color= random.choice(path.stroke_colors))
    
    final_video = CompositeVideoClip([video, 
                                      effect, 
                                      quote_icon_1.set_position((150, 150)), 
                                      quote_icon_2.set_position((1500, 750)), 
                                      quote_clip.set_position(('center', 'center')), 
                                      quote_author_clip.set_position(('center', 800))]).set_duration(5)
    
    file_name = 'final_videos/' + quote.replace(' ', '_').replace('\'', '') + '.mp4'
    final_video.write_videofile(file_name, fps= 30, codec='libx264', logger = None)
    
    try:
          

        for file in os.listdir('output/'):
            if file.startswith(id):
                os.unlink('output/'+ file )
    except:
        pass
    print(file_name)
    



quote, quote_author = 'You are the world and the world is you.', 'Krishnamurti'    
manual_quote(quote, quote_author )