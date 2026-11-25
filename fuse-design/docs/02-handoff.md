## 16. Full SVG design gallery and screen specifications

The following 50 vector artifacts are embedded directly in this Markdown. Each has a stable ID, editable source in `svg/`, and a source listing in Appendix A. Static frames are design illustrations; interactive behavior is specified in the contracts above and demonstrated only in the separate waveform lab.

### Gallery index

| ID | Artifact | Category | Primary purpose |
|---|---|---|---|
{{GALLERY_INDEX}}

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

{{GALLERY}}

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
