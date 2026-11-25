## 5. Feature inventory and priority model

**P0** = required for a coherent local player; **P1** = strong differentiator; **P2** = conditional extension; **R** = research before commitment.

| Area | Feature | Priority | UI surface | Dependency / note |
|---|---|---:|---|---|
| Playback | Open files/folders; play/pause/stop; previous/next; seek; volume/mute | P0 | Transport, import, dialogs | Decoder and host file access |
| Playback | Shuffle; repeat off/all/one; gapless where supported | P0/P1 | Transport, settings | Gapless is capability-gated |
| Playback | Resume track/position; restore queue | P1 | Settings + startup | Persisted state |
| Queue | Play next; add to queue; reorder; remove; clear; undo | P0 | Queue panel/sheet | Explicit queue store |
| Queue | Resume visible playlist context | P0 | Queue panel | Context pointer |
| Library | Index folders; incremental scan; cancel; partial results | P0 | Import, library settings | Non-destructive indexing |
| Library | Albums/tracks/artists/folders; grid/list; sort/filter | P0 | Library | Database + virtualization |
| Library | Search across local metadata | P0 | Global search | Scoped query; no implicit remote |
| Playlists | Multiple playlists; create/rename/duplicate; M3U/M3U8 export | P0/P1 | Playlists | Path portability policy |
| Playlists | Smart playlists with readable rules | P1 | Playlist builder | Query engine |
| Organization | Favorites; ratings; history; play counts | P1 | Library/history | Local metadata/store |
| Metadata | Single/batch tags; mixed values; artwork; explicit save | P1 | Tag editor | Format-specific write support |
| Metadata | File rename preview; chapter/CUE editing | P2 | Advanced tools | Separate destructive preview |
| Sound | 10-band EQ; preamp; presets; reset; numeric values | P0/P1 | Sound studio | DSP backend |
| Sound | ReplayGain/normalization; clipping protection | P1 | Settings + chain | Measurement and limiter |
| Sound | Crossfeed; tempo/pitch; effects; 20-band EQ | P2 | Advanced sound | Capability-gated |
| Output | Device chooser; route-change warning | P0/P1 | Output dialog | Host audio API |
| Output | Exclusive/bit-perfect; DSD; multichannel | P2/R | Capabilities | Backend + device negotiation |
| Visuals | Waveform/spectrum/oscilloscope/static; pause | P0/P1 | Signal region/focus view | Analysis data; reduced motion |
| Modes | Workspace; focus; mini; shade; Classic stack | P1 | Mode switcher | Shared state |
| Skins | Dark/light/high-contrast/Classic; token editor; import | P1 | Skin studio | Data-only schema + validation |
| Accessibility | Keyboard map; focus; zoom; reduced motion; AT semantics | P0 | Everywhere | Native/HTML control layer |
| Comfort | Sleep timer with fade/pause outcome | P1 | Timer dialog | No implicit system shutdown |
| Information | Track facts; embedded/local lyrics; LRC | P1 | Track details | No automatic remote fetch |
| Recovery | Missing file; decode error; permissions; offline; retry | P0 | Alerts/recovery screens | Preserve queue/library |
| Privacy | Source-folder control; export; clear history/cache | P0/P1 | Settings | Non-destructive data controls |
| Remote | Saved radio URLs; podcasts; reconnect | P2 | Radio/podcasts | Stream semantics; permissions |
| Remote | Cloud/artwork/scrobbling/providers | P2/R | Integrations | Opt-in; privacy review |
| Tools | Converter; CD rip; recording; scheduler shutdown | P2/R | Advanced tools | Legal/platform/backend review |

### Progressive disclosure policy

- **Level 1 — Listen:** import, play, pause, next, volume, queue, search.
- **Level 2 — Organize:** playlists, favorites, history, tags, smart rules.
- **Level 3 — Shape:** EQ, presets, normalization, output, timer, skins.
- **Level 4 — Extend:** providers, advanced DSP, exclusive output, conversion, recording.

