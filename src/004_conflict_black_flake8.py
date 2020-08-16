# flake8でチェックするとエラーが出るがblackでは直してくれないもの
# E203 Whitespace before ':'
name_lists = ["tarou", "hanako", "ichitarou", ""]
a = name_lists[1 + 1 :]

# E501 line too long (XX > 79 characters)
name = "jyugemujyugemu gokounosurikire kaijyarisuigyono suigyoumatu unnkoumatu."

# W503 line break before binary operator
income = (3
          + 4)
