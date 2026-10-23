# Uploading scouting results to Google Drive (multi-account)

Mahdy's Drive setup for delivering scouting artifacts. Full Drive API details
live in the bundled `google-workspace` skill; this note covers only the
profile-specific multi-account arrangement.

## Account registry

`<hermes-home>/gdrive-accounts.json` — one entry per Google account:

```json
{"accounts": {"mahdy": {"email": "...", "token_file": "google_token_mahdy.json",
  "drive_root_folder": "<root-id>", "kuliah_folder": "<kuliah-s2-id>",
  "role": "primary-read", "status": "authenticated"}}}
```

- Each account has its own token file `<hermes-home>/google_token_<name>.json`.
  The `google-workspace` scripts resolve `google_token.json` under `HERMES_HOME`
  and accept `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` as an env override — run
  them via `subprocess` with both env vars set to pick the right account:
  `HERMES_HOME=<profile>` and `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=<token file>`.
- One `google_client_secret.json` is shared by all accounts (the OAuth client is
  app-level; tokens are per-user). Auth a new account with the bundled
  `setup.py --auth-url` / `--auth-code` flow, then copy the resulting
  `google_token.json` to `google_token_<name>.json` and register it.

## Read/write split

- Read (Drive, Gmail) runs under the primary account's token.
- Uploads from a second account land in the SAME folder only if the folder is
  shared to that account with role `writer` (`drive share <folder-id> --email ... --role writer`).
  Sharing is native Drive; no code needed.
- Invoke `google_api.py` through `subprocess` per call and pass the per-account
  env vars — never mutate module constants, they are resolved at import.

## Deliverable convention

Scouting results are uploaded from the topic folder into the kuliah folder tree
(`Kuliah S2` with `pribadi`/`umum` subfolders) mirroring the local
`workspace/kuliah/{pribadi,umum}/` split. Confirm with Mahdy before any upload
or share (the google-workspace skill's write-confirmation rule applies).
