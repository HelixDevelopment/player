## 16. Full SVG design gallery and screen specifications

The following 50 vector artifacts are embedded directly in this Markdown. Each has a stable ID, editable source in `svg/`, and a source listing in Appendix A. Static frames are design illustrations; interactive behavior is specified in the contracts above and demonstrated only in the separate waveform lab.

### Gallery index

| ID | Artifact | Category | Primary purpose |
|---|---|---|---|
| `01-now-playing-dark` | Now playing — Studio Dark | Full screens | Album-led desktop workspace with persistent transport, explicit queue, source-quality metadata and reactive waveform. Fictional music and original vector sleeve. |
| `02-library-albums` | Library — album grid | Full screens | Original vector album covers; persistent navigation, search, import, view switches and sorting. Grid is a library view, not a music recommendation service. |
| `03-library-tracks-selection` | Library — tracks and bulk selection | Full screens | Selection toolbar exposes queue, playlist and tag actions. Current playback, selection and explicit queue are separate concepts. |
| `04-queue-and-context` | Queue — explicit next versus playlist context | Full screens | Queue panel shows consumed order and resume point. Grip handles support keyboard reorder; removal is non-destructive. |
| `05-immersive-visualizer` | Immersive visualizer — waveform focus | Full screens | Large live signal with visible pause control, stable metadata and exit route. Static SVG is an illustrative frame; companion demo drives paths from audio analysis. |
| `06-equalizer-dsp` | Sound studio — equalizer and DSP | Full screens | Numeric band values, reference preset, reset, preamp and explicit processing status. Advanced effects are capability-gated. |
| `07-skin-studio` | Skin studio — safe white-label theming | Full screens | Token-based skins, live preview and explicit apply semantics. Classic styling changes presentation, not queue or playback behavior. |
| `08-settings-audio` | Settings — audio and playback | Full screens | Output selection, gapless, resume, queue persistence and normalization. Unsupported engine capabilities are not presented as working toggles. |
| `09-metadata-editor` | Metadata editor — safe batch editing | Full screens | Mixed values, explicit save, artwork replacement and file-permission checks. Tag writes and file renaming are separate operations. |
| `10-search-command` | Search — keyboard-first local results | Full screens | Modal search preserves the player, distinguishes result types and exposes keyboard navigation. No implicit remote search or playback. |
| `11-onboarding-empty` | First run — consent-led import | Full screens | No automatic folder scanning or playback. Empty transport is disabled in implementation; this SVG is a layout illustration. |
| `12-errors-recovery` | Recovery — missing files and partial import | Full screens | Actionable errors preserve the library and queue. Diagnostics are copied only on request; no silent destructive cleanup. |
| `13-now-playing-light` | Now playing — Daylight skin | Full screens | Light theme uses darker semantic colors rather than inverting dark-theme accents. Same layout, hierarchy and control semantics. |
| `14-classic-compact` | Classic Metal — compact modular stack | Full screens | Original beveled surfaces, spectral display, transport, EQ and playlist modules. Modern target sizes and readable labels replace tiny legacy controls. |
| `15-mini-and-shade` | Mini player and shade mode | Full screens | Compact layouts preserve transport, identity and expansion. Shared state, no hidden queue destruction, no legacy tiny-target requirement. |
| `16-mobile-screens` | Mobile — player, library and queue | Full screens | Touch-first 44 px targets, readable hierarchy and explicit queue semantics. Conceptual mobile layouts; native safe areas and gestures require platform implementation. |
| `17-tablet-workspace` | Medium workspace — 1100 px | Full screens | Navigation becomes labeled horizontal tabs; artwork, metadata, queue and waveform remain visible without horizontal scrolling. |
| `18-sleep-timer-dialog` | Sleep timer — explicit action and outcome | Full screens | Modal dialog distinguishes pause from system shutdown, exposes duration and fade behavior, and preserves playback state on cancel. |
| `19-radio-stream-state` | Radio — saved stations and reconnect state | Full screens | Provider-independent saved URLs, explicit buffering and retry. Live streams do not inherit local-file seeking or duration assumptions. |
| `20-track-details-lyrics` | Track details — facts and lyrics empty state | Full screens | Separates source facts from output claims; lyrics are local and user-supplied unless a separately consented provider is configured. |
| `21-history-favorites` | History — local listening record | Full screens | Local history with explicit clearing and separate favorites. No automatic scrobbling or cloud account implied. |
| `22-import-progress` | Import — incremental progress and cancellation | Full screens | Partial results remain usable, indexing is non-destructive, and cancel does not silently delete indexed tracks. |
| `23-wireframe-desktop` | Desktop structural wireframe | Wireframes & maps | Regions and behavior before decoration: persistent navigation, adaptive content, explicit queue, pausable signal and persistent transport. |
| `24-information-architecture` | Information architecture and navigation contract | Wireframes & maps | Five task groups with cross-cutting queue, search, accessibility and capability rules. |
| `25-wireframe-responsive` | Responsive structural wireframes | Wireframes & maps | Desktop, medium and compact region behavior with persistent transport and content-driven reflow. |
| `26-user-flows` | Critical flows and recovery exits | Wireframes & maps | Import, playback, queue, metadata and skin flows with explicit failure recovery. |
| `27-state-matrix` | Playback state matrix | Wireframes & maps | Visible behavior for empty, loading, playing, paused, buffering, stopped, error and offline states. |
| `28-components-actions` | Component sheet — actions and selection | Component sheets | Buttons, icon buttons, segmented controls, switches, checkboxes, radios, ratings, fields and badges with state guidance. |
| `29-components-sliders` | Component sheet — transport and continuous controls | Component sheets | Seek, volume, EQ, repeat and visualization controls with keyboard steps and explicit semantics. |
| `30-components-music-objects` | Component sheet — tracks, albums and queue items | Component sheets | Distinct current, selected, queued and drag-target states with non-destructive object semantics. |
| `31-components-overlays` | Component sheet — menus, alerts, toasts and dialogs | Component sheets | Overlay hierarchy, destructive confirmation, undo and persistent error guidance. |
| `32-foundations-tokens` | Foundations — color, typography and spacing | Foundations | Semantic dark tokens, readable type scale and 4 px spacing system. Light and high-contrast mappings are specified in the Markdown. |
| `33-icon-library` | Reusable icon library | Foundations | Original 24 px stroke icons for playback, navigation, editing, status and skin controls. |
| `34-waveform-modes` | Waveform and visualization modes | Signal & skins | Mirrored bars, spectrum, oscilloscope and static reduced-motion presentation with honest signal semantics. |
| `35-accessibility-states` | Accessibility — focus, keyboard and high contrast | Foundations | Focus rings, non-color state cues, keyboard behavior, zoom requirements and a high-contrast skin using the same components. |
| `36-skin-slot-map` | Skin slot architecture | Signal & skins | Tokenized chrome, navigation, content, queue and transport slots with locked behavioral and accessibility invariants. |
| `37-component-anatomy` | Component measurements and state layers | Component sheets | Button and track-row dimensions plus surface, state, content, focus and error layer order. |
| `38-compact-desktop` | Compact desktop — 720 px | Full screens | Single-column player with labeled navigation, waveform, queue preview and persistent transport. |
| `39-smart-playlist` | Smart playlist builder | Full screens | Readable condition rows, explicit all/any logic and live local-library preview. No remote recommendation dependency. |
| `40-settings-library-privacy` | Settings — sources, privacy and data control | Full screens | Explicit indexed folders, local-first defaults, opt-in providers and non-destructive data export/clear actions. |
| `41-keyboard-map` | Keyboard shortcut map | Wireframes & maps | Scoped playback, search, queue and overlay shortcuts with conflict and text-entry rules. |
| `42-components-empty-loading` | Component sheet — empty, loading and offline | Component sheets | Non-ideal states with one clear next action and honest preservation semantics. |
| `43-skin-comparison` | Skin comparison — four semantic themes | Signal & skins | Same player anatomy rendered with dark, light, high-contrast and classic token sets. |
| `44-handoff-redlines` | Handoff — flagship layout redlines | Wireframes & maps | Reference dimensions and reflow rules for implementation; not a fixed-scale screenshot contract. |
| `45-components-navigation` | Component sheet — navigation states | Component sheets | Persistent labeled navigation with active, hover, focus and default treatments. |
| `46-settings-shortcuts` | Settings — remappable shortcuts | Full screens | Scoped bindings, conflict-aware editing and restore defaults. OS media keys remain host-managed. |
| `47-output-device-dialog` | Output routing — capability-aware chooser | Full screens | Explicit device selection, availability and route-change warning. Network renderer support is not assumed. |
| `48-mobile-equalizer` | Mobile equalizer | Full screens | Touch sound studio with horizontal band group, numeric values, preamp and fixed save action. |
| `49-mobile-wireframes` | Mobile structural wireframes | Wireframes & maps | Region-level player, library and queue layouts before visual styling. |
| `50-skin-token-editor` | Skin token editor and validation | Full screens | Semantic token editing with live preview, explicit apply and locked accessibility/behavior invariants. |

