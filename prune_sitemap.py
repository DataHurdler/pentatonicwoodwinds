"""Drop noindex-ed internal pages from the generated sitemap.

Quarto lists every rendered page. The member and internal-document pages carry
<meta name="robots" content="noindex">, so listing them in the sitemap sends
search engines two contradictory signals. Run as a Quarto post-render step.
"""
import io, re

EXCLUDE = ("member.html", "contract2026.html", "rehearsal2026.html")
p = "docs/sitemap.xml"
s = io.open(p, encoding="utf-8").read()
kept = [b for b in re.findall(r"  <url>.*?</url>\n", s, re.S)
        if not any(x in b for x in EXCLUDE)]
head = s[:s.index("  <url>")]
io.open(p, "w", encoding="utf-8", newline="\n").write(head + "".join(kept) + "</urlset>\n")
print("prune_sitemap: %d urls kept" % len(kept))
