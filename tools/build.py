"""Builds every page of zanderproduction.nl from one template, so the top bar,
phone menu, contact block and footer are the same everywhere.

Run from the repo folder:  python3 tools/build.py
Then commit the generated index.html files.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = "40"  # bump to make browsers fetch fresh css/js

CDN = "https://cdn.myportfolio.com/d1dbd0b9-d7d7-43d2-ac03-eef2bbe977e5/"
PHOTO_ME = CDN + "96b2e4b1-38e3-4fbc-bf51-d58f5eb0c1c4_rw_1920.jpg?h=ecc4ce1cb80b5c6a9a4aa10e220d145e"
PHOTO_CLUB = CDN + "96c60924-a7f4-4c87-a3f5-81a33a35f685_rw_1920.png?h=4b7cf174c878a4682a0b9cfdd7be8e19"
EMAIL = "alex.ivanov2002@gmail.com"


def yt_thumb(i):
    return f"https://i.ytimg.com/vi/{i}/hqdefault.jpg"


# ---------------------------------------------------------------- shared parts

def head(p, title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="{PHOTO_ME}">
<meta name="theme-color" content="#0f1f1a">
<link rel="icon" type="image/png" href="{p}images/favicon.png?v={V}">
<link rel="icon" href="{p}favicon.ico?v={V}" sizes="any">
<link rel="apple-touch-icon" href="{p}images/apple-touch-icon.png?v={V}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,400..900;1,62..125,400..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css?v={V}">
</head>
"""


def nav(p, page):
    home = page == "home"
    links = [
        ("Home", "#top" if home else p, "home"),
        ("Work", "#work" if home else p + "#work", "work"),
        ("Zander Production", p + "dj/", "dj"),
        ("About", "#about" if home else p + "#about", "about"),
        ("Contact", "#contact", "contact"),
    ]
    def cls(key):
        # on the home page the scroll-spy sets the highlight; elsewhere it's fixed per page
        if home:
            return ' class="is-active"' if key == "home" else ""
        return ' class="is-active"' if key == page else ""
    top = "\n    ".join(f'<a href="{h}"{cls(k)}>{t}</a>' for t, h, k in links)
    mob = "\n    ".join(
        f'<a href="{h}"{cls(k)}><span>{i:02d}</span>{t.replace("Zander Production", "Zander<br>Production")}</a>'
        for i, (t, h, k) in enumerate(links))
    return f"""<body data-page="{page}">

<header class="nav" id="top">
  <a href="{'#top' if home else p}" class="nav__name">Alexandar Ivanov</a>
  <nav class="nav__links" aria-label="Main">
    {top}
  </nav>
  <a class="nav__cv" href="{p}cv.pdf" target="_blank" rel="noopener">CV ↓</a>
  <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="mobile-menu">
    <span class="nav__toggle-lines" aria-hidden="true"><i></i><i></i></span>
    <span class="nav__toggle-text">Menu</span>
  </button>
</header>

<!-- Phone menu -->
<div class="mmenu" id="mobile-menu" aria-hidden="true">
  <nav class="mmenu__links" aria-label="Menu">
    {mob}
  </nav>
  <div class="mmenu__foot">
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <div class="mmenu__social">
      <a href="https://www.instagram.com/djzanderr/" target="_blank" rel="noopener">Instagram ↗</a>
      <a href="https://www.linkedin.com/in/alexandar-ivanov-79539a228/" target="_blank" rel="noopener">LinkedIn ↗</a>
      <a href="https://www.youtube.com/@DDJZANDER" target="_blank" rel="noopener">YouTube ↗</a>
    </div>
    <p class="mmenu__status"><span class="dot-live" aria-hidden="true"></span>Open to internships from Feb 2027</p>
  </div>
</div>
"""


