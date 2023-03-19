from os.path import isfile


def api_setup():
    def inputAPI(file):
        print("No api key stored, use /api new in game to get yours")
        file.write(input("API Key: "))
        print("Saved API Key")

    # Gets or Set API key
    if isfile("./key.text"):
        f = open("key.text", "r+")
        if f.readline() == "":
            inputAPI(f)
    else:
        f = open("key.text", "w")
        inputAPI(f)
    f.close()


api_setup()
