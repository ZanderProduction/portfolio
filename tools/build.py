"""Builds every page of zanderproduction.nl from one template, so the top bar,
phone menu, contact block and footer are the same everywhere.

Run from the repo folder:  python3 tools/build.py
Then commit the generated index.html files.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = "46"  # bump to make browsers fetch fresh css/js

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
    links = [("Home", p or "./", "home"), ("Work", p + "work/", "work"), ("DJZander", p + "dj/", "dj"),
             ("About", p + "about/", "about"), ("Contact", p + "contact/", "contact")]
    act = lambda k: ' class="is-active" aria-current="page"' if k == page else ""
    subs = [(x["title"], f'{p}work/{x["slug"]}/') for x in CASES]
    sub_top = "".join(f'<a href="{h}">{t}</a>' for t, h in subs)
    sub_mob = "".join(f'<a href="{h}">{t}</a>' for t, h in subs)
    top = []
    for t, h, k in links:
        if k == "work":
            top.append(f'<div class="nav__drop"><a href="{h}"{act(k)}>Work <i aria-hidden="true">▾</i></a><div class="nav__sub">{sub_top}</div></div>')
        else:
            top.append(f'<a href="{h}"{act(k)}>{t}</a>')
    mob = []
    for i, (t, h, k) in enumerate(links):
        label = t
        if k == "work":
            mob.append(f'<div class="mmenu__group"><div class="mmenu__row"><a href="{h}"{act(k)}><span>{i:02d}</span>{label}</a>'
                       f'<button class="mmenu__more" type="button" aria-expanded="false" aria-label="Show projects">+</button></div>'
                       f'<div class="mmenu__sub"><div class="mmenu__subin">{sub_mob}</div></div></div>')
        else:
            mob.append(f'<a href="{h}"{act(k)}><span>{i:02d}</span>{label}</a>')
    top = "\n    ".join(top); mob = "\n    ".join(mob)
    return f"""<body data-page="{page}">

<header class="nav" id="top">
  <a href="{p or './'}" class="nav__name">Alexandar Ivanov</a>
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
            lead="Email is the fastest way to reach me. I can travel anywhere in the Netherlands and do an online call any time.",
            booking=False):
    book = ('<div><dt>Bookings</dt><dd><a href="mailto:djzanderrbooking@gmail.com">djzanderrbooking@gmail.com</a></dd></div>'
            '<div><dt>Rider</dt><dd><a href="DJZander-Rider.pdf" download>Technical rider, PDF ↓</a></dd></div>'
            if booking else "")
    return f"""
<!-- ================= CONTACT ================= -->
<section class="contact" id="contact">
  <div class="section">
    <h2 class="contact__title">{title}</h2>
    <div class="contact__grid contact__grid--single">
      <div>
        <p class="contact__lead">{lead}</p>
        <dl class="contact__list">
          {book}<div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
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


def contact_band(p):
    return f"""
<section class="cband">
  <div class="cband__in">
    <h2 class="cband__title">Let's work together</h2>
    <div class="cband__links">
      <a class="cband__mail" href="mailto:{EMAIL}">{EMAIL}</a>
      <a class="cband__more" href="{p}contact/">All contact details →</a>
    </div>
  </div>
</section>
"""


def foot(p):
    return f"""
</main>

<footer class="footer">
  <span>© <span id="year">2026</span> Alexandar Ivanov / Zander Production</span>
  <a href="{p}dj/">DJZander</a>
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

