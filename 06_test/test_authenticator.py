import pytest
from authenticator import Authenticator  # Authenticatorクラスが書かれたファイルをimport

#register() メソッドで、ユーザーが正しく登録されるか
def test_register_user():
  auth = Authenticator()
  auth.register("user1", "pass1")
  assert auth.users["user1"] == "pass1"

#register() メソッドで、すでに存在するユーザー名で登録を試みた場合に、エラーメッセージが出力されるか
def test_register_duplicate_user():
  auth = Authenticator()
  auth.register("user1", "pass1")
  with pytest.raises(ValueError, match="ユーザーは既に存在します"):
    auth.register("user1", "pass2")

#login() メソッドで、正しいユーザー名とパスワードでログインできるか
def test_login_success():
  auth = Authenticator()
  auth.register("user1", "pass1")
  result = auth.login("user1", "pass1")
  assert result == "ログイン成功"

# login() メソッドで、誤ったパスワードでエラーが出るか
def test_login_wrong_password():
  auth = Authenticator()
  auth.register("user1", "pass1")
  with pytest.raises(ValueError, match="ユーザー名またはパスワードが正しくありません"):
    auth.login("user1", "wrongpass")