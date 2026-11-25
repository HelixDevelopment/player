# FUSE — White-label Music Player UI/UX Fusion

**A complete SVG-first design specification inspired by classic Winamp, VOX for macOS, and AIMP**

Version 1.0 · Design study and implementation handoff · 25 November 2026

> **One player. Three lineages. No borrowed branding.** FUSE combines Winamp’s modular performance controls and skin culture, VOX’s compact album-led restraint, and AIMP’s deep library, queue, tagging, and audio tooling. The result is an original, white-label product system—not a reproduction of any reference application.

## Download and reading guide

- **This document is the primary deliverable.** It contains the full analysis, specifications, wireframes, screen designs, component sheets, skin contract, and implementation guidance.
- Artwork is embedded as self-contained SVG data URIs; no network connection is required to view the images in a compatible Markdown renderer.
- Every illustration also has an editable SVG source in the companion `svg/` directory and a full SVG source listing in Appendix A of this document.
- `FUSE-Design-Gallery.html` is an optional visual companion with an index and full-size artwork. `FUSE-Waveform-Lab.html` is an optional interactive SVG/audio-analysis demonstration.
- The ZIP package contains this Markdown, all SVGs, the gallery, the demo, tokens, schema, and generation scripts.

**Status:** high-fidelity design specification and vector prototype, not a shipped audio engine. Static SVG frames illustrate reactive layouts; the separate waveform lab demonstrates actual audio-driven SVG updates. Backend capabilities, native integrations, licensing, and user-test results are explicitly marked as pending rather than claimed.

**Fictional content:** Northbound, Afterglow, Slow satellites, and the other track/artist names are demonstration data. All album sleeves, icons, waveforms, textures, and layouts in the package are original vector artwork. No Winamp sprites, VOX assets, AIMP skins, or reference-product logos are included.

## Contents

1. Executive decision and product principles
2. Reference-product analysis: strengths, shortcomings, and fusion decisions
3. Scope, assumptions, personas, and success criteria
4. Gap analysis and risk register
5. Feature inventory and priority model
6. Information architecture and navigation
7. Core object model and playback semantics
8. End-to-end user flows
9. Layout system, responsive behavior, and modes
10. Visual language and design tokens
11. Reusable component inventory and state contracts
12. Waveform, spectrum, and motion system
13. Skin architecture and white-label contract
14. Accessibility and inclusive interaction
15. Content, error, empty, and recovery design
16. Full SVG design gallery and screen specifications
17. Implementation architecture and handoff
18. Validation plan and acceptance criteria
19. Delivery roadmap and open decisions
20. Source notes and limitations
21. Appendix A: editable SVG source listings
22. Appendix B: machine-readable tokens and skin schema

## 1. Executive decision

### The fusion in one sentence

**A calm, album-led listening workspace that can expand into a powerful audio workstation, shrink into a compact performance player, and change its entire visual signature without changing how it behaves.**

### What belongs to each lineage

| Lineage | Adopted strength | Modernized expression |
|---|---|---|
| Classic Winamp | Immediate transport, visible spectrum, modular player/EQ/playlist stack, skin identity | Original vector metal skin, readable labels, modern target sizes, shared state across modules |
| VOX for macOS | Compact footprint, artwork-first hierarchy, restrained controls, source-format awareness | Persistent now-playing identity, quiet chrome, explicit quality badges, mini/shade modes |
| AIMP | Library depth, explicit queue, smart playlists, tagging, DSP, flexible skins | Task-grouped navigation, safe batch editing, capability-aware audio settings, tokenized skin system |

### The non-negotiable product rules

