$ErrorActionPreference = 'Stop'
$legalRoot = Join-Path $PSScriptRoot '..\outputs\referencia-legal'
$legalRoot = (Resolve-Path -LiteralPath $legalRoot).Path
$legalCommit = '15eb09b618ff08a38c4dfee06a91bd139d093f5d'
$sourceMap = [ordered]@{
    'acervo/README.md' = "https://raw.githubusercontent.com/ctresb/leis/$legalCommit/README.md"
    'acervo/PROGRESSO.md' = "https://raw.githubusercontent.com/ctresb/leis/$legalCommit/PROGRESSO.md"
    'acervo/LICENSE' = "https://raw.githubusercontent.com/ctresb/leis/$legalCommit/LICENSE"
    'acervo/federal/leis-ordinarias/2018/lei-13709-2018-08-14.md' = "https://raw.githubusercontent.com/ctresb/leis/$legalCommit/federal/leis-ordinarias/2018/lei-13709-2018-08-14.md"
    'acervo/federal/leis-ordinarias/2014/lei-12965-2014-04-23.md' = "https://raw.githubusercontent.com/ctresb/leis/$legalCommit/federal/leis-ordinarias/2014/lei-12965-2014-04-23.md"
    'acervo/federal/leis-ordinarias/2015/lei-13146-2015-07-06.md' = "https://raw.githubusercontent.com/ctresb/leis/$legalCommit/federal/leis-ordinarias/2015/lei-13146-2015-07-06.md"
    'acervo/federal/leis-ordinarias/1998/lei-9609-1998-02-19.md' = "https://raw.githubusercontent.com/ctresb/leis/$legalCommit/federal/leis-ordinarias/1998/lei-9609-1998-02-19.md"
    'acervo/federal/leis-ordinarias/1998/lei-9610-1998-02-19.md' = "https://raw.githubusercontent.com/ctresb/leis/$legalCommit/federal/leis-ordinarias/1998/lei-9610-1998-02-19.md"
    'fontes-oficiais/lgpd-planalto.html' = 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm'
    'fontes-oficiais/marco-civil-planalto.html' = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm'
    'fontes-oficiais/lei-9609-planalto.html' = 'https://www.planalto.gov.br/ccivil_03/leis/l9609.htm'
    'fontes-oficiais/direitos-autorais-planalto.html' = 'https://www.planalto.gov.br/ccivil_03/leis/l9610.htm'
    'fontes-oficiais/inclusao-planalto.html' = 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm'
}
$records = foreach ($entry in $sourceMap.GetEnumerator()) {
    $snapshotPath = Join-Path $legalRoot $entry.Key
    $snapshot = Get-Item -LiteralPath $snapshotPath
    if ($snapshot.Length -lt 500) { throw "Unexpected empty/short source: $($entry.Key)" }
    [ordered]@{
        path = $entry.Key
        url = $entry.Value
        bytes = $snapshot.Length
        sha256 = (Get-FileHash -LiteralPath $snapshotPath -Algorithm SHA256).Hash.ToLowerInvariant()
        downloaded_at_utc = $snapshot.LastWriteTimeUtc.ToString('o')
        completeness = $(if ($entry.Key -eq 'acervo/federal/leis-ordinarias/1998/lei-9609-1998-02-19.md') { 'rectification_only_not_full_law' } else { 'snapshot_not_legally_certified' })
    }
}
$manifest = [ordered]@{
    repository = 'https://github.com/ctresb/leis'
    branch = 'main'
    commit = $legalCommit
    consultation_local_date = '2026-10-21'
    consultation_timezone = 'America/Sao_Paulo'
    scope = 'Selected software-relevant laws; full corpus not downloaded or read'
    files = @($records)
}
$manifestPath = Join-Path $legalRoot 'manifesto.json'
[System.IO.File]::WriteAllText($manifestPath, ($manifest | ConvertTo-Json -Depth 6) + [Environment]::NewLine, [System.Text.UTF8Encoding]::new($false))
$checked = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
foreach ($record in $checked.files) {
    $actual = (Get-FileHash -LiteralPath (Join-Path $legalRoot $record.path) -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $record.sha256) { throw "Checksum mismatch: $($record.path)" }
}
Write-Output "Validated $($checked.files.Count) downloaded snapshots and their SHA-256 checksums."
