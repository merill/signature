#!/usr/bin/env python3
"""Builds admin-news.html (preview + Copy button) and admin-news-fragment.html (the raw signature).

Same Badges design and Outlook rules as build-final.py, with the Admin.News newsletters as the
filled chips and Maester Cloud moved to the outline row. Logos come from admin-news/*.png
(copied from merill/newsletter app/static/brand, saved at 2x) and are embedded as data URIs.
"""
import base64, pathlib

here = pathlib.Path(__file__).parent


def logo(name):
    return "data:image/png;base64," + base64.b64encode((here / "admin-news" / f"{name}.png").read_bytes()).decode()


SANS = "Calibri, Carlito, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
INK, MUTED, LINE, BRAND = "#18181b", "#71717a", "#e4e4e7", "#111113"

UTM = "?utm_source=email&utm_medium=signature"
AN = "https://admin.news/" + UTM
MC = "https://maester.cloud/" + UTM
JZ = "https://jozra.com"
MN = "https://merill.net"
LI = "https://linkedin.com/in/merill"

NAME = "Merill Fernando"
TITLE = "Founder, Jozra &middot; Publisher of Admin.News"
TAGLINE = "Independent weekly newsletters for the Microsoft admin community."

NEWSLETTERS = [
    ("entra", "Entra.News", "https://entra.news/" + UTM),
    ("intune", "Intune News", "https://intune.admin.news/" + UTM),
    ("defender", "Defender News", "https://defender.admin.news/" + UTM),
    ("purview", "Purview News", "https://purview.admin.news/" + UTM),
    ("ad", "AD News", "https://ad.admin.news/" + UTM),
]
NEWSLETTER_ROWS = [NEWSLETTERS[:3], NEWSLETTERS[3:]]


# Filled chip with a logo. As in build-final.py: fill, radius and height live on the cell, bold is a
# <strong>, and the link carries only colour. The icon is its own cell so it never sits inside a text run.
def newsletter_chip(key, text, href):
    cell = f"background-color:{BRAND};border-radius:999px;height:28px;vertical-align:middle;"
    return (f'<td style="padding:0 6px 6px 0;"><table cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">'
            f'<tr><td height="28" valign="middle" bgcolor="{BRAND}" style="{cell}padding:0 12px 0 6px;">'
            f'<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>'
            f'<td width="18" valign="middle" style="width:18px;"><a href="{href}"><img src="{logo(key)}" width="18" height="18" alt="" style="display:block;border:0;width:18px;height:18px;"></a></td>'
            f'<td valign="middle" style="padding:0 0 0 6px;">'
            f'<div style="font-family:{SANS};font-size:14px;line-height:18px;font-weight:700;color:#ffffff;mso-line-height-rule:exactly;white-space:nowrap;">'
            f'<a href="{href}" style="color:#ffffff;text-decoration:none;"><strong style="font-weight:700;">{text}</strong></a></div>'
            f'</td></tr></table></td></tr></table></td>')


def outline_chip(href, text):
    cell = f"background-color:#ffffff;border:1px solid {LINE};border-radius:999px;height:26px;vertical-align:middle;padding:0 11px;"
    return (f'<td style="padding:0 6px 6px 0;"><table cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">'
            f'<tr><td height="26" valign="middle" bgcolor="#ffffff" style="{cell}">'
            f'<div style="font-family:{SANS};font-size:14px;line-height:18px;font-weight:400;color:{INK};mso-line-height-rule:exactly;">'
            f'<a href="{href}" style="color:{INK};text-decoration:none;">{text}</a></div></td></tr></table></td>')


def chip_row(chips):
    return f'<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>{"".join(chips)}</tr></table>'


newsletter_rows = "\n  ".join(chip_row(newsletter_chip(*n) for n in row) for row in NEWSLETTER_ROWS)
outline_row = chip_row([outline_chip(AN, "Admin.News"), outline_chip(MC, "Maester Cloud"),
                        outline_chip(JZ, "Jozra"), outline_chip(MN, "merill.net"), outline_chip(LI, "LinkedIn")])