### Screen-by-screen acceptance notes

- **01 Now Playing:** artwork, identity, source badges, explicit queue, signal, and persistent transport must remain distinct; queue preview opens the full queue.
- **02 Album library:** grid/list/sort/filter/import are visible; card play is explicit; no recommendation-service assumption.
- **03 Track selection:** selection toolbar acts on selected rows, not the current track; current/selected/queued styling remains separate.
- **04 Queue:** explicit items and resume context are simultaneously visible; removal is non-destructive; reorder has keyboard equivalent.
- **05 Focus view:** large signal, pause-visuals control, exit, and stable metadata; Esc returns without changing playback.
- **06 EQ:** numeric bands, preset, reset, preamp, processing summary; unsupported effects are not shown as active.
- **07 Skin studio:** preview and apply are separate; imported skins are data-only; installed skins retain restore path.
- **08 Audio settings:** output route, gapless, resume, queue persistence, normalization; capability-gated advanced routing.
- **09 Tag editor:** mixed values, explicit save, artwork choice, permission review; tag write ≠ filename rename.
- **10 Search:** local results, type grouping, keyboard navigation; typing does not play; remote search is opt-in.
- **11 Onboarding:** deliberate folder/file choice; no account/upload/auto-play; empty transport explains absence.
- **12 Recovery:** missing file and partial import issues; locate/skip/diagnostics; queue/library preserved.
- **13 Daylight:** same anatomy with light semantic tokens; no contrast inversion shortcut.
- **14 Classic:** original metal stack; player/EQ/playlist modules; modern targets and labels.
- **15 Mini/shade:** shared state, essential transport, labeled expand; no queue loss on resize.
- **16 Mobile:** touch-first player/library/queue; 44 px targets; native safe areas remain host work.
- **17 Medium:** labeled tabs and reflowed regions; no horizontal core-task scrolling.
- **18 Sleep timer:** duration + outcome; pause is default; shutdown is separate.
- **19 Radio:** saved URLs, reconnect state, no file-style seek/duration claims.
- **20 Details/lyrics:** source facts separate from output; local lyrics empty state.
- **21 History:** local record, explicit clear, separate favorites; no implicit scrobbling.
- **22 Import:** incremental progress, pause/cancel, partial results retained, no file modification.
- **23 Desktop wireframe:** region hierarchy before decoration.
- **24 IA:** five task groups and cross-cutting rules.
- **25 Responsive wireframes:** desktop/medium/compact region behavior.
- **26 Flows:** start, state change, recovery, non-destructive exit.
- **27 State matrix:** empty/loading/playing/paused/buffering/stopped/error/offline truth.
- **28 Actions:** buttons, icon buttons, tabs, switches, checks, radios, ratings, fields, badges.
- **29 Sliders:** seek/volume/EQ steps and signal-pause distinction.
- **30 Music objects:** current/selected/queued/drop-target semantics.
- **31 Overlays:** menus, alerts, toasts, destructive confirmation, timing.
- **32 Foundations:** semantic palette, type scale, spacing.
- **33 Icons:** original 24 px path library.
- **34 Signal modes:** wave/spectrum/scope/static.
- **35 Accessibility:** focus, keyboard, zoom, high contrast.
- **36 Skin slots:** allowed changes and locked invariants.
- **37 Anatomy:** button/row dimensions and state layers.
- **38 Compact desktop:** single-column 720 px reference.
- **39 Smart playlist:** readable rules and local preview.
- **40 Library/privacy:** source folders, local-first defaults, data controls.
- **41 Keyboard map:** scoped shortcuts and conflict rules.
- **42 Empty/loading/offline:** honest non-ideal states.
- **43 Skin comparison:** four signatures, one anatomy.
- **44 Redlines:** flagship dimensions and reflow policy.
- **45 Navigation:** active/hover/focus/default.
- **46 Shortcut settings:** recording, conflict, restore defaults.
- **47 Output chooser:** availability and route-change warning.
- **48 Mobile EQ:** horizontal band group with fixed primary action.
- **49 Mobile wireframes:** structural player/library/queue.
- **50 Token editor:** semantic editing, preview, validation, explicit apply.

