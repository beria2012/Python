
import cv2
import glob
import os
import shutil
from PIL import Image


class MediaConverter:
    def __init__(self, video_url, out_dir):
        self.video_url = video_url
        self.out_dir = out_dir

    def convert_to_gif(self, out_path_file_name):
        print(f"Converting {self.video_url} to {out_path_file_name}\nPlease wait...")
        frame_folder = self.__convert_mp4_to_jpgs()
        images = glob.glob(f"{frame_folder}/*.jpg")
        images.sort()
        frames = [Image.open(image) for image in images]
        frame_one = frames[0]
        frame_one.save(out_path_file_name, format="GIF", append_images=frames,
                    save_all=True, duration=50, loop=0)
        
        print (f"Cleaning up {frame_folder}")
        shutil.rmtree(frame_folder)
        print ("Done!")

    def __convert_mp4_to_jpgs(self):
        out_path = os.path.join(self.out_dir, "output")
        os.makedirs(out_path, exist_ok = True)
        video_capture = cv2.VideoCapture(self.video_url)
        still_reading, image = video_capture.read()
        frame_count = 0
        while still_reading:
            cv2.imwrite(f"{out_path}/frame_{frame_count:03d}.jpg", image)
            still_reading, image = video_capture.read()
            frame_count += 1
        return out_path


def main():
    video_url = 'https://v16-webapp.tiktok.com/9fd20f61b3365da96cf1673d34dfe57e/62e82597/video/tos/alisg/tos-alisg-pve-0037c001/8a61fa32ef81407ca7ea11c02794de7e/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4178&bt=2089&btag=80000&cs=0&ds=3&ft=z_piDPb82NvjV-A0ROzfuCYQFAe4nRQjlV-JCtOB&mime_type=video_mp4&qs=0&rc=OjU3ODZkZTNmM2Y4NzYzM0BpM2xmNDQ6ZmlsZTMzODczNEBiLjJiYmIyNjYxYzVhMS4wYSMwMDQ2cjRfai5gLS1kMS1zcw%3D%3D&l=202208011312180102450621920D211E8D'
    outout_dir = os.path.dirname(os.path.realpath(__file__))
    converter = MediaConverter(video_url, outout_dir)
    converter.convert_to_gif(os.path.join(outout_dir, "tiktok.gif"))

if __name__ == '__main__':
    main()