# Header in its own table and the logo cell exactly the image width, for the reasons in build-final.py.
fragment = f"""<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
<tr><td>
  <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>
    <td width="40" valign="middle" style="width:40px;"><a href="{AN}"><img src="{logo('admin-news')}" width="40" height="40" alt="Admin.News" style="display:block;border:0;width:40px;height:40px;"></a></td>
    <td valign="middle" style="padding:0 0 0 12px;font-family:{SANS};font-size:15px;line-height:21px;color:{INK};">
      <div style="font-size:18px;font-weight:700;">{NAME}</div>
      <div style="font-size:14px;color:{MUTED};">{TITLE}</div>
    </td>
  </tr></table>
</td></tr>
<tr><td style="padding:12px 0 0 0;font-family:{SANS};font-size:14px;line-height:21px;color:{MUTED};max-width:480px;">
  {TAGLINE}
</td></tr>
<tr><td style="padding:10px 0 0 0;">
  {newsletter_rows}
</td></tr>
<tr><td style="padding:2px 0 0 0;">
  {outline_row}
</td></tr>
</table>"""

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin.News signature</title>
<style>
  @font-face {{ font-family:Calibri; font-weight:400; src:local("Calibri"), url("file:///Applications/Microsoft%20Outlook.app/Contents/Resources/DFonts/Calibri.ttf"); }}
  @font-face {{ font-family:Calibri; font-weight:600 700; src:local("Calibri Bold"), local("Calibri-Bold"), url("file:///Applications/Microsoft%20Outlook.app/Contents/Resources/DFonts/Calibrib.ttf"); }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; padding:40px 16px 80px; background:#f4f4f5; color:{INK}; font-family:{SANS}; -webkit-font-smoothing:antialiased; }}
  .wrap {{ max-width:680px; margin:0 auto; }}
  .top {{ display:flex; align-items:center; justify-content:space-between; margin:0 0 12px; }}
  h1 {{ font-size:18px; font-weight:600; margin:0; }}
  button {{ font:inherit; font-size:13px; font-weight:500; padding:6px 14px; border:1px solid {LINE}; border-radius:999px; background:#fff; color:{INK}; cursor:pointer; }}
  button.done {{ background:{INK}; color:#fff; border-color:{INK}; }}
  .mail {{ background:#fff; border:1px solid {LINE}; border-radius:12px; padding:24px 28px 28px; }}
  .body {{ font-size:14px; line-height:21px; color:#444; margin:0 0 22px; }}
  ol {{ color:{MUTED}; font-size:13px; line-height:20px; padding-left:20px; margin:24px 0 0; }}
</style></head><body><div class="wrap">
<div class="top"><h1>Admin.News signature</h1><button id="copy">Copy signature</button></div>
<div class="mail">
  <p class="body">Thanks, talk soon.</p>
  <div id="sig">{fragment}</div>
</div>
<ol>
  <li>Click <b>Copy signature</b>.</li>
  <li>Outlook &rarr; Settings &rarr; Accounts &rarr; Signatures &rarr; New signature.</li>
  <li>Paste, name it, and pick which account uses it. Send yourself a test.</li>
</ol>
</div>
<script>
var b = document.getElementById('copy');
b.onclick = function () {{
  var r = document.createRange(); r.selectNodeContents(document.getElementById('sig'));
  var s = getSelection(); s.removeAllRanges(); s.addRange(r);
  document.execCommand('copy'); s.removeAllRanges();
  b.textContent = 'Copied'; b.classList.add('done');
  setTimeout(function () {{ b.textContent = 'Copy signature'; b.classList.remove('done'); }}, 1800);
}};
</script>
</body></html>"""

(here / "admin-news-fragment.html").write_text(fragment)
(here / "admin-news.html").write_text(page)
print("wrote admin-news.html and admin-news-fragment.html")
