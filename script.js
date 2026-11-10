/* =============================================================
   EASY EDITS - everything you'll want to change is in this block
   ============================================================= */

// Your showreel's YouTube ID (the part after "watch?v="). Leave "" to hide.
const SHOWREEL = "";

// Links to your best Instagram reels, e.g. "https://www.instagram.com/reel/ABC123/"
const REELS = [
  // "https://www.instagram.com/reel/XXXXXXXXXXX/",
];

// Full episodes shown under a project: [video ID, title, small line, "link" if age-restricted]
// Age-restricted videos can't play inside other websites, so "link" opens them on YouTube.
const WITP_EPISODES = [
  ["VDmNOxgUtoM", "Episode 2", "12 min / camera and edit by me"],
  ["ovS9lSbq-fQ", "Episode 3", "18 min / camera and edit by me"],
];
const AYM_EPISODES = [
  ["a1_u9RdP_Gw", "Episode 1", "16 min / opens on YouTube", "link"],
  ["DbPrGk1ccdg", "Episode 2: Spice Challenge", "24 min / full episode"],
];

// YouTube sliders: [video ID, title, small line under the title]
const VLOGS = [
  ["G71JpTXkimw", "Week with Zander #1", "DJing a silent disco"],
  ["rQm6nprSxeU", "Week with Zander #2", "Obstacle run and the trip to Bulgaria"],
  ["kq_HlPN2bjI", "Week with Zander #3", "Training and a gig in Plovdiv"],
  ["K1ABtIw2OIs", "Week with Zander #4", "Orienteering camp and New Year"],
  ["hCSl4K2XNrE", "Week with Zander #5-6", "Gigs, travel and training"],
  ["tbgcMQno6HM", "Live with Dimoff, Mom4eto & Djaany", "Moonlight, 1.5K views"],
  ["vnKZxr3UuWM", "Varna Day at Moonlight", "Vlog"],
];

const SETS = [
  ["ijzeG5jlHdM", "Moombahton & Reggaeton live mix", "42 min outdoor set, 2026"],
  ["I2ZFxHv77R8", "Kingsday Block Party", "EDM and dance set"],
  ["nGDKRFYFYyc", "Hip-hop & Trap mix", "1.6K views"],
  ["Y-Z-09cwZ9U", "Summer Reggaeton mix", "Bad Bunny, Daddy Yankee, Karol G and more"],
  ["xuo8iLtqgMo", "Tech House Mix #1", "1.3K views"],
  ["P_ufeR-G_nU", "Feel the Energy", "21 min deep house mix"],
  ["ZBKbmrMX6M8", "Chalga Party Mix", "Live mix, 1.2K views"],
  ["CG0LvR0S3fU", "Bar0na Mix", "19K views"],
];

const REMIXES = [
  ["hlu_L4Spe_4", "Tishinata Im x Ne Dulja Nishto", "Mashup, 780K views"],
  ["WcvtdQSx8eg","Voices In My Head", "Balkan intro, 26K views"],
  ["9GHv63Va2lk", "Cheburashka", "House remix, 22K views"],
  ["chGSqC4mlJE", "EXAGGERATE", "My original track, official video"],
  ["-w8-WNtGwjA", "Gasolina", "Balkan remix, 3.1K views"],
  ["HtoeEiakGS0", "Mrusni & Tumni", "Zander flip, 2K views"],
  ["6IxPU6t2WVI", "Bizzey x Krisko - Drop Some", "Mashup, 2K views"],
  ["1nzmP8cYKEI", "Florin Salam - Saint Tropez", "DnB remix, 1.6K views"],
  ["0jkp2ecblQA", "Europapa", "Balkan mashup"],
  ["Dm95Soh4CCQ", "Az Sum 6 x Too Bizarre", "Mashup"],
  ["6rkB5VcFzfs", "V:RGO - OPCIQ", "Tech house remix"],
];

