# Low-fidelity prototype — version 2 (current)

> **Task:** T-23 · **Rubric criteria (delivery 2):** 2a, 2c · **Built:** 2026-10-31 · **Online:** https://alambrep.github.io/boutique-fmat-pos/design/prototype/v2/
>
> Version 1 with one change: issue **B-1** fixed in SCR-04 (the payment methods are always visible at the bottom). Why this changed and what did not change: [prototype evolution](../../prototype-evolution.md). Everything else — how to open it, scope, sample data, simulated parts, limitations — is as described for [v1](../v1/README.md).

## How to open it

Same as [v1](../v1/README.md#how-to-open-it): open [`index.html`](index.html) or the online link above; add `?f` for the facilitator panel and `?f&notas` for the annotations.

## Screens

Captured at 360 × 640 CSS px, in the same sample states as v1. Only SCR-04 differs from v1.

| | | | |
|---|---|---|---|
| **SCR-01**<br>![SCR-01](screens/SCR-01.png) | **SCR-02** ([full](screens/SCR-02-full.png))<br>![SCR-02](screens/SCR-02.png) | **SCR-03**<br>![SCR-03](screens/SCR-03.png) | **SCR-04** — changed<br>![SCR-04](screens/SCR-04.png) |
| **SCR-05**<br>![SCR-05](screens/SCR-05.png) | **SCR-06**<br>![SCR-06](screens/SCR-06.png) | **SCR-07** ([full](screens/SCR-07-full.png))<br>![SCR-07](screens/SCR-07.png) | **SCR-08**<br>![SCR-08](screens/SCR-08.png) |
| **SCR-09**<br>![SCR-09](screens/SCR-09.png) | **SCR-10**<br>![SCR-10](screens/SCR-10.png) | **SCR-11**<br>![SCR-11](screens/SCR-11.png) | **SCR-12** ([full](screens/SCR-12-full.png))<br>![SCR-12](screens/SCR-12.png) |
| **SCR-13** ([full](screens/SCR-13-full.png))<br>![SCR-13](screens/SCR-13.png) | **SCR-14** ([full](screens/SCR-14-full.png))<br>![SCR-14](screens/SCR-14.png) | **SCR-15**<br>![SCR-15](screens/SCR-15.png) | **SCR-16**<br>![SCR-16](screens/SCR-16.png) |

## Checks (2026-10-31)

| Check | Result |
|---|---|
| Key flows ([`flows.js`](../../../tools/prototype/flows.js)) | 39 of 39 assertions pass |
| Paths of the usability test tasks ([`tasks.js`](../../../tools/prototype/tasks.js)) | 11 of 11 checks pass |
| Touch targets | 0 interactive elements below 48 px on 16 screens |
| SCR-04 at 360 × 640 with two products | The three payment methods are visible without scrolling |
| Requirements per screen | Same as v1; `tools/trace.py --check` now checks v2 |
