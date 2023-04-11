# Video transcribe Tool
Use `openai-whisper` tool to transcribe audio contents of video
## Environment
`python=3.9`
### Install Package
`pip install -r requirements.txt`

## Usage

### Transcribe from existed video file(s)
```bash
# Convert Video to audio
# You can input multiple video files at the same time
python video_convert.py \
    -f <video_file_1> <video_file_2> ... <video_file_n> \
    --output-dir <output_directory>

# Transcribe audio
# You can input multiple audio files at the same time
python transcribe.py \
    -f <audio_file_1> <audio_file_2> ... <audio_file_n> \
    --model <model_name> \
    --language <language> \
    --device <device> \
    --output-dir <output_dir>

# Extract text / time information from output transcript
# You can input multiple transcript files at the same time
python transcript_cextract.py \
    -f <transcript_file_1> <transcript_file_n> ... <transcript_file_n> \
    --write-timestamp \
    --output-dir <output_directory>
```

### Transcribe YouTube videos
```bash
# Transcribe Audio of YouTube Video
python transcribe_youtube.py \
    --url <youtube_url> \
    --model <model_name> \
    --language <language> \
    --device <device> \
    --output <output_transcription_file>
```
## Example
[Video used in Example](https://youtu.be/F1WfUymkJGo)
```bash
python transcribe_youtube.py --url https://youtu.be/F1WfUymkJGo --model large --output result.json
python transcript_extract.py -f result.json --write-timestamp --output-dir ./transcript
```

### Result
```bash
# ./transcript/result.txt
[00:00:00 => 00:00:04] Crust 指的就是麵包皮的部分
[00:00:04 => 00:00:06] 既然號稱 Double Crust
[00:00:06 => 00:00:09] 這表示皮的厚度是一般麵包的雙倍嗎?
[00:00:09 => 00:00:12] 不 雖然皮的確比較厚
[00:00:12 => 00:00:15] 可是看起來應該不到雙倍
[00:00:15 => 00:00:18] 管它了 只要吃下去自然就知道答案了
[00:00:22 => 00:00:26] 沒有錯 我記得那是
[00:00:26 => 00:00:29] 我還在美國念高中的那個時候
[00:00:30 => 00:00:35] 亮 你好厲害啊 又拿到全學年的第一名啊
[00:00:35 => 00:00:37] 他的名字叫基德
[00:00:37 => 00:00:43] 啊 基德 基德是比我年長的同班同學 也是我的好友
[00:00:43 => 00:00:46] 考全學年第一 還裝得一副若無其事的轉樣
[00:00:46 => 00:00:50] 我看很快又要跳級了吧 真是討厭鬼
[00:00:51 => 00:00:54] 亮 你不要理會那些傢伙
[00:00:54 => 00:00:58] 他們只是因為比不過你 所以嫉妒你
[00:00:58 => 00:01:02] 我不僅是日本人 還不斷跳級
[00:01:02 => 00:01:06] 容易遭人嫉妒的我 多虧有他的鼓勵
[00:01:06 => 00:01:10] 打架 泡妞 發牢騷
[00:01:10 => 00:01:13] 不管做什麼我們都一起行動
[00:01:13 => 00:01:16] 而且 為了我 他什麼都願意做
[00:01:16 => 00:01:18] 從來都沒有露出半點不願
[00:01:18 => 00:01:22] 當我用功過度 身心俱疲的時候
[00:01:22 => 00:01:24] 是他幫我治療的
[00:01:24 => 00:01:26] 並沒有
[00:01:26 => 00:01:28] 當我得了思鄉病的時候
[00:01:28 => 00:01:31] 是他扮演母親的角色
[00:01:31 => 00:01:32] 並沒有
[00:01:32 => 00:01:35] 當我身上缺錢的時候
[00:01:37 => 00:01:40] 他不知從哪裡動來巨款 偷偷接濟我
[00:01:40 => 00:01:42] 不要瞎掰好嗎
[00:01:42 => 00:01:44] 可是有一天
[00:01:44 => 00:01:48] 我說亮 老實說 我又要留級了
[00:01:48 => 00:01:50] 是嗎
[00:01:50 => 00:01:54] 基德 你現在名符其實的成了
[00:01:54 => 00:01:56] Double Chris May
[00:01:56 => 00:01:59] 是這樣沒錯了 簡稱為
[00:01:59 => 00:02:00] 這還能簡稱嗎
[00:02:00 => 00:02:04] Double Crystal
[00:02:04 => 00:02:06] 這誰聽得懂啊
[00:02:06 => 00:02:11] 基德 你現在過得好嗎

```
