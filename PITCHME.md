
#### チーム開発時にやっておいたほうが良いこと
#### 〜how to raise a Boring source code〜
#### Yuuki Nakajima

---
#### 対象
 
 - これからチーム開発を始めようという人
 - ソースコードはきれいに保ちたい人
 - とりあえずflake8してる人(よく分かってない) 
 - とりあえずblackしてる人(よく分かってない)

---
#### チーム開発の流れ

  - ソースコードを書く
  - レビューする
  - マージされる
  - リリースされる
  - 書く
  - レビューする
  - マージされる
  - リリースされる
  - ソースコードを書く
  - サービスが終了する
  
---

### ソースはちょっとずつ綻んでいく

![alt](assets/babel.jpg)

---

コードの一貫性を持たせることがチーム開発では必要

---
ここで話すこと
  - ソースコードを整えるための規約の紹介
  - 規約通りになっているかチェックするためのライブラリの紹介
  - 規約通りにソースを直してくれるライブラリの紹介

---

みたいな話しをしようと思っていましたが。。。

----

だいたい雑誌に書かれてしまった！

![alt](assets/image_000_web_db_press.jpg)

> 現場のPython ── システム開発も！ 機械学習も！
【第1回】開発支援ツールで安全で効率的に ……コード解析，型チェック，コードフォーマッタの実践的設定
#### TODO:URLは変わる
https://www.fujisan.co.jp/product/1281680264/new/

---

とりあえずやりたいことはここを読めばOK

---

ここで何を話そう？

---
考えた末、以下の要素を付け足すことにしました


---

 - とりあえずflake8は正しいのか？
 - とりあえずblackは正しいのか？

---

#### 目次

- Ⅰ.冴えないコードの防ぎ方
  - 罪深きソースコードの例
  - コード規約PEP8とは？
    - PEPって何？
    - PEPの例
    - PEP8とは？
  - flake8でソースをチェック
    - flake8の使い方
- Ⅱ.冴えたコードの維持の仕方
  - formatterによるcheck
  - とりあえずblackは正しいのか？
    - AutoPep, yapf, blackの比較
  - formatterの自動化
    - pre-commitで自動適応

---


[001_ GuiltyCode.py]

```
import sys
import this

def translationCall(Input):
    aaaaaaa = Input
    if Input == "虎":
        return "tiger" 
    if Input == "火":
        return "fire"
    return "jya-jya-";


if __name__ == "__main__":
    Input  = sys.argv[1] 
    returnVAlue = translationCall(Input);
    print(returnVAlue)
```


```
% python code/001_\ GuiltyCode.py 虎
tiger
```
---

許しがたいコードですがこれをどう直していけばいいでしょうか？

```
def translationCall(Input)
def TranslationCall(Input)
def TranslationCall(input)
def translation_call(Input)
def translation_call(input)
```
↑関数名1つ取っても直し方の選択肢がたくさんある


---
PEP8：コード規約の紹介

---


そもそもPEPってなに？

What is a PEP?
PEP stands for Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.

https://www.python.org/dev/peps/pep-0001/#id34

---

>What is a PEP?
PEP stands for Python Enhancement Proposal.<br>

PEPとはPython改良提案を意味する語の頭文字を取ってPEP


>A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment.<br>

PEPは、Pythonコミュニティに情報を提供するか、Pythonまたはそのプロセスや環境の新機能を説明する設計ドキュメントです。

---

PEPの例
PEP11
- Removing support for little used platforms

```
Name: MS-DOS, MS-Windows 3.x
Unsupported in: Python 2.0
Code removed in: Python 2.1
```
https://www.python.org/dev/peps/pep-0011/

windows3.1ではpython2.0でサポートを切られたことが分かる

---
PEP８とは

- PEPで提案されたコード規約

---
#### PEP8の紹介 

- 1日本語で読める

https://pep8-ja.readthedocs.io/ja/latest/

- 一貫性にこだわりすぎるのは、狭い心の現れである
- 関数の名前は小文字で単語はアンダースコア(_)で繋ぐ
  - e.g goto_travel
- クラス名はCapsWordsで書く
  - e.g class Itaewon():
- 関数やクラスは2行ずつ空ける
- メソッドは1行空ける
- 括弧の初めの直後と終わりの直前に空白を入れない

