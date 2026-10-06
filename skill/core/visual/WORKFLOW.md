---
id: visual
title: Visuals - images, diagrams, design briefs
description: Plan and produce visuals - image generation prompts and iterations, social/ad visuals, illustrations, mockups, logos concepts, infographics, diagrams (Mermaid, flowcharts, org charts), charts, and design briefs for designers. Triggers - картинка, сгенерируй изображение, обложка, баннер, инфографика, схема, диаграмма, логотип, image, generate picture, diagram, flowchart, infographic, banner.
based_on: Stefan Sense original; design direction informed by canvas-design, theme-factory, frontend-design (Anthropic, Apache-2.0) and design-system (claude-skills, MIT)
author: M. Stefan Kassem (Stefan Sense)
---

# Visuals

## 1. Brief
Purpose and placement (feed post, banner, slide, print), size/aspect ratio, audience, brand (colors as HEX, fonts, logo provided by the user), mood, must-include elements, text on the image (exact wording, language), what to avoid.

## 2. Image generation (when the image tool is available)
Prompt structure: subject → action/composition → setting → style/medium → lighting → color palette → camera/framing → aspect ratio → text to render (in quotes) → exclusions.
- Generate, inspect, then iterate with specific changes ("move the headline to the top third, increase contrast").
- Check rendered text letter by letter; long or non-Latin text often fails — offer to overlay text later in a design tool or slide.
- Respect rights: no imitation of living artists' signature styles on request for commercial deception, no real people in misleading situations, no trademarks/logos of others as if official, no fake documents.

## 3. Diagrams and infographics
- Process/flow, org chart, sequence, timeline, mind map → Mermaid code (renders in many tools) or an image via matplotlib/graphviz if available.
- Infographic: one key message, 3–6 data points (real, sourced), visual hierarchy, source line.
- Charts: see `data-analysis` rules (labeled axes, honest baselines).

## 4. Design brief for a designer
Goal, audience, deliverables and formats, content (final texts), brand assets, references (with what to take from each), constraints, deadline, acceptance criteria.

## 5. Check
Legible at the target size, contrast sufficient (WCAG AA for text), brand colors correct, no typos, no invented data, alt text provided for accessibility.

Library: `canvas-design`, `algorithmic-art`, `theme-factory`, `design-system`, `ecc-design-system`, `slack-gif-creator`, `brand-guidelines`.
