# RTK - Rust Token Killer (Codex CLI)

**Usage**: Token-optimized CLI proxy for shell commands.

## Rule

Project adaptation for RTK 0.48.0: use a prefix only for supported commands when no active hook is observed. Do not double-wrap a command already rewritten by a native hook. Preserve PowerShell pipelines and compound-command semantics. Use `rtk proxy <command>` for full output when appropriate. This setup does not install or change global hooks.

Examples:

```bash
rtk git status
rtk cargo test
rtk npm run build
rtk pytest -q
```

## Meta Commands

```bash
rtk gain            # Token savings analytics
rtk gain --history  # Recent command savings history
rtk proxy <cmd>     # Run raw command without filtering
```

## Verification

```bash
rtk --version
rtk gain
which rtk
```
