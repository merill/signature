#!/usr/bin/env python3
"""Builds signature-fragment.html (the raw Maester signature) from the Badges design, then rebuilds index.html."""
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
# The logo cell is exactly the image width with no padding: Outlook's composer applies border-box sizing
# and caps pasted images at the cell's content width, so padding on this cell squashes the flame.
fragment = f"""<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
<tr><td>
  <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>
    <td width="40" valign="middle" style="width:40px;"><a href="{MC}"><img src="{FLAME}" width="40" height="40" alt="Maester" style="display:block;border:0;width:40px;height:40px;"></a></td>
    <td valign="middle" style="padding:0 0 0 12px;font-family:{SANS};font-size:15px;line-height:21px;color:{INK};">
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

(here / "signature-fragment.html").write_text(fragment)
print("wrote signature-fragment.html")

import runpy; runpy.run_path(str(here / "build-index.py"))