def contact(p, title="Let's work<br>together",
            lead="Email is the fastest way to reach me. I can travel anywhere in the Netherlands and do an online call any time."):
    return f"""
<!-- ================= CONTACT ================= -->
<section class="contact" id="contact">
  <div class="section">
    <h2 class="contact__title">{title}</h2>
    <div class="contact__grid contact__grid--single">
      <div>
        <p class="contact__lead">{lead}</p>
        <dl class="contact__list">
          <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          <div><dt>Phone</dt><dd><a href="tel:+31635636476">+31 6 3563 6476</a></dd></div>
          <div><dt>LinkedIn</dt><dd><a href="https://www.linkedin.com/in/alexandar-ivanov-79539a228/" target="_blank" rel="noopener">Alexandar Ivanov ↗</a></dd></div>
          <div><dt>Instagram</dt><dd><a href="https://www.instagram.com/djzanderr/" target="_blank" rel="noopener">@djzanderr ↗</a></dd></div>
          <div><dt>YouTube</dt><dd><a href="https://www.youtube.com/@DDJZANDER" target="_blank" rel="noopener">DJZander ↗</a></dd></div>
          <div class="cv-link"><dt>CV</dt><dd><a href="{p}cv.pdf" target="_blank" rel="noopener">Download PDF ↓</a></dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>
"""


def foot(p):
    return f"""
</main>

<footer class="footer">
  <span>© <span id="year">2026</span> Alexandar Ivanov / Zander Production</span>
  <a href="{p}dj/">Zander Production</a>
</footer>

<a href="#top" class="totop" aria-label="Back to the top"><span aria-hidden="true">↑</span></a>

<script src="{p}script.js?v={V}"></script>
</body>
</html>
"""


def logos(p):
    return f"""
  <div class="partners">
    <p class="label">Worked with</p>
    <ul class="logos">
      <li><img src="{p}images/logos/itvx.png" alt="ITVX" title="ITVX" style="height:30px"></li>
      <li><img src="{p}images/logos/villa-thalia.png" alt="Villa Thalia Rotterdam" title="Villa Thalia Rotterdam" style="height:52px"></li>
      <li><img src="{p}images/logos/effenaar.svg" alt="Effenaar" title="Effenaar" style="height:24px"></li>
      <li><img src="{p}images/logos/nno.png" alt="Noord Nederlands Orkest" title="Noord Nederlands Orkest" style="height:54px"></li>
      <li><img src="{p}images/logos/kiteactive.png" alt="KiteActive" title="KiteActive" style="height:30px"></li>
      <li class="logo-lockup" title="MATTERS"><img src="{p}images/logos/matters.svg" alt="" style="height:40px"><span>Matters</span></li>
      <li><img src="{p}images/logos/nhl-stenden.png" alt="NHL Stenden" title="NHL Stenden" style="height:58px"></li>
    </ul>
  </div>"""


# ---------------------------------------------------------------- projects

PROJECTS = [
    dict(slug="what-is-this-place", title="What Is This Place?", video="ZKMlw-llDe8",
         thumb=yt_thumb("ZKMlw-llDe8"),
         tag="Reality show concept / 3 episodes / MATTERS",
         line="Four blindfolded people get driven to a place they don't know and have to work out where they are.",
         role="Main camera on all 3 episodes, editor of 2 and 3, trailer"),
    dict(slug="are-you-mental", title="Are You Mental?", video="rNbgV_s9UQQ",
         thumb=yt_thumb("rNbgV_s9UQQ"),
         tag="Challenge series / 2 episodes + trailer",
         line="Two guys, a list of challenges, no polish on purpose. The tone of the show was made in the edit.",
         role="Main camera and editor on both episodes, trailer"),
    dict(slug="social-content", title="@djzanderr", thumb=PHOTO_CLUB,
         tag="Social content / my own channel",
         line="1,003,763 views between 31 May and 7 July, with no team: film at the show, edit that night, post the next day.",
         role="Filming, editing and posting"),
    dict(slug=None, title="The Mix Up!", video="7jMX52GM8R4", thumb=yt_thumb("7jMX52GM8R4"),
         tag="Short film / 24-hour challenge",
         line="One rule: start to finish in a day. Planned, shot and edited before the deadline.",
         role="Planning, camera and edit, solo",
         url="https://www.youtube.com/watch?v=7jMX52GM8R4"),
]
CASES = [x for x in PROJECTS if x["slug"]]


