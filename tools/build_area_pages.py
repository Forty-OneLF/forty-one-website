"""Build the town pages (Areas we cover) and sitemap.xml.

Usage: python3 tools/build_area_pages.py

Each town in AREAS becomes /architectural-design-<slug>/index.html.
Write every town's copy for that town. Never call the practice "architects":
"architect" is a protected title (Architects Act 1997). Use architectural design,
architectural designer, planning drawings, extension plans instead.
"""
import html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://forty-onecd.co.uk"
PHONE = "07404 611105"
WA = "https://wa.me/447404611105?text=Hi%20Lewis%2C%20I%27d%20like%20to%20talk%20about%20a%20project."

AREAS = [
  {
    "slug": "whitstable",
    "town": "Whitstable",
    "council": "Canterbury City Council",
    "title": "Architectural Design & Planning Drawings in Whitstable",
    "desc": "Architectural design, planning drawings and building regulations drawings in Whitstable, from a local practice. Extensions, loft conversions, new builds. Free 15-minute call.",
    "lead": "Forty-One is based in Whitstable, so this is home ground. We draw extensions, loft conversions, conversions and new homes across the town, and handle the planning application with Canterbury City Council from start to finish.",
    "nearby": ["Tankerton", "Seasalter", "Chestfield", "Swalecliffe", "Yorkletts", "Blean", "Herne Bay"],
    "planning": [
      ("Conservation areas", "Much of the old town, the harbour and parts of the seafront sit in conservation areas. Permitted development rights are narrower there, so a rear extension or dormer that would be fine elsewhere may need full planning permission. We check this on the first call."),
      ("Coastal flood risk", "Properties near the harbour and the seafront can fall within higher flood risk zones. Extensions and new homes there may need a flood risk assessment and raised floor levels, which we design in from the start rather than adding later."),
      ("New homes near the coast", "New homes in the district usually pay a small per-bedroom contribution towards protecting the coastal bird habitats. It's set by the council and we include it in the application so it doesn't hold up validation."),
    ],
    "faq": [
      ("Do I need planning permission for an extension in Whitstable?", "Not always. Many single-storey rear extensions and loft conversions can go ahead under permitted development, but not in a conservation area, on flats or where earlier permissions removed those rights. We'll tell you which route applies, and a Lawful Development Certificate can confirm it formally."),
      ("Which council handles applications in Whitstable?", "Canterbury City Council decides planning applications for Whitstable, Tankerton, Seasalter, Chestfield and Swalecliffe. We submit through the Planning Portal and deal with the case officer for you."),
      ("Can you visit the property?", "Yes. We're based in Whitstable, so a measured survey is usually arranged within days. We survey with a 3D scanner, which captures the whole building accurately in one visit."),
    ],
    "project": None,
  },
  {
    "slug": "herne-bay",
    "town": "Herne Bay",
    "council": "Canterbury City Council",
    "title": "Architectural Design & Planning Drawings in Herne Bay",
    "desc": "Architectural design and planning drawings in Herne Bay: extensions, loft conversions, new builds on garden plots and building regulations drawings. Free 15-minute call.",
    "lead": "We work across Herne Bay from our base five miles away in Whitstable. Recent work in the town includes new homes on garden plots, and we know how Canterbury City Council looks at schemes here.",
    "nearby": ["Beltinge", "Greenhill", "Eddington", "Hampton", "Studd Hill", "Broomfield", "Herne", "Reculver"],
    "planning": [
      ("Building on a garden plot", "Herne Bay has plenty of large gardens, and new homes behind or beside existing houses are common. Officers look closely at access, neighbours' privacy, the street scene and garden sizes. We test these early with a site layout before anything is drawn in detail."),
      ("Seafront and town centre", "The town centre and seafront are covered by a conservation area, and properties close to the sea can sit in higher flood risk zones. Both affect what you can build and what the application needs to include."),
      ("Water quality rules for new homes", "Some new homes in Herne Bay connect to a treatment works covered by the Stodmarsh water quality rules. For Herne Bay the requirement is very small and mitigation credits are available, but it still has to be dealt with in the application."),
    ],
    "faq": [
      ("Can I build a house in my garden in Herne Bay?", "Often, yes, if the plot is big enough and has decent access. We'll look at the site on a free call, then test a layout against the council's usual expectations before you commit to full drawings."),
      ("How long does planning take in Herne Bay?", "Canterbury City Council aims to decide householder applications within eight weeks of validation and new dwellings within eight to thirteen weeks. Allow a couple of weeks before that for the survey and drawings."),
      ("Do you do building regulations drawings too?", "Yes. Once planning is approved we produce the technical drawings your builder and building control need, coordinated with a structural engineer where needed."),
    ],
    "project": {"img": "house-front", "alt": "CGI of a new-build house in Herne Bay with a timber-clad, fully glazed gable", "cap": "New build · Herne Bay · CGI"},
    "review": ("The plans were completed to a high standard, delivered on time, and his communication was excellent from start to finish.", "Matthew A. · Herne Bay · Checkatrade 10/10"),
  },
  {
    "slug": "canterbury",
    "town": "Canterbury",
    "council": "Canterbury City Council",
    "title": "Architectural Design & Planning Drawings in Canterbury",
    "desc": "Architectural design and planning drawings in Canterbury: extensions, loft conversions, HMOs, listed buildings and conservation areas. Free 15-minute call.",
    "lead": "Canterbury is one of the most sensitive places in Kent to build, with a World Heritage Site, a historic centre and a large number of listed buildings. We prepare designs and applications that work with those constraints rather than against them.",
    "nearby": ["Wincheap", "Thanington", "St Stephen's", "Hales Place", "Harbledown", "Sturry", "Blean", "Bridge", "Chartham", "Littlebourne"],
    "planning": [
      ("Heritage and conservation", "The cathedral, St Augustine's Abbey and St Martin's Church form a World Heritage Site, and the city centre and many suburbs are conservation areas. Listed buildings need listed building consent as well as planning. We prepare heritage statements and detail extensions to suit."),
      ("Houses in multiple occupation", "Parts of Canterbury are covered by an Article 4 direction, so turning a family home into a small HMO needs planning permission there. The council looks at how many HMOs are already nearby, and we check this before you buy or convert."),
      ("Water quality rules for new homes", "New homes draining to the Canterbury, Westbere or Chartham treatment works must show they won't add nutrients to the Stodmarsh nature reserve. Credits to offset this are now on sale locally, and we build this into the application."),
    ],
    "faq": [
      ("Do I need planning permission in a Canterbury conservation area?", "Usually more often than elsewhere. Conservation areas limit permitted development, particularly for roof alterations, side extensions and cladding. We'll tell you what applies to your street on the free call."),
      ("Can you help convert a house to an HMO in Canterbury?", "Yes. We check whether the property is inside the Article 4 area and how many HMOs are nearby, then prepare the change of use application and layout drawings to meet room size and licensing standards."),
      ("My application in Canterbury was refused. What now?", "We'll read the decision notice and officer's report, then advise whether a revised application or an appeal is the better route. A well-targeted resubmission is often quicker than an appeal."),
    ],
    "project": {"img": "stour-kitchen", "alt": "CGI of a kitchen in an infill extension in Canterbury", "cap": "Infill extension · Canterbury · CGI"},
  },
]

