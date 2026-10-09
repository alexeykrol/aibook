# Handoff (general): полный статус aibook для продолжения на другой машине

## Metadata

- Created: 2026-10-09T07:20-07:00
- Project root: `/Users/alexeykrolmini/Code/aibook` (на другой машине — где склонирован репозиторий)
- Remote: `https://github.com/alexeykrol/aibook` — **публичный** репозиторий
- Branch: `main`
- Stable refs:
  - `dae1a2e` — коммит синхронизации рабочего состояния (AGENTS/manifest, структура, README устарели)
  - `6534eeb`, `f348ba6`, `99538fa`, `c7e8077` — 4 главы на `main` (2026-03-20)
  - ветки `agent-org-test` (`feefc51`) и `sdk-v2-test` (`c423e64`) — эксперименты автономного написания
  - живой HEAD смотреть через `git log`
- Source description: владелец переходит на другую машину; всё закоммичено и запушено, нужна точка продолжения.
- TYPE: general

## Role & Scope

Продолжение работы над книгой в новой сессии. Роли по `CLAUDE.md`: автор пишет и
принимает творческие решения; AI ведёт рутину — структуру, мета-файлы, фактчекинг,
исследования, контроль логики. **AI не пишет и не правит авторский текст без явного запроса.**
Судьба экспериментальных веток (слить / взять за основу / выбросить) — решение владельца,
не агента. До этого решения ничего из них в `main` не переносить.

## Project Context

«AI Quest: Now You Can!» — книга-квест в формате ЛитРПГ об освоении ИИ: введение,
инструкция по выживанию, 10 уровней (теория → босс → квесты → награда), приложения.
Структура (фаза 1) закрыта в декабре 2025. В марте 2026 прошли эксперименты, где автономный
агент написал полный черновик книги в двух отдельных ветках. Параллельно на `main` легли
4 главы. С апреля по октябрь 2026 содержательной работы не было — только метафайлы.

## Read First

- `CLAUDE.md` — роли автор/AI, правила, cold start
- `meta/PROJECT_SNAPSHOT.md` — вверху блок «Актуальное состояние (2026-10-09)»
- `meta/BOOK_STRUCTURE_ORDERED.md` — **источник правды по структуре** (README устарели)
- `meta/BACKLOG.md` — фазы (таблица прогресса отстаёт, см. ниже)
- `manifest.md`, `AGENTS.md`
- Для экспериментов: `git show sdk-v2-test:PROGRESS.md`, `git show sdk-v2-test:agent_org/charter/mission.md`,
  `git show agent-org-test:run_book_agent.sh`

## Grounded Facts (verified 2026-10-09)

- `git status --short --branch` → `## main...origin/main`, дерево чистое (после пуша)
- `git -c core.quotepath=off ls-tree -r --name-only main content | grep -c '\.md$'` → `6`
  (введение, инструкция, `2.2_Босс`, `3.1_Теория`, `4.2_Босс`, `A.1_Глоссарий`)
- `git rev-list --count main..origin/agent-org-test` → `100`; `main..origin/sdk-v2-test` → `101`
- `git merge-base main origin/sdk-v2-test` → `4bd3561` (обе ветки отходят от одной точки, до 4 глав на main)
- Статусы глав в `PROGRESS.md` каждой экспериментальной ветки → `done=52 pending=0`
  (zsh: писать `git show "${b}:PROGRESS.md"` — без фигурных скобок `$b:P` ломается)
- Те 4 главы, что лежат на `main`, **отличаются** от одноимённых файлов в обеих ветках (сравнение blob-хешей) — это третья, отдельная версия
- Коммиты 4 глав на `main` содержат `Co-Authored-By: Claude Opus 4.6`
- Ветки `alexeykrol2-patch-1..4` на origin — тестовые PR про `t3.md`/`t4.md` от 2025-12-09, по 1 коммиту, ценности нет

Метафайлы — карта, а не территория: перепроверяй командами выше.

## Current State

Done (verified):
- Фаза 1 «Структура» — папки, шаблоны, slash-команды (`/sync`, `/sprint-done`, `/commit`, `/explain`, `/sync-git`)
- На `main`: `1_Введение.md`, `Инструкция по выживанию.md` + 4 главы от 2026-03-20
- Две экспериментальные ветки с полным черновиком (52 главы каждая) — на origin
- В этой сессии: закоммичены и запушены все локальные изменения (`dae1a2e`), `.claude/worktrees/` добавлен в `.gitignore`,
  в `meta/PROJECT_SNAPSHOT.md` добавлен блок актуального состояния, создан этот handoff