def card(p, x):
    if x["slug"]:
        href, more, ext = f'{p}work/{x["slug"]}/', "See the project →", ""
    else:
        href, more, ext = x["url"], "Watch on YouTube ↗", ' target="_blank" rel="noopener"'
    return f"""    <a class="card" href="{href}"{ext}>
      <div class="card__img"><img loading="lazy" src="{x['thumb']}" alt=""></div>
      <p class="tag">{x['tag']}</p>
      <h3>{x['title']}</h3>
      <p class="card__line">{x['line']}</p>
      <p class="card__role">{x['role']}</p>
      <span class="card__more">{more}</span>
    </a>"""


def next_strip(p, current):
    i = [c["slug"] for c in CASES].index(current)
    n = CASES[(i + 1) % len(CASES)]
    return f"""
<div class="band invert">
  <a class="strip" href="{p}work/{n['slug']}/">
    <span class="label">Next project</span>
    <span class="strip__title">{n['title']} <i aria-hidden="true">→</i></span>
  </a>
</div>
"""


def case_head(p, x, intro):
    return f"""
<main>
<div class="band invert">
<section class="phead">
  <a class="phead__back" href="{p}#work">← All work</a>
  <p class="tag">{x['tag']}</p>
  <h1 class="phead__title">{x['title']}</h1>
  <p class="phead__intro">{intro}</p>
</section>
</div>
"""


# ---------------------------------------------------------------- pages

def page_home():
    p = ""
    cards = "\n".join(card(p, x) for x in PROJECTS)
    return head(p, "Alexandar Ivanov - Video Producer & Editor",
                "Alexandar Ivanov - video producer and editor. Series, short film and social content. Looking for a media production internship from February 2027.") + nav(p, "home") + f"""
<main>

<!-- ================= HERO ================= -->
<div class="band invert">
<section class="hero">
  <div class="hero__top">
    <h1 class="hero__title">Video producer<br>&amp; editor</h1>
  </div>

  <!-- The big video. Set SHOWREEL in script.js and your showreel replaces it. -->
  <div class="hero__video">
    <div class="hero-loop" id="hero-video" data-id="ZKMlw-llDe8" data-title="What Is This Place? - series trailer">
      <button class="hero-loop__sound" type="button" aria-pressed="false">Sound on</button>
    </div>
    <p class="hero__caption" id="hero-caption">Now playing: What Is This Place? - series trailer. Camera, editing and trailer cut by me.</p>
  </div>

  <div class="hero__bottom">
    <p class="hero__intro">I make <b>series, short film and social content</b>. Fourth-year Creative Business student at NHL Stenden, looking for a <b>media production internship from February 2027</b>.</p>
    <dl class="hero__facts">
      <div><dt>Based in</dt><dd>The Netherlands</dd></div>
      <div><dt>Available</dt><dd>From Feb 2027</dd></div>
      <div><dt>Shoot on</dt><dd>Canon 90D</dd></div>
      <div><dt>Edit in</dt><dd>DaVinci, Premiere</dd></div>
    </dl>
  </div>
</section>
</div>

<!-- ================= WORK ================= -->
<section class="section" id="work">
  <div class="section__head">
    <h2 class="h-xl">Selected work</h2>
  </div>
  <div class="cards">
{cards}
  </div>
{logos(p)}
</section>

<!-- ================= DJ LINE ================= -->
<div class="band invert">
  <a class="strip" href="dj/">
    <span class="label">Zander Production</span>
    <span class="strip__title">I also run my own DJ and MC business <i aria-hidden="true">→</i></span>
  </a>
</div>

<!-- ================= ABOUT ================= -->
<section class="section" id="about">
  <div class="about">
    <figure class="about__photo">
      <img width="1920" height="1023" loading="lazy" src="{PHOTO_ME}" alt="Alexandar Ivanov">
    </figure>
    <div class="about__text">
      <h2 class="h-xl">About me</h2>
      <p>I grew up in Bulgaria, went to the Sofia High School of Mathematics and moved to Leeuwarden in 2022 to study Creative Business at NHL Stenden. Across three years of concept projects I've worked on everything from campaign plans to full productions, so I'm comfortable taking an idea through planning and the shoot to a finished edit.</p>
      <p>From 2023 to 2025 I co-founded and led the PR team of the <b>Bulgarian Society Leeuwarden</b>. I also did a minor in <b>Intercultural and International Communication</b> and an exchange semester in <b>Málaga</b>, so working with people from everywhere is normal for me.</p>
      <p class="links"><a href="cv.pdf" target="_blank" rel="noopener">Download my CV ↓</a></p>
    </div>
  </div>
</section>
""" + contact(p) + foot(p)