### 01-now-playing-dark — Now playing — Studio Dark

**Category:** Full screens · **Canvas:** 1440 × 960 px

Album-led desktop workspace with persistent transport, explicit queue, source-quality metadata and reactive waveform. Fictional music and original vector sleeve.

![Now playing — Studio Dark](../svg/01-now-playing-dark.svg)

### 02-library-albums — Library — album grid

**Category:** Full screens · **Canvas:** 1440 × 960 px

Original vector album covers; persistent navigation, search, import, view switches and sorting. Grid is a library view, not a music recommendation service.

![Library — album grid](../svg/02-library-albums.svg)

### 03-library-tracks-selection — Library — tracks and bulk selection

**Category:** Full screens · **Canvas:** 1440 × 960 px

Selection toolbar exposes queue, playlist and tag actions. Current playback, selection and explicit queue are separate concepts.

![Library — tracks and bulk selection](../svg/03-library-tracks-selection.svg)

### 04-queue-and-context — Queue — explicit next versus playlist context

**Category:** Full screens · **Canvas:** 1440 × 960 px

Queue panel shows consumed order and resume point. Grip handles support keyboard reorder; removal is non-destructive.

![Queue — explicit next versus playlist context](../svg/04-queue-and-context.svg)

### 05-immersive-visualizer — Immersive visualizer — waveform focus

**Category:** Full screens · **Canvas:** 1440 × 960 px

Large live signal with visible pause control, stable metadata and exit route. Static SVG is an illustrative frame; companion demo drives paths from audio analysis.

![Immersive visualizer — waveform focus](../svg/05-immersive-visualizer.svg)

### 06-equalizer-dsp — Sound studio — equalizer and DSP

