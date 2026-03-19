#!/bin/bash
# Autonomous book writing loop
# Usage: bash run_book_agent.sh [max_runs]
# Default: 50 runs (enough for all 48 chapters)

set -euo pipefail

WORKDIR="$(cd "$(dirname "$0")" && pwd)"
MAX_RUNS="${1:-50}"
RUN_COUNT=0
LOG_DIR="$WORKDIR/agent_org/logs"
mkdir -p "$LOG_DIR"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Autonomous Book Agent — Continuous Loop"
echo "  Max runs: $MAX_RUNS"
echo "  Workdir: $WORKDIR"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

PROMPT='Прочитай AUTONOMOUS_MISSION.md. Выполни один цикл: найди первую pending главу в PROGRESS.md, напиши её, коммить, обнови PROGRESS.md, коммить. Если все главы done — создай финальный коммит и скажи "BOOK_COMPLETE". Работай автономно, не задавай вопросов.'

while [ "$RUN_COUNT" -lt "$MAX_RUNS" ]; do
    RUN_COUNT=$((RUN_COUNT + 1))
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    LOG_FILE="$LOG_DIR/run_${RUN_COUNT}_${TIMESTAMP}.log"

    echo ""
    echo "[RUN $RUN_COUNT/$MAX_RUNS] $(date '+%H:%M:%S') Starting..."

    # Check if book is complete
    if grep -q "BOOK_COMPLETE" "$LOG_DIR"/*.log 2>/dev/null; then
        echo "[DONE] Book marked complete in previous run. Stopping."
        break
    fi

    # Check remaining chapters
    REMAINING=$(grep -c "| pending |" "$WORKDIR/PROGRESS.md" 2>/dev/null || echo "0")
    echo "[INFO] Chapters remaining: $REMAINING"

    if [ "$REMAINING" -eq 0 ]; then
        echo "[DONE] All chapters marked done. Stopping."
        break
    fi

    # Run agent
    cd "$WORKDIR"
    claude -p "$PROMPT" --dangerously-skip-permissions > "$LOG_FILE" 2>&1 || true

    # Check result
    if grep -q "BOOK_COMPLETE" "$LOG_FILE"; then
        echo "[DONE] Agent signaled BOOK_COMPLETE."
        break
    fi

    # Show what was done
    LAST_COMMIT=$(git log --oneline -1 2>/dev/null || echo "no commit")
    echo "[RUN $RUN_COUNT] Done. Last commit: $LAST_COMMIT"

    # Brief pause between runs
    sleep 5
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Loop finished after $RUN_COUNT runs"
echo "  Logs: $LOG_DIR/"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Final stats
DONE=$(grep -c "| done |" "$WORKDIR/PROGRESS.md" 2>/dev/null || echo "0")
PENDING=$(grep -c "| pending |" "$WORKDIR/PROGRESS.md" 2>/dev/null || echo "0")
echo "  Chapters done: $DONE"
echo "  Chapters pending: $PENDING"
