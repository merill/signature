# Email signature

Outlook signature for merill@jozra.com, built as email-safe HTML and published with GitHub Pages at **https://merill.net/signature/**.

- **[index.html](index.html)**: the signature with a Copy button. Open it, click **Copy signature**, paste into Outlook.
- **[signature-fragment.html](signature-fragment.html)**: the raw signature HTML, for pasting somewhere other than Outlook.
- **[gallery.html](gallery.html)**: the ten concepts that were considered. The current signature is concept 09, Badges.

## Changing it

The HTML is generated, so edit the Python and rebuild rather than editing the HTML by hand:

```bash
python3 build-final.py      # writes index.html and signature-fragment.html
python3 build-gallery.py    # writes gallery.html
```

Wording, links and colours are variables at the top of `build-final.py`. The flame logo is embedded from `maester-logo.png` as a data URI; Outlook turns it into an inline attachment when the signature is saved, so recipients never download it.

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
