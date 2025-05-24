# streamlit-test

## pages/exp.py
Present group -> section -> pair

From google sheets, search from the top rows marked without 'done'
use the subsequent 3 groups.

Create a list of pairs
```bash
pairs = []
loop for group id:
    # Section A
    sub_pairs = []
    loop for baselines: [gt, emage, lsm, mamba, cfm_inpainting]:
        sub_pairs.append([
            group_id,
            section A,
            video_url,
            baseline_video_url,
            question for section A
        ])
    shuffle(sub_pairs)
    pairs.extend(sub_pairs)

    # Section B
    sub_pairs = []
    loop for models: [gt, cfm, emage, lsm, mamba]:
        sub_pairs.append([
            group_id,
            section B,
            video_url,
            mismatch_video_url,
            question for section B
        ])
    shuffle(sub_pairs)
    pairs.extend(sub_pairs)
```

Now, pairs should be a list of element of pairs
that can be used to create the comparison test

Create comparison test interface
two video widgets (randomize order)
form with question
submit, on_click=update_pair + process and append result to session_state

the result are values in [0, 1, 2],
0 means the target won,
1 means tied,
2 means the target lost.
where the target is the video to compare.
E.g., in section A, video_url is cfm video, which is the target,
in section B, video_url is the matched video, which is the target.

The saved result will be a list of values,
it is better to also contain information for logging to sheet,
[group_id, section, baseline_name, result] for section A
[group_id, section, model_name, result] for section B

As to write to sheet, the columns:
group_id, status, A-gt, A-emage, A-lsm, A-mamba, A-cfm_inpainting, B-gt, B-cfm, B-emage, B-lsm, B-mamba
so the information in the saved result can be used to write into the sheet.

After all pairs are evaluated, go to the outro