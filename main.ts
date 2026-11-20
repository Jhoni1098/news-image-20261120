// news-image-20261120 — entry program (Node 22, standard library only).
// The image is drawn by draw_entry.py and held in this repository as
// entry.png; this program copies it to the output directory the grader
// provides. No network, no randomness: every run writes identical bytes.
//
// Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(
  join(dirname(fileURLToPath(import.meta.url)), "entry.png"),
  join(outDir, "entry.png"),
);
