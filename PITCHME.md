
#### チーム開発時にやっておいたほうが良いこと
#### 〜how to raise a Boring source code〜
#### Yuuki Nakajima
---

#### 問題意識
- プログラマーはどうしても個人の癖がでてしまう。
- 全体としてルールが統一がされていないことがある。
- Pythonに不慣れだと他の言語の癖がでてしまう
- 後から見てとても辛いソースになる
- 開発環境が異なるとIDEで開いた瞬間に警告がたくさんでる人と出ない人がいる
---

- そういった部分をレビューで指摘するのはしんどい
- pythonの規約に対する警告などはgitの差分とかでは見過ごしてしまう
- とりあえずflake8(内容を理解せずに使ってる(自分のこと))
- とりあえずblack(内容を理解せずに使っている(自分の(ry)

---

Agenda
  - avant-title
  - introduction
  - probrem
  - An warning-ridden Prologue next!
  - What is  PEP-8?
      - about PEP(Python Enhancement Proposal)
      -　explain PEP-8
  - code check tools
      - flake8
      - mypy
      - pylint
      - seed-isort-confing
  - summary
  - use formatter 
      - About formatter
          - introduce some library
              - autopep
              - black
              - yapf
          - compare these library
   - pre-commit!
      - about pre-commit
      - example pre-commit
      - 
   - summary
   - QA 


---


```[code-1bad sample]
import sys

def TranslationCall(Input):
    if Input == "虎":
        return "tiger" 
    if Input == "火":
        return "fire"
    return "jya-jya-";


if __name__ == "__main__":
    Input  = sys.argv[1] 
    returnVAlue = TranslationCall(Input);
    print(returnVAlue)
```
正しく動作する

```
% python code/001_\ GuiltyCode.py 虎
tiger
```
---

- Pythonのコーディング規約pep8に付いて(5min)


---


---

- なんでも動けばええじゃろ?
- こまけぇことはいいんだよ！

--

そこでPEP8

---
PEPってなに？

What is a PEP?
PEP stands for Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.

We intend PEPs to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions.

Because the PEPs are maintained as text files in a versioned repository, their revision history is the historical record of the feature proposal

https://www.python.org/dev/peps/pep-0001/#id34

---

What is a PEP?
PEP stands for Python Enhancement Proposal.
→　PEPとはPython改良提案を意味する語の頭文字を取ってPEP

A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment.
→PEPは、Pythonコミュニティに情報を提供するか、Pythonまたはそのプロセスや環境の新機能を説明する設計ドキュメントです。


---
We intend PEPs to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions.

###### 私たちは、PEPが主要な新機能を提案したり、問題に関するコミュニティの意見を収集したり、Pythonに取り入れられた設計上の決定を文書化したりするための主要なメカニズムになることを意図しています。 PEPの作成者は、コミュニティ内でコンセンサスを構築し、反対意見を文書化する責任があります。
---

##### Because the PEPs are maintained as text files in a versioned repository, their revision history is the historical record of the feature proposal

##### PEPはバージョン管理されたリポジトリでテキストファイルとして維持されるため、その改訂履歴は機能提案の履歴レコードです。
---

PEPの例

いくつかのPEPを紹介

---
PEP８とは

- PEPで提案されたコード規約

---

- コード規約についていくつか紹介

---

- 正直、これを意識して書くのって辛いよね

---

- flake8について

Flake8 is a wrapper around these tools:

PyFlakes
pycodestyle
Ned Batchelder’s McCabe script

----
- flake8での実例、使用例をいくつか書く

---
formatterでformatしよう





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