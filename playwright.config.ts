import { defineConfig } from "@playwright/test";

// QA_SLOW=1 multiplies timeouts for software WebGL (SwiftShader) where a scene needs 20-30 s to compile its first frame.
// CHROMIUM_PATH points at any Chromium build when Playwright's own browser cannot be downloaded (CI sandboxes).
const slow = process.env.QA_SLOW ? 4 : 1;
const executablePath = process.env.CHROMIUM_PATH || undefined;
const baseURL = process.env.BASE_URL || "http://localhost:4181"; // BASE_URL points the specs at a deployed site instead of the local server
const origin = new URL(baseURL).origin;
const [viewW, viewH] = (process.env.QA_VIEWPORT || "1280x900").split("x").map(Number); // QA_VIEWPORT=1100x640 shrinks the window of every test: the software-rendered 3D scenes then need less memory
const quality = process.env.QA_QUALITY; // forces the scene quality tier (low | medium | high) through the same localStorage key the site uses
const args = ["--no-sandbox", "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader",
  ...(executablePath ? ["--disable-setuid-sandbox", "--disable-dev-shm-usage", "--ignore-gpu-blocklist", "--single-process", "--no-zygote", "--in-process-gpu"] : [])];

export default defineConfig({
  testDir: "./tests", testMatch: "**/*.spec.ts", timeout: 90000 * slow, expect: { timeout: 15000 * slow }, workers: 1,
  reporter: [["list"], ["json", { outputFile: "qa-results.json" }]],
  use: { baseURL, viewport: { width: viewW, height: viewH }, reducedMotion: "reduce", launchOptions: { executablePath, args },
    ...(quality ? { storageState: { cookies: [], origins: [{ origin, localStorage: [{ name: "woy-quality", value: quality }] }] } } : {}) },
});
