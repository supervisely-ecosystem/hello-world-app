import supervisely as sly
from dotenv import load_dotenv
from art import tprint

# load ENV variables for debug
# has no effect in production
if sly.is_development():
    load_dotenv("local.env")


def main():
    name = sly.env.user_login()
    print("Hello World! This app is run by the user:")
    tprint(name)


if __name__ == "__main__":
    main()
