---
id: homelab-pihole-dns
title: "Homelab Pihole Dns"
description: "Pi-hole installation, blocklist management, DNS-over-HTTPS setup, DHCP integration, local DNS records, and troubleshooting broken DNS resolution on a home network. Use when the task explicitly involves Pi-hole — installing it, managing blocklists, configuring DoH or DHCP, adding local DNS records, or diagnosing DNS resolution with Pi-hole in the path."
origin: "everything-claude-code (ECC) by Affaan Mustafa (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Homelab Pihole Dns

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **everything-claude-code (ECC)** by Affaan Mustafa, MIT licence (https://github.com/affaan-m/everything-claude-code); upstream notice: `../../licenses/LICENSE-everything-claude-code.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow are relative to this folder.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
