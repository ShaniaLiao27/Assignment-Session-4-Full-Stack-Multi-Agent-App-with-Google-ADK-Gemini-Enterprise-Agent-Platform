#!/usr/bin/env python3
"""
Injects copy-to-clipboard buttons into the claat-generated codelab HTML.
Run after every `claat export` + `cp` step.

Usage:
    python3 scripts/inject_copy_buttons.py docs/index.html
"""

import sys

SNIPPET = """
  <style>
    .copy-btn {
      position: absolute;
      top: 6px;
      right: 8px;
      padding: 3px 10px;
      font-size: 11px;
      font-family: 'Roboto', sans-serif;
      cursor: pointer;
      background: #f8f8f8;
      border: 1px solid #ccc;
      border-radius: 4px;
      color: #444;
      opacity: 0;
      transition: opacity 0.2s;
    }
    pre:hover .copy-btn { opacity: 1; }
    .copy-btn:hover { background: #e8e8e8; }
    .copy-btn.copied { color: #1e8e3e; border-color: #1e8e3e; }
  </style>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      document.querySelectorAll('pre').forEach(function (pre) {
        var code = pre.querySelector('code');
        if (!code) return;
        pre.style.position = 'relative';
        var btn = document.createElement('button');
        btn.className = 'copy-btn';
        btn.textContent = 'Copy';
        pre.appendChild(btn);
        btn.addEventListener('click', function () {
          navigator.clipboard.writeText(code.innerText).then(function () {
            btn.textContent = 'Copied!';
            btn.classList.add('copied');
            setTimeout(function () {
              btn.textContent = 'Copy';
              btn.classList.remove('copied');
            }, 2000);
          });
        });
      });
    });
  </script>
"""

MARKER = "</body>"


def inject(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    if "copy-btn" in html:
        print(f"Copy buttons already present in {path} — skipping.")
        return

    if MARKER not in html:
        print(f"ERROR: could not find {MARKER!r} in {path}", file=sys.stderr)
        sys.exit(1)

    html = html.replace(MARKER, SNIPPET + MARKER, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Copy buttons injected into {path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path/to/index.html>", file=sys.stderr)
        sys.exit(1)
    inject(sys.argv[1])