// Posters: add more by pasting image links (or "images/your-file.jpg") to this list.
const CDN = "https://cdn.myportfolio.com/d1dbd0b9-d7d7-43d2-ac03-eef2bbe977e5/";
const POSTERS = [
  "images/poster-bnr-zander-artist-card.jpg",
  "images/poster-emanuela-villa-thalia.jpg",
  "images/poster-bnr-de-club-eindhoven.jpg",
  "images/poster-for-the-culture-shooters.jpg",
  "images/poster-disney-channel-party-shooters.jpg",
  "5a436320-5705-4eca-8ae6-68e2a0d5bc51_rw_1200.PNG?h=d1b48917ad11061bb44608df53675f39",
  "b20f2650-419a-4631-ac90-020e3c69ebc0_rw_1200.jpg?h=ec84fada2efca90a53f2c74d84583d2b",
  "d47c9844-e4be-4937-99a9-9a9d16492033_rw_1200.jpg?h=c89463395793e9205e83d6e85ddb5e59",
  "da54b630-6381-4966-b3e2-1cd1224fa892_rw_1200.jpg?h=bec27c1e2b68d26445c23b98411de799",
  "471bec33-e5bd-4061-852b-4814df8b8be9_rw_1200.jpg?h=02f56ada204c8760c4c0db1fdce0ef8c",
  "8ed97530-cfe2-40ee-8bc3-f9ba859f61c0_rw_1200.jpg?h=8dd07f1cd1ebbf5a26e90e2773fdbb70",
  "fb74f639-5727-4184-94a6-c2043e9217d3_rw_1200.jpg?h=56080f1149b1ea2cfe51f0f25a0d3489",
  "1265d837-33a3-41a0-858b-312eb64bde91_rw_1200.jpg?h=0a73a78c36b0a46414fa1c0110c5737d",
  "6858f252-4ce2-425c-9c3a-7d938a79deed_rw_1200.jpg?h=bf35266404d7113a8518620ef55f44e1",
  "c5011e22-0489-4681-9970-aad8984ae0fe_rw_1200.jpg?h=1440ec658fef67cf02a7d172c93c8ccc",
  "6467c657-afd3-44a6-8ddd-3a237b70f85e_rw_1200.jpg?h=71062212a46166da108db1279e12f287",
  "17b04059-46bf-4117-aebd-09ae91d5c1b8_rw_1200.jpg?h=17d2afa7773714a6d9bf0aea632f7d3e",
  "511b2dc4-d587-406e-ad58-fedd232ce4f3_rw_1200.jpg?h=f994e241831abe8796e73925b4caff2e",
  "de6817b9-1144-4867-9397-87c6b26e0bf9_rw_1200.jpg?h=83116b07f46a4f0e9dad9405ccf9adf1",
  "4874bdf0-5a42-451e-a2c9-d0c62dfa947b_rw_1200.jpg?h=706c3937aa995b5c596ab87687780bcb",
  "fb37cc8f-1f09-4eb1-aca5-87a8c8800d16_rw_1200.jpg?h=8d11fd0efb0573726abbb2fc0d9e3cb3",
  "20c51582-e1bf-4b89-865d-642b25401f88_rw_1200.jpg?h=fb9b17056b3377c1d874d5df38c19244",
  "0ca8c447-5115-433a-b386-b68c13e9176b_rw_1200.jpg?h=6bd8aa96707e6658464c119d9bdeb810",
  "cf77c3a0-d514-44aa-80fc-060f1b850272_rw_1200.jpg?h=fcef8bdc364eda059d733fbf58f982d4",
  "c8a4e214-c1ce-4dc9-960c-693dad72a848_rw_1200.jpg?h=e07e75c7024e80286e5a8b4da1ca74a3",
  "e913bd44-13a1-4c4c-9528-9d33f1a5dfdb_rw_1200.jpg?h=07c3b59e499ee1aae3490a07afcf8d25",
  "8e567c32-0e71-424a-9ac0-d2092eed7dd4_rw_1200.jpg?h=881a786b68adbbb9ebbce4d17f8f99fa",
  "61514b92-2a84-4422-9920-64b429b19373_rw_1200.jpg?h=0294bde6c904e3728bea0e217f1e6312",
  "6d88712d-c9cc-42b6-ac62-cd716764a095_rw_1200.jpg?h=5a766b1fce849bce5c89760f85149361",
  "0e39dc28-e3a1-4659-a3a2-92461d343666_rw_600.JPG?h=30eb34c97d79126cff04f81abea3caed",
  "c48ccbe6-e7fb-4988-9bb4-e1baa61c70db_rw_1200.jpg?h=e43aae4a05501c47d6346798988219d7",
  "436b5f0a-147a-46a5-8e7f-cef696c86c5b_rw_1200.PNG?h=8c29b98be0fa180db760c3a688df85d6",
  "724e0157-fe2a-42d3-9c27-d7a689250e24_rw_1200.jpg?h=a7cd06c52b2f92dc0f931cdc6887f05b",
  "22c2e9b6-fe9d-4695-bfbf-41887f545045_rw_1920.jpg?h=f540124254891a2a94f6e13461e9498d",
  "b2969d37-24ff-4aa5-b45b-5a6def5b4666_rw_1920.JPG?h=e775cf5ce84392fcaa9e9bb827067236",
  "65fbe27e-b857-486c-83d6-c5b1a929ed62_rw_1200.PNG?h=a427a1431336962a0f82d1e20946161c",
  "a9c43954-be22-40dd-a6d3-8eb36cf0f13b_rw_1200.PNG?h=1a5c5bcfe090b2b767b33eb7f88741d5",
  "e5d6c93f-a25b-4107-89b6-2260325fbe1b_rw_1200.JPG?h=e4529cc833a9eec3eb1014c5dc44ee94",
];

