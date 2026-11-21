# Hi Tech Sofa Maker's — Furniture Catalog

A dependency-free, mobile-first furniture showroom website. No npm installation or build is required. Works as a static website on GitHub Pages.

## Open locally

Run from this folder:

```bash
python -m http.server 8000
```

Then open http://localhost:8000/. Do not double-click index.html, because the catalog uses JavaScript ES modules, which require a local web server.

## Deploy to GitHub Pages

1. Create a public repository, e.g. `hi-tech-sofa-makers`.
2. Upload all files including the `.github/workflows/deploy.yml` folder.
3. Set your default branch to `main` and push.
4. In repository **Settings → Pages**, choose **Source: GitHub Actions**.
5. The provided workflow deploys the root directory. Site URL is typically `https://YOURUSERNAME.github.io/hi-tech-sofa-makers/`.

All URLs use relative paths, so a repository subpath works automatically. You may add a custom domain using GitHub Pages settings.

## Update products and 1 / 2 / 3 photos

1. Put genuine furniture images in `images/` (prefer compressed JPG or WebP).
2. Edit `products.js`. Each product has `id`, `name`, `category`, `photos`, `real`, etc.
3. Set `photos: ['./images/sofa-001-1.webp', './images/sofa-001-2.webp', './images/sofa-001-3.webp']`.
4. The quick view automatically shows numbered buttons `1`, `2`, `3` for available images. Products with only one photo show only button `1`.
5. Set `real:true` only when photos are genuinely from the business. Illustrative SVG cards are clearly labelled as inspiration.
6. Set `published:false` to hide a product.

## What works

- Responsive catalog, categories and search
- Clickable furniture image popup with available 1/2/3 controls, swipe and keyboard arrows
- WhatsApp enquiry messages with product ID and selected variants
- Phone and email contact
- Favorite items stored in browser and combined WhatsApp enquiry
- Fabric and color selections
- Client-side custom design photo picker with **manual attachment to WhatsApp**
- Approximate local room photo preview with draggable furniture illustration
- Accessibility essentials: keyboard controls, focus management, Escape and labeled buttons

## Limitations and future development

- GitHub Pages cannot accept persistent server-side uploads or store customer data. Owner edits product files in Git.
- The custom design photo **is not automatically attached** to WhatsApp; visitors must attach it manually.
- The room overlay is illustrative and cannot accurately place/scalably render actual furniture.
- 360° is intentionally not advertised until frame sequences exist; this can be developed when the assets are provided.
- Only two genuine product photos have been provided so far, extracted from business-profile screenshots. The sofa item has three gallery images: one original and two crops of the same original photograph, **not** three distinct camera angles. Replace these crops with your three actual supplied photos. Other catalog items are explicitly marked as design inspiration illustrations.
- Real material availability, business hours, locations and service claims should be confirmed before advertising them.

## Security and privacy

This is a static site with no backend, no user registration, no embedded API credentials and no automatic photo uploads. Favorites are local browser storage. Customer-selected room photos are previewed in the browser only; external WhatsApp/email handles messages submitted by the visitor. Keep your GitHub account secured with 2FA and review any third-party code before adding it.

## Test

Run `python -m http.server 8000`, then verify navigation, categories, product photos, popup close/keyboard controls, favorites across reload, WhatsApp links, and mobile responsive layout. For actual device testing, serve through a reachable local network host or deploy to GitHub Pages.
