from pytchat import LiveChat
import pafy
import pandas as pd

pafy.set_api_key('INSERT YOUR API KEY')

video_id='SX7EnUYfb1I'
v = pafy.new(video_id)
title = v.title
author = v.author
published = v.published

print(title)
print(author)
print(published)

empty_frame = pd.DataFrame(columns=['제목', '채널 명', '스트리밍 시작 시간', '댓글 작성자', '댓글 내용', '댓글 작성 시간'])
empty_frame.to_csv('./youtube.csv')