Pending:
- Решение владельца по экспериментальным веткам (см. Open Questions)
- Фазы 2–7 в `meta/BACKLOG.md` числятся на 0% — таблица не отражает ни 4 главы на main, ни черновики в ветках
- Уровни 4–10 на `main` пустые (`.gitkeep`); уровень 9 без названия (`10_уровень_9_tbd`)

## Перенос на другую машину

```bash
git clone https://github.com/alexeykrol/aibook.git && cd aibook
git fetch origin agent-org-test sdk-v2-test
# по желанию — вернуть локальные worktrees экспериментов:
git worktree add .claude/worktrees/agent-org-test agent-org-test
git worktree add .claude/worktrees/sdk-v2-test sdk-v2-test
```

Чего в репозитории нет (жило только на старой машине):
- глобальные правила, скиллы и агенты `~/.claude/` (`rules/`, `skills/handoff`, агенты `writer`/`editor` и т.д.)
- файлы, на которые абсолютными путями ссылаются `CLAUDE.md`/`AGENTS.md`:
  `/Users/alexeykrolmini/Code/CLAUDE_CODE_PIPELINE_MODEL_SELECTION_HANDOFF.md`,
  `/Users/alexeykrolmini/Code/GPT-5.6-model-selection-guide-ru.md`, `~/.codex/AGENTS.md` (для книги не критичны)
- `aibook.code-workspace` подключает соседнюю папку `../AGIbook` — отдельный репозиторий, клонировать рядом, если нужен

## Files / Contracts In Scope

- `content/` — текст книги (авторская зона)
- `meta/` — мета-файлы (зона AI)
- `templates/` — шаблоны уровня, квеста, кейса
- `.claude/commands/` — slash-команды проекта
- экспериментальные ветки — только читать, пока владелец не решит

## Decisions Made

- `.claude/worktrees/` не коммитится: это локальные worktrees, их ветки уже на origin под теми же хешами
- По прямой команде владельца «закоммить всё» в **публичный** репозиторий ушли и служебные файлы:
  `.claude/INVESTMENT.md` (мемо стратегической ставки), `.claude/settings.json`, `AGENTS.md`, `manifest.md`
- Таблицы `PROJECT_SNAPSHOT`/`BACKLOG` целиком не переписывались — добавлен только датированный блок актуального состояния

## Open Questions / Blockers

1. **Что делать с черновиками автономного агента?** Варианты: взять одну ветку как черновую основу для авторской правки /
   разбирать по главам / оставить архивом. Противоречит правилу `CLAUDE.md` «AI не пишет авторский текст» — нужно решение владельца.
2. **Какая версия 4 глав каноническая** — та, что на `main`, или одна из веток?
3. `manifest.md` говорит `project_type=course`, а `CLAUDE.md` описывает книгу — что верно?
4. Удалить мусорные ветки `alexeykrol2-patch-1..4` на origin? (необратимо — только с подтверждения)
5. Остаётся ли репозиторий публичным, раз в нём теперь `.claude/INVESTMENT.md`?

## Recommended Next Move

Выдать владельцу короткое сравнение двух экспериментальных веток (объём, качество 2–3 глав-образцов,
соответствие `BOOK_STRUCTURE_ORDERED.md`) и получить решение по вопросу 1. До решения — только чтение.

## Kickoff Prompt

```text
Ты новая Claude Code session для проекта aibook (корень — папка клона
https://github.com/alexeykrol/aibook). Сначала открой и прочитай handoff:
.handoffs/2026-10-09-0720-full-status-sync.md
(на исходной машине: /Users/alexeykrolmini/Code/aibook/.handoffs/2026-10-09-0720-full-status-sync.md)

Затем прочитай документы из раздела "Read First". После этого GROUND-VERIFY
факты командами из "Grounded Facts"; не доверяй metafiles без проверки.

Твоя роль: продолжение работы над книгой-квестом. AI ведёт структуру,
мета-файлы, фактчекинг и анализ; авторский текст не пишет и не правит без
явного запроса. Экспериментальные ветки только читаешь — их судьбу решает владелец.

После чтения и проверки выдай в чат Verification Report:
- Understood: роль, scope, состояние своими словами (не эхо handoff).
- Verified: какие команды прогнал и совпали ли факты (с реальными числами).
- Discrepancies: расхождения или `—`.
- Questions: вопросы или `—`.
- Readiness: `ready on confirmation` / `blocked: ...`, плюс proposed first move.

Не начинай работу до подтверждения владельца.
```
