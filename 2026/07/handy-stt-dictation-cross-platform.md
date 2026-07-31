<!--
.. title: Handy - Best cross platform Dictation app (Free)
.. slug: handy-stt-dictation-cross-platform
.. date: 2026-07-29 05:19:39 UTC+05:30
.. tags: cross-platform, dictation, speech-to-text
.. category: 
.. link: 
.. description: Best open
.. type: text
-->

### Context 

Around 2016, I explored various speech-to-text (STT) tools to reduce strain on writs due to RSI(Repetetive Strain Injury) and gave up on them due to their limitations.

With AI advancements, these tools have come a long way.

### Open Source STT Tools

[Handy](https://github.com/cjpais/Handy)

[TypeWhisper](https://github.com/TypeWhisper)

[FluidVoice](https://github.com/altic-dev/FluidVoice)

[HyperWhisper](https://github.com/ray-amjad/hyperwhisper-app)

[VoiceInk](https://github.com/Beingpax/VoiceInk)

There are couple of paid tools but they didn't work well in noisy environment.

After trying out all these tools with local models like Parakeet, Voxstral, and Cohere Transcribe, I found that Handy + Cohere Transcribe is the best combination for my needs.

![mac-tts-models.png](/images/mac-tts-models.png)

Handy has post processing as an experimental feature where we can send output of STT to other LLM models and get a fine grained output.

![mac-tts-post-process.png](/images/mac-tts-post-process.png)

For example, when I dictate "git push dash dash force", the output is "git push --force" after post processing.

### Conclusion


I let AI to write [handy_stats.py](https://github.com/ChillarAnand/init/blob/main/handy_stats.py) script to track my dictation stats. I am dictating more than 10K characters per day which reduces strain on my fingers/writs.