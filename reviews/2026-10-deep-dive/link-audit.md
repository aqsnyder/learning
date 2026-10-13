# Link Audit: Pre-existing Links (October 2026)

This audit covers every external link that was in the repo **before** the October 2026 review and survived it: 704 links in total.

| Batch | Links | How they were checked | Result |
|---|---|---|---|
| arXiv | 116 | `arxiv.org/abs/<id>` against title and authors | 8 citation mismatches, all fixed ([details](link-audit-arxiv.md)) |
| GitHub | 33 | Fetched from Aaron's machine (github.com is reachable there) | 32 ok. `aqsnyder/KiCAD_Template_Snyder` returns 404 to an anonymous request: private or renamed. **Aaron to confirm**; pcb notes it as a private repo. |
| Everything else | 555 | Three paced auditors, 2026-10-13. DOIs were checked through Crossref (DataCite as fallback), YouTube through oEmbed, and all other pages by fetching them. | ok 440 · moved 16 · mismatch 21 · broken 18 · unverifiable 60 |

Every link added during the review was opened when it was added, so it is not part of this audit.

**Outcome for the 115 non-ok links:**
- **55 fixed:** a moved link was updated, a dead link replaced by a verified equivalent, or the citation text corrected.
- **3 dead:** no equivalent replacement could be found. They were marked dead at first; the final pass removed two of them and replaced the third with the course author's book.
- **57 unchanged:** the page could not be checked. Robots rules, JavaScript-only pages, HTTP 429 rate limits and publisher bot walls are the usual reasons. For most, nothing suggests the resource is gone. Four look likely dead and should be checked by hand first:
  - L1-141, the Quanta philosophy tag page (it failed twice while the Quanta homepage loaded)
  - L2-125, OXT.me (possibly discontinued)
  - L2-008, Arduino's boards page (it now redirects to a page of retired boards)
  - L3-078, MacKay's book PDF (the whole host refused the fetcher)

Per-file details of each fix are in each curriculum's review file, under "Link-audit fixes (2026-10-13)".

## Fixed (55)

