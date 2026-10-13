#!/usr/bin/env python3
"""Builds gallery.html: ten email-signature concepts, each an email-safe table with a Copy button."""
import base64, pathlib

here = pathlib.Path(__file__).parent
FLAME = "data:image/png;base64," + base64.b64encode((here / "maester-logo.png").read_bytes()).decode()
JMARK = "data:image/png;base64," + base64.b64encode((here / "jozra-mark.png").read_bytes()).decode()

SANS = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'Geist Mono', Menlo, Consolas, 'Courier New', monospace"
SERIF = "Georgia, 'Times New Roman', serif"
DISPLAY = "Archivo, Inter, 'Segoe UI', Helvetica, Arial, sans-serif"

INK, MUTED, FAINT, LINE = "#18181b", "#71717a", "#a1a1aa", "#e4e4e7"
RED, BRAND = "#d22c31", "#111113"
JPAPER, JINK, JORANGE, JLINE, JMUTED = "#f6f3ec", "#16140f", "#d8420b", "#d9d3c4", "#6b655a"

MC = "https://maester.cloud/?utm_source=email&utm_medium=signature"
MCBLOG = "https://maester.cloud/blog/?utm_source=email&utm_medium=signature"
MANIFESTO = "https://maester.cloud/manifesto?utm_source=email&utm_medium=signature"
MD = "https://maester.dev"
JZ = "https://jozra.com"
EN = "https://entra.news"
MN = "https://merill.net"
LI = "https://linkedin.com/in/merill"


def a(href, text, color=INK, weight="normal", extra=""):
    return f'<a href="{href}" style="color:{color};font-weight:{weight};text-decoration:none;{extra}">{text}</a>'


def table(inner, width=None, extra=""):
    w = f' width="{width}"' if width else ""
    return f'<table cellpadding="0" cellspacing="0" border="0"{w} style="border-collapse:collapse;{extra}">{inner}</table>'


def hairline(color=LINE, pad="12px 0 0 0"):
    return (f'<tr><td style="padding:{pad};">{table(f"<tr><td height=\"1\" style=\"height:1px;line-height:1px;font-size:1px;background-color:{color};\">&nbsp;</td></tr>", width="100%")}</td></tr>')


def links(items, color=MUTED, size=12, sep="&nbsp;&nbsp;&middot;&nbsp;&nbsp;", font=SANS):
    body = sep.join(a(h, t, color) for h, t in items)
    return f'<div style="font-family:{font};font-size:{size}px;line-height:18px;color:{color};">{body}</div>'


designs = []

# 1 Quiet: plain text, no image.
designs.append(("Quiet", "Plain text, no image, nothing to download. For people who think signatures should get out of the way.", table(f"""
<tr><td style="font-family:{SANS};font-size:14px;line-height:21px;color:{INK};">
  <div style="font-weight:600;">Merill Fernando</div>
  <div style="color:{MUTED};">Founder, Jozra. Creator of Maester.</div>
  <div style="padding-top:10px;">{a(MC, "Maester Cloud", INK, 600)}<span style="color:{MUTED};">: the evidence layer for Microsoft 365 security.</span></div>
  <div style="padding-top:10px;">{links([(JZ, "jozra.com"), (EN, "entra.news"), (LI, "LinkedIn")], size=13)}</div>
</td></tr>""")))

# 2 Flame and hairline: logo, vertical rule, stacked text.
designs.append(("Flame and hairline", "The classic layout, done quietly. Mark on the left, a single vertical rule, and Maester Cloud as a sentence rather than a button.", table(f"""
<tr>
  <td valign="top" style="padding:2px 16px 0 0;"><a href="{MC}"><img src="{FLAME}" width="40" height="40" alt="Maester" style="display:block;border:0;width:40px;height:40px;"></a></td>
  <td style="border-left:1px solid {LINE};padding:0 0 0 16px;font-family:{SANS};font-size:14px;line-height:21px;color:{INK};">
    <div style="font-weight:600;">Merill Fernando</div>
    <div style="font-size:13px;color:{MUTED};">Founder, Jozra &middot; Creator of Maester</div>
    <div style="padding-top:10px;">{a(MC, "Maester Cloud", INK, 600)} <span style="color:{MUTED};">Know what changed in your Microsoft 365 security posture.</span> {a(MC, "&rarr;", RED, 600)}</div>
    <div style="padding-top:10px;">{links([(JZ, "jozra.com"), (EN, "entra.news"), (MN, "merill.net"), (LI, "LinkedIn")])}</div>
  </td>
</tr>""")))

