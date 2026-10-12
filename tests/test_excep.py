import unittest


def login(username):
  if not username:
    raise ValueError("Имя пользователя не может быть пустым")
  return f"Привет, {username}"


class TestAuth(unittest.TestCase):

  def test_login_empty_username(self):
    # Проверяем тип исключения И то, что в сообщении есть фраза "не может быть пустым"
    with self.assertRaisesRegex(ValueError, "не может быть пустым"):
      login("")


