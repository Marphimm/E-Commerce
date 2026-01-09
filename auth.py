import hashlib
from data import users

current_user = None

def hash_password (password):
  encoded_password = password.encode()
  hashed_password = hashlib.sha256(encoded_password).hexdigest()

  return hashed_password

def register(username, password, role):
    global current_user

    for user in users:
        if user["username"] == username:
            print("Username sudah digunakan.")
            return

    user_id = len(users) + 1
    new_user = {
        "id": user_id,
        "username": username,
        "password": hash_password(password),
        "role": role
    }

    users.append(new_user)
    print("Registrasi berhasil.")

def login (username, password):
  global current_user
  hashed_input_pw = hash_password(password)
  
  for user in users:
    if user["username"] == username and user["password"] == hashed_input_pw:
      current_user = user
      return True
  
  return False

def logout():
  global current_user
  current_user = None


def is_logged_in():
  return current_user is not None

def require_login():
  if not is_logged_in():
    print('login Terlebih Dahulu')
    return True
  return False