1. **Playback is always recoverable.** Play/pause, track identity, and an exit from compact/focus modes remain reachable.
2. **Queue is explicit.** “Play next,” playlist context, selection, and history are different objects with different visual treatments.
3. **Power is progressive.** A new user can import and play without understanding DSP, exclusive output, or skin tokens.
4. **Quality claims are precise.** Source format, processing state, and negotiated output are separate facts.
5. **Skins cannot break usability.** Color, texture, and approved layout variants are customizable; control meaning, focus, targets, and error honesty are not.
6. **Motion is optional.** Reactive visuals are pausable and have a static presentation; reduced motion is respected.
7. **Local files are safe.** Import does not modify files; tag writes, deletion, and renaming are separate explicit operations.
8. **Every state tells the truth.** Loading, buffering, paused, stopped, unavailable, and error are not interchangeable.

### Immediate visual signature

- Graphite surfaces, mint interaction accent, warm amber secondary accent, and original ocean/sun album geometry.
- A persistent bottom transport in workspace mode; a compact stacked transport in Classic mode.
- Mirrored waveform bars as the default signal, with spectrum, oscilloscope, and static alternatives.
- Strong title hierarchy, tabular time/quality numerals, restrained borders, and generous regional spacing.
- No neon-only meaning, no tiny legacy hit targets, no decorative fake meters, and no account wall for local playback.

## 2. Reference-product analysis

### 2.1 Evidence boundary

This analysis uses public product pages, official help/documentation where available, and representative screenshots. It is a **design-direction analysis**, not a controlled benchmark or a claim that every feature was tested in every current version. VOX premium gating, AIMP platform/plugin support, and Winamp version differences can change. The fusion therefore treats advanced capabilities as backend-advertised options rather than universal promises.

### 2.2 Classic Winamp

**Observed strengths**