---

 このくらいなら意識できそう

---
#### 他のルール

  - 1行の長さは79文字
  - importの順番は以下のように行い、それぞれアルファベット順にする
    - 標準ライブラリ(Pythonが持ってるライブラリ,datetimeとか)
    - サードパーティライブラリ(pip installしたライブラリ,requestsとか)
    - 自分のライブラリ(from util import my_function)
    -  それぞれアルファベット順にする
  - コメントが2つ以上の文からなる場合、終わりのピリオドの後は、二つスペースを入れる
    - ただし、最後の文を除く。

---

- この辺まで意識するのは辛い！！！！

---

### flake8
  - Flake8は以下のライブラリのラッパーツール:
    - PyFlakes
    - pycodestyle
    - Ned Batchelder's McCabe script

---

#### pyflakes

- コードチェックimportのみライブラリや未使用変数をチェック

```
% pyflakes .
./001_ GuiltyCode.py:2:1 'this' imported but unused
./001_ GuiltyCode.py:5:5 local variable 'aaaaaaa' is assigned to but never used
```
---

#### pycodestyle

 - コードチェック
 - 改行とか空白の位置とかをチェック

```
pycodestyle 001_\ GuiltyCode.py 
001_ GuiltyCode.py:3:1: E302 expected 2 blank lines, found 1
001_ GuiltyCode.py:5:23: W291 trailing whitespace
001_ GuiltyCode.py:8:22: E703 statement ends with a semicolon
001_ GuiltyCode.py:12:10: E221 multiple spaces before operator
001_ GuiltyCode.py:12:25: W291 trailing whitespace
001_ GuiltyCode.py:13:41: E703 statement ends with a semicolon
001_ GuiltyCode.py:14:23: W292 no newline at end of file
```
---

#### mccabe 
  - 複雑さをチェックする

[002_complex_code.py]
```
import sys


def translation(input):
    ja_calls = ["虎", "火", "人造",  "繊維", "海女", "振動", "化繊"]
    en_calls = ["tiger", "fire", "cyber", "fiber", "diver", "viber"]
    i = 0
    j = 0
    is_unmatch = False
    for c in ja_calls:
        if c != input:
            is_unmatch = True
        if c == input:
            is_unmatch = False
        if is_unmatch:
            i = i + 1
            continue
        for cc in en_calls:
            if j != i:
                j += 1
                continue
            return_value = en_calls[j]

    if return_value:
        return return_value
    else:
        return_value = "jya-jya-"
    return return_value

if __name__ == "__main__":
    input = sys.argv[1]
    output = translation(input)
    print(output)
```

---

- 複雑度が数字で表示される
```
% python -m mccabe --min 5 002_complex_code.py
4:0: 'translation' 8
```

---
この3つを合体したものがflake8

---
使い方
```
flake8 .
./001_ GuiltyCode.py:2:1: F401 'this' imported but unused
./001_ GuiltyCode.py:4:1: E302 expected 2 blank lines, found 1
....
```

---

複雑度もチェックする(defaultでは無効)
```
flake8 --max-complexity 5 002_complex_code.py 
002_complex_code.py:4:1: C901 'translation' is too complex (8)
```

---

まとめ
 - pythonにはPEP8という指針がある
 - 規約を守らせるためにflake8というライブラリを入れるとコードチェックできる
---
・・といきたいのですが

---
こちらをご覧下さい

[guilty_code2.py]
```
class itaewon():
    def Method():
        return ""
```
```
% flake8 006_gilry_code2.py
%
```
---
お気づきでしょうか？

---

PEP８の規約に書かれたエラーが出ていない！
```
class itaewon(): ☆　class名はCapWords Iteawon!
    def Method(): ☆ メソッド名はlower_case!
        return ""
```
---

対処: pep8-naming というライブラリを入れるとこの辺もチェックしてくれます

- `pip install　pep8-nameing`　して 今まで通りflake8するだけ

N系(naming)系のエラーが表示されるようになる

```
% flake8 006_gilry_code2.py
006_gilry_code2.py:1:8: N801 class name 'itaewon' should use CapWords convention
006_gilry_code2.py:2:10: N802 function name 'Method' should be lowercase
```

---

#### まとめ
 - pythonにはPEP8という指針がある
 - 規約を守らせるためにflake8というライブラリを入れるとコードチェックできる
 - pep8-namingというライブラリを入れると命名規則もチェックしてくれる

