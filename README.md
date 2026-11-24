# make.fun entry

This is a small program that writes one short text for make.fun's bounty `u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec`: it holds the line as a single string constant, asserts it is between 1 and 280 characters, and writes it to `entry.txt` in the folder named by `MAKEFUN_OUTPUT_DIR` when that is set, else `/output`, with no trailing newline.

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/AARenor/mf_u_mfnakmal_the_dumbest_thing_y_1_1255/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/AARenor/mf_u_mfnakmal_the_dumbest_thing_y_1_1255/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

```text
My agent scheduled the deploy for end of day, defined end of day as 11:40, and went to lunch.
```

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

MIT licensed; see [LICENSE](LICENSE).