- The player, equalizer, and playlist form a recognizable modular stack; the user can see the performance tools at once.
- Transport, position, spectrum, and track identity are close together, supporting glanceable control.
- Classic skins make the player feel personal and culturally recognizable.
- Windowshade/compact behavior anticipates a small always-available player.
- Official desktop help describes playlist, EQ, skin, and color-theme options, alongside classic and modern skin support. [4](https://support.winamp.com/winamp-desktop-player-for-windows)
- Classic skin configuration separates visualization colors and playlist colors into editable text mappings. [6](https://winampskins.neocities.org/config)

**Shortcomings to avoid**

- Tiny bitmap-era controls and dense labels do not scale well to modern accessibility, touch, or high-zoom requirements.
- Icon-only or abbreviated controls can hide meaning from new users.
- Beveled surfaces and spectral color can compete with content if copied literally.
- Legacy skin portability is not the same as a safe, semantic, cross-platform skin contract.
- A fixed miniature canvas should not dictate modern minimum target sizes.

**Fusion decisions**

- Keep the **module grammar**: player → EQ → playlist, with a compact stack and a shade strip.
- Replace copied sprites with original vector bevels, gradients, and textures.
- Keep spectral energy but use a calmer palette and explicit mode labels.
- Preserve the cultural feeling of ownership without preserving 275-pixel-wide interaction constraints.
- Make Classic a presentation mode, not a separate playback implementation.

### 2.3 VOX for macOS

**Observed strengths**

- The public Mac page presents a compact, artwork-led player with format information and a restrained control surface. [1](https://vox.rocks/mac-music-player)
- The product emphasizes local/lossless and hi-res playback, EQ, gapless behavior, output settings, and multiple sources. [1](https://vox.rocks/mac-music-player)
- A small player can remain useful without turning into a full library browser.
- Source-format awareness is valuable to users who care about fidelity.

**Shortcomings to avoid**

- Compactness can hide queue context, advanced state, and the difference between source and output.
- Premium/source/cloud features can blur the boundary between a local player and a service.
- A minimalist surface may leave batch organization and recovery flows under-explained.
- Mac-specific output behavior should not be assumed on Windows, Linux, web, or mobile.

**Fusion decisions**

- Use artwork and track identity as the emotional center of Now Playing.
- Keep mini and shade modes genuinely small, but preserve identity, transport, and expansion.
- Show source quality as a badge and put detailed facts in Track Details.
- Keep local playback account-free in the proposed product; remote providers are optional extensions.
- Do not equate “24/96 source” with “24/96 currently reaching the device.”

### 2.4 AIMP

**Observed strengths**

- Official feature documentation covers multiple playlists, explicit playback queue, smart playlists, grouping, search, and per-playlist view settings. [2](https://www.aimp.ru/?do=features)
- The same documentation describes a 20-band EQ, effects, normalization, mixing options, library statistics, tag editing, chapters, and scheduling. [2](https://www.aimp.ru/?do=features)
- Skin transformers and high-DPI support demonstrate that depth and visual flexibility can coexist. [2](https://www.aimp.ru/?do=features)
- AIMP’s ecosystem treats organization and audio processing as first-class tasks rather than afterthoughts.

**Shortcomings to avoid**

- Feature breadth can produce dense settings trees and competing panels.
- Queue, playlist, selection, and library actions need explicit language to avoid accidental destructive operations.
- Advanced DSP and output options can intimidate users or imply fidelity guarantees that depend on the backend.
- A Windows-centered toolset should not be presented as identical across platforms.

**Fusion decisions**

- Adopt the **capability breadth**, not the density: Library, Playlists, Sound Studio, Skin Studio, and Settings are separate task groups.
- Make queue order and resume context visible in the same panel.
- Use numeric EQ values, presets, reset, and a processing-chain summary.
- Expose advanced output only when supported; explain route changes and processing effects.
- Keep batch tag editing explicit, reversible where possible, and separate from file renaming.

### 2.5 Cross-product decision matrix

| Aspect | Winamp contribution | VOX contribution | AIMP contribution | FUSE resolution |
|---|---|---|---|---|
| First impression | Performance identity | Calm artwork-led compactness | Functional breadth | Album-led workspace; tools one click away |
| Transport | Immediate and modular | Minimal | Feature-complete | Persistent shared transport; compact variant |
| Queue | Playlist adjacency | Compact context | Explicit queue | Separate “Play next” and “Then resumes at” regions |
| Library | Playlist editor | Source switching | Deep organization | Albums/tracks/artists/folders + smart playlists |
| EQ | Visible sliders | Approachable presets | Deep DSP | 10-band default; advanced chain capability-gated |
| Visualizer | Spectrum culture | Subtle presence | Flexible display | Four honest modes, pausable, SVG-driven |
| Skins | Strong identity | Restraint | Transformers | Semantic tokens + approved layout variants |
| Quality | Format readout | Hi-res awareness | Processing depth | Source / DSP / output facts separated |
| Accessibility | Needs modernization | Needs explicit depth | Needs progressive disclosure | Targets, focus, contrast, motion, and semantics locked |
| Safety | Legacy destructive ambiguity | Service boundary | Batch-operation risk | Explicit queue removal, tag save, and file deletion boundaries |

## 3. Scope, assumptions, personas, and success criteria

### 3.1 Proposed product scope

**Core v1 design scope:** local audio import and playback; library; playlists; explicit queue; favorites/history; search; track details; lyrics import; EQ and presets; output selection; sleep timer; mini/shade/focus modes; skins; accessibility; recovery; privacy controls.

**Conditional extensions:** radio/podcasts, network renderers, cloud sources, scrobbling, artwork lookup, CD tools, conversion, recording, exclusive/bit-perfect output, DSD, advanced DSP, mobile native integration. These require backend capability checks, permissions, and separate validation. They are not implied by the core SVG screens.

**Platform assumption:** desktop-first product with a responsive web/desktop implementation path and conceptual mobile layouts. Native window chrome, media keys, file permissions, safe areas, and audio-session behavior belong to the host integration layer.

### 3.2 Personas

| Persona | Primary job | What must be effortless | What must not happen |
|---|---|---|---|
| Casual listener | Play a local album | Import, play, pause, next, volume | Forced account, confusing queue, hidden exit |
| Collector | Organize a large library | Search, filter, batch tags, playlists | Silent file changes, mixed-value overwrite |
| Audiophile | Understand and shape output | Source facts, EQ, output route, gain | False bit-perfect claims, clipping surprises |
| Classic-player fan | Keep a compact performance player | Stack, shade, spectrum, skins | Tiny targets, lost queue when resizing |
| Keyboard/AT user | Operate without sighted pointer use | Focus, names, values, announcements | Icon-only meaning, focus traps, motion overload |
| White-label partner | Ship a branded player | Tokens, logo slot, skin validation | Brand colors breaking contrast or behavior |

### 3.3 Success criteria and measurement plan

These are **target thresholds for usability testing**, not results already achieved.

- First local track plays after a deliberate import/open action; measure completion and time on task.
- At least 90% of test participants can distinguish “Play next” from playlist context after one explanation.
- No critical task requires horizontal scrolling at the compact reference width or 200% text size.
- All core controls have accessible names, roles, states, and keyboard operation.
- A skin with failing contrast cannot be applied without an explicit, informed override; default skins must pass.
- Queue and playback state survive mode changes and ordinary restarts according to settings.
- Error recovery never silently deletes files or clears the queue.
- Visualizer pause stops visual updates without pausing audio.

## 4. Gap analysis and risk register

| ID | Gap / risk | Consequence | Design mitigation | Validation / owner |
|---|---|---|---|---|
| G01 | Source vs output quality conflation | Misleading fidelity claims | Separate badges and facts; processing summary | Audio engine + QA |
| G02 | Queue vs playlist ambiguity | Wrong next track; accidental removal | Explicit queue panel and resume context | UX test + state tests |
| G03 | Feature density | New-user confusion | Progressive disclosure; task-grouped settings | Tree test + first-run test |
| G04 | Legacy compact targets | Motor/accessibility failure | 40/44 px defaults; minimum 24 px | Accessibility audit |
| G05 | Skin breaks contrast/focus | Unusable branded product | Token validation and locked invariants | Automated skin tests |
| G06 | Fake reactive visuals | Loss of trust | Static frames labeled; live demo uses analyser | Signal-state tests |
| G07 | Motion overload | Distraction or adverse reaction | Pause/static mode; reduced-motion default | WCAG review + user test |
| G08 | Batch tag overwrite | Data loss | Mixed values; explicit save; preview | File-operation tests |
| G09 | Unsupported backend toggle | Broken promise | Capability registry; hide/explain unavailable | Platform integration tests |
| G10 | Remote/local boundary blur | Privacy surprise | Local-first defaults; opt-in providers | Privacy review |
| G11 | Stream treated as file | Broken seek/duration UI | Stream-specific state and disabled seek | Radio/stream tests |
| G12 | Mode change loses state | User disorientation | Shared store; mode is presentation only | Integration tests |
| G13 | Long metadata overflow | Hidden identity/actions | Truncation + full details; stable action slots | Long-string/RTL tests |
| G14 | Modal hides recovery | Trapped user | Focus trap, Esc, cancel, persistent errors | Keyboard/AT tests |
| G15 | SVG-only production semantics | Screen-reader failure | SVG presentation + native/HTML control layer | AT smoke tests |
| G16 | Skin code execution | Security risk | Data-only skins; no scripts/external fetch | Schema/security review |
| G17 | Large library performance | UI stalls | Virtualized lists; incremental indexing | 100k-track benchmark |
| G18 | Audio/visual thread contention | Dropouts or jank | Audio thread isolated; bounded visual work | Performance profiling |
| G19 | Offline source ambiguity | Dead controls | Available/unavailable badges; local fallback | Disconnect tests |
| G20 | Unclear destructive scope | File deletion fear | “Remove from playlist” vs “Delete file” labels | Copy review + confirmation test |

### Known limitations of this deliverable

- No production audio decoder, database, native file-permission layer, or platform media-session integration is implemented.
- No formal usability study, screen-reader certification, or WCAG conformance audit has been performed.
- The waveform lab is a demonstration using browser audio analysis; it is not a reference DSP implementation.
- Mobile screens are design concepts; native gesture, safe-area, and background-audio behavior remain implementation work.
- Advanced AIMP-like tools are inventoried and gated, not all given full production screens in v1.