| Key | Where | Status | Auditor's finding | Now |
|---|---|---|---|---|
| L1-006 | econ/11-ai-alignment-economics-and-frontiers, econ/courses | moved | aisafetyfundamentals.com 302-redirects to the BlueDot Impact homepage; the landing page does not mention the 'AI Safety Fundamentals' name and the… | Link replaced |
| L1-009 | bio/06-computational-chemistry-and-drug-discovery | mismatch | URL resolves and is the right resource, but the citation metadata is off: the page names no 'Trott & Olson' as authors of these docs and shows… | Citation text corrected; URL kept |
| L1-019 | bio/02-genetics-and-genomics | unverifiable | WebFetch returned CLIENT_ERROR on both attempts (4xx; cannot tell 404/removed from bot-block), so the Broad Institute GWAS explainer could not be… | Replaced after a later check |
| L1-027 | econ/07-network-economics, econ/courses | broken | Listed slug social-and-economic-networks returned a 4xx (WebFetch CLIENT_ERROR) while other Coursera course pages in this batch loaded fine; the… | Link replaced |
| L1-029 | econ/08-computational-economics | moved | princeton.edu/~arora/pubs/MWsurvey.pdf no longer serves the PDF (302 to author's new homepage); the paper is open access at Theory of Computing (PDF… | Link replaced |
| L1-057 | bio/11-frontiers | mismatch | Author list in context is slightly wrong: the Science paper's first four authors are Nguyen, Poli, Durrant, Kang; 'Thomas' (Armin W. Thomas) is 8th… | Citation text corrected; URL kept |
| L1-076 | bio/03-structural-biology | broken | ibiology.org/structural-biology/ returned a 4xx (WebFetch CLIENT_ERROR); the live iBiology homepage menu/footer has no Structural Biology category… | Link replaced |
| L1-102 | bio/09-neuroscience | moved | mhprofessional.com URL 302-redirects to the generic McGraw Hill higher-ed page (https://www.mheducation.com/highered.html), not the book; the book… | Link replaced |
| L1-128 | bio/02-genetics-and-genomics | mismatch | URL now serves a different book: product id P200000006876 returns Biology: The Core (3rd ed., Eric J. Simon, Pearson 2019/2020) although the slug… | Link replaced |
| L1-142 | bio/03-structural-biology | broken | www.rcsb.org/training returned a 4xx (WebFetch CLIENT_ERROR) while the RCSB homepage loads fine; training now lives on PDB-101: the homepage links… | Link replaced |
| L1-149 | math/04-optimization, math/courses | broken | The listed lowercase path see.stanford.edu/course/ee364a returned a 4xx (WebFetch CLIENT_ERROR); the SEE site serves the course at the capitalized… | Link replaced |
| L1-159 | econ/08-computational-economics | mismatch | URL resolves and is CS364B, but the course title in the context is wrong: CS364B is titled 'Frontiers in Mechanism Design', not 'Algorithmic Game… | Citation text corrected; URL kept |
| L1-176 | bio/courses | broken | Most likely deleted or private, but not certain. Evidence: (1) YouTube oEmbed for playlist PLnNiWLiUs3PSJqm-aFLCmaYe-Q89_ycWm returned a 4xx… | Link replaced |
| L2-010 | bio/08-genomic-medicine | moved | basicbooks.com now 302-redirects to hachettebookgroup.com (Basic Books pages moved). Title/author/year in context are correct. | Link replaced |
| L2-012 | bio/01-biochemistry | mismatch | URL resolves but is a generic, large resource search listing, not an identifiable 'Enzyme Catalysis & Protein Structure' collection; the claimed… | Link replaced |
| L2-016 | btc/06-network-and-p2p | broken | The live map of reachable Bitcoin nodes is not currently served; site shows only a holding/announcement page. Context description ('Live map of… | Link replaced |
| L2-030 | bio/04-bioinformatics-and-sequence-analysis | moved | Soft-404: the old session/cart-style default.tpl URL resolves but shows the CSHL Press homepage, not the Mount book. The book's current product page… | Link replaced |
| L2-049 | bio/07-protein-engineering-and-design | mismatch | MINOR: DOI/title/year are right, but the truncated author list '..., Fraser, J. S.' ends on the wrong name - James S. Fraser is the 11th of 12… | Citation text corrected; URL kept |
| L2-052 | philosophy/09-free-will-and-agency | mismatch | MINOR: DOI, title and year are right, but the paper has four authors; the context credits only 'Benjamin Libet' (should be Libet et al.). Title in… | Citation text corrected; URL kept |
| L2-062 | bio/00-molecular-biology-fundamentals, bio/courses | broken | Soft-404 on a KEY item (bio/00 and bio/courses #1): the MITx 7.00x 'Introduction to Biology - The Secret of Life' (Eric Lander) page no longer exists… | Link replaced |
| L2-067 | bio/03-structural-biology | moved | garlandscience.com now 302-redirects to the Routledge homepage (https://www.routledge.com/), not to the book; the book's current product page is on… | Link replaced |
| L2-073 | math/10-causal-inference | mismatch | Resolves (no 404/redirect) but the served content is the old 2015 draft-book page, not the 'What If' (2020) edition the context cites, and no… | Link replaced |
| L2-083 | econ/07-network-economics | unverifiable | Could not confirm that JSTOR stable/1816044 is Katz & Shapiro, 'Network Externalities, Competition, and Compatibility' (AER 75(3):424-440, 1985).… | Replaced after a later check |
| L2-102 | econ/10-monetary-economics-and-crypto | mismatch | MINOR: link works, but it is the 1990 'Argument Refined' (3rd) edition, while the context says 1976 (the original IEA Hobart Paper date) and spells… | Citation text corrected; URL kept |
| L2-112 | ml/06-transformers-and-attention | mismatch | MINOR: link works and is the right resource, but the linked page is the 2022 rewrite (v2022, new authors credited) whereas the context says 'Harvard… | Citation text corrected; URL kept |
| L2-136 | bio/09-neuroscience | moved | portal.brain-map.org now 302-redirects to https://brain-map.org/; the content matches the context description. | Link replaced |
| L2-138 | math/03-probability-and-statistics | moved | The old projects.iq.harvard.edu URL could not be fetched (WebFetch ROBOTS_DISALLOWED), so its current behavior is unconfirmed; the Stat 110 site is… | Link replaced |
| L2-145 | pcb/02-schematic-capture, pcb/blogs-and-references | moved | samacsys.com now 302-redirects to https://supplyframe.com/samacsys (SamacSys is now part of Supplyframe). Content still matches 'Free component… | Link replaced |
| L2-152 | math/03-probability-and-statistics, math/books | moved | Old www.stat.columbia.edu/~gelman/book/ now 302-redirects to https://sites.stat.columbia.edu/gelman/book/ (Columbia Statistics moved its personal… | Link replaced |
| L2-164 | math/04-optimization | moved | The repo path web.stanford.edu/~jduchi/PCMIConvex.pdf returned a target-side CLIENT_ERROR (probably removed/moved; Duchi's homepage loads but does… | Link replaced |
| L2-168 | ml/03-neural-network-fundamentals, ml/courses | broken | Probable dead handle (error text gives no explicit status). Replace with the verified official channel (fix_url); the course site… | Link replaced |
| L2-180 | bio/courses | unverifiable | rate-limited: the oEmbed lookup returned CLIENT_ERROR (4xx - can mean video deleted/private, or simply embedding disabled), and the follow-up fetch… | Replaced after a later check |
| L3-001 | philosophy/blogs-and-references | broken | Old priority-path topic page is gone after 80,000 Hours reorganised its topic archive. Closest verified replacement for 'career-oriented resource on… | Link replaced |
| L3-005 | ml/11-frontiers, ml/blogs-and-references | moved | 302 redirect: the AI Index now lives on the Stanford HAI site; old aiindex.stanford.edu/report/ no longer serves the report page itself | Link replaced |
| L3-012 | bio/blogs-and-references | mismatch | Site resolves, but its name is 'PLOS Biologue' (blog for three PLOS journals), not 'PLOS Biology Community'; the label in the repo is not the site's… | Citation text corrected; URL kept |
| L3-016 | bio/04-bioinformatics-and-sequence-analysis | mismatch | Link goes to the BLAST search home page, not to 'Tutorials and Documentation'; the help/docs live at /doc/blast-help/ ('Welcome to BLAST Help', with… | Citation text corrected; URL kept |
| L3-017 | econ/02-game-theory, econ/books | broken | The /coursesingt path returns a client error (likely 404; WebFetch does not expose the code) while the site root… | Link replaced |
| L3-018 | bio/02-genetics-and-genomics | broken | Dead link; also the title 'A Brief Guide to Genomics' is an NHGRI (genome.gov) fact sheet, not a Broad Institute page. NHGRI page confirmed live… | Link replaced |
| L3-027 | bio/courses | broken | Specialization URL does not load; likely retired or renamed. No replacement verified | Link replaced |
| L3-029 | math/06-graph-theory-and-combinatorics, math/courses | mismatch | Repo labels it a 'Yale course on spectral graph theory'; the page is the FOCS 2007 tutorial companion page, not a course. A real course page exists… | Link replaced |
| L3-031 | pcb/11-reference-projects | moved | 302 redirect from datasheets.raspberrypi.com to pip.raspberrypi.com (Product Information Portal). Portal home does not itself mention 'reference… | Link replaced |
| L3-044 | bio/08-genomic-medicine | mismatch | Citation (title, first authors, year) is correct, but the repo description is wrong: the paper is about the 'missing heritability' problem (why… | Citation text corrected; URL kept |
| L3-062 | econ/04-mechanism-design | moved | 302 redirect from www.elsevier.com/books/... to shop.elsevier.com/books/...; author/year in repo are correct | Link replaced |
| L3-075 | bio/00-molecular-biology-fundamentals | mismatch | URL no longer lands on a cell-biology video collection; it serves one talk by Janet Iwasa (no Ron Vale). The real topic collection is the Cell… | Link replaced |
| L3-082 | philosophy/blogs-and-references | moved | 302 redirect: the journal moved from University of Chicago Press to Cambridge Core; old /toc/phos/current no longer serves it | Link replaced |
| L3-086 | econ/07-network-economics | mismatch | The JSTOR ID 3590984 is the wrong paper, not Rochet & Tirole. Rochet & Tirole's 'Platform Competition in Two-Sided Markets' (JEEA 1(4):990-1029, Jun… | Link replaced |
| L3-091 | btc/10-development-and-programming, btc/courses | mismatch | Link goes to the Saylor site home page, not to the CS120: Bitcoin for Developers I course the row names; the specific course page was not found (no… | Link replaced |
| L3-097 | bio/01-biochemistry | mismatch | Link, title, edition and year are right, but the author list is incomplete: the 8th edition adds Aaron Hoskins as a third author | Citation text corrected; URL kept |
| L3-104 | econ/00-economic-thinking, econ/courses | moved | 302 redirect from mru.org/principles-economics-microeconomics to learn.mru.org/courses/principles-of-microeconomics | Link replaced |
| L3-127 | bio/06-computational-chemistry-and-drug-discovery | mismatch | Pearson link no longer shows Leach's book (product ID now points at an unrelated title). The repo citation (Leach, A. R., 2001, 2nd ed., Prentice… | Link replaced |
| L3-134 | philosophy/08-language-and-meaning | broken | No SEP entry appears to exist at the slug /entries/philosophy-language/. Replacement not found: the SEP search endpoint is robots-disallowed for the… | Link replaced |
| L3-164 | econ/04-mechanism-design | broken | The Stanford-hosted PDF is gone (Milgrom's pages moved to milgrom.net); new location of the paper not found. Repo citation (Ausubel & Milgrom, The… | Link replaced |
| L3-167 | pcb, pcb/06-signal-integrity, pcb/07-emc-and-compliance … | mismatch | Wrong channel. The channel actually titled 'Dr. EMC' is @DrEMC-sf8rx (ID UCS5NRq0KDCZEksZEX4PGcdQ), owned by Anton Tichenko (Principal Electronics… | Link replaced |
| L3-170 | pcb/00-electronics-fundamentals, pcb/courses | broken | Handle @greatscaboratory does not exist. GreatScott!'s channel is @greatscottlab (channel ID UC6mIxFTvXkWQVEHPsEdflzQ, 'Awesome Electronics… | Link replaced |
| L3-176 | ml/06-transformers-and-attention, ml/courses | mismatch | Playlist is the 2023 offering of CS224N, not 2021 as the repo row states; lecturer not named in the visible description (repo says Manning et al.) | Citation text corrected; URL kept |

## Dead, later removed or replaced (3)

Each of these rows was first marked "⚠️ Link dead (checked Oct 2026)". The final pass removed the two retired Coursera courses (econ/03 and econ/06), and replaced Robert Wright's course (philosophy/10) with his book *Why Buddhism Is True*.

| Key | Where | Auditor's finding |
|---|---|---|
| L2-024 | econ/06-behavioral-economics | Probable dead link (not conclusively confirmed): two separate fetches returned a target-side CLIENT_ERROR, while another Coursera course page… |
| L2-026 | econ/03-decision-theory, econ/courses | Probable dead link (not conclusively confirmed): two fetches returned a target-side CLIENT_ERROR while another Coursera course page… |
| L3-026 | philosophy/10-eastern-philosophy-and-mind, philosophy/courses | Course page is gone (soft-404 to a category page). The repo's existing caveat that the course may no longer be offered on Coursera is correct; the… |

## Unchanged: could not be verified (57)

| Key | Where | Why it couldn't be checked |
|---|---|---|
| L1-002 | math/08-abstract-algebra | fetch blocked by robots.txt (ROBOTS_DISALLOWED) for abstract.ups.edu and also for abstract.pugetsound.edu;… |
| L1-020 | bio/00-molecular-biology-fundamentals | WebFetch returned SERVER_ERROR for cambridge.org/core (publisher likely blocks automated fetching); could not… |
| L1-032 | econ/01-microeconomics | WebFetch ROBOTS_DISALLOWED, so resolution and the 1990 edition year could not be confirmed |
| L1-041 | bio/11-frontiers | Could not verify: api.crossref.org/works/10.1016/j.cell.2006.07.024 returned CLIENT_ERROR on both attempts… |
| L1-055 | bio/05-systems-biology | rate-limited: WebFetch proxy rejected the Crossref request with HTTP 429 and said not to re-fetch; page not… |
| L1-070 | bio/03-structural-biology | WebFetch returned CLIENT_ERROR (4xx) on both attempts for global.oup.com; cannot tell removal from… |
| L1-072 | btc/00-history-and-philosophy | WebFetch ROBOTS_DISALLOWED, so resolution of the PDF and its title/date could not be confirmed |
| L1-086 | econ/04-mechanism-design | rate-limited: WebFetch proxy rejected the Crossref request with HTTP 429 and said not to re-fetch; JSTOR… |
| L1-087 | econ/04-mechanism-design | rate-limited: WebFetch proxy rejected the Crossref request with HTTP 429 and said not to re-fetch; JSTOR… |
| L1-090 | bio/courses | Fetcher received only generic SPA metadata, so the AP Biology course content could not be confirmed (a… |
| L1-103 | econ/05-information-economics, econ/books | WebFetch ROBOTS_DISALLOWED, so the page and the 2004 publication year could not be confirmed |
| L1-123 | physics/blogs-and-references | Legacy department URL resolves (no 404) but ends on the JS-rendered OCW search app, so a Physics-specific… |
| L1-141 | philosophy/blogs-and-references | quantamagazine.org/tag/philosophy/ returned CLIENT_ERROR twice while the Quanta homepage (L1-140) fetched… |
| L1-151 | philosophy/blogs-and-references | rate-limited: WebFetch proxy rejected the request with HTTP 429 and said not to re-fetch; the Minds and… |
| L1-165 | btc/00-history-and-philosophy | WebFetch ROBOTS_DISALLOWED, so resolution and title/date of bmoney.txt could not be confirmed |
| L1-179 | pcb/07-emc-and-compliance | Search-query link (the repo labels it Search YouTube), so it resolves by construction and cannot be checked… |
| L2-008 | pcb/11-reference-projects | Legacy arduino.cc/en/Main/Boards no longer serves a current boards/reference-designs page; it redirects to a… |
| L2-014 | btc/blogs-and-references | WebFetch returned SITE_BLOCKED (fetch tool refuses this domain); could not check. Bitcoin Stack Exchange is a… |
| L2-023 | physics/06-computational-physics | Two fetches both failed with CLIENT_ERROR ('error while fetching', target-side) - could be a 404 or bot… |
| L2-072 | ml/02-classical-ml, ml/books | WebFetch returned ROBOTS_DISALLOWED for this host (site's robots.txt blocks fetchers), so the page could not… |
| L2-074 | econ/09-social-choice-and-voting | Both fetches failed with CLIENT_ERROR (target-side; likely bot block or removed legacy URL): the repo's… |
| L2-085 | econ/02-game-theory | rate-limited: WebFetch proxy answered HTTP 429 on the Crossref lookup… |
| L2-088 | btc/01-cryptography-foundations | Page loads without redirect or error indication, but its content is client-rendered so the course title could… |
| L2-089 | math/01-linear-algebra | Page loads without redirect or error indication, but its content is client-rendered so the course title could… |
| L2-090 | bio/00-molecular-biology-fundamentals | Page loads without redirect or error indication, but its content is client-rendered so the unit… |
| L2-110 | ml/12-interpretability-and-alignment | Page content could not be read, so the 'TransformerLens & Mech Interp tutorials' description was not… |
| L2-114 | README.md, bio, btc … | WebFetch returned ROBOTS_DISALLOWED for this host, so the page could not be read. notebooklm.google.com is… |
| L2-125 | btc/blogs-and-references | WebFetch returned ROBOTS_DISALLOWED for this host, so the page could not be read. Manual check advisable:… |
| L2-128 | econ/06-behavioral-economics | Fetch failed with CLIENT_ERROR (target-side; penguinrandomhouse.com typically blocks automated fetchers), so… |
| L2-130 | physics/blogs-and-references | WebFetch returned SITE_BLOCKED (fetch tool refuses stackexchange domains); could not check. Physics Stack… |
| L2-146 | bio/blogs-and-references | Fetch failed with CLIENT_ERROR (target-side; science.org typically blocks automated fetchers), so the blog… |
| L2-147 | philosophy/blogs-and-references | WebFetch returned ROBOTS_DISALLOWED for sciencedirect.com, so the journal page could not be read. 'Artificial… |
| L2-156 | physics/07-quantum-computing | WebFetch returned ROBOTS_DISALLOWED for theory.caltech.edu, so the page could not be read. Citation (John… |
| L2-165 | bio/01-biochemistry | Fetch failed with CLIENT_ERROR (target-side; wiley.com typically blocks automated fetchers, though it could… |
| L2-179 | pcb/08-multi-layer-and-stackup | WebFetch returned ROBOTS_DISALLOWED (YouTube search-results pages are disallowed). The URL is a dynamic… |
| L3-007 | ml/00-historical-foundations | WebFetch refused with ROBOTS_DISALLOWED (site robots.txt blocks the fetcher); title/author could not be… |
| L3-019 | bio/04-bioinformatics-and-sequence-analysis | The page itself returned a server error twice (another Cambridge Core journal page loaded fine, so this may… |
| L3-052 | bio/04-bioinformatics-and-sequence-analysis | Crossref API returned a client error on both attempts (cause unknown; other Crossref lookups in this batch… |
| L3-061 | econ/blogs-and-references | WebFetch returned SITE_BLOCKED (economist.com blocks automated fetching); site is the well-known publication,… |
| L3-074 | physics/blogs-and-references | WebFetch refused with ROBOTS_DISALLOWED (site robots.txt blocks the fetcher); page could not be read |
| L3-078 | math/05-information-theory, math/books | WebFetch got a client error (4xx) for /itprnn/book.pdf, /itprnn/book.html AND the site root… |
| L3-083 | econ/05-information-economics | JSTOR blocks automated fetching, so link resolution unconfirmed; the repo citation (title, Akerlof, 1970)… |
| L3-084 | econ/09-social-choice-and-voting | JSTOR blocks automated fetching, so link resolution unconfirmed; the repo citation (title, Gibbard, 1973)… |
| L3-085 | philosophy/01-philosophy-of-mind | JSTOR blocks automated fetching, so link resolution unconfirmed; the repo citation (title, Nagel, 1974)… |
| L3-095 | bio/06-computational-chemistry-and-drug-discovery | rate-limited |
| L3-099 | math/blogs-and-references | WebFetch returned SITE_BLOCKED (access to the site is blocked for the fetcher); could not be checked.… |
| L3-100 | math/blogs-and-references | WebFetch returned SITE_BLOCKED (access to the site is blocked for the fetcher); could not be checked |
| L3-103 | bio/09-neuroscience, bio/books | WebFetch refused with ROBOTS_DISALLOWED (mitpress.mit.edu robots.txt blocks the fetcher); could not be read |
| L3-106 | ml/13-graphs-geometry-and-science | nature.com returned a server error on both attempts so the page itself was not confirmed; the repo citation… |
| L3-126 | ml/blogs-and-references | Could not confirm either the site's identity or the repo's statement that Papers With Code was sunset in July… |
| L3-146 | physics/08-condensed-matter-and-materials | science.org returned a client error (likely bot block) and the Crossref lookup for DOI… |
| L3-147 | econ/blogs-and-references | WebFetch refused with ROBOTS_DISALLOWED (sciencedirect.com robots.txt blocks the fetcher); journal page could… |
| L3-151 | econ/blogs-and-references | SSRN returned a client error for this path and for the site root https://www.ssrn.com/, so the failure is… |
| L3-165 | bio/05-systems-biology | wiley.com returned a client error (4xx; likely bot-blocking of the publisher site, cannot distinguish from a… |
| L3-166 | econ/09-social-choice-and-voting, econ/books | WebFetch refused with ROBOTS_DISALLOWED (yalebooks.yale.edu robots.txt blocks the fetcher); page could not be… |
| L3-175 | math/08-abstract-algebra | Playlist exists and is on abstract algebra, but the Harvard / Benedict Gross attribution could not be… |
| L3-185 | bio/06-computational-chemistry-and-drug-discovery | Site resolves and belongs to the Irwin and Shoichet labs, but a bot challenge hides the content, so the… |

## Re-running this audit

Run `python tools/check_repo.py --urls` to list every link, then follow step 2 of the [`audit-curriculum`](../../.agents/skills/audit-curriculum/SKILL.md) skill. What made this run reliable:
- Pace page fetches (about one every 10–20 s per agent).
- After an HTTP 429, wait a few minutes and **don't refetch that page in the same run**. Retrying is what exhausted the budget the first time.
- Treat a YouTube oEmbed 4xx as inconclusive. It also happens for live playlists.
- Check the GitHub links from a machine with GitHub access.
