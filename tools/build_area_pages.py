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
# Month the planning facts on every town page were last checked against their sources.
# The monthly planning-facts check updates this (and any changed facts) after Lewis approves.
REVIEWED = "November 2026"
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
    "sources": [('Stodmarsh water quality rules', 'https://www.canterbury.gov.uk/planning-and-building/how-planning-applications-are-affected-stodmarsh-water-quality')],
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
    "sources": [('Stodmarsh water quality rules', 'https://www.canterbury.gov.uk/planning-and-building/how-planning-applications-are-affected-stodmarsh-water-quality')],
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
  {
    "slug": "margate",
    "sources": [('Cliftonville Development Plan Document', 'https://www.thanet.gov.uk/wp-content/uploads/2018/03/Cliftonville_DPD_03_2010.pdf')],
    "town": "Margate",
    "council": "Thanet District Council",
    "title": "Architectural Design & Planning Drawings in Margate",
    "desc": "Architectural design and planning drawings in Margate and Cliftonville: extensions, loft conversions, flat and HMO conversions, building regulations drawings. Free 15-minute call.",
    "lead": "Margate's big Victorian and Edwardian houses, seafront terraces and Cliftonville villas make for some of the most rewarding projects in Kent. We design extensions, loft conversions and conversions across the town and take the application through Thanet District Council.",
    "nearby": ["Cliftonville", "Westbrook", "Garlinge", "Northdown", "Palm Bay", "Westgate-on-Sea", "Westwood"],
    "planning": [
      ("Conservation areas", "The old town, the seafront and much of Cliftonville sit in conservation areas, including Dalby Square, Ethelbert Road and Northdown Road. Windows, roofs, front boundaries and extensions visible from the street get extra scrutiny, so we design with that in mind from the outset."),
      ("Flats and HMOs", "An Article 4 direction covers the whole of Thanet, so turning a family house into a small HMO needs planning permission. In Cliftonville, a specific policy resists splitting houses last used as family homes into flats, and new HMOs aren't permitted in mapped parts of Cliftonville and Margate Central. We check what's realistic before you buy or spend on drawings."),
      ("New homes near the coast", "New homes in Thanet pay a small per-bedroom contribution to protect the Thanet Coast's wintering birds. We include it in the application so it doesn't hold up validation."),
    ],
    "faq": [
      ("Can I convert my house into flats in Margate?", "Sometimes. It depends on the street, the size of the house and the flats you'd create. We'll look at the property and the council's policies on a free call and give you a straight answer before you commit."),
      ("Do I need planning permission for a loft conversion in Cliftonville?", "If the house is in a conservation area, roof alterations facing the street usually need permission. Elsewhere many lofts fall under permitted development. We'll confirm which applies to your house."),
      ("Which council handles applications in Margate?", "Thanet District Council decides planning applications for Margate, Cliftonville, Westgate-on-Sea and the rest of the district. We submit and deal with the case officer for you."),
    ],
    "project": None,
  },
  {
    "slug": "ramsgate",
    "town": "Ramsgate",
    "council": "Thanet District Council",
    "title": "Architectural Design & Planning Drawings in Ramsgate",
    "desc": "Architectural design and planning drawings in Ramsgate: extensions, loft conversions, listed buildings, conservation areas and building regulations drawings. Free 15-minute call.",
    "lead": "Ramsgate has some of the finest Regency and Victorian streets on the Kent coast, around the Royal Harbour and along the cliff tops. We design extensions, alterations and conversions that respect that character and handle the application with Thanet District Council.",
    "nearby": ["Royal Harbour", "Pegwell", "Newington", "Nethercourt", "Westwood", "Minster", "Cliffsend"],
    "planning": [
      ("Conservation areas and Article 4", "Much of the town is in the Ramsgate, Royal Esplanade or Montefiore conservation areas. On parts of streets such as Nelson Crescent, Paragon, Albion Hill and Prospect Terrace, an Article 4 direction removes the usual householder freedoms, so changes such as windows and doors can need permission. We check your address first."),
      ("Listed buildings", "Ramsgate has a large number of listed buildings, and works inside as well as outside need listed building consent. We prepare the heritage statement and detail the work so it's acceptable to the conservation officer."),
      ("HMOs and new homes", "An Article 4 direction across Thanet means a family house to small HMO change needs planning permission, and new homes pay a small coastal habitat contribution. Both are built into our applications."),
    ],
    "faq": [
      ("Do I need permission to change windows in Ramsgate?", "In many central and harbourside streets, yes. The conservation areas and an Article 4 direction remove the usual freedom to change windows and doors. We'll check your property and prepare the application if needed."),
      ("Can you help with a listed building in Ramsgate?", "Yes. We survey the building, prepare drawings and a heritage statement, and apply for listed building consent alongside planning where both are needed."),
      ("How long does planning take with Thanet District Council?", "The council aims to decide householder applications within eight weeks of validation. Listed building consent runs to a similar timescale, and we submit both together."),
    ],
    "project": None,
  },
  {
    "slug": "broadstairs",
    "sources": [("Broadstairs & St Peter's Neighbourhood Plan", 'https://www.broadstairs.gov.uk/?p=154')],
    "town": "Broadstairs",
    "council": "Thanet District Council",
    "title": "Architectural Design & Planning Drawings in Broadstairs",
    "desc": "Architectural design and planning drawings in Broadstairs and St Peter's: extensions, loft conversions, new homes and building regulations drawings. Free 15-minute call.",
    "lead": "From the seafront around Viking Bay to the 1930s houses inland, Broadstairs has a strong character people want to protect. We design extensions, loft conversions and new homes that suit the town and take them through Thanet District Council.",
    "nearby": ["St Peter's", "Reading Street", "Kingsgate", "Dumpton", "Joss Bay", "Westwood"],
    "planning": [
      ("Neighbourhood plan", "Broadstairs and St Peter's has its own neighbourhood plan, which carries real weight in planning decisions alongside Thanet's Local Plan. It sets expectations on design and character, and we reference it directly in applications here."),
      ("Conservation areas", "The town centre and seafront, St Peter's village, Reading Street and Kingsgate are all conservation areas. Permitted development is narrower there, particularly for roof and street-facing changes."),
      ("Coastal and HMO rules", "New homes pay a small per-bedroom contribution towards protecting the Thanet Coast, and an Article 4 direction across Thanet means converting a house to a small HMO needs planning permission."),
    ],
    "faq": [
      ("Do I need planning permission for an extension in Broadstairs?", "Many single-storey rear extensions are permitted development, but not in a conservation area in every case, and not where earlier permissions removed those rights. We'll tell you which route applies on the free call."),
      ("Does the neighbourhood plan affect my application?", "Yes. The council must take it into account, so applications in Broadstairs and St Peter's are stronger when the design and statement show how they meet its policies."),
      ("Can you visit the property?", "Yes. We're 20 minutes away in Whitstable and survey with a 3D scanner, so one visit captures everything we need."),
    ],
    "project": None,
  },
  {
    "slug": "birchington",
    "sources": [('Thanet neighbourhood plans', 'https://www.thanet.gov.uk/info-pages/local-plan-updates/'), ('Birchington Conservation Area Appraisal', 'https://www.thanet.gov.uk/?p=38692')],
    "town": "Birchington",
    "council": "Thanet District Council",
    "title": "Architectural Design & Planning Drawings in Birchington",
    "desc": "Architectural design and planning drawings in Birchington and Minnis Bay: bungalow extensions, dormers, porches, garden buildings and building regulations drawings. Free 15-minute call.",
    "lead": "Birchington is full of bungalows and chalet homes with plenty of potential for extending up or out. We design dormers, extensions, porches and garden buildings across the village and handle the application with Thanet District Council.",
    "nearby": ["Minnis Bay", "Westgate-on-Sea", "Acol", "St Nicholas at Wade", "Epple Bay", "Margate"],
    "planning": [
      ("Bungalows and dormers", "Adding a first floor or large dormers to a bungalow is the most common project here. Officers look at the effect on the street and on neighbours' light and privacy, so we test the massing early and show it in 3D before you commit."),
      ("Conservation area and neighbourhood plan", "The village centre is a conservation area with a recently adopted appraisal, and Birchington has its own neighbourhood plan (2023), which the council must take into account. Both shape what is acceptable on materials, scale and visibility."),
      ("Porches, outbuildings and permitted development", "Many porches and garden rooms need no planning permission if they stay within size and height limits, and a Lawful Development Certificate can confirm it. We'll tell you which side of the line your plans fall."),
    ],
    "faq": [
      ("Can I add a first floor to my bungalow in Birchington?", "Often, yes, with planning permission. Success depends on the height, how it sits with neighbouring homes and overlooking. We'll test options before full drawings."),
      ("Do I need planning permission for a garden room?", "Usually not if it's single-storey, within the height limits for its distance from the boundary, and not used as a separate home. We can confirm it with a Lawful Development Certificate."),
      ("Which council handles Birchington applications?", "Thanet District Council. We prepare and submit the application and deal with the case officer until a decision."),
    ],
    "project": None,
  },
  {
    "slug": "faversham",
    "sources": [("Faversham Neighbourhood Plan", "https://news.swale.gov.uk/news/new-faversham-neighbourhood-plan"), ("Faversham Conservation Area Appraisal", "https://swale.gov.uk/__data/assets/pdf_file/0008/453905/Faversham_CA_Appraisal_Aug_2023_V3.1_AA_Final.pdf")],
    "town": "Faversham",
    "council": "Swale Borough Council",
    "title": "Architectural Design & Planning Drawings in Faversham",
    "desc": "Architectural design and planning drawings in Faversham: extensions, loft conversions, listed buildings, conservation area work and building regulations drawings. Free 15-minute call.",
    "lead": "Faversham is one of the best-preserved historic towns in Kent, and that shapes almost every project here. We design extensions, alterations and new homes that respect it and take them through Swale Borough Council.",
    "nearby": ["Ospringe", "Davington", "Oare", "Preston", "Goodnestone", "Graveney", "Boughton under Blean", "Selling"],
    "planning": [
      ("Listed buildings and the conservation area", "The town has around 350 listed buildings, and the centre has been a conservation area since 1971, with an Article 4 direction removing some householder freedoms. Expect listed building consent and careful detailing for many town-centre projects."),
      ("Faversham Neighbourhood Plan", "A new neighbourhood plan was made in December 2024 and replaces the old Faversham Creek plan. It carries weight in decisions, so we show how a design meets its policies."),
      ("New homes near the marshes", "New homes within reach of the North Kent Marshes pay a per-home contribution towards protecting wintering birds. We include it in the application so it doesn't delay validation."),
    ],
    "faq": [
      ("Do I need listed building consent in Faversham?", "If the building is listed, yes, for most work affecting its character, inside or out. We check the listing and prepare the drawings and heritage statement the council needs."),
      ("Can I extend a house in the Faversham conservation area?", "Usually, but design and materials matter more, and some changes that are normally permitted development need permission here. We'll set out what's realistic on the free call."),
      ("Which council handles Faversham applications?", "Swale Borough Council. We submit through the Planning Portal and deal with the case officer until a decision."),
    ],
    "project": None,
  },
  {
    "slug": "sittingbourne",
    "town": "Sittingbourne",
    "council": "Swale Borough Council",
    "title": "Architectural Design & Planning Drawings in Sittingbourne",
    "desc": "Architectural design and planning drawings in Sittingbourne: house extensions, loft conversions, HMOs, new homes and building regulations drawings. Free 15-minute call.",
    "lead": "Sittingbourne is growing fast, and many homeowners are extending rather than moving. We design extensions, loft conversions and new homes across the town and handle the application with Swale Borough Council.",
    "nearby": ["Milton Regis", "Kemsley", "Murston", "Bapchild", "Borden", "Tunstall", "Bobbing", "Iwade", "Isle of Sheppey"],
    "planning": [
      ("Swale's extension guidance", "Swale has its own householder guide on extension size, roof shapes and protecting neighbours. Designing to it from the start avoids the most common reasons for refusal here."),
      ("HMOs across the borough", "Swale made a borough-wide Article 4 direction in 2026, so turning a family house into a small HMO needs planning permission, judged against a new HMO planning document."),
      ("Historic centres", "The High Street and Milton Regis are both conservation areas, where alterations need more care with materials and frontage design."),
    ],
    "faq": [
      ("Do I need planning permission for an extension in Sittingbourne?", "Many single-storey rear extensions and loft conversions are permitted development, but not all. We'll tell you which route your project needs, and a Lawful Development Certificate can confirm it."),
      ("Can I turn my house into an HMO in Sittingbourne?", "You now need planning permission even for a small HMO, because of the borough-wide Article 4 direction. We prepare the application and layout to meet the council's HMO standards."),
      ("Which council handles Sittingbourne applications?", "Swale Borough Council, which also covers Faversham and the Isle of Sheppey."),
    ],
    "project": None,
  },
  {
    "slug": "chatham",
    "sources": [("Arches Neighbourhood Plan referendum", "https://democracy.medway.gov.uk/mgconvert2pdf.aspx?id=73901")],
    "town": "Chatham",
    "council": "Medway Council",
    "title": "Architectural Design & Planning Drawings in Chatham",
    "desc": "Architectural design and planning drawings in Chatham: extensions, loft conversions, flat and HMO conversions, building regulations drawings. Free 15-minute call.",
    "lead": "Chatham's terraces and Victorian villas suit extensions, loft conversions and conversions, but Medway has firm rules on flats and HMOs. We design to them and handle the application with Medway Council.",
    "nearby": ["Luton", "Brompton", "Walderslade", "Lordswood", "Princes Park", "Wayfield", "Rochester", "Gillingham"],
    "planning": [
      ("Flats and HMOs", "Medway has specific policies on converting houses to flats, and an Article 4 direction means small HMOs need planning permission in wards including Chatham Central & Brompton, Fort Pitt, Luton and Watling. We check your address before you buy or spend on drawings."),
      ("Dockyard and Brompton", "The Historic Dockyard, Brompton Lines and parts of central Chatham are conservation areas, some with Article 4 directions that remove the usual householder freedoms, so check before changing windows, doors or roofs."),
      ("Neighbourhood plan and new homes", "Part of Chatham is covered by the Arches Neighbourhood Plan, approved at referendum in 2024. New homes near the estuary also pay a per-home contribution towards protecting the North Kent Marshes."),
    ],
    "faq": [
      ("Can I convert a house into flats in Chatham?", "Sometimes. Medway's flat conversion policy looks at the size of the house, the flats created, parking and amenity space. We'll give you a straight view before you commit."),
      ("Do I need permission for an HMO in Chatham?", "In the Article 4 wards, yes, even for a small HMO. Elsewhere a small HMO may be permitted development. We'll check which applies."),
      ("Which council handles Chatham applications?", "Medway Council, which covers Chatham, Rochester, Gillingham, Strood and Rainham."),
    ],
    "project": None,
  },
  {
    "slug": "rochester",
    "town": "Rochester",
    "council": "Medway Council",
    "title": "Architectural Design & Planning Drawings in Rochester",
    "desc": "Architectural design and planning drawings in Rochester: extensions, listed buildings, conservation areas, flat conversions and building regulations drawings. Free 15-minute call.",
    "lead": "Historic Rochester, with the castle, the cathedral and the High Street, is one of Kent's most sensitive places to build. We design extensions and alterations that respect it and handle planning and listed building consent with Medway Council.",
    "nearby": ["Strood", "Frindsbury", "Borstal", "Wainscott", "Cuxton", "Rochester Riverside", "Chatham"],
    "planning": [
      ("Historic Rochester", "The city centre, Star Hill to Sun Pier and New Road are conservation areas, and Historic Rochester has an Article 4 direction that removes the usual householder freedoms. Many buildings are also listed."),
      ("Backland and infill homes", "Medway has a specific policy for new homes built behind or beside existing houses, covering access, overlooking and the size of plots and gardens. We test these early with a site layout."),
      ("Flats and HMOs", "Converting houses to flats is judged against Medway's flat conversion policy, and an Article 4 direction requires permission for small HMOs in wards including Strood North & Frindsbury."),
    ],
    "faq": [
      ("Do I need permission to replace windows in Rochester?", "In Historic Rochester it may, because of the Article 4 direction, and it always does for a listed building. We'll check your property first."),
      ("Can you help with a listed building in Rochester?", "Yes. We survey, draw and prepare the heritage statement, and apply for listed building consent and planning together where both are needed."),
      ("Can I build a house in my garden in Rochester?", "Possibly, if access, plot size and neighbours' privacy work. Medway's backland policy sets the tests, and we'll check them before full drawings."),
    ],
    "project": None,
  },
  {
    "slug": "gillingham",
    "town": "Gillingham",
    "council": "Medway Council",
    "title": "Architectural Design & Planning Drawings in Gillingham",
    "desc": "Architectural design and planning drawings in Gillingham and Rainham: rear extensions, loft conversions, HMOs, flats and building regulations drawings. Free 15-minute call.",
    "lead": "Gillingham's Victorian and Edwardian terraces are ideal for rear extensions and loft conversions. We design them to work for growing families and handle the application with Medway Council.",
    "nearby": ["Rainham", "Twydall", "Hempstead", "Wigmore", "Parkwood", "Brompton", "Chatham"],
    "planning": [
      ("Terraces, lofts and rear extensions", "Most terraced lofts and single-storey rear extensions can use permitted development, but neighbour consultation and size limits still apply. We confirm the route and, where useful, secure a Lawful Development Certificate."),
      ("HMOs in Gillingham North and South", "An Article 4 direction confirmed in 2026 means converting a house to a small HMO needs planning permission in Gillingham North and Gillingham South wards, among others."),
      ("Conservation areas", "Gillingham Green and Gillingham Park are conservation areas, and Gillingham Park also has an Article 4 direction, so some normally permitted changes need permission there."),
    ],
    "faq": [
      ("Do I need planning permission for a loft conversion in Gillingham?", "Usually not for a typical rear dormer on a terraced or semi-detached house, unless it's in a conservation area or permitted development rights have been removed. We'll confirm on the free call."),
      ("Can I turn my house into an HMO in Gillingham?", "In Gillingham North and South you need planning permission even for a small HMO. We prepare the application and layouts to Medway's standards."),
      ("Which council handles Gillingham applications?", "Medway Council. We submit and deal with the case officer until a decision."),
    ],
    "project": None,
  },
]