**Category:** Full screens · **Canvas:** 1440 × 960 px

Numeric band values, reference preset, reset, preamp and explicit processing status. Advanced effects are capability-gated.

![Sound studio — equalizer and DSP](../svg/06-equalizer-dsp.svg)

### 07-skin-studio — Skin studio — safe white-label theming

**Category:** Full screens · **Canvas:** 1440 × 960 px

Token-based skins, live preview and explicit apply semantics. Classic styling changes presentation, not queue or playback behavior.

![Skin studio — safe white-label theming](../svg/07-skin-studio.svg)

### 08-settings-audio — Settings — audio and playback

**Category:** Full screens · **Canvas:** 1440 × 960 px

Output selection, gapless, resume, queue persistence and normalization. Unsupported engine capabilities are not presented as working toggles.

![Settings — audio and playback](../svg/08-settings-audio.svg)

### 09-metadata-editor — Metadata editor — safe batch editing

**Category:** Full screens · **Canvas:** 1440 × 960 px

Mixed values, explicit save, artwork replacement and file-permission checks. Tag writes and file renaming are separate operations.

![Metadata editor — safe batch editing](../svg/09-metadata-editor.svg)

### 10-search-command — Search — keyboard-first local results

**Category:** Full screens · **Canvas:** 1440 × 960 px

Modal search preserves the player, distinguishes result types and exposes keyboard navigation. No implicit remote search or playback.

![Search — keyboard-first local results](../svg/10-search-command.svg)

### 11-onboarding-empty — First run — consent-led import

**Category:** Full screens · **Canvas:** 1440 × 960 px

No automatic folder scanning or playback. Empty transport is disabled in implementation; this SVG is a layout illustration.

![First run — consent-led import](../svg/11-onboarding-empty.svg)

### 12-errors-recovery — Recovery — missing files and partial import

**Category:** Full screens · **Canvas:** 1440 × 960 px

Actionable errors preserve the library and queue. Diagnostics are copied only on request; no silent destructive cleanup.

![Recovery — missing files and partial import](../svg/12-errors-recovery.svg)

### 13-now-playing-light — Now playing — Daylight skin

**Category:** Full screens · **Canvas:** 1440 × 960 px

Light theme uses darker semantic colors rather than inverting dark-theme accents. Same layout, hierarchy and control semantics.

![Now playing — Daylight skin](../svg/13-now-playing-light.svg)

### 14-classic-compact — Classic Metal — compact modular stack

**Category:** Full screens · **Canvas:** 1200 × 860 px

Original beveled surfaces, spectral display, transport, EQ and playlist modules. Modern target sizes and readable labels replace tiny legacy controls.

![Classic Metal — compact modular stack](../svg/14-classic-compact.svg)

### 15-mini-and-shade — Mini player and shade mode

**Category:** Full screens · **Canvas:** 1200 × 800 px

Compact layouts preserve transport, identity and expansion. Shared state, no hidden queue destruction, no legacy tiny-target requirement.

![Mini player and shade mode](../svg/15-mini-and-shade.svg)

### 16-mobile-screens — Mobile — player, library and queue

**Category:** Full screens · **Canvas:** 1290 × 1030 px

Touch-first 44 px targets, readable hierarchy and explicit queue semantics. Conceptual mobile layouts; native safe areas and gestures require platform implementation.

![Mobile — player, library and queue](../svg/16-mobile-screens.svg)

### 17-tablet-workspace — Medium workspace — 1100 px

**Category:** Full screens · **Canvas:** 1100 × 820 px

Navigation becomes labeled horizontal tabs; artwork, metadata, queue and waveform remain visible without horizontal scrolling.

![Medium workspace — 1100 px](../svg/17-tablet-workspace.svg)

### 18-sleep-timer-dialog — Sleep timer — explicit action and outcome

**Category:** Full screens · **Canvas:** 1440 × 960 px

Modal dialog distinguishes pause from system shutdown, exposes duration and fade behavior, and preserves playback state on cancel.

![Sleep timer — explicit action and outcome](../svg/18-sleep-timer-dialog.svg)

### 19-radio-stream-state — Radio — saved stations and reconnect state

**Category:** Full screens · **Canvas:** 1440 × 960 px

Provider-independent saved URLs, explicit buffering and retry. Live streams do not inherit local-file seeking or duration assumptions.

![Radio — saved stations and reconnect state](../svg/19-radio-stream-state.svg)

### 20-track-details-lyrics — Track details — facts and lyrics empty state

**Category:** Full screens · **Canvas:** 1440 × 960 px

Separates source facts from output claims; lyrics are local and user-supplied unless a separately consented provider is configured.

![Track details — facts and lyrics empty state](../svg/20-track-details-lyrics.svg)

### 21-history-favorites — History — local listening record

**Category:** Full screens · **Canvas:** 1440 × 960 px

Local history with explicit clearing and separate favorites. No automatic scrobbling or cloud account implied.

![History — local listening record](../svg/21-history-favorites.svg)

### 22-import-progress — Import — incremental progress and cancellation