/* ============================================================= */

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const lists = { VLOGS, SETS, REMIXES };

// Showreel goes into the big video at the top
if (SHOWREEL) {
  const hv = document.getElementById("hero-video");
  hv.dataset.id = SHOWREEL;
  hv.dataset.title = "Showreel";
  document.getElementById("hero-caption").textContent = "Showreel - a minute of my work.";
}

// Episodes under projects
const epLists = { WITP_EPISODES, AYM_EPISODES };
document.querySelectorAll(".episodes").forEach((box) => {
  const list = epLists[box.dataset.list] || [];
  if (!list.length) return;
  box.innerHTML = `<p class="episodes__label">Full episodes</p>` + list.map(([id, title, meta, mode]) => {
    const card = mode === "link"
      ? `<a class="ep-link" href="https://www.youtube.com/watch?v=${esc(id)}" target="_blank" rel="noopener"><div class="yt yt--static" data-id="${esc(id)}" data-label="Watch on YouTube ↗"></div>`
      : `<div><div class="yt" data-id="${esc(id)}" data-title="${esc(title)}"></div>`;
    return card + `<p class="ep__title">${esc(title)}</p><p class="ep__meta">${esc(meta || "")}</p>` + (mode === "link" ? `</a>` : `</div>`);
  }).join("");
});