# Council-level planning context, shown on every town page for that council.
# Each fact must come from a source listed here. The monthly check re-reads these sources.
COUNCILS = {
  "Canterbury City Council": {
    "plan": "Applications are decided under the Canterbury District Local Plan (adopted 2017). A replacement plan has been through its final public consultation but is not yet adopted, so the 2017 policies still apply.",
    "policies": [
      ("DBE3 Principles of Design", "The main design test for all new building, including new homes on garden or infill plots."),
      ("DBE6 Alterations and Extensions", "Extensions must suit the original house and street and avoid harming neighbours' light, outlook and privacy."),
      ("DBE4 Residential Space Standards", "New homes and flats must meet national minimum room and floor-area sizes."),
      ("HD6 Housing in Multiple Occupation", "Controls new HMOs, alongside the Article 4 direction area mapped in the plan."),
      ("HE6 and HE8 Conservation Areas", "Development in or near a conservation area must preserve or enhance its character."),
      ("HE4 and HE5 Listed Buildings", "Changes to listed buildings and their settings need to protect their special interest."),
    ],
    "sources": [
      ("Canterbury adopted Local Plan", "https://www.canterbury.gov.uk/planning-and-building/planning-policies/adopted-local-plan"),
      ("Draft Local Plan consultation", "https://haveyoursay.canterbury.gov.uk/draft-canterbury-district-local-plan-regulation-19-consultation"),
      ("Coastal habitat contributions", "https://www.canterbury.gov.uk/planning-and-building/planning-obligations/planning-obligations-special-protection-areas-samms"),
    ],
  },
  "Thanet District Council": {
    "plan": "Applications are decided under the Thanet Local Plan (adopted 2020) and, in Cliftonville, the Cliftonville Development Plan Document (2010). Work on a replacement plan has only just started.",
    "policies": [
      ("QD02 General Design Principles", "The main design test, covering extensions and new homes, including building on garden land where it isn't harmful to the area."),
      ("QD03 Living Conditions", "Protects neighbours' light, outlook and privacy, and sets the living standards for new homes."),
      ("HO19 Houses in Multiple Occupation", "New HMOs are not permitted in the mapped parts of Cliftonville and Margate Central."),
      ("HO8 Cliftonville West and Margate Central", "Area policy aimed at improving housing quality in these wards."),
      ("HE02 Development in Conservation Areas", "Development must preserve or enhance the conservation area's character."),
      ("Kent Design Guide", "Adopted county-wide design guidance that the council also uses."),
    ],
    "sources": [
      ("Thanet Local Plan 2020", "https://www.thanet.gov.uk/info-pages/local-plan-updates/"),
      ("New Local Plan timetable", "https://www.thanet.gov.uk/timetable-published-in-preparation-for-a-new-local-plan-2/"),
      ("Thanet conservation areas", "https://www.thanet.gov.uk/info-pages/conservation-area/"),
      ("Thanet HMO Article 4", "https://democracy.thanet.gov.uk/ieDecisionDetails.aspx?AIId=10021"),
    ],
  },
  "Swale Borough Council": {
    "plan": "Applications are decided under Bearing Fruits 2031, the Swale Local Plan (adopted 2017). A replacement plan has finished its final public consultation and is due to go to examination, so the 2017 policies still apply for now.",
    "policies": [
      ("CP 4 Requiring good design", "The main design test for extensions and new homes."),
      ("DM 14 General development criteria", "Covers effects on neighbours, the street and highway safety."),
      ("Designing an Extension – A Guide for Householders", "Swale's own guidance on extension size, roof form and protecting neighbours."),
      ("DM 32 and DM 33 Listed buildings and conservation areas", "Work affecting listed buildings or conservation areas must protect their character."),
      ("Houses in Multiple Occupation SPD (2026)", "Sets out how HMO applications are judged, alongside a borough-wide Article 4 direction made in 2026."),
    ],
    "sources": [
      ("Swale Local Plan", "https://swale.gov.uk/local-plan-for-swale/"),
      ("Local Plan Review consultation", "https://swale.gov.uk/your-council/consultations/local-plan-publication-draft-consultation-regulation-19"),
      ("Designing an Extension guide", "https://swale.gov.uk/news-and-your-council/publications/planning-and-planning-policy/designing-an-extension-a-guide-for-householders"),
      ("HMO Article 4 direction", "https://swale.gov.uk/your-council/consultations/article-4-direction-affecting-houses-in-multiple-occupation-approval"),
      ("Coastal habitat contributions (SAMMS)", "https://swale.gov.uk/news-and-your-council/publications/planning-and-planning-policy/strategic-access-management-and-monitoring-strategy-samms"),
    ],
  },
  "Medway Council": {
    "plan": "Applications are still decided under the Medway Local Plan (2003). Its replacement, the Medway Local Plan 2041, is being examined by a government inspector, and its draft policies are starting to carry weight.",
    "policies": [
      ("BNE1 General Principles for Built Development", "The main design test, used for extensions as Medway has no separate extensions policy."),
      ("BNE2 Amenity Protection", "Protects neighbours' light, outlook and privacy."),
      ("H6 Flat Conversions", "Sets the tests for converting houses into flats."),
      ("H7 Multiple Occupation", "Controls HMOs, alongside an Article 4 direction in seven wards."),
      ("H9 Backland and Tandem Development", "Applies to new homes built behind or beside existing houses."),
      ("BNE12–BNE18 Conservation areas and listed buildings", "Protect the character of Medway's historic areas and buildings."),
    ],
    "sources": [
      ("Medway Local Plan 2041 roadmap", "https://www.medway.gov.uk/info/200542/medway_local_plan_2041/1824/roadmap_to_delivering_our_new_local_plan"),
      ("Medway Local Plan 2003", "https://www.medway.gov.uk/download/downloads/id/2400/medway_local_plan_2003.pdf"),
      ("HMO Article 4 wards", "https://democracy.medway.gov.uk/ieIssueDetails.aspx?IId=42771"),
      ("Article 4 directions", "https://www.medway.gov.uk/info/200147/applying_for_planning_permission/553/article_4_directions/2"),
      ("Current planning policies", "https://www.medway.gov.uk/info/200149/planning_policy/146/current_planning_policies/5"),
    ],
  },
}

