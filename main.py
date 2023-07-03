
from moviepy.editor import *
import functions as func


def main():
    #------------------Generating uniq id
    id = func.uniq_id() 
    #------------------Picking the Topic from the Data File
    index, topic = func.topic_pick()
    print(topic)
    #------------------Writing the description for topic using ChatGPT
    topic_extension = func.chatGPT(topic=topic)

    print('sub_clips :', len(topic_extension))

    #-----------------Intro for topic
    title_intro = func.title_intro(topic=topic, id = id)

    channel_intro = VideoFileClip('gallery\\Intro.mp4')
    channel_outro = VideoFileClip('gallery\\outro.mp4')

    clips = [channel_intro, title_intro]

    for i, text in enumerate(topic_extension):
        clip_video = func.topic_clips(text, id, i)
        clips.append(clip_video)

    clips.append(channel_outro)

    final_video = concatenate_videoclips(clips=clips)

    file_name = 'final_videos/' + topic.replace(' ', '_').replace('\'', '') + '.mp4'

    final_video.write_videofile(file_name, fps= 30, codec='libx264', logger = None)
    
    try:
        func.data_manger(topic=topic, index=index)

        for file in os.listdir('output/'):
            if file.startswith(id):
                os.unlink('output/'+ file )
    except:
        pass
    print(file_name)



def manual_main(topic:str, description:list):
    #------------------Generating uniq id
    id = func.uniq_id() 
    #------------------Picking the Topic from the Data File
    topic = topic
    print(topic)
    #------------------Writing the description for topic using ChatGPT
    topic_extension = description

    print('sub_clips :', len(topic_extension))

    #-----------------Intro for topic
    title_intro = func.title_intro(topic=topic, id = id)

    channel_intro = VideoFileClip('gallery\\Intro.mp4')
    channel_outro = VideoFileClip('gallery\\outro.mp4')

    clips = [channel_intro, title_intro]

    for i, text in enumerate(topic_extension):
        clip_video = func.topic_clips(text, id, i)
        clips.append(clip_video)

    clips.append(channel_outro)

    final_video = concatenate_videoclips(clips=clips)

    file_name = 'final_videos/' + topic.replace(' ', '_').replace('\'', '') + '.mp4'

    final_video.write_videofile(file_name, fps= 30, codec='libx264', logger = None)
    
    try:
        for file in os.listdir('output/'):
            if file.startswith(id):
                os.unlink('output/'+ file )
    except:
        pass
    print(file_name)
    
    
    


topic_title = "The Importance of Sleep for Optimal Health"

para1 = "A good night's sleep is crucial for maintaining optimal health and well-being. Sleep plays a vital role in various aspects of our physical and mental health. During sleep, our bodies undergo important processes that promote healing, restore energy levels, and support cognitive functions."
para2 = "Quality sleep is associated with numerous health benefits. It helps regulate hormones, such as cortisol and insulin, which are critical for metabolism and blood sugar control. Sufficient sleep also boosts immune function, reducing the risk of infections and chronic diseases."

topic_description = [para1, para2]

manual_main(topic=topic_title,
            description= topic_description)

