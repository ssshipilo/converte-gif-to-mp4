import moviepy.editor as mp
import moviepy.editor as mpe
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips, CompositeVideoClip
import os
 
folder = './import/'
folder_result = './result/'
formated = 'mp4';

file = []
audio = []

for filename in os.listdir(folder):
        if filename[filename.rfind(".") + 1:] in ['gif']:
                file.append(filename)

for item in enumerate(file):
        clip = mp.VideoFileClip(folder + item[1])
        split = item[1].split('.')[0];
        clip.write_videofile(folder + split + f".{formated}")



# Concatanation video; example:
def concatanationVideo(folder, fomat_video):
        """
        The function is used for concatenation, takes the parameter:\n
        `array` - list video
        """

        # ----------
        # Video find
        resultVideo = []
        for filename in os.listdir(folder):
                if filename[filename.rfind(".") + 1:] in [fomat_video['video']]:
                        resultVideo.append(filename)

        res_arr = []
        for item in enumerate(resultVideo):
                clip = VideoFileClip(folder + item[1])
                res_arr.append(clip)

        final_clip = concatenate_videoclips(res_arr)
        final_clip.write_videofile(folder_result + "result.mp4")


        # ----------
        # Audio find
        res_audio = []
        for filename in os.listdir(folder):
                if filename[filename.rfind(".") + 1:] in [fomat_video['audio']]:
                        res_audio.append(filename)

        audios = []
        for item in enumerate(res_audio):
                clip = AudioFileClip(folder + item[1])
                audios.append(clip)

        final_audio = concatenate_audioclips(audios)
        final_audio.write_audiofile(folder_result + "result.mp3")
        

        # Concatanation video and audio
        my_clip = mpe.VideoFileClip(f"./result/result.{fomat_video['video']}")
        audio_background = mpe.AudioFileClip(f"./result/result.{fomat_video['audio']}")
        final_clip = my_clip.set_audio(audio_background)
        final_clip.write_videofile('vide.mp4' ,fps=25)
        

concatanationVideo(folder, {'video': formated, 'audio': 'mp3'})