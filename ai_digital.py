# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
def generate_text():
    # 获取文本框1中的关键字
    keyword = request.form['keyword']
    print(keyword)
    # 调用AI生成文本的函数，生成文章
    generated_text = generate_text_function(keyword)
    # 将生成的文章返回给前端
    return generated_text

@app.route('/generate_video', methods=['POST'])
def generate_video():
    # 获取文本框2中的文章内容
    article = request.form['generatedText']
    # 获取其他选项的值，如数字人播报、视频比例、背景音乐和朗读音色
    narrator = request.form['avatar']
    video_ratio = request.form['videoRatio']
    background_music = request.form['music']
    voice_tone = request.form['voice']
    
    print(narrator, video_ratio, background_music, voice_tone)
    # 调用AI生成视频的函数，生成视频并返回生成进度
    progress = generate_video_function(article, narrator, video_ratio, background_music, voice_tone)
    # 将生成进度返回给前端
    return progress

if __name__ == '__main__':
    app.run()

