# Email signature

Outlook signatures, built as email-safe HTML and published with GitHub Pages at **https://merill.net/signature/**. One page holds all of them, each with its own Copy button:

- **Merill, Maester Cloud**: for merill@jozra.com. Concept 09, Badges, from [gallery.html](gallery.html).
- **Merill, Admin.News**: the same design with the five newsletters (Entra, Intune, Defender, Purview, AD) as filled chips and an orange **Sponsor a newsletter** chip linking to sponsors.admin.news.
- **Admin.News editors**: the Admin.News design with a form for the editor's name, title, LinkedIn, website and one other link. Empty fields drop out. Share the page link with editors.

## Changing it

The HTML is generated, so edit the Python and rebuild rather than editing the HTML by hand:

```bash
python3 build-admin-news.py  # writes admin-news-fragment.html and the editor templates, then index.html
python3 build-final.py       # writes signature-fragment.html, then index.html
python3 build-gallery.py     # writes gallery.html
```

Both build scripts finish by running `build-index.py`, which puts every fragment on `index.html`. Wording, links and colours are variables at the top of each script. The flame logo is embedded from `maester-logo.png`, and the Admin.News logos from `admin-news/` (copied from `merill/newsletter` `app/static/brand` at 2x), all as data URIs. Outlook turns them into inline attachments when the signature is saved, so recipients never download them.

The editor signature is `admin-news-editor-template.html` with `%%NAME%%`, `%%TITLE%%` and `%%LINKS%%` placeholders; the page fills them in and builds link chips from `admin-news-chip-template.html`.

## Installing in Outlook

1. Open the page and click **Copy signature**.
2. Outlook → Settings → Accounts → Signatures → New signature.
3. Paste, name it, set it as the default for the jozra.com account, and send yourself a test.

## Things learned the hard way

Outlook's composer rewrites pasted HTML, so the markup is shaped around what survives:

- It keeps a link's colour but **drops `font-weight` and `line-height` from links**. Text styling lives on `div`s and table cells, and bold is a `<strong>`; links carry only colour.
- It **copies a link's background onto the text run inside**, which draws a square fill under a rounded one. Fills, borders and radii live on table cells, never on links.
- A row that spans both columns of a table stretches the narrower column, so the logo and name sit in their own nested table.
- Pills have a fixed cell height with `valign="middle"` so the text is centred without relying on line-height.
- Classic Outlook for Windows ignores `border-radius`; those recipients see square chips.

Font stack is Calibri, then Carlito, then the system font, so phones render in San Francisco or Roboto at the same sizes. Weights are 400 and 700 only, since Calibri has no semibold.
