import json
from argparse import ArgumentParser
from math import floor

# formats seconds to HH:MM:SS,MS format
def format(seconds):
    ms = (seconds - floor(seconds)) * 1000
    s = floor(seconds)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{floor(ms):03d}"


def main(filename: str):

    # read file from arguments and parse it
    file = open(filename, "r")
    subtitle = json.loads(file.read())
    file.close()

    # encode all of the body into srt format
    subl = ""
    for index, body in enumerate(subtitle["body"], 1):
        start = format(body["from"])
        end = format(body["to"])
        formated = f"{index}\n{start} --> {end}\n{body['content']}\n\n"
        if body["location"] == 2:
            subl += formated

    # write file
    subf = open(filename.replace(".json", ".srt"), "w")
    subf.write(subl.strip())
    subf.close()


if __name__ == "__main__":

    # parse arguments
    ap = ArgumentParser(
        "jsontosrt", description="turns bilibili subtitle to srt subtitiles"
    )
    ap.add_argument("file", nargs="+", help="files")
    arg = ap.parse_args()

    # take all the arguments and feed it to main one by one
    for file in arg.file:
        main(file)