SERVICES = [
  ("House extensions", "Single and double-storey, side, rear and wraparound."),
  ("Loft conversions", "Dormers, hip-to-gable and mansards, with the stair worked out early."),
  ("Planning applications", "Drawings, statements and submission, then we deal with the council."),
  ("Building regulations drawings", "Technical drawings your builder and building control can work from."),
  ("New homes and small developments", "Garden plots, replacement dwellings and multi-unit schemes."),
  ("Change of use and HMOs", "Office, retail and house conversions, including prior approval."),
]

CSS = """:root{--paper:#F1F1EE;--sheet:#FBFBF9;--ink:#17191B;--muted:#5C5F5C;--line:#CDCBC4;--oak:#94663A;--on-brand:#FFFFFF;--wrap:1040px;--f-display:"Montserrat","Helvetica Neue",Arial,sans-serif;--f-mono:"Montserrat","Helvetica Neue",Arial,sans-serif;--f-body:"Montserrat","Helvetica Neue",Arial,sans-serif;color-scheme:light}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--paper:#111213;--sheet:#1F2021;--ink:#ECEAE5;--muted:#A2A09A;--line:#2F3031;--oak:#C99663;--on-brand:#111213;color-scheme:dark}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:"Montserrat","Helvetica Neue",Arial,sans-serif;font-size:16px;line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:inherit}img{display:block;max-width:100%;height:auto}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 16px}
.cta{display:inline-block;background:var(--oak);color:var(--on-brand);border:1px solid var(--oak);text-decoration:none;font-weight:500;font-size:14px;padding:10px 18px;border-radius:2px}.cta:hover{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.hnav{display:flex;align-items:center;gap:28px}.hnav a:not(.cta){text-decoration:none;font-size:14px;font-weight:500}.hnav a:not(.cta):hover{color:var(--oak)}
@media (max-width:860px){.hnav a:not(.cta){display:none}}
.top .wrap{max-width:1240px}
.cta.alt{background:transparent;color:var(--ink);border:1px solid var(--ink)}.cta.alt:hover{color:var(--paper)}
.label{font-size:12px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
h1,h2,h3{font-weight:600;line-height:1.12;margin:0;letter-spacing:-.01em;text-wrap:balance}
h1{font-size:clamp(30px,5vw,48px);margin:12px 0 18px}h2{font-size:clamp(23px,3vw,30px);margin:8px 0 18px}h3{font-size:17px;margin:0 0 6px}
section{padding:48px 0;border-bottom:1px solid var(--line)}
.lead{font-size:18px;max-width:62ch}.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.card{background:var(--sheet);border:1px solid var(--line);padding:18px}.card p{margin:0;color:var(--muted);font-size:15px}
.points{display:grid;gap:22px}.points p{margin:0;max-width:68ch}
.policies{margin-top:32px;background:var(--sheet);border:1px solid var(--line);padding:20px}.policies .plan{margin:0 0 12px;color:var(--muted);font-size:15px;max-width:68ch}
.policies ul{list-style:none;margin:0;padding:0;display:grid;gap:12px}.policies li{display:grid;gap:2px;border-top:1px solid var(--line);padding-top:12px}.policies li b{font-weight:600;font-size:15px}.policies li span{font-size:15px;color:var(--muted)}
.reviewed{margin-top:16px;font-size:13px;color:var(--muted)}.reviewed a{color:var(--muted)}
.nearby{display:flex;flex-wrap:wrap;gap:8px;padding:0;margin:0;list-style:none}.nearby li{border:1px solid var(--line);padding:4px 12px;font-size:14px}
figure{margin:0}figcaption{font-size:13px;color:var(--muted);margin-top:8px}
blockquote{margin:22px 0 0;padding-left:16px;border-left:3px solid var(--oak);font-size:17px;max-width:62ch}blockquote cite{display:block;font-style:normal;font-size:13px;color:var(--muted);margin-top:8px}
details{border-top:1px solid var(--line);padding:14px 0}details:last-child{border-bottom:1px solid var(--line)}summary{cursor:pointer;font-weight:600}details p{margin:10px 0 0;max-width:68ch}
footer{background:var(--ink);color:color-mix(in srgb,var(--paper) 72%,transparent);font-size:13px;padding:28px 0 40px}footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px}
@media (max-width:560px){.top .cta{padding:8px 12px;font-size:13px}}
"""


