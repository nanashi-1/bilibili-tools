from argparse import ArgumentParser
import json
from os.path import join, isdir
from os import mkdir
from json import loads
from shutil import move


def main(dir, video, entry, output):
    entryf = open(join(dir, entry), "r")
    entrys = entryf.read()
    title, ep = (loads(entrys)["title"], loads(entrys)["ep"]["index"])
    entryf.close()
    if not isdir(join(output, title)):
        mkdir(join(output, title))
    if "PV" in ep or "SP" in ep: move(join(dir, video), join(output, title, f"{title} - {ep}.mkv"))
    else: move(join(dir, video), join(output, title, f"{title} - e{int(ep):02d}.mkv"))


if __name__ == "__main__":
    ap = ArgumentParser("package", description="package everything")
    ap.add_argument(
        "-o", "--output", "-output", help="the output directory", required=True
    )
    ap.add_argument("-e", "--entry", "-entry", help="the entry file", required=True)
    ap.add_argument("-v", "--video", "-video", help="the video file", required=True)
    ap.add_argument("dirs", nargs="+", help="the input directory")
    args = ap.parse_args()
    for dir in args.dirs:
        main(dir, args.video, args.entry, args.output)