CASES = [
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
    dict(slug="the-mix-up", title="The Mix Up!", video="7jMX52GM8R4", thumb=yt_thumb("7jMX52GM8R4"),
         tag="Short film / 24-hour challenge",
         line="One rule: start to finish in a day. Planned, shot and edited before the deadline.",
         role="Planning, camera and edit, solo"),
    dict(slug="week-with-zander", title="Week with Zander", video="hCSl4K2XNrE", thumb=yt_thumb("hCSl4K2XNrE"),
         tag="Vlog series / YouTube",
         line="My vlog series about gigs, travel and training. Nothing is scripted, so every episode gets found in the edit.",
         role="Filming and editing, every episode"),
    dict(slug="vsa-music-videos", title="VSA music videos", video="sZbNW_AUgt0", thumb=yt_thumb("sZbNW_AUgt0"),
         tag="Music videos / 3 videos / Bulgarian artist VSA", home=False,
         line="My first music video project: a summer in the studio with a friend, three videos and no proper equipment.",
         role="Shot on an iPhone 14 Pro and an old Lumix"),
    dict(slug="bulgarian-society-leeuwarden", title="Bulgarian Society Leeuwarden", home=False,
         thumb=CDN + "00159df6-464c-42c9-b506-bd160dd2d3d9_rw_1920.png?h=3564799de40e4e31deed437d846df51f",
         tag="Social media / posters and reels / 2023 - 2025",
         line="I co-founded the society and led its PR: the look, the Instagram, and most of the posters and reels until June 2025.",
         role="Co-founder and Head of PR, one reel at 376K views"),
]
ZANDER = dict(title="DJZander", thumb=PHOTO_CLUB,
              tag="Social content / DJ and MC business",
              line="My own DJ and MC business, and the channel I film and edit for it: 1,003,763 views between 31 May and 7 July, with no team.",
              role="Bookings, DJ and MC, filming, editing and posting")


def card(p, x, href, more="See the project →"):
    return f"""    <a class="card" href="{href}">
      <div class="card__img"><img loading="lazy" src="{x['thumb']}" alt=""></div>
      <p class="tag">{x['tag']}</p>
      <h3>{x['title']}</h3>
      <p class="card__line">{x['line']}</p>
      <p class="card__role">{x['role']}</p>
      <span class="card__more">{more}</span>
    </a>"""


def all_cards(p, home=False):
    c = [card(p, x, f"{p}work/{x['slug']}/") for x in CASES if not home or x.get("home", True)]
    return "\n".join(c)


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
  <a class="phead__back" href="{p}work/">← All work</a>
  <p class="tag">{x['tag']}</p>
  <h1 class="phead__title">{x['title']}</h1>
  <p class="phead__intro">{intro}</p>
</section>
</div>
"""


# ---------------------------------------------------------------- pages

HERO = """
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

  <div class="hero__bottom hero__bottom--solo">
    <p class="hero__intro">I make <b>series, short film and social content</b>. Fourth-year Creative Business student at NHL Stenden, looking for a <b>media production internship from February 2027</b>.</p>
  </div>
</section>
</div>
"""


def simple_head(title, intro=None, label=None):
    lab = f'<p class="label label--accent">{label}</p>' if label else ""
    it = f'<p class="phead__intro">{intro}</p>' if intro else ""
    return f"""
<main>
<div class="band invert">
<section class="phead phead--page">
  {lab}
  <h1 class="phead__title">{title}</h1>
  {it}
</section>
</div>
"""


def page_home():
    p = ""
    return head(p, "Alexandar Ivanov - Video Producer & Editor",
                "Alexandar Ivanov - video producer and editor. Series, short film and social content. Looking for a media production internship from February 2027.") + nav(p, "home") + "\n<main>\n" + HERO + f"""
<section class="section">
  <div class="section__head">
    <h2 class="h-xl">Selected work</h2>
    <a class="section__more" href="work/">All work →</a>
  </div>
  <div class="cards">
{all_cards(p, home=True)}
  </div>
{logos(p)}
</section>
""" + contact_band(p) + foot(p)


def page_work():
    p = "../"
    return head(p, "Work - Alexandar Ivanov",
                "Series, short film and social content by Alexandar Ivanov.") + nav(p, "work") + simple_head(
        "Work", "Series, short film and social content. Open a project for the full story, the credits and the episodes.") + f"""