SERVICES = [
  ("House extensions", "Single and double-storey, side, rear and wraparound."),
  ("Loft conversions", "Dormers, hip-to-gable and mansards, with the stair worked out early."),
  ("Planning applications", "Drawings, statements and submission, then we deal with the council."),
  ("Building regulations drawings", "Technical drawings your builder and building control can work from."),
  ("New homes and small developments", "Garden plots, replacement dwellings and multi-unit schemes."),
  ("Change of use and HMOs", "Office, retail and house conversions, including prior approval."),
]

CSS = """:root{--paper:#F1F1EE;--sheet:#FBFBF9;--ink:#17191B;--muted:#5C5F5C;--line:#CDCBC4;--oak:#94663A;--wrap:1040px;color-scheme:light}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--paper:#111213;--sheet:#1F2021;--ink:#ECEAE5;--muted:#A2A09A;--line:#2F3031;--oak:#C99663;color-scheme:dark}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:"Montserrat","Helvetica Neue",Arial,sans-serif;font-size:16px;line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:inherit}img{display:block;max-width:100%;height:auto}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 16px}
.top{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--paper) 92%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;height:64px}
.mark{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:700;letter-spacing:.06em;font-size:14px}
.mark img{width:30px;height:30px}.mark span{display:flex;flex-direction:column;line-height:1.15}.mark small{font-weight:500;font-size:10px;letter-spacing:.14em;color:var(--muted)}
.cta{display:inline-block;background:var(--ink);color:var(--paper);text-decoration:none;font-weight:600;font-size:14px;padding:11px 18px;border-radius:2px}
.cta.alt{background:transparent;color:var(--ink);border:1px solid var(--ink)}
.label{font-size:12px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
h1,h2,h3{font-weight:600;line-height:1.12;margin:0;letter-spacing:-.01em;text-wrap:balance}
h1{font-size:clamp(30px,5vw,48px);margin:12px 0 18px}h2{font-size:clamp(23px,3vw,30px);margin:8px 0 18px}h3{font-size:17px;margin:0 0 6px}
section{padding:48px 0;border-bottom:1px solid var(--line)}
.lead{font-size:18px;max-width:62ch}.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.card{background:var(--sheet);border:1px solid var(--line);padding:18px}.card p{margin:0;color:var(--muted);font-size:15px}
.points{display:grid;gap:22px}.points p{margin:0;max-width:68ch}
.nearby{display:flex;flex-wrap:wrap;gap:8px;padding:0;margin:0;list-style:none}.nearby li{border:1px solid var(--line);padding:4px 12px;font-size:14px}
figure{margin:0}figcaption{font-size:13px;color:var(--muted);margin-top:8px}
blockquote{margin:22px 0 0;padding-left:16px;border-left:3px solid var(--oak);font-size:17px;max-width:62ch}blockquote cite{display:block;font-style:normal;font-size:13px;color:var(--muted);margin-top:8px}
details{border-top:1px solid var(--line);padding:14px 0}details:last-child{border-bottom:1px solid var(--line)}summary{cursor:pointer;font-weight:600}details p{margin:10px 0 0;max-width:68ch}
.others a{margin-right:16px}
footer{background:var(--ink);color:color-mix(in srgb,var(--paper) 72%,transparent);font-size:13px;padding:28px 0 40px}footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px}
@media (max-width:560px){.top .cta{padding:9px 12px;font-size:13px}}
"""


