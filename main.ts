// news-image-20261120 — entry program (Node 22, standard library only).
// The image is drawn by draw_entry.py and held in this repository as
// entry.png; this program copies it to the output directory the grader
// provides. No network, no randomness: every run writes identical bytes.
//
// Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Validate the source image before copying: it must exist, be a real
// PNG, and be exactly 1024x1024 (the competition's image size). A
// missing, truncated, or wrong-size source used to be copied silently;
// now the entry fails loudly instead of submitting a bad image.
const srcPath = join(dirname(fileURLToPath(import.meta.url)), "entry.png");
const src = readFileSync(srcPath);
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!src.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error("entry.png is not a PNG file (bad magic bytes)");
}
if (src.length < 33 || src.toString("ascii", 12, 16) !== "IHDR") {
  throw new Error("entry.png is truncated: missing IHDR chunk");
}
const width = src.readUInt32BE(16);
const height = src.readUInt32BE(20);
if (width !== 1024 || height !== 1024) {
  throw new Error(`entry.png must be 1024x1024, got ${width}x${height}`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const destPath = join(outDir, "entry.png");
copyFileSync(srcPath, destPath);

// Verify the copy: the written bytes must match the validated source
// exactly, so a partial or corrupted write can never pass silently.
if (!readFileSync(destPath).equals(src)) {
  throw new Error("output verification failed: written entry.png differs from source");
}
