# YouTube Automation!

This is a basic concept for a automated youtube channel. I take facts from ChatGPT given certain rules (like some "partition words" to split the facts into 2 pieces) and make a short videoclip with it to upload to youtube or instagram reels.

## 💡 How it works?

- Ask ChatGPT to generate facts with the required rules to split the fact if needed.
- Keep the generated facts in text files to be used in the program.
- Download some background videos to place the facts on. (I have included code to resize the videos into 9:16 aspect ratio for shorts/reels)
- Run the `main.py` file. (Make sure the files are in the required path as mentioned in the code)
- The `main.py` file should generate videos and save them to an "export folder".
- Now just upload the videos! (I will be looking into automating the uploads as well in the future)

## 🚀 Getting started:

1. Clone this repository! <br>

- Using SSH: `git clone git@github.com:mokshablr/YouTube-Automation.git` <br>
- Using HTTP: `git clone https://github.com/mokshablr/YouTube-Automation.git`

2. Ensure you have the [dependencies](#dependencies) installed.

3. Upload your choice of background videos into `/backgrounds`, text file with facts into `/facts`.

4. Have a folder `/exports` to save the generated videoclips into.

## 📦 Dependencies:

1. ImageMagick
2. FFmpeg

## Hope this helps! ❤️