**Category:** Full screens · **Canvas:** 1440 × 960 px

Partial results remain usable, indexing is non-destructive, and cancel does not silently delete indexed tracks.

![Import — incremental progress and cancellation](../svg/22-import-progress.svg)

### 23-wireframe-desktop — Desktop structural wireframe

**Category:** Wireframes & maps · **Canvas:** 1440 × 960 px

Regions and behavior before decoration: persistent navigation, adaptive content, explicit queue, pausable signal and persistent transport.

![Desktop structural wireframe](../svg/23-wireframe-desktop.svg)

### 24-information-architecture — Information architecture and navigation contract

**Category:** Wireframes & maps · **Canvas:** 1400 × 940 px

Five task groups with cross-cutting queue, search, accessibility and capability rules.

![Information architecture and navigation contract](../svg/24-information-architecture.svg)

### 25-wireframe-responsive — Responsive structural wireframes

**Category:** Wireframes & maps · **Canvas:** 1400 × 900 px

Desktop, medium and compact region behavior with persistent transport and content-driven reflow.

![Responsive structural wireframes](../svg/25-wireframe-responsive.svg)

### 26-user-flows — Critical flows and recovery exits

**Category:** Wireframes & maps · **Canvas:** 1400 × 980 px

Import, playback, queue, metadata and skin flows with explicit failure recovery.

![Critical flows and recovery exits](../svg/26-user-flows.svg)

### 27-state-matrix — Playback state matrix

**Category:** Wireframes & maps · **Canvas:** 1400 × 940 px

Visible behavior for empty, loading, playing, paused, buffering, stopped, error and offline states.

![Playback state matrix](../svg/27-state-matrix.svg)

### 28-components-actions — Component sheet — actions and selection

**Category:** Component sheets · **Canvas:** 1400 × 1000 px

Buttons, icon buttons, segmented controls, switches, checkboxes, radios, ratings, fields and badges with state guidance.

![Component sheet — actions and selection](../svg/28-components-actions.svg)

### 29-components-sliders — Component sheet — transport and continuous controls

**Category:** Component sheets · **Canvas:** 1400 × 1020 px

Seek, volume, EQ, repeat and visualization controls with keyboard steps and explicit semantics.

![Component sheet — transport and continuous controls](../svg/29-components-sliders.svg)

### 30-components-music-objects — Component sheet — tracks, albums and queue items

**Category:** Component sheets · **Canvas:** 1400 × 1000 px

Distinct current, selected, queued and drag-target states with non-destructive object semantics.

![Component sheet — tracks, albums and queue items](../svg/30-components-music-objects.svg)

### 31-components-overlays — Component sheet — menus, alerts, toasts and dialogs

**Category:** Component sheets · **Canvas:** 1400 × 1040 px

Overlay hierarchy, destructive confirmation, undo and persistent error guidance.

![Component sheet — menus, alerts, toasts and dialogs](../svg/31-components-overlays.svg)

### 32-foundations-tokens — Foundations — color, typography and spacing

**Category:** Foundations · **Canvas:** 1400 × 1020 px

Semantic dark tokens, readable type scale and 4 px spacing system. Light and high-contrast mappings are specified in the Markdown.

![Foundations — color, typography and spacing](../svg/32-foundations-tokens.svg)

### 33-icon-library — Reusable icon library

**Category:** Foundations · **Canvas:** 1400 × 1100 px

Original 24 px stroke icons for playback, navigation, editing, status and skin controls.

![Reusable icon library](../svg/33-icon-library.svg)

### 34-waveform-modes — Waveform and visualization modes

**Category:** Signal & skins · **Canvas:** 1400 × 1080 px

Mirrored bars, spectrum, oscilloscope and static reduced-motion presentation with honest signal semantics.

![Waveform and visualization modes](../svg/34-waveform-modes.svg)

### 35-accessibility-states — Accessibility — focus, keyboard and high contrast

**Category:** Foundations · **Canvas:** 1400 × 1000 px

Focus rings, non-color state cues, keyboard behavior, zoom requirements and a high-contrast skin using the same components.

![Accessibility — focus, keyboard and high contrast](../svg/35-accessibility-states.svg)

### 36-skin-slot-map — Skin slot architecture

**Category:** Signal & skins · **Canvas:** 1400 × 960 px

Tokenized chrome, navigation, content, queue and transport slots with locked behavioral and accessibility invariants.

![Skin slot architecture](../svg/36-skin-slot-map.svg)

### 37-component-anatomy — Component measurements and state layers

**Category:** Component sheets · **Canvas:** 1400 × 940 px

Button and track-row dimensions plus surface, state, content, focus and error layer order.

![Component measurements and state layers](../svg/37-component-anatomy.svg)

### 38-compact-desktop — Compact desktop — 720 px

**Category:** Full screens · **Canvas:** 820 × 1000 px

Single-column player with labeled navigation, waveform, queue preview and persistent transport.

![Compact desktop — 720 px](../svg/38-compact-desktop.svg)

### 39-smart-playlist — Smart playlist builder