# 3 Manifesto: a quoted line leads.
designs.append(("Manifesto", "Leads with the idea instead of the product. The product follows as the proof.", table(f"""
<tr><td style="font-family:{SERIF};font-size:16px;line-height:24px;color:{INK};font-style:italic;border-left:2px solid {RED};padding:2px 0 2px 14px;">
  Security guidance should not only be written down.<br>It should be executable.
</td></tr>
<tr><td style="padding:14px 0 0 0;font-family:{SANS};font-size:14px;line-height:21px;color:{INK};">
  <div style="font-weight:600;">Merill Fernando</div>
  <div style="font-size:13px;color:{MUTED};">Founder, Jozra &middot; Creator of Maester &middot; {a(MANIFESTO, "Read the manifesto", MUTED)}</div>
  <div style="padding-top:10px;">{a(MC, "Maester Cloud &rarr;", INK, 600)} <span style="color:{MUTED};">the evidence layer for Microsoft 365 security</span></div>
  <div style="padding-top:10px;">{links([(JZ, "jozra.com"), (EN, "entra.news"), (LI, "LinkedIn")])}</div>
</td></tr>""")))

# 4 Pill: one pill-shaped CTA in brand black.
designs.append(("Pill", "One call to action, pill shaped, in Maester Cloud's near-black rather than red. The flame is the only colour.", table(f"""
<tr>
  <td valign="middle" style="padding:0 12px 0 0;"><img src="{FLAME}" width="44" height="44" alt="Maester" style="display:block;border:0;width:44px;height:44px;"></td>
  <td valign="middle" style="font-family:{SANS};font-size:14px;line-height:20px;color:{INK};">
    <div style="font-size:16px;font-weight:600;">Merill Fernando</div>
    <div style="font-size:13px;color:{MUTED};">Founder, Jozra &middot; Creator of Maester</div>
  </td>
</tr>
<tr><td colspan="2" style="padding:14px 0 0 0;font-family:{SANS};font-size:14px;line-height:21px;color:{INK};">
  Maester Cloud keeps years of your Microsoft 365 security evidence and tells you the moment it drifts.
</td></tr>
<tr><td colspan="2" style="padding:12px 0 0 0;">
  {table(f'''<tr>
    <td style="background-color:{BRAND};border-radius:999px;padding:8px 18px;">{a(MC, "See Maester Cloud", "#ffffff", 600, f"font-family:{SANS};font-size:13px;line-height:18px;")}</td>
    <td style="padding:0 0 0 16px;">{links([(JZ, "jozra.com"), (EN, "entra.news"), (LI, "LinkedIn")], size=13)}</td>
  </tr>''')}
</td></tr>""")))

# 5 Terminal: security as code, mono aligned list.
designs.append(("Terminal", "Security as code. A monospace index of what you make, with Maester Cloud first. Reads as a practitioner, not a marketer.", table(f"""
<tr><td style="font-family:{SANS};font-size:14px;line-height:21px;color:{INK};">
  <div style="font-weight:600;">Merill Fernando</div>
  <div style="font-size:13px;color:{MUTED};">Founder, Jozra &middot; Creator of Maester</div>
</td></tr>
<tr><td style="padding:12px 0 0 0;">
  {table(f'''
  <tr><td style="font-family:{MONO};font-size:12px;line-height:20px;color:{RED};padding:0 16px 0 0;">&#9656; {a(MC, "maester.cloud", INK, 600, f"font-family:{MONO};")}</td><td style="font-family:{MONO};font-size:12px;line-height:20px;color:{INK};">The evidence layer for Microsoft 365 security</td></tr>
  <tr><td style="font-family:{MONO};font-size:12px;line-height:20px;color:{FAINT};padding:0 16px 0 0;">&nbsp;&nbsp;{a(MD, "maester.dev", MUTED, extra=f"font-family:{MONO};")}</td><td style="font-family:{MONO};font-size:12px;line-height:20px;color:{MUTED};">Open-source security tests, free forever</td></tr>
  <tr><td style="font-family:{MONO};font-size:12px;line-height:20px;color:{FAINT};padding:0 16px 0 0;">&nbsp;&nbsp;{a(EN, "entra.news", MUTED, extra=f"font-family:{MONO};")}</td><td style="font-family:{MONO};font-size:12px;line-height:20px;color:{MUTED};">Weekly Microsoft Entra newsletter</td></tr>
  <tr><td style="font-family:{MONO};font-size:12px;line-height:20px;color:{FAINT};padding:0 16px 0 0;">&nbsp;&nbsp;{a(JZ, "jozra.com", MUTED, extra=f"font-family:{MONO};")}</td><td style="font-family:{MONO};font-size:12px;line-height:20px;color:{MUTED};">The company behind them</td></tr>
  ''')}
</td></tr>""")))