<section class="section section--case">
  <div class="cards">
{all_cards(p)}
  </div>
{logos(p)}
</section>
""" + contact_band(p) + foot(p)


def case_page(x, title, desc, intro, credits, facts, extra="", caption=None, media=None, credits_label="Credits"):
    p = "../../"
    dl = lambda rows: "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows)
    if media is None:
        media = f"""<div class="yt yt--big" data-id="{x['video']}" data-title="{x['title']}"></div>
  <p class="case__caption">{caption or "The trailer, cut by me."}</p>"""
    cols = f"""
    <div>
      <p class="label">{credits_label}</p>
      <dl class="credits">{dl(credits)}</dl>
    </div>""" if credits else ""
    return head(p, title, desc) + nav(p, "work") + case_head(p, x, intro) + f"""
<section class="section section--case">
  {media}

  <div class="case">{cols}
    <div>
      <p class="label">The project</p>
      <dl class="credits">{dl(facts)}</dl>
    </div>
  </div>
  {extra}
</section>
""" + next_strip(p, x["slug"]) + contact_band(p) + foot(p)


def page_witp():
    return case_page(CASES[0], "What Is This Place? - Alexandar Ivanov",
        "Reality show concept for MATTERS. Main camera on all 3 episodes, editor of episodes 2 and 3, trailer.",
        "Four blindfolded people get driven to a place they don't know. A host gives them clues until they figure out where they are. We developed the format as a team and shot three episodes to pitch it.",
        [("Concept", "with the team"), ("Main camera", "all 3 episodes"), ("Editor", "episodes 2 &amp; 3"), ("Trailer", "cut by me")],
        [("Format", "reality show concept"), ("Episodes", "3, shot to pitch"), ("With", "MATTERS")],
        '<div class="episodes" data-list="WITP_EPISODES"></div>')


def page_aym():
    return case_page(CASES[1], "Are You Mental? - Alexandar Ivanov",
        "Challenge series. Main camera and editor on both episodes, trailer.",
        "Two guys, a list of challenges, no polish on purpose. The tone of the show was made in the edit, from a big pile of raw footage to something that feels loose but keeps moving.",
        [("Writing", "with the team"), ("Main camera", "both episodes"), ("Editor", "both episodes"), ("Trailer", "cut by me")],
        [("Format", "challenge series"), ("Episodes", "2 + trailer"), ("Style", "raw, made in the edit")],
        '<div class="episodes" data-list="AYM_EPISODES"></div>')


def page_mixup():
    return case_page(CASES[2], "The Mix Up! - Alexandar Ivanov",
        "Short film made in 24 hours. Planning, camera and edit by Alexandar Ivanov.",
        "A semester assignment with one rule: start to finish in a day. I planned the shoot, filmed it and delivered the final edit before the deadline.",
        [("Planning", "solo"), ("Camera", "solo"), ("Editor", "solo")],
        [("Format", "short film"), ("Deadline", "24 hours"), ("Context", "semester assignment")],
        caption="The full film.")


def page_wwz():
    return case_page(CASES[3], "Week with Zander - Alexandar Ivanov",
        "Vlog series about gigs, travel and training. Filmed and edited by Alexandar Ivanov.",
        "My vlog series about gigs, travel and training. Nothing is scripted, so every episode gets found in the edit.",
        [("Idea", "my own series"), ("Camera", "me"), ("Editor", "every episode")],
        [("Format", "vlog series"), ("Topics", "gigs, travel, training"), ("Where", "YouTube")],
        '''<div class="row">
    <div class="row__head row__head--inline">
      <h3>All episodes</h3>
      <p>Gigs, trips and training, plus a few extras.</p>
    </div>
    <div class="slider" data-list="VLOGS"></div>
  </div>''',
        caption="Week with Zander #5-6: gigs, travel and training.")


def page_vsa():
    return case_page(CASES[4], "VSA music videos - Alexandar Ivanov",
        "Three music videos for the Bulgarian artist VSA, shot on an iPhone 14 Pro and an old Lumix camera.",
        "One summer I was in the studio with a friend of mine, the Bulgarian artist VSA, and we decided to film some music videos. It was my first music video project and we didn't have proper equipment: everything was filmed on an iPhone 14 Pro and an old Lumix camera. But the passion was there.",
        [],
        [("Artist", "VSA / BlackSheep"), ("Videos", "3, released in 2023"), ("Shot on", "iPhone 14 Pro, old Lumix"), ("First", "music video project")],
        '<div class="episodes" data-list="VSA_VIDEOS" data-label="The other two videos"></div>',
        caption="STANDART, the official video.")


def page_bsl():
    reel = "https://www.instagram.com/reel/DJuIaMXtGJP/"
    media = f"""<div class="bsl">
    <a class="bsl__reel" href="{reel}" target="_blank" rel="noopener">
      <img width="548" height="858" src="{CDN}6f2e1a4a-fead-4d72-bc78-ea65194efa81_rw_600.png?h=26db4e9d4bf6024d3673bb274273542a" alt="Reel: Who is the imposter? (Balkan edition), 376K views">
      <span class="yt__play">Watch the reel ↗</span>
    </a>
    <div class="bsl__side">
      <div class="bubbles bubbles--one">
        <div class="bubble bubble--hot"><b data-count="376" data-suffix="K">376K</b><span>views on one reel I made</span></div>
      </div>
      <a class="bsl__grid" href="https://www.instagram.com/bulgariansociety.lwd/" target="_blank" rel="noopener">
        <img width="1920" height="1615" loading="lazy" src="{CASES[5]['thumb']}" alt="The society's Instagram profile">
      </a>
      <p class="links"><a href="https://www.instagram.com/bulgariansociety.lwd/" target="_blank" rel="noopener">@bulgariansociety.lwd on Instagram ↗</a></p>
    </div>
  </div>"""
    return case_page(CASES[5], "Bulgarian Society Leeuwarden - Alexandar Ivanov",
        "Co-founder and Head of PR of the Bulgarian Society Leeuwarden, 2023 - 2025. Posters, reels and the society's Instagram.",
        "I co-founded the Bulgarian Society Leeuwarden and led its PR team, shaping the society's look and public profile. I grew the Instagram from the very beginning in 2023 and made most of the posters and reels until I left the society in June 2025.",
        [("Role", "co-founder, Head of PR"), ("Instagram", "grown from zero"), ("Content", "most posters and reels"), ("Events", "DJ, venues and clubs")],
        [("Years", "2023 - June 2025"), ("Team", "weekly meetings"), ("Members", "interviews and selection"), ("Best reel", "376K views")],
        media=media, credits_label="What I did")


def page_about():
    p = "../"
    return head(p, "About - Alexandar Ivanov",
                "About Alexandar Ivanov, video producer and editor from Bulgaria, based in the Netherlands.") + nav(p, "about") + f"""
