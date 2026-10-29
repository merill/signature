#!/usr/bin/env python3
"""Builds the Admin.News signatures, then rebuilds index.html.

- admin-news-fragment.html: Merill's Admin.News signature.
- admin-news-editor-template.html: the same design for any editor, with %%NAME%%, %%TITLE%% and
  %%LINKS%% placeholders that the form on index.html fills in.
- admin-news-chip-template.html: one outline chip with %%HREF%% and %%TEXT%%, for the editor's own links.

Same Badges design and Outlook rules as build-final.py. Logos come from admin-news/*.png
(copied from merill/newsletter app/static/brand, saved at 2x) and are embedded as data URIs.
"""
import base64, pathlib

here = pathlib.Path(__file__).parent


def logo(name):
    return "data:image/png;base64," + base64.b64encode((here / "admin-news" / f"{name}.png").read_bytes()).decode()


SANS = "Calibri, Carlito, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
INK, MUTED, LINE, BRAND = "#18181b", "#71717a", "#e4e4e7", "#111113"
SPONSOR = "#ea580c"

UTM = "?utm_source=email&utm_medium=signature"
AN = "https://admin.news/" + UTM
SP = "https://sponsors.admin.news/" + UTM
MC = "https://maester.cloud/" + UTM
JZ = "https://jozra.com"
MN = "https://merill.net"
LI = "https://linkedin.com/in/merill"

TAGLINE = "Independent weekly newsletters for the Microsoft admin community."

NEWSLETTERS = [
    ("entra", "Entra.News", "https://entra.news/" + UTM),
    ("intune", "Intune News", "https://intune.admin.news/" + UTM),
    ("defender", "Defender News", "https://defender.admin.news/" + UTM),
    ("purview", "Purview News", "https://purview.admin.news/" + UTM),
    ("ad", "AD News", "https://ad.admin.news/" + UTM),
]


def wrap_chip(inner_cell):
    return (f'<td style="padding:0 6px 6px 0;"><table cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">'
            f'<tr>{inner_cell}</tr></table></td>')


# Filled chip with a logo. As in build-final.py: fill, radius and height live on the cell, bold is a
# <strong>, and the link carries only colour. The icon is its own cell so it never sits inside a text run.
def newsletter_chip(key, text, href):
    cell = f"background-color:{BRAND};border-radius:999px;height:28px;vertical-align:middle;padding:0 12px 0 6px;"
    return wrap_chip(
        f'<td height="28" valign="middle" bgcolor="{BRAND}" style="{cell}">'
        f'<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>'
        f'<td width="18" valign="middle" style="width:18px;"><a href="{href}"><img src="{logo(key)}" width="18" height="18" alt="" style="display:block;border:0;width:18px;height:18px;"></a></td>'
        f'<td valign="middle" style="padding:0 0 0 6px;">'
        f'<div style="font-family:{SANS};font-size:14px;line-height:18px;font-weight:700;color:#ffffff;mso-line-height-rule:exactly;white-space:nowrap;">'
        f'<a href="{href}" style="color:#ffffff;text-decoration:none;"><strong style="font-weight:700;">{text}</strong></a></div>'
        f'</td></tr></table></td>')


def sponsor_chip():
    cell = f"background-color:{SPONSOR};border-radius:999px;height:28px;vertical-align:middle;padding:0 14px;"
    return wrap_chip(
        f'<td height="28" valign="middle" bgcolor="{SPONSOR}" style="{cell}">'
        f'<div style="font-family:{SANS};font-size:14px;line-height:18px;font-weight:700;color:#ffffff;mso-line-height-rule:exactly;white-space:nowrap;">'
        f'<a href="{SP}" style="color:#ffffff;text-decoration:none;"><strong style="font-weight:700;">Sponsor a newsletter &rarr;</strong></a></div></td>')


def outline_chip(href, text):
    cell = f"background-color:#ffffff;border:1px solid {LINE};border-radius:999px;height:26px;vertical-align:middle;padding:0 11px;"
    return wrap_chip(
        f'<td height="26" valign="middle" bgcolor="#ffffff" style="{cell}">'
        f'<div style="font-family:{SANS};font-size:14px;line-height:18px;font-weight:400;color:{INK};mso-line-height-rule:exactly;">'
        f'<a href="{href}" style="color:{INK};text-decoration:none;">{text}</a></div></td>')


def chip_row(chips):
    return f'<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>{"".join(chips)}</tr></table>'


newsletter_rows = "\n  ".join([
    chip_row(newsletter_chip(*n) for n in NEWSLETTERS[:3]),
    chip_row([*(newsletter_chip(*n) for n in NEWSLETTERS[3:]), sponsor_chip()]),
])


# Header in its own table and the logo cell exactly the image width, for the reasons in build-final.py.
def fragment(name, title, links_row):
    return f"""<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
<tr><td>
  <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>
    <td width="40" valign="middle" style="width:40px;"><a href="{AN}"><img src="{logo('admin-news')}" width="40" height="40" alt="Admin.News" style="display:block;border:0;width:40px;height:40px;"></a></td>
    <td valign="middle" style="padding:0 0 0 12px;font-family:{SANS};font-size:15px;line-height:21px;color:{INK};">
      <div style="font-size:18px;font-weight:700;">{name}</div>
      <div style="font-size:14px;color:{MUTED};">{title}</div>
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
  {links_row}
</td></tr>
</table>"""


merill = fragment(
    "Merill Fernando",
    "Founder, Jozra &middot; Publisher of Admin.News",
    chip_row([outline_chip(AN, "Admin.News"), outline_chip(MC, "Maester Cloud"),
              outline_chip(JZ, "Jozra"), outline_chip(MN, "merill.net"), outline_chip(LI, "LinkedIn")]),
)

# The editor's own links are filled in by the page; Admin.News always comes first.
editor = fragment("%%NAME%%", "%%TITLE%%", chip_row([outline_chip(AN, "Admin.News"), "%%LINKS%%"]))

(here / "admin-news-fragment.html").write_text(merill)
(here / "admin-news-editor-template.html").write_text(editor)
(here / "admin-news-chip-template.html").write_text(outline_chip("%%HREF%%", "%%TEXT%%"))
print("wrote admin-news-fragment.html and the editor templates")

import runpy; runpy.run_path(str(here / "build-index.py"))