# 6 Dark card: the Maester Cloud hero, in miniature.
designs.append(("Dark card", "Maester Cloud's dark hero in miniature. Stands out in a thread of white emails, and the flame reads best on dark.", table(f"""
<tr><td style="background-color:{INK};border-radius:12px;padding:18px 20px;">
  {table(f'''
  <tr>
    <td valign="middle" style="padding:0 14px 0 0;"><a href="{MC}"><img src="{FLAME}" width="40" height="40" alt="Maester" style="display:block;border:0;width:40px;height:40px;"></a></td>
    <td valign="middle" style="font-family:{SANS};font-size:14px;line-height:20px;color:#ffffff;">
      <div style="font-size:16px;font-weight:600;">Merill Fernando</div>
      <div style="font-size:13px;color:{FAINT};">Founder, Jozra &middot; Creator of Maester</div>
    </td>
  </tr>
  <tr><td colspan="2" style="padding:14px 0 0 0;font-family:{SANS};font-size:14px;line-height:21px;color:#ffffff;">
    {a(MC, "Maester Cloud", "#ffffff", 600)} <span style="color:{FAINT};">The evidence layer for Microsoft 365 security.</span> {a(MC, "&rarr;", "#f87171", 600)}
  </td></tr>
  <tr><td colspan="2" style="padding:12px 0 0 0;">{links([(JZ, "jozra.com"), (EN, "entra.news"), (MN, "merill.net"), (LI, "LinkedIn")], color=FAINT)}</td></tr>
  ''')}
</td></tr>""", width="520")))

# 7 Two columns: you on the left, the product on the right.
designs.append(("Two columns", "You on the left, Maester Cloud on the right as its own small card. Keeps the person and the product from competing.", table(f"""
<tr>
  <td valign="top" style="padding:0 24px 0 0;font-family:{SANS};font-size:14px;line-height:21px;color:{INK};">
    <div style="font-size:16px;font-weight:600;">Merill Fernando</div>
    <div style="font-size:13px;color:{MUTED};">Founder, Jozra</div>
    <div style="font-size:13px;color:{MUTED};">Creator of Maester</div>
    <div style="padding-top:10px;">{links([(JZ, "jozra.com")], size=13)}</div>
    <div>{links([(EN, "entra.news")], size=13)}</div>
    <div>{links([(LI, "LinkedIn")], size=13)}</div>
  </td>
  <td valign="top" style="border-left:1px solid {LINE};padding:0 0 0 24px;">
    {table(f'''
    <tr><td valign="middle" style="padding:0 10px 0 0;"><img src="{FLAME}" width="32" height="32" alt="" style="display:block;border:0;width:32px;height:32px;"></td>
        <td valign="middle" style="font-family:{SANS};font-size:14px;line-height:20px;color:{INK};font-weight:600;">Maester Cloud</td></tr>
    <tr><td colspan="2" style="padding:8px 0 0 0;font-family:{SANS};font-size:13px;line-height:19px;color:{MUTED};max-width:240px;">Know what changed in your Microsoft 365 security posture. Years of history, drift between runs, alerts when it moves.</td></tr>
    <tr><td colspan="2" style="padding:8px 0 0 0;">{a(MC, "maester.cloud &rarr;", RED, 600, f"font-family:{SANS};font-size:13px;")}</td></tr>
    ''')}
  </td>
</tr>""")))

