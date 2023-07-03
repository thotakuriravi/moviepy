import shorts_functions as func
from moviepy.editor import *

def shorts_main():
    
    id = func.uniq_id()
    
    index, topic = func.topic_pick()
    
    topic_description = func.chatGPT(topic=topic)
    
    title_intro = func.title_intro(topic=topic, id=id)
    
    clips = [title_intro]
    
    for i, text in enumerate(topic_description):
        clip_video = func.topic_clips(text, id, i)
        clips.append(clip_video)
        
    
    final_video = concatenate_videoclips(clips=clips)

    file_name = 'final_videos/' + topic.replace(' ', '_').replace('\'', '') + '.mp4'

    final_video.write_videofile(file_name, fps= 30, codec='libx264', logger = None)




def manual_shorts_main(topic, description):
    
    id = func.uniq_id()
    
    # index, topic = func.topic_pick()
    
    # topic_description = func.chatGPT(topic=topic)
    topic_description = description
    
    title_intro = func.title_intro(topic=topic, id=id)
    
    clips = [title_intro]
    
    for i, text in enumerate(topic_description):
        clip_video = func.topic_clips(text, id, i)
        clips.append(clip_video)
        
    
    final_video = concatenate_videoclips(clips=clips)

    file_name = 'final_videos/' + topic.replace(' ', '_').replace('\'', '') + '.mp4'

    final_video.write_videofile(file_name, fps= 30, codec='libx264', logger = None)




topic = "The Importance of Sleep for Optimal Health"

para1 = "A good night's sleep is crucial for maintaining optimal health and well-being. Sleep plays a vital role in various aspects of our physical and mental health. During sleep, our bodies undergo important processes that promote healing, restore energy levels, and support cognitive functions."

para2 = "Quality sleep is associated with numerous health benefits. It helps regulate hormones, such as cortisol and insulin, which are critical for metabolism and blood sugar control. Sufficient sleep also boosts immune function, reducing the risk of infections and chronic diseases."

description = [para1, para2]









shorts_main()

# manual_shorts_main(topic, description)





