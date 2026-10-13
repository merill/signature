#!/usr/bin/env python3
"""Builds index.html (preview + Copy button) and signature-fragment.html (the raw signature) from the Badges design."""
import base64, pathlib

here = pathlib.Path(__file__).parent
FLAME = "data:image/png;base64," + base64.b64encode((here / "maester-logo.png").read_bytes()).decode()

# Calibri ships with Office on Mac and Windows; Carlito is its metric-compatible stand-in elsewhere, then the system font.
SANS = "Calibri, Carlito, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
INK, MUTED, LINE, BRAND = "#18181b", "#71717a", "#e4e4e7", "#111113"

MC = "https://maester.cloud/?utm_source=email&utm_medium=signature"
JZ = "https://jozra.com"
EN = "https://entra.news"
MN = "https://merill.net"
LI = "https://linkedin.com/in/merill"

# Outlook's composer rewrites links: it keeps a link's colour but drops its font-weight and line-height,
# and copies its background onto the text run, which draws a square fill under the rounded one.
# So the fill, border, radius and height live on a cell, the text styling on a div, and the link stays bare.
def chip(href, text, filled):
    color = "#ffffff" if filled else INK
    if filled:
        cell = f"background-color:{BRAND};border-radius:999px;height:28px;vertical-align:middle;padding:0 12px;"
        height, label = 28, f'<strong style="font-weight:700;">{text}</strong>'
    else:
        cell = f"background-color:#ffffff;border:1px solid {LINE};border-radius:999px;height:26px;vertical-align:middle;padding:0 11px;"
        height, label = 26, text
    return (f'<td style="padding:0 6px 6px 0;"><table cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">'
            f'<tr><td height="{height}" valign="middle" bgcolor="{BRAND if filled else "#ffffff"}" style="{cell}">'
            f'<div style="font-family:{SANS};font-size:14px;line-height:18px;font-weight:{700 if filled else 400};color:{color};mso-line-height-rule:exactly;">'
            f'<a href="{href}" style="color:{color};text-decoration:none;">{label}</a></div></td></tr></table></td>')


# The header sits in its own table: if it shared columns with the wider rows below, the logo column
# would be stretched to take its share of the extra width and the gap to the name would grow.
fragment = f"""<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
<tr><td>
  <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>
    <td width="40" valign="middle" style="width:40px;padding:0 12px 0 0;"><a href="{MC}"><img src="{FLAME}" width="40" height="40" alt="Maester" style="display:block;border:0;width:40px;height:40px;"></a></td>
    <td valign="middle" style="font-family:{SANS};font-size:15px;line-height:21px;color:{INK};">
      <div style="font-size:18px;font-weight:700;">Merill Fernando</div>
      <div style="font-size:14px;color:{MUTED};">Founder, Jozra &middot; Creator of Maester</div>
    </td>
  </tr></table>
</td></tr>
<tr><td style="padding:12px 0 0 0;font-family:{SANS};font-size:14px;line-height:21px;color:{MUTED};max-width:480px;">
  Building <a href="{MC}" style="color:{INK};text-decoration:none;"><strong style="font-weight:700;color:{INK};">Maester Cloud</strong></a>, the evidence layer for Microsoft 365 security. Keeping security testing open for everyone.
</td></tr>
<tr><td style="padding:10px 0 0 0;">
  <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>
    {chip(MC, "Maester Cloud", True)}
    {chip(EN, "Entra.News", False)}
    {chip(JZ, "Jozra", False)}
    {chip(MN, "merill.net", False)}
    {chip(LI, "LinkedIn", False)}
  </tr></table>
</td></tr>
</table>"""

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Email signature</title>
<style>
  /* Preview only, not part of the signature: use an installed Calibri, or borrow it from the Outlook bundle when
     this page is opened locally on a Mac. On GitHub Pages without Calibri the preview falls back to the system font. */
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
<div class="top"><h1>Email signature</h1><button id="copy">Copy signature</button></div>
<div class="mail">
  <p class="body">Thanks, talk soon.</p>
  <div id="sig">{fragment}</div>
</div>
<ol>
  <li>Click <b>Copy signature</b>.</li>
  <li>Outlook &rarr; Settings &rarr; Accounts &rarr; Signatures &rarr; New signature.</li>
  <li>Paste, name it, and set it as the default for the jozra.com account. Send yourself a test.</li>
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

(here / "signature-fragment.html").write_text(fragment)
(here / "index.html").write_text(page)
print("wrote index.html and signature-fragment.html")
