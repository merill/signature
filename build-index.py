#!/usr/bin/env python3
"""Builds index.html: every signature on one page, each with its own Copy button.

Reads the fragments written by build-final.py and build-admin-news.py, so run those (they call
this script at the end). The editor signature is filled in live from the form on the page.
"""
import json, pathlib

here = pathlib.Path(__file__).parent
read = lambda name: (here / name).read_text()

SANS = "Calibri, Carlito, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
INK, MUTED, LINE = "#18181b", "#71717a", "#e4e4e7"

maester = read("signature-fragment.html")
admin_news = read("admin-news-fragment.html")
editor_template = read("admin-news-editor-template.html")
chip_template = read("admin-news-chip-template.html")


def card(sig_id, title, note, fragment, form=""):
    return f"""<section>
<div class="top"><div><h2>{title}</h2><p class="note">{note}</p></div><button class="copy" data-target="{sig_id}">Copy signature</button></div>
{form}<div class="mail">
  <p class="body">Thanks, talk soon.</p>
  <div id="{sig_id}">{fragment}</div>
</div>
</section>"""


form = """<form class="fields" id="editor-form" autocomplete="off">
  <label>Name<input name="name" placeholder="Your name"></label>
  <label>Title<input name="title" placeholder="Editor, Intune News"></label>
  <label>LinkedIn URL<input name="linkedin" placeholder="https://linkedin.com/in/you"></label>
  <label>Website URL<input name="site" placeholder="https://yourblog.com"></label>
  <label>Website label<input name="siteLabel" placeholder="yourblog.com"></label>
  <label>Other link label<input name="otherLabel" placeholder="YouTube"></label>
  <label class="wide">Other link URL<input name="other" placeholder="https://youtube.com/@you"></label>
</form>"""

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Email signatures</title>
<style>
  /* Preview only, not part of the signatures: use an installed Calibri, or borrow it from the Outlook bundle when
     this page is opened locally on a Mac. On GitHub Pages without Calibri the preview falls back to the system font. */
  @font-face {{ font-family:Calibri; font-weight:400; src:local("Calibri"), url("file:///Applications/Microsoft%20Outlook.app/Contents/Resources/DFonts/Calibri.ttf"); }}
  @font-face {{ font-family:Calibri; font-weight:600 700; src:local("Calibri Bold"), local("Calibri-Bold"), url("file:///Applications/Microsoft%20Outlook.app/Contents/Resources/DFonts/Calibrib.ttf"); }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; padding:40px 16px 80px; background:#f4f4f5; color:{INK}; font-family:{SANS}; -webkit-font-smoothing:antialiased; }}
  .wrap {{ max-width:720px; margin:0 auto; }}
  h1 {{ font-size:22px; font-weight:700; margin:0 0 28px; }}
  section {{ margin:0 0 40px; }}
  .top {{ display:flex; align-items:flex-start; justify-content:space-between; gap:16px; margin:0 0 12px; }}
  h2 {{ font-size:18px; font-weight:600; margin:0; }}
  .note {{ font-size:13px; color:{MUTED}; margin:2px 0 0; }}
  button {{ font:inherit; font-size:13px; font-weight:500; padding:6px 14px; border:1px solid {LINE}; border-radius:999px; background:#fff; color:{INK}; cursor:pointer; white-space:nowrap; }}
  button.done {{ background:{INK}; color:#fff; border-color:{INK}; }}
  .mail {{ background:#fff; border:1px solid {LINE}; border-radius:12px; padding:24px 28px 28px; overflow-x:auto; }}
  .body {{ font-size:14px; line-height:21px; color:#444; margin:0 0 22px; }}
  .fields {{ display:grid; grid-template-columns:1fr 1fr; gap:10px 14px; background:#fff; border:1px solid {LINE}; border-radius:12px; padding:18px 20px; margin:0 0 12px; }}
  .fields label {{ display:flex; flex-direction:column; gap:4px; font-size:12px; font-weight:600; color:{MUTED}; }}
  .fields .wide {{ grid-column:1 / -1; }}
  .fields input {{ font:inherit; font-size:14px; font-weight:400; color:{INK}; padding:7px 10px; border:1px solid {LINE}; border-radius:8px; width:100%; }}
  .fields input:focus {{ outline:2px solid #a1a1aa; outline-offset:0; border-color:#a1a1aa; }}
  @media (max-width:560px) {{ .fields {{ grid-template-columns:1fr; }} }}
  ol {{ color:{MUTED}; font-size:13px; line-height:20px; padding-left:20px; margin:0; }}
</style></head><body><div class="wrap">
<h1>Email signatures</h1>
{card("sig-maester", "Merill &middot; Maester Cloud", "For merill@jozra.com.", maester)}
{card("sig-admin-news", "Merill &middot; Admin.News", "For Admin.News work.", admin_news)}
{card("sig-editor", "Admin.News editors", "Fill in your details, then copy. Leave a field empty to drop it.", "", form)}
<ol>
  <li>Click <b>Copy signature</b> on the one you want.</li>
  <li>Outlook &rarr; Settings &rarr; Accounts &rarr; Signatures &rarr; New signature.</li>
  <li>Paste, name it, and pick which account uses it. Send yourself a test.</li>
</ol>
</div>
<script>
var EDITOR = {json.dumps(editor_template)};
var CHIP = {json.dumps(chip_template)};

function esc(s) {{
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}}
function url(s) {{
  s = s.trim();
  if (!s) return '';
  if (!/^https?:\\/\\//i.test(s)) s = 'https://' + s;
  return s;
}}
function host(u) {{
  try {{ return new URL(u).hostname.replace(/^www\\./, ''); }} catch (e) {{ return u; }}
}}
function chip(href, text) {{
  return CHIP.replace('%%HREF%%', esc(href)).replace('%%TEXT%%', esc(text));
}}

var f = document.getElementById('editor-form');
function render() {{
  var v = function (n) {{ return f.elements[n].value.trim(); }};
  var links = '';
  var site = url(v('site'));
  if (site) links += chip(site, v('siteLabel') || host(site));
  var li = url(v('linkedin'));
  if (li) links += chip(li, 'LinkedIn');
  var other = url(v('other'));
  if (other) links += chip(other, v('otherLabel') || host(other));
  document.getElementById('sig-editor').innerHTML = EDITOR
    .replace('%%NAME%%', esc(v('name') || 'Your name'))
    .replace('%%TITLE%%', esc(v('title') || 'Editor, Admin.News'))
    .replace('%%LINKS%%', links);
}}
f.addEventListener('input', render);
render();

document.querySelectorAll('button.copy').forEach(function (b) {{
  b.onclick = function () {{
    var r = document.createRange(); r.selectNodeContents(document.getElementById(b.dataset.target));
    var s = getSelection(); s.removeAllRanges(); s.addRange(r);
    document.execCommand('copy'); s.removeAllRanges();
    b.textContent = 'Copied'; b.classList.add('done');
    setTimeout(function () {{ b.textContent = 'Copy signature'; b.classList.remove('done'); }}, 1800);
  }};
}});
</script>
</body></html>"""

(here / "index.html").write_text(page)
print("wrote index.html")
