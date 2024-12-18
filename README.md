# whisper-wer

This application uses jiwer to calculate word error rate (WER) and other measures between two text files.

## Instructions

This requires jiwer:
```pip install jiwer```

The application will ask for full filepaths of the hypothesis (i.e. whisper-generated) transcript and a reference transcript.

Its output will show normalized versions of hypothesis and reference texts, indicators for word/character differences, and the following measures:
- match error rate (mer)
- word information lost (wil)
- word information preserved (wip)
- word error rate (wer)