// Big video at the top: plays muted on loop, "Sound on" restarts it with sound
(() => {
  const box = document.getElementById("hero-video");
  if (!box) return;
  const id = box.dataset.id;
  const iframe = document.createElement("iframe");
  iframe.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&mute=1&loop=1&playlist=${id}&controls=0&modestbranding=1&rel=0&playsinline=1&iv_load_policy=3&cc_load_policy=0&enablejsapi=1&origin=${encodeURIComponent(location.origin)}`;
  iframe.title = box.dataset.title || "Video";
  iframe.allow = "autoplay; encrypted-media; picture-in-picture";
  iframe.setAttribute("tabindex", "-1");
  box.prepend(iframe);
  const cmd = (func, args = []) =>
    iframe.contentWindow && iframe.contentWindow.postMessage(JSON.stringify({ event: "command", func, args }), "*");
  // listen to the player and switch YouTube's auto subtitles off
  iframe.addEventListener("load", () => {
    iframe.contentWindow.postMessage(JSON.stringify({ event: "listening", id: 1, channel: "widget" }), "*");
    [300, 1500, 4000].forEach((t) => setTimeout(() => cmd("unloadModule", ["captions"]), t));
  });
  window.addEventListener("message", (e) => {
    if (!String(e.origin).includes("youtube")) return;
    try {
      const d = JSON.parse(e.data);
      if (d.event === "onReady" || (d.info && d.info.playerState === 1)) cmd("unloadModule", ["captions"]);
    } catch (_) {}
  });
  const btn = box.querySelector(".hero-loop__sound");
  let soundOn = false;
  btn.addEventListener("click", () => {
    soundOn = !soundOn;
    if (soundOn) { cmd("seekTo", [0, true]); cmd("unMute"); cmd("setVolume", [100]); cmd("playVideo"); }
    else { cmd("mute"); }
    btn.textContent = soundOn ? "Sound off" : "Sound on";
    btn.setAttribute("aria-pressed", String(soundOn));
    box.classList.toggle("is-sound", soundOn);
  });
})();

// Phone menu
(() => {
  const btn = document.querySelector(".nav__toggle");
  const menu = document.getElementById("mobile-menu");
  if (!btn || !menu) return;
  const label = btn.querySelector(".nav__toggle-text");
  const set = (open) => {
    document.body.classList.toggle("menu-open", open);
    btn.setAttribute("aria-expanded", String(open));
    menu.setAttribute("aria-hidden", String(!open));
    label.textContent = open ? "Close" : "Menu";
  };
  btn.addEventListener("click", () => set(!document.body.classList.contains("menu-open")));
  menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => set(false)));
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") set(false); });
  window.addEventListener("resize", () => { if (window.innerWidth > 760) set(false); });
})();

// Address bar follows the section you're in (#work, #music, #about, #contact)
(() => {
  const ids = ["work", "music", "about", "contact"];
  const sections = ids.map((id) => document.getElementById(id)).filter(Boolean);
  const navLinks = [...document.querySelectorAll('.nav__links a, .mmenu__links a')];
  let current = null, ticking = false;
  const update = () => {
    ticking = false;
    const line = window.innerHeight * 0.35;
    let active = null;
    for (const s of sections) if (s.getBoundingClientRect().top <= line) active = s.id;
    if (active === current) return;
    current = active;
    const url = active ? "#" + active : location.pathname + location.search;
    history.replaceState(null, "", url);
    navLinks.forEach((a) => a.classList.toggle("is-active", a.getAttribute("href") === "#" + active));
  };
  window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });

  // On refresh with #section: land on it again once images and sliders have loaded
  if (location.hash && ids.includes(location.hash.slice(1))) {
    const target = document.getElementById(location.hash.slice(1));
    let userScrolled = false;
    const mark = () => { userScrolled = true; };
    ["wheel", "touchmove", "keydown"].forEach((e) => window.addEventListener(e, mark, { once: true, passive: true }));
    const jump = () => { if (!userScrolled) target.scrollIntoView({ behavior: "instant", block: "start" }); };
    requestAnimationFrame(jump);
    window.addEventListener("load", () => setTimeout(jump, 50));
  }
  update();
})();

// Menu clicks: scroll to the section, then correct if anything above it changed size meanwhile
(() => {
  const navH = () => (document.querySelector(".nav")?.offsetHeight || 64);
  const topOf = (el) => el.getBoundingClientRect().top + window.scrollY - navH();
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    const id = a.getAttribute("href").slice(1);
    const el = id && id !== "top" ? document.getElementById(id) : null;
    if (!el) return;
    a.addEventListener("click", (e) => {
      e.preventDefault();
      const go = () => {
        window.scrollTo({ top: topOf(el), behavior: "smooth" });
        const settle = () => {
          const off = el.getBoundingClientRect().top - navH();
          if (Math.abs(off) > 3) window.scrollTo({ top: topOf(el), behavior: "smooth" });
        };
        if ("onscrollend" in window) window.addEventListener("scrollend", settle, { once: true });
        setTimeout(settle, 1100);
      };
      // wait one frame so the phone menu has released the page before scrolling
      requestAnimationFrame(() => requestAnimationFrame(go));
    });
  });
})();

// Build sliders
document.querySelectorAll(".slider").forEach((slider) => {
  const name = slider.dataset.list;
  let slides;
  if (name === "POSTERS") {
    slides = POSTERS.map((p) => {
      const src = /^https?:|^images\//.test(p) ? p : CDN + p;
      return `<div class="slide"><img loading="lazy" src="${esc(src)}" alt="DJZander show poster"></div>`;
    });
  } else {
    slides = (lists[name] || []).map(([id, title, meta]) =>
      `<div class="slide"><div class="yt" data-id="${esc(id)}" data-title="${esc(title)}"></div>` +
      `<p class="slide__title">${esc(title)}</p><p class="slide__meta">${esc(meta || "")}</p></div>`
    );
  }
  slider.innerHTML =
    `<div class="slider__track">${slides.join("")}</div>` +
    `<div class="slider__nav"><button type="button" data-dir="-1" aria-label="Previous">←</button>` +
    `<button type="button" data-dir="1" aria-label="Next">→</button>` +
    `<span class="slider__count">${slides.length} ${name === "POSTERS" ? "posters" : "videos"}</span></div>`;

  const track = slider.querySelector(".slider__track");
  slider.querySelectorAll("[data-dir]").forEach((b) =>
    b.addEventListener("click", () => track.scrollBy({ left: Number(b.dataset.dir) * track.clientWidth * 0.9 }))
  );

  // drag to scroll on desktop
  let down = false, startX = 0, startLeft = 0, moved = false;
  track.addEventListener("pointerdown", (e) => {
    if (e.pointerType !== "mouse") return;
    down = true; moved = false; startX = e.clientX; startLeft = track.scrollLeft;
    track.style.scrollSnapType = "none";
  });
  window.addEventListener("pointermove", (e) => {
    if (!down) return;
    const dx = e.clientX - startX;
    if (Math.abs(dx) > 4) moved = true;
    track.scrollLeft = startLeft - dx;
  });
  window.addEventListener("pointerup", () => {
    if (!down) return;
    down = false; track.style.scrollSnapType = "";
  });
  track.addEventListener("click", (e) => { if (moved) { e.stopPropagation(); e.preventDefault(); moved = false; } }, true);
  track.addEventListener("dragstart", (e) => e.preventDefault());
});

// YouTube lite embeds: thumbnail first, real player on click
document.querySelectorAll(".yt").forEach((el) => {
  const id = el.dataset.id;
  const title = el.dataset.title || "video";
  el.style.backgroundImage = `url(https://i.ytimg.com/vi/${id}/hqdefault.jpg)`;
  if (el.classList.contains("yt--static")) {
    el.innerHTML = `<span class="yt__play">${el.dataset.label || "Watch"}</span>`;
    return;
  }
  el.setAttribute("role", "button");
  el.setAttribute("tabindex", "0");
  el.setAttribute("aria-label", `Play ${title}`);
  el.innerHTML = `<span class="yt__play">Play</span>`;
  const play = () => {
    if (el.querySelector("iframe")) return;
    const f = document.createElement("iframe");
    f.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;
    f.title = title;
    f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
    f.allowFullscreen = true;
    el.appendChild(f);
  };
  el.addEventListener("click", play);
  el.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); play(); } });
});