def esc(s):
    return html.escape(s, quote=True)


def schema(a):
    url = f"{SITE}/architectural-design-{a['slug']}/"
    data = [
        {
            "@context": "https://schema.org",
            "@type": "ProfessionalService",
            "@id": f"{SITE}/#business",
            "name": "Forty-One Architecture",
            "url": f"{SITE}/",
            "telephone": "+447404611105",
            "email": "enquiries@forty-onecd.co.uk",
            "address": {"@type": "PostalAddress", "addressLocality": "Whitstable", "addressRegion": "Kent", "addressCountry": "GB"},
        },
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": f"Architectural design and planning drawings in {a['town']}",
            "serviceType": "Architectural design",
            "provider": {"@id": f"{SITE}/#business"},
            "areaServed": [{"@type": "Place", "name": a["town"]}] + [{"@type": "Place", "name": n} for n in a["nearby"]],
            "url": url,
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": a["town"], "item": url},
            ],
        },
    ]
    return json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")


def page(a):
    t = a["town"]
    url = f"{SITE}/architectural-design-{a['slug']}/"
    services = "".join(f'<div class="card"><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for n, d in SERVICES)
    points = "".join(f"<div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>" for h, p in a["planning"])
    nearby = "".join(f"<li>{esc(n)}</li>" for n in a["nearby"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>" for q, ans in a["faq"])
    others = "".join(f'<a href="/architectural-design-{o["slug"]}/">{esc(o["town"])}</a>' for o in AREAS if o is not a)
    work = ""
    if a.get("project"):
        p = a["project"]
        work = f'<figure><img src="/img/{p["img"]}.jpg" alt="{esc(p["alt"])}" loading="lazy" width="1200" height="800"><figcaption>{esc(p["cap"])}</figcaption></figure>'
    if a.get("review"):
        q, who = a["review"]
        work += f"<blockquote>“{esc(q)}”<cite>{esc(who)}</cite></blockquote>"
    work_sec = f'<section><div class="wrap"><span class="label">Work in {esc(t)}</span><h2>Recent work nearby</h2>{work}<div class="btns"><a class="cta alt" href="/#work">See more projects</a></div></div></section>' if work else ""
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(a['title'])} | Forty-One</title>
<meta name="description" content="{esc(a['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Forty-One Architecture">
<meta property="og:title" content="{esc(a['title'])}"><meta property="og:description" content="{esc(a['desc'])}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/img/share.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema(a)}</script>
</head>
<body>
<header class="top"><div class="wrap">
<a class="mark" href="/"><img src="/forty-one-logo.svg" alt="" width="30" height="30"><span>FORTY-ONE<small>ARCHITECTURE</small></span></a>
<a class="cta" href="/#book">Book a free call</a>
</div></header>
<main>
<section><div class="wrap">
<span class="label">{esc(t)} · {esc(a['council'])}</span>
<h1>Architectural design and planning drawings in {esc(t)}</h1>
<p class="lead">{esc(a['lead'])}</p>
<div class="btns"><a class="cta" href="/#book">Book a free 15-minute call</a><a class="cta alt" href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE}</a></div>
</div></section>
<section><div class="wrap">
<span class="label">Services</span><h2>What we do in {esc(t)}</h2>
<div class="grid">{services}</div>
</div></section>
<section><div class="wrap">
<span class="label">Local knowledge</span><h2>Planning in {esc(t)}: what to know</h2>
<div class="points">{points}</div>
</div></section>
{work_sec}
<section><div class="wrap">
<span class="label">How it works</span><h2>From first call to building on site</h2>
<div class="grid">
<div class="card"><h3>1. Free 15-minute call</h3><p>Tell us about the project. We'll say what's likely to need planning and what it will cost.</p></div>
<div class="card"><h3>2. Survey and design</h3><p>A 3D measured survey, then design options and CGIs so you can see it before it's built.</p></div>
<div class="card"><h3>3. Planning</h3><p>We prepare and submit the application, then handle the council until a decision.</p></div>
<div class="card"><h3>4. Technical drawings</h3><p>Building regulations drawings for your builder and building control.</p></div>
</div>
</div></section>
<section><div class="wrap">
<span class="label">Area covered</span><h2>{esc(t)} and nearby</h2>
<ul class="nearby">{nearby}</ul>
<p style="margin-top:18px" class="others">Also covering: {others} and the rest of Kent and London.</p>
</div></section>
<section><div class="wrap">
<span class="label">FAQs</span><h2>Common questions in {esc(t)}</h2>
{faq}
<div class="btns"><a class="cta" href="/#book">Book a free call</a><a class="cta alt" href="/#contact">Send an enquiry</a></div>
</div></section>
</main>
<footer><div class="wrap"><span><b>Forty-One Architecture</b> · Part of the Forty-One Group · Whitstable, Kent · {PHONE}</span><span>A trading name of Forty-One Consult and Design Ltd · Company no. 16366675 · <a href="/privacy.html">Privacy notice</a></span></div></footer>
</body>
</html>
"""


def main():
    urls = [f"{SITE}/"]
    for a in AREAS:
        d = os.path.join(ROOT, f"architectural-design-{a['slug']}")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(a))
        urls.append(f"{SITE}/architectural-design-{a['slug']}/")
    urls.append(f"{SITE}/privacy.html")
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
    sm += "</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(sm)
    print("\n".join(urls))


if __name__ == "__main__":
    main()