A feature never appears as an enabled control merely because a reference product has it. The capability registry determines whether it is available, unavailable with explanation, or hidden because the platform cannot support it.

## 6. Information architecture and navigation

### Primary navigation

```text
FUSE shell
├── Now playing
│   ├── Performance / artwork / signal
│   ├── Explicit queue preview
│   └── Track details / lyrics
├── Library
│   ├── Albums
│   ├── Tracks
│   ├── Artists
│   └── Folders
├── Playlists
│   ├── Standard playlists
│   ├── Smart playlists
│   └── Playlist builder
├── Favorites
├── History
├── Radio / Podcasts [conditional]
├── Sound studio
│   ├── EQ / presets
│   ├── Processing chain
│   └── Output capabilities
├── Skin studio
│   ├── Installed skins
│   ├── Token editor
│   └── Import / validation
└── Settings
    ├── Audio
    ├── Library / sources
    ├── Appearance / accessibility
    ├── Shortcuts
    └── Privacy / data
```

### Navigation rules

- Desktop ≥1200 px: persistent labeled sidebar; content and queue may coexist.
- 900–1199 px: labeled horizontal tabs; queue becomes a panel/sheet when space is insufficient.
- <900 px: single-column content; persistent mini transport; queue is a labeled sheet.
- Mobile: bottom navigation only when it does not compete with the mini player; otherwise labeled header tabs and a back stack.
- Sound Studio, Skin Studio, and Settings are reachable from the header and command search; they are not buried inside Now Playing.
- Active navigation is indicated by tint **and** position/weight; focus is a separate ring.
- Core destinations are not disabled when empty; they open useful empty states.

### Search and command behavior

- `Ctrl/⌘+F` focuses local search. Results are grouped by type: artist, album, track, playlist, station.
- Typing never triggers playback. Enter opens the highlighted result; an explicit Play action starts audio.
- Remote search is labeled and opt-in. Offline remote results are marked unavailable.
- Search preserves the player and explicit queue. Closing search returns focus to the invoking control.
- Recent searches are local and clearable; no query is sent to a provider without consent.

## 7. Core object model and playback semantics

### 7.1 Separate objects

| Object | Meaning | Visual treatment | Typical actions |
|---|---|---|---|
| Library item | Indexed audio file and metadata | Normal row/card | Play, queue, favorite, edit |
| Playback context | Ordered source: album, playlist, folder | “Playing from …” header | Play context, shuffle context |
| Current track | Audio actually playing or paused | Accent title + signal icon | Pause, seek, details |
| Explicit queue | User-added future items overriding context | “Up next” panel + order | Reorder, remove, clear |
| Selection | Rows targeted by a batch action | Checkbox + selection tint | Queue, playlist, tags |
| Favorite | User-marked item independent of playback | Heart/state label | Toggle favorite |
| History | Record of past playback | Timestamped list | Replay, queue, clear |
| Stream | Remote live source | Buffering/live badge | Retry, stop; no file seek |

### 7.2 Queue algorithm (specified behavior)

1. Playing a context sets `contextId`, `contextOrder`, and `contextIndex`; it does not silently copy the entire library into the explicit queue.
2. “Play next” inserts after the current item in the explicit queue. “Add to queue” appends.
3. At track end, consume the first explicit queue item if one exists.
4. When the explicit queue is empty, advance the context according to shuffle/repeat settings.
5. Removing a queued item changes only the queue. Undo restores its position if the surrounding context is still valid.
6. Clearing the queue leaves the current track and context intact; show the resume point.
7. If the resume item is unavailable, enter recovery and preserve the remaining context.
8. Shuffle affects context traversal, not the user’s explicit queue order, unless the user explicitly chooses “Shuffle queue.”
9. Repeat One repeats the current track only when the explicit queue is empty; otherwise the queue still advances. This rule must be explained in the repeat tooltip.
10. Mode changes never mutate queue order.

### 7.3 Playback state machine

