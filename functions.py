from time import sleep


def login(email, secret, robot):
    login_url = "https://accounts.spotify.com/en-GB/login"
    robot.get(login_url)
    old_url = robot.current_url
    username = "login-username"
    password = "login-password"
    button = "login-button"
    username_element = robot.find_element("id", username)
    password_element = robot.find_element("id", password)
    button_element = robot.find_element("id", button)
    username_element.send_keys(email)
    password_element.send_keys(secret)
    button_element.click()
    sleep(1)
    new_url = robot.current_url
    if old_url != new_url:
        print("Sucess")
    else:
        print("Fail")
    sleep(5)
    robot.quit()

def sign_up():
    signup_url = "https://www.spotify.com/en-GB/signup"