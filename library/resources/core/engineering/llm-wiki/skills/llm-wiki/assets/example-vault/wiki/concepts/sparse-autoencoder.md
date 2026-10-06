---
title: Sparse Autoencoder
category: concept
summary: Dictionary-learning method for decomposing polysemantic neurons into monosemantic features
tags: [interpretability, sparse-autoencoders, dictionary-learning]
sources: 1
updated: 2026-04-10
---

# Sparse Autoencoder

## Definition
A neural-network-based dictionary-learning method that decomposes the activations of a target model's layer into a larger set of sparsely-active features, each of which is hoped to be monosemantic (interpretable as a single concept).

## Origin

## Key claims
- SAEs extract features that are *more* monosemantic than raw neurons — cited from [[sources/monosemanticity]]
- The resulting feature dictionary is larger than the original layer width (overcomplete)
- Features come in interpretable families (specific tokens, contexts, circuits)

## Contrasts with
- **Linear probing** — supervised; requires you to know what feature to look for
- **Direct neuron inspection** — limited by polysemanticity

## Open questions
- Does it scale beyond one-layer models?
- Are the features truly monosemantic or just more monosemantic?

## Used in
- [[synthesis/interpretability-overview]]
- [[sources/monosemanticity]]