```text
empty ──open/import──> ready
ready ──play──> loading ──success──> playing
loading ──failure──> error
loading ──cancel──> ready
playing ──pause──> paused ──play──> playing
playing ──buffer underrun──> buffering ──data──> playing
playing/paused ──stop──> stopped
playing/paused ──end──> next decision
next decision ──queue item──> loading
next decision ──context item──> loading
next decision ──no next──> stopped
error ──locate/retry──> loading
error ──skip──> next decision
buffering ──retry exhausted──> error
```

**UI truth table**

| State | Primary button | Signal | Seek | Queue | Recovery |
|---|---|---|---|---|---|
| Empty | Disabled Play with explanation | Static placeholder | Disabled | No context | Import/open |
| Loading | Cancel/back where safe | Static + progress | Disabled until duration known | Target visible | Timeout/retry |
| Playing | Pause | Live or paused visuals | Enabled for seekable media | Current marked | Pause/next |
| Paused | Play | Frozen frame | Enabled | Position retained | Resume |
| Buffering | Pause/skip | Last frame + label | Only if stream semantics allow | Honest position | Retry/local |
| Stopped | Play from start | Static art | Reset/disabled by policy | Context retained | Choose track |
| Error | Retry only if safe | No fake live signal | Disabled | Preserved | Locate/skip/diagnostics |
| Offline | Local playback enabled | Local only | Local rules | Remote marked unavailable | Retry remote later |

### 7.4 Quality and processing model

- `source`: codec, sample rate, bit depth, channels, bitrate, duration, file size, ReplayGain tags.
- `processing`: EQ enabled, preamp, normalization, crossfeed, limiter, effects, measured gain changes.
- `output`: selected device, negotiated format, exclusive/shared mode, channel mapping, backend status.

The UI displays source badges by default. A “bit-perfect” claim requires an end-to-end verified path and is suppressed when EQ, gain, crossfeed, mixing, or unsupported conversion is active. Peak/RMS values are analysis measurements, not a guarantee of analog output level.

## 8. End-to-end user flows

### 8.1 First import

1. Welcome screen explains local-only indexing and no automatic playback.
2. User chooses a folder or files; host permission prompt is separate and explicit.
3. Indexing starts incrementally; existing results remain usable.
4. Progress shows processed/total when known; indeterminate progress is labeled when total is unknown.
5. Unsupported, permission-denied, and missing files appear in a review list.
6. Cancel stops indexing and keeps completed results; it does not delete audio.
7. Library ready; user presses Play deliberately.

**Failure exits:** permission denied → explain access and retry; disconnected drive → mark source offline; partial decode issues → keep valid tracks.

### 8.2 Play and queue

1. User chooses a track/album or presses Play on a context.
2. Loading state appears; transport and identity update together.
3. Playing state updates all modes and the signal.
4. “Play next” adds an item and announces the new count; undo is available.
5. Queue panel shows explicit items and “Then resumes at …”.
6. Reorder by drag handle or `Alt+Up/Down`; insertion line and announcement confirm the move.
7. Remove/clear is non-destructive and undoable.

### 8.3 Batch tag edit

1. Select rows; selection toolbar appears.
2. Open Edit metadata; mixed values remain “Multiple values.”
3. Changed fields are marked; untouched mixed fields stay untouched.
4. Artwork replacement and numbering are separate choices.
5. Save writes supported embedded tags; filename renaming is not implied.
6. Per-file failures retain form edits and identify the affected files.
7. Unsupported fields are read-only with an explanation.

### 8.4 Skin change

1. Open Skin Studio; choose an installed skin or import a data-only package.
2. Preview tokens in desktop/compact/mobile variants.
3. Validate contrast, target sizes, required slots, font fallback, and schema version.
4. Apply explicitly; previous skin remains available for undo.
5. Invalid skin is rejected without changing the current skin.
6. Restore defaults is always reachable.

### 8.5 Sleep timer

1. Choose a preset or custom duration.
2. Choose outcome: fade then pause, pause at end of track, or another supported action.
3. Confirm; timer badge shows remaining time and outcome.
4. Cancel restores normal playback without changing files.
5. System shutdown/hibernate is a separate permission-gated feature, never the default timer outcome.

