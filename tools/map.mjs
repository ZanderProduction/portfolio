// Builds the data for the "Where I've played" map on the DJZander page.
// Run once when cities change:  (cd /tmp/mapbuild && node /home/claude/ghpages/tools/map.mjs)
// Needs: npm i d3-geo topojson-client world-atlas   (in the folder you run it from)
// Writes tools/map-data.json, which tools/build.py turns into the inline SVG.
import { readFileSync, writeFileSync } from "fs";
import { createRequire } from "module";
import { dirname, join } from "path";
import { fileURLToPath } from "url";
const require = createRequire(join(process.cwd(), "x.js"));
const { geoConicConformal, geoPath } = require("d3-geo");
const { feature } = require("topojson-client");
const world = JSON.parse(readFileSync(require.resolve("world-atlas/countries-50m.json"), "utf8"));
const here = dirname(fileURLToPath(import.meta.url));

// Countries played (ISO numeric codes used by world-atlas)
const PLAYED = { "528": "Netherlands", "056": "Belgium", "276": "Germany", "826": "United Kingdom", "724": "Spain", "100": "Bulgaria" };

// [city, country code, lat, lon, extra]   (LABEL below sets where a name sits when cities are close)
const CITIES = [
  ["Leeuwarden", "528", 53.2012, 5.7999], ["Groningen", "528", 53.2194, 6.5665], ["Amsterdam", "528", 52.3676, 4.9041],
  ["Rotterdam", "528", 51.9244, 4.4777], ["Breda", "528", 51.5719, 4.7683], ["Eindhoven", "528", 51.4416, 5.4697],
  ["Maastricht", "528", 50.8514, 5.6910],
  ["Brussels", "056", 50.8503, 4.3517], ["Sint-Truiden", "056", 50.8167, 5.1864],
  ["Hamburg", "276", 53.5511, 9.9937],
  ["London", "826", 51.5074, -0.1278, "December 2026"],
  ["Madrid", "724", 40.4168, -3.7038], ["Barcelona", "724", 41.3874, 2.1686],
  ["Sofia", "100", 42.6977, 23.3219], ["Plovdiv", "100", 42.1354, 24.7453], ["Ruse", "100", 43.8356, 25.9657],
  ["Varna", "100", 43.2141, 27.9147], ["Sunny Beach", "100", 42.6950, 27.7100], ["Targovishte", "100", 43.2512, 26.5722],
  ["Kozloduy", "100", 43.7783, 23.7206], ["Bansko", "100", 41.8383, 23.4885],
];

const LABEL = { Leeuwarden: "l", Brussels: "l", "Sint-Truiden": "b", Maastricht: "r", Breda: "l", Rotterdam: "l", Groningen: "r", Kozloduy: "l", Varna: "r", "Sunny Beach": "b" };
const W = 1000, H = 760;
const view = { type: "Feature", geometry: { type: "Polygon", coordinates: [[[-10.5, 35], [-10.5, 57.5], [30.5, 57.5], [30.5, 35], [-10.5, 35]]] } };
const proj = geoConicConformal().parallels([40, 56]).rotate([-10, 0]).fitExtent([[10, 10], [W - 10, H - 10]], view).clipExtent([[0, 0], [W, H]]);
const path = geoPath(proj);
const r1 = (s) => s.replace(/(\d+\.\d)\d+/g, "$1");

const countries = feature(world, world.objects.countries).features
  .map((f) => ({ id: f.id, name: f.properties.name, d: path(f), played: !!PLAYED[f.id], f }))
  .filter((c) => {
    if (!c.d) return false;
    const [[a, b], [x, y]] = path.bounds(c.f);
    return x > 0 && y > 0 && a < W && b < H && (x - a) * (y - b) > 4;
  });
const out = {
  W, H,
  countries: countries.map((c) => ({ id: c.id, name: PLAYED[c.id] || c.name, played: c.played, d: c.played ? r1(c.d) : c.d.replace(/(\d+)\.\d+/g, "$1") })),
  cities: CITIES.map(([name, cc, lat, lon, note]) => {
    const [x, y] = proj([lon, lat]);
    return { name, cc, x: +x.toFixed(1), y: +y.toFixed(1), note: note || "", lab: LABEL[name] || "r" };
  }),
  zoom: {},
};
// zoom boxes: Netherlands and Belgium share one (they're close together)
const box = (ids) => {
  let [x0, y0, x1, y1] = [Infinity, Infinity, -Infinity, -Infinity];
  for (const c of countries.filter((c) => ids.includes(c.id))) {
    const [[a, b], [cc, d]] = path.bounds(c.f);
    x0 = Math.min(x0, a); y0 = Math.min(y0, b); x1 = Math.max(x1, cc); y1 = Math.max(y1, d);
  }
  return [x0, y0, x1, y1].map((v) => +v.toFixed(1));
};
out.zoom["528"] = out.zoom["056"] = box(["528", "056"]);
for (const id of ["276", "826", "724", "100"]) out.zoom[id] = box([id]);
writeFileSync(join(here, "map-data.json"), JSON.stringify(out));
console.log("countries", out.countries.length, "bytes", JSON.stringify(out).length, out.zoom);