# 8 Jozra paper: company-first, warm palette.
designs.append(("Jozra paper", "Company first, in Jozra's warm paper and orange. Maester Cloud is the lead product rather than the whole identity.", table(f"""
<tr><td style="background-color:{JPAPER};border-radius:10px;padding:18px 20px;">
  {table(f'''
  <tr>
    <td valign="middle" style="padding:0 12px 0 0;"><a href="{JZ}"><img src="{JMARK}" width="36" height="36" alt="Jozra" style="display:block;border:0;width:36px;height:36px;border-radius:6px;"></a></td>
    <td valign="middle" style="font-family:{DISPLAY};font-size:15px;line-height:20px;color:{JINK};">
      <div style="font-weight:700;letter-spacing:-0.01em;">Merill Fernando</div>
      <div style="font-family:{SANS};font-size:13px;color:{JMUTED};">Founder, {a(JZ, "Jozra", JMUTED)} &middot; Tools for the people who keep Microsoft 365 secure</div>
    </td>
  </tr>
  <tr><td colspan="2" style="padding:14px 0 0 0;">{table(f"<tr><td height=\"1\" style=\"height:1px;line-height:1px;font-size:1px;background-color:{JLINE};\">&nbsp;</td></tr>", width="100%")}</td></tr>
  <tr><td colspan="2" style="padding:12px 0 0 0;font-family:{SANS};font-size:13px;line-height:20px;color:{JINK};">
    <div><span style="color:{JORANGE};font-weight:700;">01</span>&nbsp;&nbsp;{a(MC, "Maester Cloud", JINK, 600)} <span style="color:{JMUTED};">The evidence layer for Microsoft 365 security</span> {a(MC, "&rarr;", JORANGE, 700)}</div>
    <div><span style="color:{JMUTED};">02</span>&nbsp;&nbsp;{a(MD, "Maester", JINK)} <span style="color:{JMUTED};">Open-source security tests for Microsoft 365</span></div>
    <div><span style="color:{JMUTED};">03</span>&nbsp;&nbsp;{a(EN, "Entra.News", JINK)} <span style="color:{JMUTED};">Weekly, read by 19,000 Microsoft admins</span></div>
  </td></tr>
  ''')}
</td></tr>""", width="540")))

# 9 Badges: shadcn-style chips.
chip_filled = f"display:inline-block;background-color:{BRAND};color:#ffffff;border-radius:999px;padding:4px 12px;font-family:{SANS};font-size:12px;line-height:16px;font-weight:600;text-decoration:none;"
chip_outline = f"display:inline-block;border:1px solid {LINE};color:{INK};border-radius:999px;padding:3px 11px;font-family:{SANS};font-size:12px;line-height:16px;font-weight:500;text-decoration:none;"
designs.append(("Badges", "shadcn badges as the link row. Maester Cloud is the only filled chip, so the hierarchy is obvious without a button.", table(f"""
<tr>
  <td valign="middle" style="padding:0 12px 0 0;"><img src="{FLAME}" width="40" height="40" alt="Maester" style="display:block;border:0;width:40px;height:40px;"></td>
  <td valign="middle" style="font-family:{SANS};font-size:14px;line-height:20px;color:{INK};">
    <div style="font-size:16px;font-weight:600;">Merill Fernando</div>
    <div style="font-size:13px;color:{MUTED};">Founder, Jozra &middot; Creator of Maester</div>
  </td>
</tr>
<tr><td colspan="2" style="padding:12px 0 0 0;font-family:{SANS};font-size:13px;line-height:20px;color:{MUTED};">
  Making security testing open, reusable, and available to everyone.
</td></tr>
<tr><td colspan="2" style="padding:10px 0 0 0;">
  {table(f'''<tr>
    <td style="padding:0 6px 6px 0;"><a href="{MC}" style="{chip_filled}">Maester Cloud</a></td>
    <td style="padding:0 6px 6px 0;"><a href="{MD}" style="{chip_outline}">Maester</a></td>
    <td style="padding:0 6px 6px 0;"><a href="{EN}" style="{chip_outline}">Entra.News</a></td>
    <td style="padding:0 6px 6px 0;"><a href="{JZ}" style="{chip_outline}">Jozra</a></td>
    <td style="padding:0 6px 6px 0;"><a href="{LI}" style="{chip_outline}">LinkedIn</a></td>
  </tr>''')}
</td></tr>""")))

# 10 Editorial: the mission as a headline.
designs.append(("Editorial", "The mission as a serif headline, with you as the byline. Feels like a masthead, not a business card.", table(f"""
<tr><td style="font-family:{SERIF};font-size:19px;line-height:26px;color:{INK};letter-spacing:-0.01em;">
  Make security testing open, reusable,<br>and available to everyone.
</td></tr>
<tr><td style="padding:10px 0 0 0;font-family:{SANS};font-size:11px;line-height:16px;letter-spacing:0.08em;text-transform:uppercase;color:{MUTED};">
  Merill Fernando &nbsp;&middot;&nbsp; Founder, Jozra &nbsp;&middot;&nbsp; Creator of Maester
</td></tr>
{hairline(pad="14px 0 0 0")}
<tr><td style="padding:12px 0 0 0;font-family:{SANS};font-size:14px;line-height:21px;color:{INK};">
  Building {a(MC, "Maester Cloud", INK, 600)}, the evidence layer for Microsoft 365 security. {a(MC, "&rarr;", RED, 600)}
</td></tr>
<tr><td style="padding:10px 0 0 0;">{links([(JZ, "jozra.com"), (EN, "entra.news"), (MN, "merill.net"), (LI, "LinkedIn")])}</td></tr>""", width="520")))