def page_witp():
    p = "../../"
    x = CASES[0]
    return head(p, "What Is This Place? - Alexandar Ivanov",
                "Reality show concept for MATTERS. Main camera on all 3 episodes, editor of episodes 2 and 3, trailer.") + nav(p, "work") + case_head(
        p, x, "Four blindfolded people get driven to a place they don't know. A host gives them clues until they figure out where they are. We developed the format as a team and shot three episodes to pitch it.") + f"""
<section class="section section--case">
  <div class="yt yt--big" data-id="{x['video']}" data-title="What Is This Place? - trailer"></div>
  <p class="case__caption">The trailer, cut by me.</p>

  <div class="case">
    <div>
      <p class="label">Credits</p>
      <dl class="credits">
        <div><dt>Concept</dt><dd>with the team</dd></div>
        <div><dt>Main camera</dt><dd>all 3 episodes</dd></div>
        <div><dt>Editor</dt><dd>episodes 2 &amp; 3</dd></div>
        <div><dt>Trailer</dt><dd>cut by me</dd></div>
      </dl>
    </div>
    <div>
      <p class="label">The project</p>
      <dl class="credits">
        <div><dt>Format</dt><dd>reality show concept</dd></div>
        <div><dt>Episodes</dt><dd>3, shot to pitch</dd></div>
        <div><dt>With</dt><dd>MATTERS</dd></div>
      </dl>
    </div>
  </div>

  <div class="episodes" data-list="WITP_EPISODES"></div>
</section>
""" + next_strip(p, x["slug"]) + contact(p) + foot(p)


def page_aym():
    p = "../../"
    x = CASES[1]
    return head(p, "Are You Mental? - Alexandar Ivanov",
                "Challenge series. Main camera and editor on both episodes, trailer.") + nav(p, "work") + case_head(
        p, x, "Two guys, a list of challenges, no polish on purpose. The tone of the show was made in the edit, from a big pile of raw footage to something that feels loose but keeps moving.") + f"""
<section class="section section--case">
  <div class="yt yt--big" data-id="{x['video']}" data-title="Are You Mental? - trailer"></div>
  <p class="case__caption">The trailer, cut by me.</p>

  <div class="case">
    <div>
      <p class="label">Credits</p>
      <dl class="credits">
        <div><dt>Writing</dt><dd>with the team</dd></div>
        <div><dt>Main camera</dt><dd>both episodes</dd></div>
        <div><dt>Editor</dt><dd>both episodes</dd></div>
        <div><dt>Trailer</dt><dd>cut by me</dd></div>
      </dl>
    </div>
    <div>
      <p class="label">The project</p>
      <dl class="credits">
        <div><dt>Format</dt><dd>challenge series</dd></div>
        <div><dt>Episodes</dt><dd>2 + trailer</dd></div>
        <div><dt>Style</dt><dd>raw, made in the edit</dd></div>
      </dl>
    </div>
  </div>

  <div class="episodes" data-list="AYM_EPISODES"></div>
</section>
""" + next_strip(p, x["slug"]) + contact(p) + foot(p)


