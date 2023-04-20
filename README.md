# Video transcribe Tool
Use `openai-whisper` tool to transcribe audio contents of video
## Environment
`python=3.9`
### Install Package
`pip install -r requirements.txt`

## Usage

### Transcribe files
```bash
python transcribe.py \
    -f <audio/video_file_or_YouTubeURL_1> <audio/video_file_or_YouTubeURL_2> ... <audio/video_file_or_YouTubeURL_n> \
    --model <model_name> \
    --output-dir <output_directory>
```

You can execute `transcribe.py` to transcribe multiple video/audio files or YouTube videos.
input of `--files-or-urls` accept `.mp4` / `.mp3` / `.wav` files and YouTube URL, input them together is OK

```bash
python transcribe.py -f your_audio_dir/audio.mp3 your_video_dir/video.mp4 <YouTube_URL>
```

### Convert Transcribe File to SRT format file
```bash
python transcript_to_srt.py \
    -f <transcript_file_1> <transcript_file_2> ... <transcript_file_n> \
    --output-dir <output_directory>
```

### Text Summarize (Demostrative)
You can execute `summarize.py` to get text summary of transcribe file text.
But it may not a useful function currently... just a demostrative function right now.
```bash
python summarize.py \
    -f <transcript_file_1> <transcript_file_2> ... <transcript_file_n> \
    --output-dir <output_directory>
```

## Example
[Video used in Example](https://youtu.be/F1WfUymkJGo)
```bash
python transcribe.py -f https://youtu.be/F1WfUymkJGo --model large --output-dir transcript
python transcript_to_srt.py -f transcript/* --output-dir ./srt
```

### SRT Result
```bash
1
00:00:00,000 --> 00:00:04,000
Crust 指的就是面包皮的部分

2
00:00:04,000 --> 00:00:06,000
既然號稱 Double Crust

3
00:00:06,000 --> 00:00:09,000
這表示皮的厚度是一般面包的雙倍嗎?

4
00:00:09,000 --> 00:00:12,000
不,雖然皮的確比較厚

5
00:00:12,000 --> 00:00:15,000
可是看起來應該不到雙倍

6
00:00:15,000 --> 00:00:19,000
管它了,只要吃下去自然就知道答案了

7
00:00:19,000 --> 00:00:22,000
Oh, no!

8
00:00:22,000 --> 00:00:24,000
沒有錯

9
00:00:24,000 --> 00:00:26,000
我記得那時

10
00:00:26,000 --> 00:00:30,000
我還在美國念高中的那個時候

11
00:00:30,000 --> 00:00:32,000
亮,你好厲害啊

12
00:00:32,000 --> 00:00:35,000
又拿到全學年的第一名啊

13
00:00:35,000 --> 00:00:37,000
他的名字叫基德

14
00:00:37,000 --> 00:00:39,000
啊,基德

15
00:00:39,000 --> 00:00:42,000
基德是比我年長的同班同學

16
00:00:42,000 --> 00:00:43,000
也是我的好友

17
00:00:43,000 --> 00:00:44,000
考全學年第一

18
00:00:44,000 --> 00:00:46,000
還裝得一副若無其事的轉讓

19
00:00:46,000 --> 00:00:48,000
我看很快又要跳級了吧

20
00:00:48,000 --> 00:00:50,000
真是討厭鬼

21
00:00:51,000 --> 00:00:54,000
亮,你不要理會那些傢伙

22
00:00:54,000 --> 00:00:56,000
他們只是因為比不過你

23
00:00:56,000 --> 00:00:58,000
所以嫉妒你

24
00:00:58,000 --> 00:01:00,000
我不僅是日本人

25
00:01:00,000 --> 00:01:02,000
還不斷跳級

26
00:01:02,000 --> 00:01:04,000
容易遭人嫉妒的我

27
00:01:04,000 --> 00:01:06,000
多虧有他的鼓勵

28
00:01:06,000 --> 00:01:10,000
打架,泡妞,發牢騷

29
00:01:10,000 --> 00:01:13,000
不管做什麼我們都一起行動

30
00:01:13,000 --> 00:01:16,000
而且,為了我他什麼都願意做

31
00:01:16,000 --> 00:01:18,000
從來都沒有露出半點不願

32
00:01:18,000 --> 00:01:22,000
當我用功過度,身心俱疲的時候

33
00:01:22,000 --> 00:01:24,000
是他幫我治療的

34
00:01:24,000 --> 00:01:26,000
並沒有

35
00:01:26,000 --> 00:01:28,000
當我得了思鄉病的時候

36
00:01:28,000 --> 00:01:31,000
是他扮演母親的角色

37
00:01:31,000 --> 00:01:32,000
並沒有

38
00:01:32,000 --> 00:01:34,000
當我身上缺錢的時候

39
00:01:37,000 --> 00:01:39,000
他不知從哪裡動來巨款

40
00:01:39,000 --> 00:01:40,000
偷偷接濟我

41
00:01:40,000 --> 00:01:42,000
不要瞎掰好嗎

42
00:01:42,000 --> 00:01:44,000
可是有一天

43
00:01:44,000 --> 00:01:46,000
我說亮,老實說

44
00:01:46,000 --> 00:01:48,000
我又要留級了

45
00:01:48,000 --> 00:01:50,000
是嗎

46
00:01:50,000 --> 00:01:52,000
哎,基德

47
00:01:52,000 --> 00:01:54,000
你現在名符其實的成了

48
00:01:54,000 --> 00:01:56,000
Double Christmas

49
00:01:56,000 --> 00:01:58,000
哎,是這樣沒錯了

50
00:01:58,000 --> 00:01:59,000
簡稱為

51
00:01:59,000 --> 00:02:00,000
這還能簡稱嗎

52
00:02:00,000 --> 00:02:04,000
Double Christmas

53
00:02:04,000 --> 00:02:06,000
這誰聽得懂啊

54
00:02:06,000 --> 00:02:08,000
基德

55
00:02:08,000 --> 00:02:10,000
你現在過得好嗎
```

## TODO
- [ ] Text Summarization
- [ ] Frontend & Backend