import streamlit as s

col1, col2, col3, col4, col5 = s.columns([2, 3, 2, 2, 2])
col6,col7 = s.columns([2,1])
ten = ''
sc = ''
tc = ''
tt = ''
v = ''
so = ''
with col1:
  b1 = s.button("con mèo")

if b1:
  with col7:
    s.image("https://tse4.mm.bing.net/th?id=OIP.Si4ivaE9XuP2QcWAf5YVPAHaE9&pid=Api&P=0&h=180")
  with col6:
      v = "https://youtu.be/Mle5Xtckzdc"
      so = "meo.mp3"
      s.video(v,format = 'mp4')
      s.audio(so,format = 'mp3')
with col2:
  b2 = s.button("con chó")
  if b2:
    with col7:
      s.image("https://tse1.mm.bing.net/th?id=OIP.diY65IdV9ekzJkrQQleNegHaEK&pid=Api&P=0&h=180")
    with col6:
      v = "https://youtu.be/Jjql2hBR7Dw"
      so = "cho.mp3"
      s.video(v, format='mp4')
      s.audio(so, format='mp3')
with col3:
  b3 = s.button("con chim")
  if b3:
    with col7:
      s.image("https://tse1.mm.bing.net/th?id=OIP.daz0MKGJWZk8eh141E2XzAHaEK&pid=Api&P=0&h=180")
    with col6:
      v = "https://youtu.be/VjE0Kdfos4Y"
      so = "chim.mp3"
      s.video(v, format='mp4')
      s.audio(so, format='mp3')
with col4:
  b4 = s.button("con heo")
  if b4:
    with col7:
            s.image("https://i.ytimg.com/vi/DX5VbKSF4qY/maxresdefault.jpg")
    with col6:
          v = "https://youtu.be/0dFwx95ufEk"
          so = "heo.mp3"
          s.video(v, format='mp4')
          s.audio(so, format='mp3')
with col5:
  b5 = s.button("con bò")
  if b5:
    with col7:
          s.image("https://tse2.mm.bing.net/th?id=OIP.ihK_2aS6bOIZ9aJrxAgc7wHaEK&pid=Api&P=0&h=180")
    with col6:
          v = "https://youtu.be/eqNFkY7gAOw"
          so = "bo.mp3"
          s.video(v, format='mp4')
          s.audio(so, format='mp3')
if b1:
  ten = "Con vật:con mèo"
  sc = "Số chân: 4"
  tc = "tính cách: thích ở một mình"
  tt = "thuộc tính : nhanh nhẹn"
if b2:
  ten = "Con vật:con chó"
  sc = "Số chân: 4"
  tc = "tính cách: trung thành"
  tt = "thuộc tính : thân thiện"
if b3:
  ten = "Con vật:con chim"
  sc = "Số chân: 2"
  tc = "tính cách: kiên trì"
  tt = "thuộc tính : biết bay"
if b4:
  ten = "Con vật:con lợn"
  sc = "Số chân: 4"
  tc = "tính cách: thích sạch sẽ"
  tt = "thuộc tính : mập mạp"
if b5:
  ten = "Con vật:con bò"
  sc = "Số chân: 4"
  tc = "tính cách: thích ăn"
  tt = "thuộc tính : to lớn"

with s.expander("giới thiệu con vật"):
  s.write(ten)
  s.write(sc)
  s.write(tc)
  s.write(tt)



      
      