### 8.6 Error recovery

1. Playback pauses safely; current item and queue are preserved.
2. Persistent alert identifies the file/problem and likely cause.
3. Locate file, retry, skip, or copy diagnostics are explicit.
4. Diagnostics exclude audio contents and private paths by default.
5. Skip advances according to queue/context rules; it does not clear the queue.

## 9. Layout system, responsive behavior, and modes

### Reference canvases

| Surface | Canvas | Purpose |
|---|---:|---|
| Desktop workspace | 1440 × 960 | Flagship layout and redlines |
| Medium workspace | 1100 × 820 | Tablet/small desktop reflow |
| Compact desktop | 720 × 760 content region | Single-column behavior |
| Mini player | 420 × 248 | Small persistent player |
| Shade strip | 560 × 72 | Minimal transport + identity |
| Classic stack | 880 px reference width; 560 px minimum | Player/EQ/playlist modules |
| Mobile | 390 × 844 | Touch-first concept |

These are logical-pixel design references, not fixed production window sizes. Production reflows content and permits vertical scrolling; it does not uniformly scale the desktop UI down.

### Desktop grid

- Sidebar: 224 px at the flagship reference.
- Content gutter: 24 px; internal region gaps: 24–32 px.
- Now Playing artwork: 328 px reference; identity column fluid; queue: 480 px reference.
- Signal region spans content width; transport is fixed at the bottom.
- Panel radius: 12–14 px; control radius: 8–10 px; pill radius: half height.
- Base spacing: 4 px; common steps: 4, 8, 12, 16, 24, 32, 48, 64.

### Reflow rules

- ≥1200: sidebar + content + optional queue column.
- 900–1199: labeled tabs; artwork/identity and queue stack or share a row when space allows.
- <900: single column; queue opens as a sheet; transport remains persistent.
- Mobile: artwork scales to available width; metadata wraps; secondary actions move to labeled overflow only when necessary.
- At 200% text size, action labels wrap or controls grow vertically; no clipped primary actions.
- Long titles truncate visually with full value in details/accessible name; primary action labels never truncate.
- RTL mirrors navigation and row order, but time progression and transport direction follow locale/media conventions and are tested explicitly.

### Mode contract

| Mode | Keeps | Adds / changes | Must not do |
|---|---|---|---|
| Workspace | Full library + transport | Queue/signal regions | Hide core playback |
| Focus | Identity + signal + transport | Large visualization, exit | Trap without Esc/back |
| Mini | Identity + transport + expand | Compact signal | Clear queue or lose state |
| Shade | Identity + essential transport + expand | Minimal height | Hide expand or shrink targets below policy |
| Classic | Same objects/state | Modular stack, metal texture | Change queue semantics or use legacy tiny targets |

## 10. Visual language and design tokens

### Semantic palette — Studio Dark

| Token | Value | Role |
|---|---|---|
| `surface.canvas` | `#101519` | Deepest background |
| `surface.shell` | `#151C21` | App shell / sidebar |
| `surface.panel` | `#1B242B` | Panels and transport |
| `surface.raised` | `#243139` | Hover / selected / raised controls |
| `border.default` | `#35454E` | Subtle separation; not sole control boundary |
| `text.primary` | `#F3F7F6` | Main text |
| `text.secondary` | `#ADBDC5` | Metadata / supporting text |
| `text.tertiary` | `#84969F` | Low-emphasis labels; validate on actual surface |
| `accent.primary` | `#79E3C2` | Primary action / active signal |
| `accent.on-primary` | `#10251F` | Text/icon on mint |
| `accent.secondary` | `#F3C580` | Warm highlight / peaks |
| `info` | `#91BFFF` | Informational accent |
| `warning` | `#F3C580` | Attention; paired with icon/text |
| `danger` | `#FF9B9B` | Error/destructive; paired with message |
| `focus.ring` | `#FFFFFF` | High-contrast focus indicator |

### Daylight mapping