def homepage_header():
    """Logo markup and header CSS copied from index.html, so town pages always match the homepage."""
    import re
    idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    mark = re.search(r'<a class="mark".*?</a>', idx, re.S).group(0).replace('href="#home"', 'href="/"')
    css = "\n".join(l for l in idx.splitlines() if re.match(r'\s*(@media[^{]*\{\s*)?\.(top|mark)\b', l))
    return mark, css


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
    MARK, HEADER_CSS = homepage_header()
    t = a["town"]
    url = f"{SITE}/architectural-design-{a['slug']}/"
    services = "".join(f'<div class="card"><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for n, d in SERVICES)
    points = "".join(f"<div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>" for h, p in a["planning"])
    c = COUNCILS[a["council"]]
    pols = "".join(f'<li><b>{esc(r)}</b><span>{esc(d)}</span></li>' for r, d in c["policies"])
    srcs = c["sources"] + a.get("sources", [])
    srcs_html = " · ".join(f'<a href="{esc(u)}" rel="noopener" target="_blank">{esc(l)}</a>' for l, u in srcs)
    nearby = "".join(f"<li>{esc(n)}</li>" for n in a["nearby"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>" for q, ans in a["faq"])
    others = ", ".join(f'<a href="/architectural-design-{o["slug"]}/">{esc(o["town"])}</a>' for o in AREAS if o is not a)
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
<style>{CSS}
{HEADER_CSS}</style>
<script type="application/ld+json">{schema(a)}</script>
</head>
<body>
<header class="top"><div class="wrap">
{MARK}
<nav class="hnav"><a href="/#services">Services</a><a href="/#work">Work</a><a href="/#about">About</a><a href="/#contact">Contact</a><a class="cta" href="/#book">Book a free call</a></nav>
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
<div class="policies"><h3>Local policies we design to</h3><p class="plan">{esc(c["plan"])}</p><ul>{pols}</ul></div>
<p class="reviewed">Planning information last reviewed {REVIEWED}. Sources: {srcs_html}</p>
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
<footer><div class="wrap"><span><b style="color:var(--paper);font-weight:600">Forty-One Architecture</b> · Part of the Forty-One Group · Whitstable, Kent · {PHONE}</span><span>A trading name of Forty-One Consult and Design Ltd · Company no. 16366675 · <a href="/privacy.html">Privacy notice</a></span></div></footer>
</body>
</html>
"""


def update_homepage_links():
    import re
    p = os.path.join(ROOT, "index.html")
    h = open(p, encoding="utf-8").read()
    links = [f'<a href="/architectural-design-{a["slug"]}/">{a["town"]}</a>' for a in AREAS]
    h = re.sub(r"<span>Areas: .*?</span>", "<span>Areas: " + " · ".join(links) + "</span>", h, count=1, flags=re.S)
    h = re.sub(r"work across Kent and London, including .*?\. If you", "work across Kent and London, including " + ", ".join(links[:-1]) + " and " + links[-1] + ". If you", h, count=1, flags=re.S)
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h)
    d = json.loads(m.group(1))
    d["areaServed"] = [{"@type": "AdministrativeArea", "name": n} for n in ["Kent", "London"] + [a["town"] for a in AREAS]]
    h = h.replace(m.group(1), json.dumps(d))
    open(p, "w", encoding="utf-8").write(h)


def main():
    update_homepage_links()
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
