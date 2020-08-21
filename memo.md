https://sessionize.com/app/speaker/session/203858

https://docs.google.com/document/d/1g8Ly6n03avly-p3GMoQZhS9hIFm9-WwsoHTSUgqS0ZI/edit#heading=h.7uitjdlqo2we


提出したプロポーザル

pythonのソースコードを綺麗に保つためのいくつかの方法について説明します。
- 対象
- チーム開発で新規プロジェクトを立ち上げる方
- ソース管理はきっちりやりたい方(""と''が混在して欲しくない)
- 耳学問でpre-commitとかflake8とかpep8とか訊いたことがあるけどよく分からない方
- formatterで内容は分からないけど適当に他のプロジェクトで使ってるものを使い回してる方


この登壇ではPythonのコーディング規約であるPEP8に付いての簡単な説明から、flake8のようなラッパーツール、
blackのようなformatterそしてそれらを自動で適用させるためのpre-commit、そしてそこに導入するべき他のformatter(mypyやseed-isort-configなど)に付いて簡単に説明し、ソースをどのように修正してくれるのかなどを実例を示しながら説明していきたいと思います。


構成とタイムラインは以下のとおりです。
- 導入（3min）
- 自己紹介
- 問題意識
- チーム開発の場合、どうしても個人の癖がでてしまい、全体としてルールが統一がされていないことがある。 また開発環境の違いによっては警告がでる人と出ない人の差などがあり不快感もある。
レビューの時でもそうした本質的ではない部分で指摘することは時間の無駄となっている。
- Pythonのコーディング規約pep8に付いて(5min)
- pep8とはなにか？
- 実例紹介
- formatterについて（10min）
- autopepについての説明と実例
- blackについての説明と実例
− yapfについての説明と実例
- それぞれの比較
- pre-commitでformatterを自動化(8min)
- 指定方法の実例
- 上記の他に指定しておくといいものの紹介
- seed-isort-confingやmypyなど
- まとめ (1min)
- 質疑応答 (3min)




pep8について調査する(まずはその思想的背景からいきたい)

参考資料
pep-8
https://pep8-ja.readthedocs.io/ja/latest/
日本語版
https://www.python.org/dev/peps/pep-0008/

---
### pep8を読む

pep8とプロジェクト毎のルールがあったらプロジェクトを優先する

PEP 20 にもあるように "可読性重要" です。

##### この規約を神聖視してはいけない(大事な価値転倒！)

細かい事例紹介

1重引用符か二重引用符かはどちらを優先するかはここでは示さない

英語を話さない国出身の Python プログラマの方々へ：あなたのコードが、自分の言葉を話さない人に 120% 読まれないと確信していなければ、コメントを英語で書くようにお願いします。

ドキュメンテーション文字列(別名 "docstrings")を書くための規約は、PEP 257 に記載

----

formatterの調査
- flake8
- autopep
- black 
- yapf


## スライドの統一感をどう持たすか？
絶対にイラストやさんは使わない


ストーリー下手でいきたい
タイトルの元ネタは全部冴えカノでいく
how to raise a boring code
冴えないコードの育て方  


Question

---
 #### which is correnct?

```
if (condition)
 {
   …
}
```

```
if (condition){
  …
}
```
---

Can't choose!✋

---
collect!✋

```
if (condition)
 {
   …
}
```

---

collect!✋
```
if (condition){
  …
}
```

---
> 「本質的な選択肢」であり、十分に「深い仮説がある」問題でありながら、よいイシューではない、というものが存在する。
> それは、明確な答えを出せない問題だ。

> 安宅和人. イシューからはじめよ  知的生産の「シンプルな本質」 (Japanese Edition) (Kindle の位置No.687-689). Kindle 版. 
---


## this is not issue!

```
if (condition)
 {
   …
}
```

 or 

```
if (condition){
  …
}
```