Canvas `#E9EFEE`; shell `#F7FAF9`; panel `#FFFFFF`; raised `#E7EFED`; text `#172B27`; secondary text `#4E655F`; accent `#116B53`; on-accent `#FFFFFF`; warning `#8B530D`; danger `#A32D38`. Light theme uses darker semantic colors rather than inverting dark-theme accents.

### High Contrast mapping

Canvas/shell `#000000`; panel `#101010`; raised `#202020`; border `#BDBDBD`; text `#FFFFFF`; secondary `#E0E0E0`; accent `#A8FFDA`; on-accent `#000000`. The same components and layout are retained.

### Typography

- Primary: Inter / system sans fallback (`SF Pro Display`, `Segoe UI`, Arial, sans-serif).
- Numerals/time/code: JetBrains Mono / SFMono-Regular / Consolas / monospace; tabular numerals.
- Scale: display 40/54; screen title 28/38; section 18/24; body 14/20; metadata 12/16; overline 11/14.
- Weights: 400 body, 500 labels, 600 section/action, 650–750 display/brand where supported.
- SVG sources use live text for editability. Production may use native text; export outlines only for final static artwork if font licensing and editing requirements allow.

### Elevation and texture

- Default: tonal surfaces + 1 px borders; shadows are optional and never the only boundary.
- Classic: original vector bevel gradient, restrained highlights, no copied bitmap sprites.
- Album art: original vector geometry; real user artwork is raster-safe inside a vector frame.
- No glass blur over dense text; no continuous background animation behind reading content.

## 11. Reusable component inventory and state contracts

### 11.1 Component registry

| ID | Component | Variants | Required states | Key rules |
|---|---|---|---|---|
| C01 | Button | Primary, secondary, quiet, destructive | Default, hover, focus, pressed, disabled, loading | 40 px desktop / 44 touch; label or accessible name |
| C02 | Icon button | Ghost, solid, active | Default, hover, focus, pressed, disabled | 40/44 wrapper; tooltip + accessible name |
| C03 | Split button | Primary + menu | Closed, open, focused, disabled | Menu does not change primary meaning |
| C04 | Segmented control | 2–4 options | Selected, unselected, focus, disabled | Selected uses tint + weight/position |
| C05 | Tabs | Workspace, library, settings | Active, hover, focus, overflow | Labels persist; arrow-key navigation |
| C06 | Navigation item | Sidebar, header, mobile | Default, active, hover, focus | Icon + label; empty destination remains usable |
| C07 | Search field | Inline, command | Empty, typed, loading, results, no results, error | Typing never auto-plays |
| C08 | Text field | Default, numeric, multiline | Default, focus, filled, error, disabled, read-only | Label outside; error identifies correction |
| C09 | Select / combobox | Native-like, searchable | Closed, open, selected, focus, unavailable | Capability unavailable explained |
| C10 | Checkbox | Unchecked, checked, mixed | Focus, disabled | Mixed never silently overwrites |
| C11 | Radio | Unselected, selected | Focus, disabled | One choice in group |
| C12 | Switch | On, off | Focus, disabled, pending | State label; pending not shown as applied |
| C13 | Slider | Seek, volume, EQ, preamp | Default, hover, focus, drag, disabled | Value text; keyboard steps; min/max |
| C14 | Rating | 0–5 stars | Empty, partial, full, focus | Accessible value; not color-only |
| C15 | Badge | Format, quality, queue, live, offline | Neutral, soft, warning, error | Short factual text; details available |
| C16 | Transport | Full, compact, shade | Empty, loading, playing, paused, buffering, error | Shared state; stable geometry |
| C17 | Track row | Default, current, selected, queued, unavailable | Hover, focus, drag, drop-target | Current ≠ selected ≠ queued |
| C18 | Album card | Grid, compact | Default, hover, focus, unavailable | Play action explicit; card opens details |
| C19 | Queue item | Pending, current, resume | Hover, focus, drag, removing | Handle + remove; non-destructive |
| C20 | Playlist row | Standard, smart, offline | Default, active, focus, editing | Type and availability visible |
| C21 | Progress | Determinate, indeterminate | Running, paused, canceled, complete | Label; cancel when supported |
| C22 | Alert | Info, success, warning, error | Inline, persistent, dismissible | Error persists; undo when useful |
| C23 | Toast | Success, undo, info | Enter, hover/focus, dismiss | Never sole error record |
| C24 | Dialog | Confirm, form, chooser | Open, focus, submitting, error | Focus trap; Esc/cancel; return focus |
| C25 | Menu / popover | Context, overflow, select | Open, focus, disabled item | One top layer; predictable close |
| C26 | Tooltip | Label, shortcut, explanation | Delayed, focus-visible | Not sole carrier of critical info |
| C27 | Empty state | Library, search, lyrics, queue | Empty, loading, offline | One primary next action |
| C28 | Signal | Wave, spectrum, scope, static | Live, paused, frozen, unavailable | Pause visuals ≠ pause audio |
| C29 | Skin card | Installed, preview, invalid | Default, selected, hover, focus | Validation before apply |
| C30 | Token field | Color, number, enum | Valid, invalid, pending | Semantic name; contrast feedback |
| C31 | Shortcut row | Default, recording, conflict | Focus, conflict, saved | Conflict before save; restore defaults |
| C32 | Timer chip | Duration, outcome | Running, paused, expired | Outcome explicit; cancel reachable |
| C33 | Source row | Available, offline, permission | Default, focus, removing | Remove source ≠ delete files |
| C34 | Capability row | Supported, unsupported, unknown | Available, disabled, checking | Never fake an enabled toggle |
| C35 | Window/mode control | Mini, shade, focus, expand | Default, focus, unavailable | Exit always reachable |

