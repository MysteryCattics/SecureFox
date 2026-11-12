#!/usr/bin/env python3
"""Apply SecureFox defaults to a Firefox source checkout."""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit('Usage: apply_source_defaults.py path/to/browser/app/profile/firefox.js')
path = Path(sys.argv[1])
text = path.read_text()
marker = '// BEGIN SECUREFOX DEFAULTS v0.2'
if marker in text:
    raise SystemExit('SecureFox defaults already present; refusing duplicate')
block = '''
// BEGIN SECUREFOX DEFAULTS v0.2
pref("network.trr.mode", 3);
pref("network.trr.uri", "https://cloudflare-dns.com/dns-query");
pref("network.trr.custom_uri", "https://cloudflare-dns.com/dns-query");
pref("network.trr.bootstrapAddress", "1.1.1.1");
pref("dom.security.https_only_mode", true);
pref("dom.security.https_only_mode_pbm", true);
pref("privacy.trackingprotection.enabled", true);
pref("privacy.trackingprotection.pbmode.enabled", true);
pref("network.cookie.cookieBehavior", 5);
pref("media.peerconnection.ice.no_host", true);
pref("media.peerconnection.ice.default_address_only", true);
pref("network.dns.disablePrefetch", true);
pref("network.prefetch-next", false);
pref("browser.send_pings", false);
// END SECUREFOX DEFAULTS v0.2
'''
path.write_text(text.rstrip('\n') + '\n' + block)
print('SecureFox defaults applied:', path)
