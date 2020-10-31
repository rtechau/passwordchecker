import requests
import hashlib
import tkinter as tk

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

def user_pass():
  # password = input('Please Enter A Password That You Would Like To Check: ')
  password = str(pass_entry.get())
  count = pwned_api_check(password)
  if count:
    pass_resp['text'] = f'{password} was found {count} times... you should change your password!'
  else:
    pass_resp['text'] = f'{password} was NOT found it is safe to use!'

def main():
  while True:
    user_pass()
    break

def clear_pass():
  pass_entry.delete(0, 'end')

window = tk.Tk()
window.title('Pwned Password Checker')
pass_entry = tk.Entry(master=window)
check_button = tk.Button(master=window, text='Check My Password', command=main)
clear_entry = tk.Button(master=window, text='Clear', command=clear_pass)
pass_resp = tk.Label(master=window, text='')
pass_entry.grid(row=0, column=0)
check_button.grid(row=0, column=1)
clear_entry.grid(row=0, column=2)
pass_resp.grid(row=1, column=0)
window.mainloop()