<main>
<div class="band invert">
<section class="section section--about">
  <div class="about">
    <figure class="about__photo">
      <img width="1920" height="1023" src="{PHOTO_ME}" alt="Alexandar Ivanov">
    </figure>
    <div class="about__text">
      <h1 class="h-xl">About me</h1>
      <p>I grew up in Bulgaria, went to the Sofia High School of Mathematics and moved to Leeuwarden in 2022 to study Creative Business at NHL Stenden. Across three years of concept projects I've worked on everything from campaign plans to full productions, so I'm comfortable taking an idea through planning and the shoot to a finished edit.</p>
      <p>I've always loved music. I started playing guitar as a kid, and then came DJing, and with it remixes, mashups and tracks that are now past <b>500,000 streams on Spotify</b>, <b>100,000 listens a year on SoundCloud</b> and <b>1.5 million views on YouTube</b>. I've performed and MC'd at clubs, bars, private events and dinner parties.</p>
      <p>From 2023 to 2025 I co-founded and led the PR team of the <b>Bulgarian Society Leeuwarden</b>. I shaped the society's look and grew its Instagram from nothing, sat in on interviews to pick new members, joined the weekly team meetings, and handled the club owners and venues for our events, where I was also the DJ.</p>
      <p>I did a six-month minor in <b>Intercultural and International Communication</b> and a semester exchange in <b>Málaga</b>, so working with people from everywhere is normal for me.</p>
    </div>
  </div>