def page_social():
    p = "../../"
    x = CASES[2]
    return head(p, "@djzanderr social content - Alexandar Ivanov",
                "1,003,763 views between 31 May and 7 July on my own Instagram, filmed and edited by me.") + nav(p, "work") + case_head(
        p, x, "As a DJ I needed content and had no team, so I built my own routine: film at the show, edit the same night, post the next day. Short videos built around the moment the crowd reacts.") + f"""
<section class="section section--case">
  <div class="insta insta--case">
    <div class="bubbles">
      <div class="bubble bubble--hot"><b data-count="1003763">1,003,763</b><span>views between 31 May and 7 July</span></div>
      <div class="bubble"><b data-count="602596">602,596</b><span>accounts reached</span></div>
      <div class="bubble"><b data-count="92" data-suffix="%">92%</b><span>of views from people who didn't follow me yet</span></div>
      <div class="bubble"><b data-count="4293">4,293</b><span>new followers in 30 days, almost all from reels</span></div>
    </div>
    <div class="insta__text">
      <p class="label">The insights</p>
      <p>Screenshots straight from Instagram. Almost all of the reach came from people who didn't follow me yet, which means the reels were getting pushed to new audiences on their own.</p>
      <p class="links"><a href="https://www.instagram.com/djzanderr/" target="_blank" rel="noopener">Watch the reels on Instagram ↗</a></p>
    </div>
    <div class="insta__shots">
      <img width="1179" height="2556" loading="lazy" src="{CDN}2014eb0c-6765-4a27-87a1-fd05a0edc585_rw_1200.PNG?h=2306495005db6a0f2586b1e92e5cd2e3" alt="Instagram insights: 1,003,763 views">
      <img width="1179" height="2556" loading="lazy" src="{CDN}0a34cb01-e3d6-468a-976a-e2b182264d6f_rw_1200.PNG?h=fad3f78056be6dda5270d97dbaef4bfd" alt="Instagram insights: 4,293 new followers in 30 days">
    </div>
    <div id="reels" class="reels"></div>
  </div>
</section>

<div class="band invert">
  <section class="section section--tight">
    <div class="row row--first">
      <div class="row__head">
        <h3>Week with Zander</h3>
        <p>My vlog series about gigs, travel and training. Nothing is scripted, so every episode gets found in the edit.</p>
      </div>
      <div class="slider" data-list="VLOGS"></div>
    </div>
  </section>
</div>
""" + next_strip(p, x["slug"]).replace('<div class="band invert">', '<div class="band">', 1) + contact(p) + foot(p)