### 11.2 Interaction geometry

- Minimum pointer target: 24 × 24 CSS px, consistent with WCAG 2.2 Target Size (Minimum); design defaults are 40 px desktop and 44 px touch. [8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- Icon glyph: 20–24 px inside a 40/44 px wrapper.
- Track row: 56 px default; compact desktop may use 48 px; touch does not go below 44 px.
- Button: 40 px high, 9 px radius, 14 px horizontal padding; icon 18 px + 10 px gap.
- Focus ring: 2 px, 2 px offset, drawn above state tint; never removed.
- Drag handle: visible grip; keyboard alternative `Alt+Up/Down`; insertion line plus announcement.
- Sliders: Arrow = small step; Page = larger step; Home/End = bounds; numeric value available.

### 11.3 State layering

1. Surface token.
2. Hover/selected/pressed tint.
3. Content: icon, label, value.
4. Focus ring.
5. Drag insertion/error message.

Disabled controls reduce emphasis but retain readable explanation. Loading controls preserve geometry and expose a busy state; they do not silently change action meaning.

## 12. Waveform, spectrum, and motion system

### 12.1 Four presentation modes

| Mode | Data | Best use | Truthfulness rule |
|---|---|---|---|
| Mirrored waveform | Time-domain envelope / amplitude history | Default listening and seek context | Played/unplayed distinction; no fake live motion |
| Spectrum | FFT magnitudes grouped into log-spaced bands | Classic performance view | Label analysis; peak caps decay honestly |
| Oscilloscope | Time-domain samples | Signal inspection | Stable centerline; clipping indicator separate |
| Static / reduced motion | Artwork + optional numeric state | Accessibility / low power | No continuous motion; audio unaffected |

### 12.2 Data pipeline

```text
Decoder / source
  → optional DSP chain
  → analysis tap (post-processing, pre-output where supported)
  → bounded ring buffers
  → UI aggregation worker / throttled bridge
  → SVG path / rect / transform updates
  → output device
```

- Audio rendering remains on the audio thread; UI work never blocks it.
- Web demonstration uses `AnalyserNode` time-domain and frequency data. MDN documents `getFloatTimeDomainData` and `getFloatFrequencyData` for these purposes. [9](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode)
- Native implementations use an equivalent analysis tap and a bounded queue; they do not copy entire audio buffers to the UI.
- Analysis point is labeled. Post-DSP analysis does not prove the final device output format.
- When no fresh data exists, freeze the last frame and label it; do not generate random “live” bars.

### 12.3 Visual update budget

- Target: 30 fps visual updates on desktop; 20 fps in compact/low-power mode; static when paused or hidden.
- Aggregate to 96–192 waveform columns and 32–64 spectrum bands for typical panels; scale down on compact surfaces.
- Reuse SVG nodes and update attributes; do not rebuild the entire SVG tree every frame.
- Use a ring buffer for history; bound memory and drop old visual frames rather than audio.
- Pause when the document/window is hidden; resume with fresh data, not stale animation.
- Reduced motion defaults to static or low-rate numeric updates; no flashing, strobing, rotation, or camera zoom.
- Visualization pause is separate from audio pause and is always reachable in focus view.

### 12.4 Seeking versus signal pause

- Seek slider: changes playback position; drag previews time, release commits.
- Signal pause: stops visual updates only.
- Static mode: replaces animated presentation without changing playback.
- Live streams: disable file-style seeking and duration; show live/buffering state instead.

### 12.5 SVG production contract

- Root SVG has `viewBox`, title/desc for meaningful artwork, and stable IDs.
- Decorative layers are hidden from assistive technology; interactive controls have native/HTML semantics.
- Use `path`, `rect`, `circle`, `line`, `text`, `clipPath`, gradients, and symbols; no external scripts in skin assets.
- Waveform group exposes `data-role="signal"` and mode/state attributes.
- Skin tokens map to fills/strokes through a controlled theme layer; arbitrary CSS/JS injection is forbidden.
- Static design SVGs are illustrative frames. The interactive lab is the only artifact that claims live audio-driven updates.

## 13. Skin architecture and white-label contract

### 13.1 What a skin may change

- Semantic colors, approved typography scale/family fallback, radius, border weight, texture, vector artwork, logo slot, signal palette, and approved layout variant.
- Density within locked minimum target sizes.
- Decorative bevels/gradients in Classic mode.

### 13.2 What a skin may not change

- Control meaning, queue semantics, playback state truth, focus order, minimum targets, error honesty, privacy defaults, or permission boundaries.
- Add executable scripts, remote fetches, arbitrary HTML, or new privileged actions.
- Remove labels from core navigation or hide the exit from compact/focus modes.

### 13.3 Package structure

```text
brand-skin/
├── manifest.json       # schema version, id, name, version, capabilities
├── tokens.json         # semantic values only
├── assets/
│   ├── logo.svg        # optional white-label mark
│   ├── texture.svg     # optional decorative vector texture
│   └── fallback-art.svg
└── preview.svg         # optional static preview
```

### 13.4 Validation pipeline

1. Parse JSON against schema; reject unknown executable fields.
2. Check schema version and required semantic tokens.
3. Resolve colors and compute contrast against actual adjacent surfaces.
4. Validate radius/density bounds and required layout slots.
5. Sanitize SVG assets: no scripts, event handlers, external references, or foreign objects.
6. Render preview in desktop/compact/mobile variants.
7. Run focus/target/overflow checks.
8. Apply only after explicit confirmation; keep previous skin for undo.

### 13.5 White-label slots

- `brand.logo`, `brand.wordmark`, `brand.productName`, `brand.accent`, `brand.surface`, `brand.signalPalette`.
- Default demonstration brand is FUSE; replace all brand strings and logo geometry through tokens/assets, not by editing component behavior.
- Legal/trademark clearance for a final brand is outside this design study.

### 13.6 Classic skin specifics

- Original metal gradient and bevel geometry; no Winamp sprite extraction.
- Player/EQ/playlist modules share the same store as workspace mode.
- Minimum logical width 560 px; reference stack 880 px.
- EQ bands retain numeric values and reset; playlist rows retain readable labels and modern targets.
- Shade mode keeps essential transport and expand; it is not a pixel-perfect legacy clone.

## 14. Accessibility and inclusive interaction

### Normative targets

- Text contrast ≥4.5:1 for normal text; large text ≥3:1, with documented exceptions. [7](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- Meaningful control boundaries/state indicators and focus indicators ≥3:1 against adjacent colors where required. [10](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- Pointer targets ≥24 × 24 CSS px minimum; default 40/44 px. [8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- Moving/auto-updating content has pause/stop/hide control; reduced motion is respected. [11](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- Core playback remains usable at 200% text size and compact equivalent width; test 400% zoom reflow behavior.

### Keyboard contract

| Key | Action | Scope / guard |
|---|---|---|
| Space | Play/pause | Not while typing or activating a focused button |
| Left/Right | Seek ±5 s | Seekable media only |
| Shift+Left/Right | Seek ±30 s | Clamp to bounds |
| Up/Down | Volume ±1% | When transport region is focused |
| M | Mute/unmute | Not while typing |
| Q | Add selection to queue | Announce count + undo |
| Alt+Up/Down | Reorder queue item | Focused queue item only |
| Ctrl/⌘+F | Search | Focus search field |
| Ctrl/⌘+, | Settings | Preserve return focus |
| Esc | Close top layer | Then leave focus view; never quit app |
| ? | Shortcut reference | Not while typing |

All bindings are remappable; conflicts are detected before save. OS media keys remain host-managed unless a separately permitted global-shortcut integration exists.

### Assistive technology contract

- SVG is presentation; production controls are native buttons/inputs or correctly roled HTML/SVG hybrids.
- Every icon button has an accessible name; decorative SVG is hidden.
- Sliders expose min/max/current value and units.
- Queue changes announce item, new position, and count; not every animation frame.
- Current track changes announce once; buffering/error changes announce once.
- Modal dialogs trap focus, close with Esc/cancel, and return focus to the invoker.
- Focus is never obscured by sticky transport or overlays.
- Color is reinforced by text, icon, shape, or position.

### Motion and sensory safety

- No flashing/strobing; no rapid full-screen luminance changes.
- Reduced motion: static artwork or low-rate numeric signal; no slide/bounce/pulse.
- Hover/focus pauses toast dismissal; errors remain persistent.
- Audio never starts automatically on import, skin apply, or mode change.

## 15. Content, error, empty, and recovery design

### Voice and terminology

- Use “Play next,” “Add to queue,” “Then resumes at,” “Remove from playlist,” “Delete file,” “Source quality,” “Output device,” “Pause visualization.”
- Avoid ambiguous “Add,” “Remove,” “HD,” “Lossless output,” or “Live” without context.
- Error copy: what happened → what remains safe → what the user can do.
- Counts are explicit: “3 explicit tracks,” “8 tracks · 34 min,” “1,668 of 2,418 files indexed.”

### Empty states

| Surface | Message pattern | Primary action |
|---|---|---|
| Library | No albums yet; choose a folder | Choose folder |
| Search | No local matches; check spelling or filters | Clear filters |
| Queue | No explicit items; context resumes | Add selected / open library |
| Lyrics | No embedded lyrics; add local file | Add lyrics file |
| History | No listening history yet | Play something |
| Radio offline | Station unavailable; local library remains | Retry / return to library |

### Error taxonomy

- Missing file → locate/skip; preserve queue.
- Unsupported codec → explain format support; keep valid library items.
- Permission denied → explain access; retry after permission.
- Decode failure → retry/skip; diagnostics on request.
- Tag write failure → retain edits; identify files.
- Device unavailable → keep current route or choose another; warn about brief pause.
- Skin invalid → reject; keep current skin.
- Stream reconnecting → show attempt/buffer state; retry/local fallback.

### Destructive boundaries

- Remove from playlist ≠ remove source folder ≠ delete audio file.
- Clear history ≠ clear favorites ≠ clear queue.
- Clear cache ≠ remove indexed library.
- System shutdown is never the default sleep-timer outcome.
- Confirmation dialogs name the exact scope and offer a safe default.