</section>
</div>

<section class="section">
  <div class="cvgrid cvgrid--page">
    <div class="cvcol">
      <p class="label">Experience</p>
      <ol class="timeline">
        <li><span>2020 - now</span><div><b>Freelance DJ / Zander Production</b><p>Own registered business: bookings, clients, international logistics, shows and content</p></div></li>
        <li><span>2022 - now</span><div><b>Freelance video editor &amp; content creator</b><p>Concept, filming and editing for university, freelance and personal projects</p></div></li>
        <li><span>2023 - 2025</span><div><b>Bulgarian Society Leeuwarden</b><p>Co-founder and Head of PR</p></div></li>
        <li><span>2019 - 2022</span><div><b>System administrator, Finance Help Ltd</b><p>Part-time IT support around the office, WordPress</p></div></li>
      </ol>
    </div>
    <div class="cvcol">
      <p class="label">Education</p>
      <ol class="timeline">
        <li><span>2022 - now</span><div><b>NHL Stenden, Creative Business</b><p>Minor in Intercultural &amp; International Communication, exchange semester in Málaga</p></div></li>
        <li><span>2016 - 2021</span><div><b>Sofia High School of Mathematics</b></div></li>
      </ol>
      <p class="label label--gap">Tools</p>
      <p class="plainlist">DaVinci Resolve / Premiere Pro / Adobe Creative Cloud / CapCut / Canva / Canon 90D / FL Studio / Logic / Ableton / Pioneer CDJ-3000 / Microsoft Office</p>
      <p class="label label--gap">Also good at</p>
      <p class="plainlist">Concept development / content strategy / photography / audio engineering / planning and deadlines / team leadership</p>
      <p class="label label--gap">Languages</p>
      <p class="plainlist">English / Bulgarian</p>
      <p class="links"><a href="{p}cv.pdf" target="_blank" rel="noopener">Download my CV ↓</a></p>
    </div>
  </div>
</section>
""" + contact_band(p) + foot(p)


def page_contact():
    p = "../"
    return head(p, "Contact - Alexandar Ivanov",
                "Get in touch with Alexandar Ivanov for internships, video work or DJ bookings.") + nav(p, "contact") + "\n<main>\n" + contact(
        p, "Let's work<br>together",
        "Email is the fastest way to reach me. I can travel anywhere in the Netherlands and do an online call any time. For DJ bookings, send me the date, the place and the vibe.").replace(
        '<h2 class="contact__title">', '<h1 class="contact__title">').replace("</h2>", "</h1>", 1).replace(
        'class="contact"', 'class="contact contact--page"', 1) + foot(p)


def page_dj():
    p = "../"
    return head(p, "DJZander - DJ, MC & content",
                "DJ, MC and event content by DJZander. 1,003,763 Instagram views between 31 May and 7 July, clubs, concerts and private events.") + nav(p, "dj") + f"""
<main>
<div class="band invert">
<section class="phead phead--dj">
  <p class="label label--accent">DJZander</p>
  <h1 class="phead__title">DJ, MC and the guy filming it</h1>
  <div class="phead__cols">
    <p>I started playing clubs and events in 2020 and it turned into a real job, so I registered it with the <a href="https://www.kvk.nl/bestellen/#/99829398000064874893?origin=search" target="_blank" rel="noopener">KVK</a>. I do all of it: bookings and client contact, the rider, the set, playing and MC-ing, and then filming and editing the recap and promo content.</p>
    <p>Playing for a crowd every weekend teaches you to read a room and change plans on the spot. That's the same thing I do in an edit. Remixes, mashups and my own tracks are past <b>500,000 streams on Spotify</b> and <b>1.5 million views on YouTube</b>.</p>
  </div>
  <nav class="jump" aria-label="On this page">
    <a href="#shows">Shows</a><a href="#content">Social content</a><a href="#posters">Posters</a><a href="#music">Music</a><a href="#contact">Book a show</a><a class="jump__dl" href="DJZander-Rider.pdf" download>Tech rider ↓</a>
  </nav>