def page_dj():
    p = "../"
    return head(p, "Zander Production - DJ & MC",
                "DJ, MC and event content by Zander Production. Clubs, concerts, festivals and private events in the Netherlands and abroad.") + nav(p, "dj") + f"""
<main>
<div class="band invert">
<section class="phead phead--dj">
  <p class="label label--accent">Zander Production</p>
  <h1 class="phead__title">DJ, MC and the guy filming it</h1>
  <div class="phead__cols">
    <p>I started playing clubs and events in 2020 and it turned into a real job, so I registered it with the <a href="https://www.kvk.nl/bestellen/#/99829398000064874893?origin=search" target="_blank" rel="noopener">KVK</a>. I do all of it: bookings and client contact, the rider, the set, playing and MC-ing, and then filming and editing the recap and promo content.</p>
    <p>Playing for a crowd every weekend teaches you to read a room and change plans on the spot. Remixes, mashups and my own tracks are past <b>500,000 streams on Spotify</b>, <b>100,000 listens a year on SoundCloud</b> and <b>1.5 million views on YouTube</b>.</p>
  </div>
  <p class="links"><a href="#contact">Book a show →</a></p>
</section>
</div>

<section class="section">
  <ul class="highlights">
    <li><span>Concerts</span><p>DJ at concerts with big artists like <b>Emanuela, BNR, Andrea, Bilyanish, Mom4eto</b> and more</p></li>
    <li><span>Sound</span><p>Audio engineering and soundchecks for big artists</p></li>
    <li><span>Shows</span><p>Clubs, festivals and private events all over <b>the Netherlands, Belgium, Spain, Germany and Bulgaria</b></p></li>
  </ul>

  <div class="photos">
    <img width="1898" height="1866" class="photos__a" loading="lazy" src="{PHOTO_CLUB}" alt="DJZander playing a full club">
    <img width="799" height="800" loading="lazy" src="{CDN}5866923a-11a0-4d61-abc7-222ec103b29b_rw_1200.jpeg?h=060566d1b0cd63c4c897c6f0d2448c52" alt="DJZander behind the decks">
    <img width="1333" height="2000" loading="lazy" src="{CDN}4475cec4-844a-49d6-9e04-3eae8bce22c1_rw_1920.png?h=71246d4ed41777e5b41be6e4ed71b43b" alt="DJZander mixing">
    <img width="3840" height="2560" class="photos__d" loading="lazy" src="{CDN}657403d0-4243-46fe-b70a-8abb69768e06_rw_3840.jpg?h=efc9db612df5a4147626837a48fab024" alt="DJZander at a show">
  </div>

  <div class="row">
    <div class="row__head row__head--inline">
      <h3>The posters</h3>
      <p>Some of the nights I've played.</p>
    </div>
    <div class="slider slider--posters" data-list="POSTERS"></div>
  </div>
</section>

<div class="band invert">
<section class="section section--tight">
  <div class="row row--first">
    <div class="row__head row__head--inline">
      <h3>Spotify Wrapped</h3>
      <p>My remixes and mashups, from the artist side.</p>
    </div>
    <div class="wrapped">
      <div class="wr wr--green">
        <p class="wr__year">2024</p>
        <div class="wr__stats">
          <div><b>252K</b><span>streams</span></div>
          <div><b>25K</b><span>listeners</span></div>
          <div><b>10K</b><span>hours listened</span></div>
          <div><b>82</b><span>countries</span></div>
        </div>
      </div>
      <div class="wr wr--pink">
        <p class="wr__year">2025</p>
        <div class="wr__stats">
          <div><b>92.4K</b><span>streams</span></div>
          <div><b>16.4K</b><span>listeners</span></div>
          <div><b>3.6K</b><span>hours listened</span></div>
          <div><b>75</b><span>countries</span></div>
        </div>
      </div>
      <div class="wr wr--purple">
        <p class="wr__year">Top track</p>
        <p class="wr__track">Tishinata Im x Ne Dulja Nishto<br><i>Zander mashup</i></p>
        <p class="wr__big">449,149<span>streams on Spotify</span></p>
        <p class="wr__big wr__big--sm">780K<span>views on YouTube</span></p>
      </div>
    </div>
    <p class="links"><a href="https://open.spotify.com/artist/6pP7SHyXTSZmpFe6pGnu7P" target="_blank" rel="noopener">DJZander on Spotify ↗</a></p>
  </div>
</section>
</div>

<section class="section section--tight">
  <div class="row row--first">
    <div class="row__head row__head--inline">
      <h3>Sets</h3>
      <p>Recorded live, from outdoor reggaeton to tech house.</p>
    </div>
    <div class="slider" data-list="SETS"></div>
  </div>

  <div class="row">
    <div class="row__head row__head--inline">
      <h3>Remixes &amp; mashups</h3>
      <p>Balkan and Bulgarian hits flipped for the club, plus my original track.</p>
    </div>
    <div class="slider" data-list="REMIXES"></div>
  </div>
</section>
""" + contact(p, "Book<br>a show",
              "Clubs, concerts, private events and dinner parties. Send me the date, the place and the vibe, and I'll get back to you fast.") + foot(p)


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", rel)


if __name__ == "__main__":
    write("index.html", page_home())
    write("work/what-is-this-place/index.html", page_witp())
    write("work/are-you-mental/index.html", page_aym())
    write("work/social-content/index.html", page_social())
    write("dj/index.html", page_dj())