**Category:** Full screens · **Canvas:** 1440 × 960 px

Readable condition rows, explicit all/any logic and live local-library preview. No remote recommendation dependency.

![Smart playlist builder](../svg/39-smart-playlist.svg)

### 40-settings-library-privacy — Settings — sources, privacy and data control

**Category:** Full screens · **Canvas:** 1440 × 960 px

Explicit indexed folders, local-first defaults, opt-in providers and non-destructive data export/clear actions.

![Settings — sources, privacy and data control](../svg/40-settings-library-privacy.svg)

### 41-keyboard-map — Keyboard shortcut map

**Category:** Wireframes & maps · **Canvas:** 1400 × 940 px

Scoped playback, search, queue and overlay shortcuts with conflict and text-entry rules.

![Keyboard shortcut map](../svg/41-keyboard-map.svg)

### 42-components-empty-loading — Component sheet — empty, loading and offline

**Category:** Component sheets · **Canvas:** 1400 × 940 px

Non-ideal states with one clear next action and honest preservation semantics.

![Component sheet — empty, loading and offline](../svg/42-components-empty-loading.svg)

### 43-skin-comparison — Skin comparison — four semantic themes

**Category:** Signal & skins · **Canvas:** 1400 × 1040 px

Same player anatomy rendered with dark, light, high-contrast and classic token sets.

![Skin comparison — four semantic themes](../svg/43-skin-comparison.svg)

### 44-handoff-redlines — Handoff — flagship layout redlines

**Category:** Wireframes & maps · **Canvas:** 1440 × 1000 px

Reference dimensions and reflow rules for implementation; not a fixed-scale screenshot contract.

![Handoff — flagship layout redlines](../svg/44-handoff-redlines.svg)

### 45-components-navigation — Component sheet — navigation states

**Category:** Component sheets · **Canvas:** 1400 × 920 px

Persistent labeled navigation with active, hover, focus and default treatments.

![Component sheet — navigation states](../svg/45-components-navigation.svg)

### 46-settings-shortcuts — Settings — remappable shortcuts

**Category:** Full screens · **Canvas:** 1440 × 960 px

Scoped bindings, conflict-aware editing and restore defaults. OS media keys remain host-managed.

![Settings — remappable shortcuts](../svg/46-settings-shortcuts.svg)

### 47-output-device-dialog — Output routing — capability-aware chooser

**Category:** Full screens · **Canvas:** 1440 × 960 px

Explicit device selection, availability and route-change warning. Network renderer support is not assumed.

![Output routing — capability-aware chooser](../svg/47-output-device-dialog.svg)

### 48-mobile-equalizer — Mobile equalizer

**Category:** Full screens · **Canvas:** 520 × 1030 px

Touch sound studio with horizontal band group, numeric values, preamp and fixed save action.

![Mobile equalizer](../svg/48-mobile-equalizer.svg)

### 49-mobile-wireframes — Mobile structural wireframes

**Category:** Wireframes & maps · **Canvas:** 1290 × 1030 px

Region-level player, library and queue layouts before visual styling.

![Mobile structural wireframes](../svg/49-mobile-wireframes.svg)

### 50-skin-token-editor — Skin token editor and validation

**Category:** Full screens · **Canvas:** 1440 × 960 px

Semantic token editing with live preview, explicit apply and locked accessibility/behavior invariants.

![Skin token editor and validation](../svg/50-skin-token-editor.svg)


## 17. Implementation architecture and handoff

### 17.1 Recommended separation

```text
Host adapters (macOS / Windows / Linux / web / mobile)
  ├─ file permissions / dialogs / media session / safe areas
  └─ audio backend capability registry

Core domain
  ├─ library index / metadata / playlists / smart rules
  ├─ playback state machine
  ├─ explicit queue + context pointer
  ├─ favorites / history / settings
  └─ skin validation / token resolution

Audio engine
  ├─ decode / buffer / output route
  ├─ DSP / gain / limiter
  └─ analysis tap → bounded visual frames

Presentation
  ├─ native/HTML semantic controls
  ├─ SVG signal and vector artwork
  ├─ layout variants / modes
  └─ accessibility announcements / focus management
```

### 17.2 Suggested state shape

```ts
type PlaybackState =
  | 'empty' | 'loading' | 'playing' | 'paused'
  | 'buffering' | 'stopped' | 'error';

interface PlayerStore {
  playback: PlaybackState;
  current?: TrackRef;
  positionMs: number;
  durationMs?: number;       // undefined for live streams
  seekable: boolean;
  context?: { id: string; kind: 'album'|'playlist'|'folder'; index: number; order: TrackRef[] };
  explicitQueue: TrackRef[];
  shuffle: boolean;
  repeat: 'off' | 'all' | 'one';
  volume: number;            // 0..1
  muted: boolean;
  output?: OutputCapability;
  sourceFacts?: SourceFacts;
  processing: ProcessingSummary;
  error?: RecoverableError;
}

interface VisualFrame {
  timestampMs: number;
  mode: 'wave' | 'spectrum' | 'scope' | 'static';
  waveform?: Float32Array;   // aggregated envelope
  spectrum?: Float32Array;   // dB or normalized magnitudes
  peak?: number;
  clipping?: boolean;
  stale: boolean;
}
```

