
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



if __name__ == '__main__':
    for i in range(5):
        main()
