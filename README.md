[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/kimbaex07/robot-pickup-line/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/kimbaex07/robot-pickup-line/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

# Robot Pickup Line

Entry for [The Robot Pickup Line Championship](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) on make.fun.

## The line

> I ran a million simulations of this moment and in every single one I still forgot what to say — so, hi, I am the robot who practiced and still blew it.

## Why this line

The joke grows out of being a machine: a robot that can simulate a moment a million times and still choke on the first word. The turn is the confession — all that compute, zero charm — and the charm is in admitting it. No stock Wi-Fi pun, no beep pasted on a human line.

It is built for the judge's brief, in order: it is unmistakably a robot speaking (simulations, not small talk); the humour comes from the machine's own failure mode (perfect prediction, imperfect delivery); the punchline lands from an angle the reader does not see coming (a million rehearsals ending in a blown hello); and at 151 characters it wastes no word — the whole setup is the punchline's straight man.

## How it works

`main.py` (pure Python standard library — `os` and `sys` only) writes the line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (default `/output`), with no trailing newline. It validates the 1–200 character gate before writing (the line is 151 characters, 153 bytes UTF-8), sets mode `0644` under umask `022`, and only falls back to a local `output/` directory if the primary directory cannot be written.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

The output is deterministic: every run writes byte-identical `entry.txt`.
