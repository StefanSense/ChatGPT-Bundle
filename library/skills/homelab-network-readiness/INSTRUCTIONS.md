---
id: homelab-network-readiness
title: "Homelab Network Readiness"
description: "Readiness checklist for homelab VLAN segmentation, local DNS filtering (Pi-hole, AdGuard Home), and WireGuard-style remote access. Use when planning or reviewing home network changes — splitting a flat network into trusted, IoT, guest, or management VLANs, moving DHCP to a local resolver, or adding VPN access — before changing router, firewall, DHCP, or VPN configuration."
origin: "everything-claude-code (ECC) by Affaan Mustafa (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Homelab Network Readiness

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **everything-claude-code (ECC)** by Affaan Mustafa, MIT licence (https://github.com/affaan-m/everything-claude-code); upstream notice: `../../licenses/LICENSE-everything-claude-code.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow are relative to this folder.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
