# bilibili-tools

converts downloaded bilibili videos into usable types. _Note: This is created for linux and it is not guaranteed to work with other OSes. If you made it work with your OS please let me know._

## How it Works

bilibili store downloaded videos in their own folders with the video, audio and subtitles. bilibili-tools converts the subtitles into srt and combine it with the video and audio. It also package it in a format Plex server can read.

## Usage

### get entire season

1. First take the downloads folder from bilibili and put it into your computer. You can find it inside `Android/data/com.bstar.intl/download`. _Note: you should download the entire season first_

2. Go to the the folder where you left the download folder and start your terminal there.

3. When you open the downloads folder you will see random looking folders. Select one of it.

4. Run

```
git clone https://github.com/nanashi-1/bilibili-tools.git
```

This will download the tools into `bilibili-tools`.

5. Run

```
python bilibili-tools/jsontosrt.py download/${season_id}/*/subtitle.json
```

Remember to replace the `${season_id}` with the folder you selected earlier.

This will convert every `subtitle.json` into `subtitle.srt`.

6. Run

```
for i in download/${season_id}/*/64; do ffmpeg -i $i/video.m4s -i $i/audio.m4s -i $i/../subtitle.srt -map 0 -map 1:a:0 -map 2 -codec copy $i.mkv; done;
```

This will combine video, audio and subtitles, though the subtitles are softsub. If you want hardsub you can use `-vf` option instead. Replace 64 if you did not download it in 720p. See [How To Burn Subtitles Into Video.](https://trac.ffmpeg.org/wiki/HowToBurnSubtitlesIntoVideo)

7. Now all the videos are ready. You can take them one by one in `${season_id}/*/64.mkv` or you can run

```
python bilibili-tools/package.py -o . -v 64.mkv -e entry.json download/${season_id}/*
```

to package it automatically.

Note:

- Some animes have their episode 1 indexed as PV
