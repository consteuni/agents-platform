# Coding Harness

Skill per guidare un agente nello sviluppo di codice mantenibile: comprensione del progetto, principi di ingegneria del software, implementazione, verifiche con evidenze e continuità tra sessioni.

Segue linguaggi, framework e strumenti già presenti nel progetto. Contiene istruzioni, riferimenti e template; non richiede un runtime, script, hook o dipendenze aggiuntive.

## Scegli il client

| Client | Installazione personale, disponibile nei progetti locali | Richiamo |
| --- | --- | --- |
| Codex CLI / estensione IDE | `~/.agents/skills/coding-harness/` | `$coding-harness` oppure `/skills` |
| Claude Code | `~/.claude/skills/coding-harness/` | `/coding-harness` |
| Cursor | `~/.cursor/skills/coding-harness/` | `/` nella chat Agent, poi seleziona la skill |
| ChatGPT con gestione skill | Creazione personale tramite `@skill-creator` | `@` e selezione della skill |

Disponibile globalmente significa disponibile nei progetti di quell'utente e di quella macchina. L'agente può sceglierla quando la richiesta corrisponde alla descrizione; per usarla con certezza, richiamala esplicitamente all'inizio del lavoro.

Le cartelle locali non vengono automaticamente installate in ChatGPT o nelle sessioni cloud. I metadati [openai.yaml](coding-harness/agents/openai.yaml) configurano la presentazione e consentono il richiamo implicito nei client che li supportano; non sostituiscono l'installazione.

## Prepara la sorgente

I comandi seguenti usano Bash su Linux, macOS o WSL. Gli esempi assumono che la repo sia in `~/codici/agents-platform`; cambia il percorso se necessario.

Se hai già scaricato o clonato la repo, usa quella cartella. Altrimenti:

```bash
mkdir -p "$HOME/codici"
git clone https://github.com/consteuni/agents-platform.git "$HOME/codici/agents-platform"
```

Installa sempre l'intera cartella `coding-harness/`: copiare solo `SKILL.md` rende indisponibili riferimenti e template. La repo contiene la sorgente della skill e non si attiva da sola.

## Installa per il tuo client

