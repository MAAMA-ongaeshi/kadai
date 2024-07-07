import streamlit as st
import numpy as np

st.title("キミのたいせつないのちをまもれるかな？！")
st.header("おおきなこえでこたえてね")

biginner_word_pairs = {
    "いか": "いかない!  しらない人についていかない！もししらない人にさそわれても、おうちのひとにそうだんしてからでかけよう！",
    "の": "のらない！  しらない人のくるまにのらない!",
    "お": "おおごえをだす！  こわいときはたすけて、とおおきなこえをだそう",
    "す": "すぐにげる！ こわいときはそのばからすぐにげよう。",
    "し": "しらせる！  こわいめにあったらすぐちかくのおとなにしらせよう",
    "いちにん": "１人・ひとりであそばない！  わるい人はひとりでいるこどもをねらっています",
    "まえ": "でかけるまえにおうちの人に、「だれ」と「どこ」へいくのかを、いおう!"
}

intermediate_words_pairs = {
    "おうだんほどうをわたるよ": "みぎみてひだりみて、てをあげて",
    "まがりかどにきたよ": "みぎみてひだりみてうしろみて、まえをみてすすもう！",
    "あ、はんたいがわでおかあさんをみつけたよ": "とびださない、はしらない、まわりをよくみてね",
    "ボールがころがっていっちゃった": "おいかけない、くるまがきていないかよくたしかめて！",
    "どうろでボールあそびはたのしいな": "だめだね、ボールあそびはきまったばしょでね。",
    "はしっこをあるくから、うしろむきあるきしよ〜": "どうろでは、しっかりまえをみて、ちゅういしながらあるこう"
}

quiz_data_set = {
  "いかのおすし1人前": biginner_word_pairs,
  "こうつうルール": intermediate_words_pairs
}

level = st.sidebar.radio("レベルを選択", ["いかのおすし1人前","こうつうルール"])
word_pairs = quiz_data_set[level]

if st.button("もんだい"):
  index = np.random.randint(0,7)
  english_word = list(word_pairs.keys())[index]
  st.markdown(f"## {english_word}")

  with st.expander("わかったかな？"):
    japanese_word = word_pairs[english_word]
    st.write(f"## {japanese_word}")

if st.button("つぎは、わかるかな"):
  placeholder = st.empty()
  placeholder.empty()

import pandas as pd
#import streamlit as st

if st.button("おわったら、ダンスしよう！！"):
  link = '♪いかのおすしいちにんまえ　ダンス♪　https://youtu.be/RdQcna4kwqg?t=8'
  st.markdown(link, unsafe_allow_html=True)