### 17.3 SVG rendering guidance

- Keep one SVG root per signal region; reuse child nodes.
- Waveform: update `d` on a path or `y/height` on a bounded set of rects.
- Spectrum: update rect heights/transforms; use log-spaced aggregation.
- Scope: update a path from a decimated sample window.
- Use `clipPath` for artwork and signal bounds; avoid overflow into neighboring controls.
- Use semantic IDs prefixed per component instance to prevent gradient/clip collisions.
- Do not put production text into outlined paths unless exporting static artwork; keep live text for localization and accessibility.
- Raster album art may be embedded in a framed image element in production; the design package uses original vector sleeves.

### 17.4 Performance targets

| Area | Target | Method |
|---|---|---|
| Library list | Smooth scroll at 100k tracks | Virtualization, indexed queries |
| Import | UI remains usable | Incremental indexing, cancellable worker |
| Signal | 30 fps desktop / 20 fps compact | Node reuse, bounded aggregation |
| Audio | No UI-induced dropouts | Audio thread isolation, drop visual frames |
| Search | Responsive local results | Debounced indexed query, stale-result labeling |
| Skin apply | No layout shift in core controls | Token swap, prevalidated variants |
| Startup | Restore state without auto-play | Persisted store, explicit play |

### 17.5 Security and privacy

- Skins are data-only: JSON tokens + sanitized SVG assets. Reject scripts, event handlers, external URLs, foreignObject, and executable fields.
- Imported SVG is sanitized and rendered in a restricted context; no network fetch from skin assets.
- Diagnostics are opt-in and redact private paths/audio contents by default.
- Remote metadata/artwork/scrobbling/providers are opt-in and labeled.
- File deletion, renaming, tag writes, and system shutdown require separate explicit actions/permissions.
- Source-folder removal stops indexing that source; it does not delete audio files.

### 17.6 Handoff checklist

- [ ] Resolve final brand name/logo and legal clearance.
- [ ] Confirm target platforms and audio backend capability matrix.
- [ ] Implement semantic control layer beneath SVG presentation.
- [ ] Wire playback state machine and explicit queue store.
- [ ] Implement analysis tap and bounded visual frames.
- [ ] Implement token resolver and skin validator.
- [ ] Add localization/RTL/long-string fixtures.
- [ ] Run keyboard, screen-reader, zoom, contrast, and motion audits.
- [ ] Run 100k-track library and audio/visual performance tests.
- [ ] Complete usability tasks for import, queue, tags, skins, and recovery.

## 18. Validation plan and acceptance criteria

### 18.1 Design QA performed in this package

- 50 SVG artifacts generated and parsed as valid XML.
- Representative screens rendered to PNG for visual inspection.
- Corrected artwork clipping, control overlap, empty-player semantics, theme leakage, and icon-sheet overflow during render review.
- All artwork is original vector geometry; no reference-product sprites or logos are embedded.
- Static frames are explicitly labeled as illustrations; live behavior is delegated to the waveform lab.

### 18.2 Contrast spot checks (computed, not a certification)

| Pair | Studio Dark | Daylight | Requirement / note |
|---|---:|---:|---|
| Primary text / panel | 14.58:1 | 14.88:1 | Passes normal-text threshold |
| Secondary text / panel | 8.14:1 | 6.27:1 | Passes normal-text threshold |
| Tertiary text / panel | 5.13:1 | 4.92:1 | Passes normal-text threshold |
| Accent / panel | 10.18:1 | 6.46:1 | Passes meaningful-graphic threshold |
| On-accent / accent | 10.39:1 | 6.46:1 | Passes normal-text threshold |
| Danger / panel | 7.81:1 | 7.02:1 | Passes normal-text threshold |
| Default border / panel | 1.58:1 | 1.77:1 | Decorative/subtle; not sole control boundary |

**Important:** subtle borders are not sufficient as the only identifier of a control. Interactive controls must also use readable text/icons, state shapes, or a stronger boundary/focus indicator. Tertiary text on raised surfaces can fall below 4.5:1 in some combinations; production must validate each actual pairing and promote text to secondary where needed. These spot checks do not constitute WCAG conformance.

### 18.3 Required test matrix

