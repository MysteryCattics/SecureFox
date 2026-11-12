# SecureFox

Experimental Firefox-based Linux browser build with privacy-oriented default preferences.

This repository contains a source patch script and a GitHub Actions build workflow. It does **not** contain a security-audited browser or a tested binary. Firefox sources are obtained from Mozilla during CI; defaults are not enforced policies. Strict Cloudflare DoH may break DNS on some networks, and does not guarantee system-wide leak prevention.

Build: Actions → SecureFox Linux experimental build → Run workflow. The workflow also runs when the workflow file is first pushed.
