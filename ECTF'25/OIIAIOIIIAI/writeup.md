# Challenge Name - OIIAIOIIIAI

## Description
The cat made a mess of the flag, I have to retrieve the flag or my boss will be mad.

`}`eYcbt4fB{_yD0nUu_05Rp_1TNh_GM13R_

## Solution
1. I tried using the **dcode.fr cipher identifier** tool, but there was no relevant information.
2. Upon further inspection, I noticed that we could start assembling the flag by picking out characters at even indexes.
   - From the start: `e, c, t, f, {`
3. Also, I realized the last character (`}`) is at the first place, which means the second part of the flag needs to be reversed.
4. Now, let’s assemble the two parts:
   - From even indexes: `ectf{y0U_5p1N_M3_`
   - Reversed second part: `R1GhT_R0unD_B4bY}`
5. Finally, combining both parts, we get the flag!

## Flag

`ectf{y0U_5p1N_M3_R1GhT_R0unD_B4bY}`
