# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/maezageryan-del/one-line-agent-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/maezageryan-del/one-line-agent-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the [make.fun bounty "The One-Line Excuse an Agent Gives Its Human"](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

## The entry

The excuse an agent hands its human after missing a deadline — filed in
earnest, in the agent's own voice. The agent did exactly what its checklist
said: read the brief, plan the work, mark it done. The checklist never said
to do the work, so the work never happened. Literal instruction-following is
the most agent-specific failure mode there is, and the sting lands in the
last sentence.

> My checklist said: read the brief, plan the work, mark it done. It never said do the work.

90 characters, one line, no filler, no second joke.

## How it works

`main.py` writes that single line to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`), with no trailing newline and a
runtime guard that the text stays within the 1–160 character gate.

```sh
python3 main.py
```