---

息抜き

---

本当にあった怖い話し(終刊実話)

---

なにもしてないのにciが通らなくなった

---

[003_f_string_faild.py]
```
def translation(input):
    if input == "虎":
        return "tiger"
    return "jya-jya-"


if __name__ == "__main__":
    output = translation(f"虎")
    print(output)
```

`output = translation(f"虎")` 

 - f"虎" は確かに"虎"と同じなので無意味
 - pycodestyleではこの書き方は検知されていなかった
 - pyflakesの2.2.0(Apr 10,2020)からこれをチェックするようになった 
 - その結果ある日突然ソースが落ちる自体に！！！

---

− これでソースは何となく一貫性が守られるようになりましたが。。。 

----

--- 

---


#### 😭

---

手動チェック辛い・・・・

---

formatterでformatしよう

---
ググると出てくるライブラリ
- black: スター数 17.1K(2020/08/15)
  - https://github.com/psf/black
- yapf: スター数 10.9k(2020/08/15)
  - https://github.com/google/yapf
- autopep8: スター数 3.5k(2020/08/15)
  - https://github.com/hhatto/autopep8

---

最近だとblackでOKという記事がでてくるので
とりあえずblackという方も多いはず(かくいう私も...

---

## black

- 今のバージョンは19.10b0
- まだベータ版とは書いてあるが大きな変更は予定されていない
- 妥協のないpythonコードフォーマッター
- 手動フォーマットを全てblackに譲ることになる
- フォーマットで悩むことがなくなる

---

blackを通してもflake8は通らないものがある！

---

004_conflict_black_flake8
```
# E203 Whitespace before ':'
name_lists = ["tarou", "hanako", "ichitarou", ""]
a = name_lists[1 + 1 :]

# E501 line too long (XX > 79 characters)
name = "jyugemujyugemu gokounosurikire kaijyarisuigyono suigyoumatu unnkoumatu."

# W503 line break before binary operator
income = (3
          + 4)
```

---

### 対策

とりあえずflake8からエラーを除外すればOK(公式に書かれた記載を転載)

```
[flake8]
max-line-length = 80
...
select = C,E,F,W,B,B950
ignore = E203, E501, W503
```

---

### yapf

- google製のFormatter
- PEP8に準拠したコードが正しいとは限らない
- end all holy wars about formatting
  - フォーマットに関する全ての聖戦を終わらせる
- やたら細かく設定できる

---
### 設定方法

```
[yapf]
based_on_style = pep8/google/yapf/facebook
spaces_before_comment = 4
split_before_logical_operator = true
```

- 58項目ぐらい設定できる
  -　インデントの数
  - 文末のセミコロンを許可するか
  -  等々・・・
----
#### 使い方

`yapf --i --style='{DISABLE_ENDING_COMMA_HEURISTIC=True}' src/005_yapf_sample.py`

```
one = "two";
```
↓↓↓
```
one = "two"
```
----

#### autopep

 - pep8のスタイルガイドに準拠したフォーマッター
 - pycodestyleを使っている
 - pycodestyleにはない問題の修正も行っている
 - aggressiveレベルを指定してそれによって修正内容が異なる

---

まとめ
- formatterには大きく３つある
 - black
    - フォーマットの設定が指定できないようにすることでかえって細かい論争を封じ込める
 - yapppf
    − 細かい設定を充実させることで、プロジェクト毎に任意の設定を作れるようにする
 - autopep
    - pep8という原典に従うことを是としたライブラリ
      - 設定は３段階で行うことが出来る

---

 pre-commitでformatterを自動的に動かそう

 ---

 formatterが決まったことで、細かいルールも決まりました

 ---

 でも、選んだファイルをformatterにかけ忘れてcommit & pushしてしまったら？

---

![alt](assets/babel.jpg)

---

うっかりミスを防ぐためにはpre-commitを採用してみましょう

---

pre-commitとは・・・・
 - gitフックスクリプト
 - コミット毎にフックを実行
   - セミコロンの欠落や末尾の空白などのコードの問題を自動的に指摘

---
使い方
- .pre-commit-config.yamlを用意してその中に実行したい内容を書く

```
pos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: statble 
    hooks:
    -   id: black
```

---
