# Thesis presentation, version 1

Built on the university template (MTCS-MRMC5_Thesis-Presentation_Template.pptx). Slide 1 is the template's title slide, unchanged; its old speaker notes (from another thesis) were replaced. All numbers come from Thesis_Refocused_Verified_v18.md (see handouts/Number_Source_Map.csv).

## Files
- Thesis_Presentation_v1.pptx: 21 main slides, a backup divider and 10 backup slides (B1–B10). The speaker script is in the speaker notes. All slides use a fade transition.
- handouts/Speaker_Script.docx: full script with the timing plan and backup-slide guide.
- handouts/QA_Preparation.docx: 40 likely questions, each with an answer, the thesis evidence and the slide to show.
- handouts/Cheat_Sheet.docx and handouts/Cheat_Sheet.pdf: one page of key numbers to keep at the lectern.
- handouts/FAQ.docx: 20 plain-language questions for a general audience.
- handouts/Glossary.docx: 35 terms.
- handouts/Audience_Handout.pdf: one-page summary to hand out.
- handouts/Number_Source_Map.csv: every number used on the slides, traced to the thesis.
- handouts/Rehearsal_Timing_Sheet.html: opens in a browser; a stopwatch with per-slide targets that saves your runs.
- handouts/Day_of_Checklist.html: opens in a browser; a checklist that remembers what you have ticked.
- visuals/: the new diagrams and charts. The Python code that draws them is make_visuals.py and make_b5_fig9_corrected.py.
- build_deck.py, content.py, docs_content.py, gen_docs.py, render_preview.py: the scripts that rebuild everything.

## Notes
- Timing: the script is 2,225 words. Planned time is 19 min 30 s including pauses and the vote. Skipping slides 12, 14 and 15 saves 1 min 50 s.
- The previews were drawn without an office suite, so the slides should be checked once in PowerPoint (fonts and line breaks).
- Export a PDF copy from PowerPoint (File > Save As > PDF) as a fallback for the day.
- The legend of Figure 9 in the thesis (v18) says "V1 — 335-window corpus". The thesis text (ch.4.5) says the earlier model was trained on 497 windows. Backup slide B5 uses a corrected copy of the figure. The thesis figure itself should be corrected too.