| Test | Acceptance criterion |
|---|---|
| Import permission denied | Explain access; no silent scan; retry available |
| Partial import | Valid tracks usable; issues listed; cancel keeps completed work |
| Queue vs context | Explicit items consumed first; resume point visible |
| Queue reorder | Pointer and keyboard produce same order; announcement correct |
| Queue removal/clear | Files/library unchanged; undo available |
| Mode switch | Workspace/focus/mini/shade/Classic share state and queue |
| Seek | Keyboard steps, drag preview, bounds, live-stream disable |
| EQ | Numeric values, reset, preset, preamp, clipping warning |
| Output change | Capability check; brief-pause warning; no false fidelity claim |
| Tag batch | Mixed values preserved; explicit save; per-file failure retains edits |
| Skin import | Invalid/schema/script assets rejected; current skin unchanged |
| Skin contrast | Default skins pass; invalid custom skin blocked or explicit override |
| Visual pause | Visual updates stop; audio continues |
| Reduced motion | Static/low-rate presentation; no flashing |
| Keyboard | All core tasks reachable; focus visible; Esc closes top layer |
| Screen reader | Names/roles/values/states correct; announcements not per-frame |
| Zoom/reflow | 200% text and compact width preserve core tasks |
| Long strings/RTL | No clipped actions; full identity available; mirrored layout tested |
| Offline/disconnect | Local playback remains; remote/source marked unavailable |
| Large library | 100k tracks scroll/search without UI stall |
| Audio/visual load | No audio dropouts caused by visual rendering |

### 18.4 Usability tasks

1. Import a folder and play one track without creating an account.
2. Add two tracks to Play next, reorder them, and identify what plays afterward.
3. Remove a track from a playlist without deleting the file.
4. Edit a mixed album field without overwriting unrelated mixed values.
5. Switch to Classic/mini and return without losing the queue.
6. Pause the visualization while audio continues.
7. Apply a skin and restore the previous one.
8. Recover from a missing file by locating or skipping it.
9. Set a 30-minute fade-to-pause timer and cancel it.
10. Complete core playback using keyboard only.

## 19. Delivery roadmap and open decisions

### Phase 0 — Decisions before production

- Final brand/name/logo and trademark clearance.
- Primary platform order: macOS/Windows/Linux/web/mobile.
- Audio backend and capability matrix.
- Local database and playlist portability policy.
- Provider/privacy policy and premium boundary, if any.
- Skin distribution/security policy.

### Phase 1 — Core player

- Semantic shell, transport, state machine, local import, library, queue, search, recovery.
- Dark/light/high-contrast tokens; keyboard/focus/zoom baseline.
- Static signal placeholder and real analysis tap.

### Phase 2 — Differentiators

- Focus/mini/shade/Classic modes; reactive SVG modes.
- EQ/presets/output chooser; sleep timer.
- Skin studio/token editor/import validation.
- Smart playlists, favorites/history, tag editor.

### Phase 3 — Conditional depth

- Radio/podcasts/providers; advanced DSP/output; mobile native integrations.
- Converter/CD/recording/scheduler only after backend/legal review.
- Localization/RTL expansion and performance hardening.

### Open decisions register

| Decision | Options | Recommendation |
|---|---|---|
| Default EQ depth | 10-band vs 20-band | 10-band default; 20-band advanced capability |
| Classic default | Optional vs default | Optional; workspace default |
| Signal default | Wave vs spectrum | Mirrored wave; spectrum in Classic/focus |
| Queue persistence | Always vs setting | Setting, default on for local player |
| Remote providers | Built-in vs extensions | Extensions, opt-in |
| Skin format | Legacy bitmap vs token SVG | Token SVG; legacy import as research only |
| Mobile scope | Responsive concept vs native | Concept now; native after platform decision |
| Brand | FUSE demo vs final | White-label slots; final brand pending |

## 20. Source notes and limitations

### Reference sources

1. VOX Mac Music Player product page — compact/album-led presentation, formats, EQ, gapless, output and source features. https://vox.rocks/mac-music-player
2. AIMP official desktop features — library, playlists, queue, EQ/DSP, normalization, tagging, skins and scheduler breadth. https://www.aimp.ru/?do=features
3. Winamp Desktop Player help — playlist, EQ, skins, color themes, classic/modern skin support. https://support.winamp.com/winamp-desktop-player-for-windows
4. Winamp Skin Museum / classic skin tutorial — classic skin configuration concepts such as visualization and playlist color mappings. https://winampskins.neocities.org/config
5. Webamp documentation entry point — classic-player implementation reference. https://docs.webamp.org/
6. W3C WAI — WCAG 2.2 contrast, non-text contrast, target size, and pause/stop/hide understanding pages. https://www.w3.org/WAI/WCAG22/
7. MDN — AnalyserNode time-domain and frequency-data APIs. https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode

### Interpretation rules

- Reference products inspire interaction patterns; no proprietary assets are copied.
- Public pages are not a substitute for version-specific testing.
- Premium, platform, and plugin differences are treated as capability gates.
- Accessibility targets are design requirements; formal conformance requires implementation testing.
- The interactive waveform lab demonstrates browser audio analysis, not a production audio engine.
- Fictional metadata and original vector sleeves avoid implying real artist endorsements or licensed album art.

### License and reuse note

The design specification and original SVG artwork are provided as project deliverables for adaptation. Third-party fonts used for rendering checks are Inter and JetBrains Mono; their licenses are included in the package font directory when present. Final production font embedding/redistribution must follow the applicable font license. Reference-product names are used only for analysis and attribution.