Questi comandi sono per una prima installazione. Se la destinazione esiste già, segui [Aggiornamento](#aggiornamento) per conservarne una copia.

### Codex CLI e IDE

```bash
(
  set -eu
  repo_dir="$HOME/codici/agents-platform"
  skill_dir="$HOME/.agents/skills/coding-harness"
  test -f "$repo_dir/coding-harness/SKILL.md"
  test ! -e "$skill_dir"
  test ! -L "$skill_dir"
  mkdir -p "$skill_dir"
  cp -R "$repo_dir/coding-harness/." "$skill_dir/"
)
```

Apri Codex nel progetto e scrivi:

```text
$coding-harness Implementa questa funzionalità seguendo le convenzioni del progetto.
```

Con `/skills` puoi cercare la skill. Codex rileva le modifiche alle skill; se non compare, riavvialo.

### Claude Code

```bash
(
  set -eu
  repo_dir="$HOME/codici/agents-platform"
  skill_dir="$HOME/.claude/skills/coding-harness"
  test -f "$repo_dir/coding-harness/SKILL.md"
  test ! -e "$skill_dir"
  test ! -L "$skill_dir"
  mkdir -p "$skill_dir"
  cp -R "$repo_dir/coding-harness/." "$skill_dir/"
)
```

Avvia Claude Code nel progetto e scrivi:

```text
/coding-harness Correggi questo bug e verifica il comportamento.
```

La cartella personale rende la skill disponibile nei progetti locali. Per controllare il caricamento, apri il menu `/` e cerca `coding-harness`.

### Cursor

```bash
(
  set -eu
  repo_dir="$HOME/codici/agents-platform"
  skill_dir="$HOME/.cursor/skills/coding-harness"
  test -f "$repo_dir/coding-harness/SKILL.md"
  test ! -e "$skill_dir"
  test ! -L "$skill_dir"
  mkdir -p "$skill_dir"
  cp -R "$repo_dir/coding-harness/." "$skill_dir/"
)
```

Apri **Customize → Skills**, poi nella chat Agent digita `/` e seleziona `coding-harness`. Se la skill non viene rilevata dopo l'installazione, riapri il client.

Cursor legge anche `~/.agents/skills/` e directory compatibili con altri client: se l'hai già installata per Codex, verifica prima se è disponibile ed evita copie con lo stesso nome. Per i Cloud Agents, la documentazione indica la sincronizzazione delle skill da `~/.cursor/skills/` tramite **Settings → Agents → Sync Skills for Cloud Agents**; un'installazione locale da sola non viene trasferita alle sessioni remote.

### ChatGPT

Quando il client offre gestione e creazione di skill, richiama `@skill-creator` e chiedi:

> Crea una skill personale chiamata coding-harness usando la cartella coding-harness di https://github.com/consteuni/agents-platform. Mantieni i riferimenti e i template, il funzionamento solo tramite istruzioni e i principi di ingegneria del software.

Rendi la sorgente accessibile al creator tramite il collegamento GitHub connesso o i file della cartella. Dopo che il creator ha confermato il salvataggio, seleziona la skill con `@`. Per aggiornarla, chiedi allo stesso creator di aggiornare la skill personale esistente dalla repo, preservando eventuali personalizzazioni dichiarate.

La presenza di `~/.agents/skills/` sul tuo computer non installa una skill nel tuo account ChatGPT. Questa repo non contiene ancora un pacchetto plugin da installare dal catalogo.

## Aggiornamento

Per un'installazione tramite copia, aggiorna prima la sorgente e poi sostituisci la cartella installata. Il procedimento conserva la vecchia versione fuori dalle directory scandite dai client e impedisce che file rimossi dalla sorgente restino nella nuova copia.

Scegli **una sola** destinazione per il client che vuoi aggiornare:

```bash
# Codex
skill_dir="$HOME/.agents/skills/coding-harness"

# Claude Code: usa questa riga al posto della precedente
# skill_dir="$HOME/.claude/skills/coding-harness"

# Cursor: usa questa riga al posto della precedente
# skill_dir="$HOME/.cursor/skills/coding-harness"
```

Poi esegui:

```bash
(
  set -eu
  repo_dir="$HOME/codici/agents-platform"
  test "$(git -C "$repo_dir" branch --show-current)" = main
  if [ -n "$(git -C "$repo_dir" status --porcelain)" ]; then
    echo "La sorgente contiene modifiche locali: gestiscile prima dell'aggiornamento."
    exit 1
  fi
  git -C "$repo_dir" pull --ff-only
  test -f "$repo_dir/coding-harness/SKILL.md"
  if [ -L "$skill_dir" ]; then
    echo "La skill è un collegamento: usa la procedura per symlink."
    exit 1
  fi
  backup_root="$HOME/.local/share/coding-harness/backups"
  mkdir -p "$backup_root"
  backup_dir="$(mktemp -d "$backup_root/update-XXXXXXXX")"
  if [ -e "$skill_dir" ]; then
    mv "$skill_dir" "$backup_dir/coding-harness"
  fi
  mkdir -p "$skill_dir"
  cp -R "$repo_dir/coding-harness/." "$skill_dir/"
  echo "Skill aggiornata. Backup: $backup_dir"
)
```

Il controllo iniziale interrompe l'aggiornamento se la sorgente ha modifiche locali, si trova su un altro branch o il pull non può avanzare senza merge. Se la cartella deriva da un archivio ZIP, scarica una nuova versione della sorgente e applica la parte di backup e copia: `git pull` richiede un clone Git.

Se avevi personalizzato la skill installata, confronta il backup con la nuova versione e riporta soltanto le modifiche desiderate. Verifica poi il richiamo nel client; apri una nuova sessione se continua a usare la versione precedente. Ripeti l'aggiornamento per ogni copia separata che utilizzi.

### Alternativa: collegamento alla sorgente

Codex e Claude Code documentano il supporto a cartelle skill collegate tramite symlink. Su Linux/macOS/WSL, per una destinazione ancora inesistente puoi evitare una seconda copia:

```bash
(
  set -eu
  repo_dir="$HOME/codici/agents-platform"
  skill_root="$HOME/.agents/skills"
  # Per Claude Code: skill_root="$HOME/.claude/skills"
  test -f "$repo_dir/coding-harness/SKILL.md"
  test ! -e "$skill_root/coding-harness"
  test ! -L "$skill_root/coding-harness"
  mkdir -p "$skill_root"
  ln -s "$repo_dir/coding-harness" "$skill_root/coding-harness"
)
```

Se hai già una copia, spostala prima fuori dalla directory skill e conservala; non creare un collegamento dentro la copia esistente. Con un symlink, aggiorni soltanto la repo con `git pull --ff-only` dopo aver verificato branch e modifiche locali. Il collegamento vedrà la nuova sorgente senza ricopiare file. Non spostare o eliminare la repo; gli eventuali cambi locali alla sorgente diventano immediatamente visibili alla skill.

## Installazione per un solo progetto

Usa queste destinazioni nel progetto al posto della cartella personale:

| Client | Destinazione nel progetto |
| --- | --- |
| Codex | `.agents/skills/coding-harness/` |
| Claude Code | `.claude/skills/coding-harness/` |
| Cursor | `.cursor/skills/coding-harness/` oppure `.agents/skills/coding-harness/` |

Copia l'intera cartella e condividila con il progetto se serve al team. Per le sessioni remote, rendila disponibile nell'ambiente remoto o nella repo secondo il client. Non dare per scontato che una cartella presente sul computer locale esista anche lì.

## Se non la trovi

1. Controlla che il percorso termini con `coding-harness/SKILL.md`, senza un secondo livello `coding-harness/coding-harness/`.
2. Controlla che l'inizio del file contenga il frontmatter con `name: coding-harness` e `description`.
3. Verifica che `references/`, `assets/` e `agents/` siano state copiate insieme al file.
4. Cerca la skill nel menu del client e prova il richiamo esplicito. Se necessario, riapri il client.
5. Controlla che non sia disabilitata nelle impostazioni e che non ci siano copie con lo stesso nome in directory diverse.

Per Codex, questi controlli si possono eseguire dal terminale:

```bash
codex --version
ls "$HOME/.agents/skills/coding-harness/SKILL.md"
sed -n '1,6p' "$HOME/.agents/skills/coding-harness/SKILL.md"
```

## Risorse e utilizzo

| Risorsa | Scopo |
| --- | --- |
| [SKILL.md](coding-harness/SKILL.md) | Istruzioni principali e scelta del flusso minimo |
| [ENGINEERING.md](coding-harness/references/ENGINEERING.md) | SOLID, KISS, DRY, YAGNI, contratti, sicurezza e testabilità |
| [WORKFLOW.md](coding-harness/references/WORKFLOW.md) | Ricerca, debugging, verifiche, review e checkpoint |
| [STATE.md](coding-harness/references/STATE.md) | Campi dello stato, evidenze e condizioni di verifica |
| [PROJECT_STATE.md](coding-harness/assets/templates/PROJECT_STATE.md) | Checkpoint compatto in Markdown |
| [PROJECT_STATE.json](coding-harness/assets/templates/PROJECT_STATE.json) | Checkpoint strutturato opzionale |
| [PROJECT_RECORD.md](coding-harness/assets/templates/PROJECT_RECORD.md) | Piani, decisioni ed evidenze più estese |
| [openai.yaml](coding-harness/agents/openai.yaml) | Metadati e prompt iniziale per client compatibili |

Per lavori continuativi, usa le convenzioni di stato del progetto oppure scegli un file canonico in `agent-state/`, in Markdown o JSON. Le piccole modifiche e le review non richiedono nuovi file di pianificazione. Lo stato di manutenzione di questa sorgente rimane in [REPOSITORY_STATE.md](REPOSITORY_STATE.md) e non va copiato nei progetti.

In un ambiente senza caricatore di skill, puoi usare [PROJECT_START_PROMPT.md](PROJECT_START_PROMPT.md) e chiedere all'agente di leggere la cartella sorgente. Le istruzioni guidano il comportamento; permessi reali e protezioni della repo determinano quali operazioni sono disponibili.

## Ispirazione e documentazione

Le migliorie del flusso prendono spunto da [ECC di Affaan Mustafa](https://github.com/affaan-m/ECC), revisione `ef648e01899ba3e8dc6371642deaaf64b4477775`: ricerca progressiva del contesto, test significativi, verifiche esplicite e checkpoint prima dei cambi di fase. Le istruzioni sono scritte per questa skill; non includono codice eseguibile o testi sostanziali copiati da ECC.

Procedure dei client verificate il 7 ottobre 2026 sulle documentazioni ufficiali:

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code: Skills](https://code.claude.com/docs/en/skills)
- [Cursor: Agent Skills](https://cursor.com/docs/skills)

Il vecchio kit è stato rimosso dalla sorgente; le versioni precedenti restano nella cronologia Git.