</section>
</div>

<section class="section" id="shows">
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
</section>

<div class="band invert" id="content">
<section class="section">
  <div class="insta insta--case">
    <div class="insta__text insta__text--head">
      <p class="tag">Social content / my own channel</p>
      <h2 class="h-xl">@djzanderr</h2>
      <p>As a DJ I needed content and had no team, so I built my own routine: film at the show, edit the same night, post the next day. Short videos built around the moment the crowd reacts.</p>
      <p class="card__role">Filming, editing and posting</p>
    </div>
    <div class="bubbles">
      <div class="bubble bubble--hot"><b data-count="1003763">1,003,763</b><span>views between 31 May and 7 July</span></div>
      <div class="bubble"><b data-count="602596">602,596</b><span>accounts reached</span></div>
      <div class="bubble"><b data-count="92" data-suffix="%">92%</b><span>of views from people who didn't follow me yet</span></div>
      <div class="bubble"><b data-count="4293">4,293</b><span>new followers in 30 days, almost all from reels</span></div>
    </div>
    <div class="insta__text">
      <p class="label">The insights</p>
      <p>Screenshots straight from Instagram. Almost all of the reach came from people who didn't follow me yet, so the reels were getting pushed to new audiences on their own.</p>
      <p class="links"><a href="https://www.instagram.com/djzanderr/" target="_blank" rel="noopener">Watch the reels on Instagram ↗</a></p>
    </div>
    <div class="insta__shots">
      <img width="1179" height="2556" loading="lazy" src="{CDN}2014eb0c-6765-4a27-87a1-fd05a0edc585_rw_1200.PNG?h=2306495005db6a0f2586b1e92e5cd2e3" alt="Instagram insights: 1,003,763 views">
      <img width="1179" height="2556" loading="lazy" src="{CDN}0a34cb01-e3d6-468a-976a-e2b182264d6f_rw_1200.PNG?h=fad3f78056be6dda5270d97dbaef4bfd" alt="Instagram insights: 4,293 new followers in 30 days">
    </div>
    <div id="reels" class="reels"></div>
  </div>
</section>
</div>

<section class="section section--tight" id="posters">
  <div class="row row--first">
    <div class="row__head row__head--inline">
      <h3>The posters</h3>
      <p>Some of the nights I've played.</p>
    </div>
    <div class="slider slider--posters" data-list="POSTERS"></div>
  </div>
</section>

<div class="band invert" id="music">
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
              "Clubs, concerts, private events and dinner parties. Send the date, the place and the vibe to my booking email and I'll get back to you fast.", booking=True) + foot(p)


REDIRECT = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Zander Production</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{to}">
<meta http-equiv="refresh" content="0; url={to}"></head>
<body><a href="{to}">Zander Production</a></body></html>
"""


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", rel)


if __name__ == "__main__":
    write("index.html", page_home())
    write("work/index.html", page_work())
    write("work/what-is-this-place/index.html", page_witp())
    write("work/are-you-mental/index.html", page_aym())
    write("work/week-with-zander/index.html", page_wwz())
    write("work/the-mix-up/index.html", page_mixup())
    write("work/vsa-music-videos/index.html", page_vsa())
    write("work/bulgarian-society-leeuwarden/index.html", page_bsl())
    write("work/social-content/index.html", REDIRECT.format(to="../../dj/#content"))
    write("dj/index.html", page_dj())
    write("about/index.html", page_about())
    write("contact/index.html", page_contact())