// Instagram reels
if (REELS.length) {
  document.getElementById("reels").innerHTML = REELS.map((u) =>
    `<blockquote class="instagram-media" data-instgrm-permalink="${esc(u)}" data-instgrm-version="14"></blockquote>`
  ).join("");
  const s = document.createElement("script");
  s.async = true;
  s.src = "https://www.instagram.com/embed.js";
  document.body.appendChild(s);
}

// CV links stay hidden until cv.pdf is in the folder
fetch("cv.pdf", { method: "HEAD" })
  .then((r) => { if (!r.ok || (r.headers.get("content-type") || "").includes("text/html")) throw 0; })
  .catch(() => document.querySelectorAll(".cv-link").forEach((n) => (n.style.display = "none")));

// Count-up for the Instagram numbers
const counters = document.querySelectorAll("[data-count]");
const runCount = (el) => {
  const end = Number(el.dataset.count), suffix = el.dataset.suffix || "", t0 = performance.now(), dur = 1400;
  const step = (t) => {
    const p = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - p, 3)));
    el.textContent = v.toLocaleString("en-US") + suffix;
    if (p < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
};
if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const co = new IntersectionObserver((entries) => entries.forEach((en) => {
    if (en.isIntersecting) { runCount(en.target); co.unobserve(en.target); }
  }), { threshold: 0.6 });
  counters.forEach((c) => co.observe(c));
}

// Fade in on scroll
const fadeEls = document.querySelectorAll(".project, .row, .insta, .partners, .highlights, .photos, .about, .cvgrid, .services");
if ("IntersectionObserver" in window) {
  fadeEls.forEach((el) => el.classList.add("fade"));
  const io = new IntersectionObserver((entries) => entries.forEach((en) => {
    if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
  }), { threshold: 0.08 });
  fadeEls.forEach((el) => io.observe(el));
}

document.getElementById("year").textContent = new Date().getFullYear();