cards = []
for i, (name, note, html) in enumerate(designs, 1):
    cards.append(f"""
<section class="card" id="d{i}">
  <header>
    <div><span class="num">{i:02d}</span><h2>{name}</h2></div>
    <button data-target="sig{i}">Copy</button>
  </header>
  <p class="note">{note}</p>
  <div class="mail">
    <p class="body">Thanks, talk soon.</p>
    <div class="sig" id="sig{i}">{html}</div>
  </div>
</section>""")

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Signature concepts</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Geist+Mono:wght@400;500&family=Archivo:wght@600;700&display=swap" rel="stylesheet">
<style>
  :root {{ --ink:{INK}; --muted:{MUTED}; --line:{LINE}; --bg:#f4f4f5; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; padding:40px 16px 80px; background:var(--bg); color:var(--ink); font-family:{SANS}; -webkit-font-smoothing:antialiased; }}
  .wrap {{ max-width:720px; margin:0 auto; }}
  h1 {{ font-size:22px; font-weight:600; margin:0 0 6px; letter-spacing:-0.01em; }}
  .lede {{ color:var(--muted); font-size:14px; line-height:21px; margin:0 0 32px; }}
  .card {{ margin:0 0 36px; }}
  .card header {{ display:flex; align-items:center; justify-content:space-between; margin:0 0 4px; }}
  .card header div {{ display:flex; align-items:baseline; gap:10px; }}
  .num {{ font-family:{MONO}; font-size:12px; color:var(--muted); }}
  h2 {{ font-size:15px; font-weight:600; margin:0; }}
  .note {{ color:var(--muted); font-size:13px; line-height:19px; margin:0 0 12px; max-width:560px; }}
  button {{ font:inherit; font-size:13px; font-weight:500; padding:6px 14px; border:1px solid var(--line); border-radius:999px; background:#fff; color:var(--ink); cursor:pointer; }}
  button:hover {{ background:#fafafa; }}
  button.done {{ background:var(--ink); color:#fff; border-color:var(--ink); }}
  .mail {{ background:#fff; border:1px solid var(--line); border-radius:12px; padding:24px 28px 28px; }}
  .body {{ font-size:14px; line-height:21px; color:#444; margin:0 0 22px; }}
  .how {{ margin-top:48px; padding-top:24px; border-top:1px solid var(--line); color:var(--muted); font-size:13px; line-height:20px; }}
  .how ol {{ padding-left:20px; margin:8px 0 0; }}
</style></head><body><div class="wrap">
<h1>Signature concepts</h1>
<p class="lede">Ten directions, each a working, email-safe signature. Previews use Inter and Geist Mono; recipients without those fonts see Segoe UI or Helvetica. Rounded corners show everywhere except classic Outlook for Windows, which squares them.</p>
{''.join(cards)}
<div class="how">
  To use one:
  <ol>
    <li>Click <b>Copy</b> on the design you want.</li>
    <li>Outlook &rarr; Settings &rarr; Accounts &rarr; Signatures &rarr; New signature.</li>
    <li>Paste, name it, and set it as the default for the jozra.com account. Send yourself a test.</li>
  </ol>
</div>
</div>
<script>
document.querySelectorAll('button[data-target]').forEach(function (b) {{
  b.onclick = function () {{
    var r = document.createRange(); r.selectNodeContents(document.getElementById(b.dataset.target));
    var s = getSelection(); s.removeAllRanges(); s.addRange(r);
    document.execCommand('copy'); s.removeAllRanges();
    b.textContent = 'Copied'; b.classList.add('done');
    setTimeout(function () {{ b.textContent = 'Copy'; b.classList.remove('done'); }}, 1800);
  }};
}});
</script>
</body></html>"""

(here / "gallery.html").write_text(page)
print("wrote gallery.html", len(page), "bytes")
