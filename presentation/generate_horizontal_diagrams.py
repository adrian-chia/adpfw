import os
import sys
from pathlib import Path
from datetime import datetime, timezone
from loguru import logger
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dynamic path detection
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Logging setup following user rules
iso_now = datetime.now(timezone.utc).astimezone().strftime("%Y%m%d_%H%M%S")
log_path = BASE_DIR / f"generate_diagrams_{iso_now}.log"
logger.add(log_path, rotation="10 MB", level="INFO")
logger.info("Initializing horizontal diagram generator")

def create_horizontal_system_pipeline():
    logger.info("Generating horizontal system pipeline diagram...")
    fig, ax = plt.subplots(figsize=(16, 7.5), dpi=300, facecolor="#0f172a")
    ax.set_facecolor("#0f172a")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Title
    ax.text(8, 7.9, "END-TO-END ADAPTIVE DETECTION & MITIGATION PIPELINE", 
            ha="center", va="center", color="#38bdf8", fontsize=18, fontweight="bold", fontfamily="sans-serif")
    ax.text(8, 7.45, "Real-time Telemetry Ingestion -> Window Aggregation -> TCN Sequence Modeling -> Dynamic Throttling", 
            ha="center", va="center", color="#94a3b8", fontsize=11, fontfamily="sans-serif")

    # Stages data
    stages = [
        {
            "num": "01",
            "title": "TELEMETRY INGESTION",
            "subtitle": "FastAPI + API Gateway",
            "items": ["Layer 7 HTTP Header Capture", "TLS Handshake Fingerprints", "JA3 / JA4 & Cipher Suites", "Source IP & Auth Outcome"],
            "box_color": "#1e293b",
            "border_color": "#38bdf8",
            "accent": "#0284c7",
            "x": 0.6, "y": 1.4, "w": 2.6, "h": 5.2
        },
        {
            "num": "02",
            "title": "FEATURE ENGINEERING",
            "subtitle": "PostgreSQL Windowing",
            "items": ["1-min Contiguous Windows", "4 Macro Behavioral Signals:", "• Failure Rate (Ground truth)", "• Unique IPs Cardinality", "• JA3 Hash Diversity", "• Aggregate Request Volume"],
            "box_color": "#1e293b",
            "border_color": "#818cf8",
            "accent": "#4f46e5",
            "x": 3.7, "y": 1.4, "w": 2.6, "h": 5.2
        },
        {
            "num": "03",
            "title": "SEQUENCE MODELING",
            "subtitle": "Temporal ConvNet (TCN)",
            "items": ["Sliding Window (L = 10 min)", "Dilated Causal Convolutions", "Dilations: d = 1, 2, 4", "Receptive Field: 29 Steps", "Parameters: 28,241 (Compact)", "Strict Train/Val Split (70/15/15)"],
            "box_color": "#1e293b",
            "border_color": "#a855f7",
            "accent": "#9333ea",
            "x": 6.8, "y": 1.4, "w": 2.7, "h": 5.2
        },
        {
            "num": "04",
            "title": "INLINE INFERENCE",
            "subtitle": "Commodity Server CPU",
            "items": ["StandardScaler Normalization", "Fast Feedforward Execution", "Average Latency: 0.65 ms", "P99 Tail: 1.64 ms (< 2ms SLA)", "Sigmoid Attack Probability", "pos_weight Imbalance Tuning"],
            "box_color": "#1e293b",
            "border_color": "#f59e0b",
            "accent": "#d97706",
            "x": 10.0, "y": 1.4, "w": 2.6, "h": 5.2
        },
        {
            "num": "05",
            "title": "ADAPTIVE THROTTLING",
            "subtitle": "Zero-Day Mitigation",
            "items": ["Dynamic Policy Modulation", "Attack Score >= Threshold:", "  [!] Progressive Rate-Limiting", "  [!] CAPTCHA Challenge", "  [!] Zero Impact on Humans", "False Positive Rate: 0.04%"],
            "box_color": "#1e293b",
            "border_color": "#10b981",
            "accent": "#059669",
            "x": 13.1, "y": 1.4, "w": 2.5, "h": 5.2
        },
    ]

    for st in stages:
        # Outer card box
        rect = patches.FancyBboxPatch(
            (st["x"], st["y"]), st["w"], st["h"],
            boxstyle="round,pad=0.15,rounding_size=0.2",
            facecolor=st["box_color"],
            edgecolor=st["border_color"],
            linewidth=2,
            zorder=2
        )
        ax.add_patch(rect)

        # Header accent badge
        header_badge = patches.FancyBboxPatch(
            (st["x"] + 0.15, st["y"] + st["h"] - 0.95), st["w"] - 0.3, 0.75,
            boxstyle="round,pad=0.08,rounding_size=0.12",
            facecolor=st["accent"],
            edgecolor="none",
            zorder=3
        )
        ax.add_patch(header_badge)

        # Stage number & title
        ax.text(st["x"] + st["w"]/2, st["y"] + st["h"] - 0.45, f"STAGE {st['num']}",
                ha="center", va="center", color="#ffffff", fontsize=9, fontweight="bold", zorder=4)
        ax.text(st["x"] + st["w"]/2, st["y"] + st["h"] - 0.75, st["title"],
                ha="center", va="center", color="#ffffff", fontsize=10, fontweight="bold", zorder=4)

        # Subtitle
        ax.text(st["x"] + st["w"]/2, st["y"] + st["h"] - 1.25, st["subtitle"],
                ha="center", va="center", color=st["border_color"], fontsize=9.5, fontweight="semibold", style="italic", zorder=4)

        # Divider line
        ax.plot([st["x"] + 0.25, st["x"] + st["w"] - 0.25], [st["y"] + st["h"] - 1.5, st["y"] + st["h"] - 1.5],
                color="#334155", linewidth=1.2, zorder=3)

        # Bullets
        y_text = st["y"] + st["h"] - 1.85
        for item in st["items"]:
            color = "#f87171" if "[!]" in item else ("#e2e8f0" if not item.startswith("•") else "#cbd5e1")
            fontweight = "bold" if "[!]" in item or item.startswith("0") or "Signals:" in item else "normal"
            ax.text(st["x"] + 0.22, y_text, item, ha="left", va="center", color=color,
                    fontsize=8.5, fontweight=fontweight, fontfamily="sans-serif", zorder=4)
            y_text -= 0.52

    # Draw arrows connecting the stages
    arrow_props = dict(arrowstyle="-|>", color="#38bdf8", lw=3, mutation_scale=22)
    ax.annotate("", xy=(3.65, 4.0), xytext=(3.25, 4.0), arrowprops=arrow_props, zorder=5)
    ax.annotate("", xy=(6.75, 4.0), xytext=(6.35, 4.0), arrowprops=arrow_props, zorder=5)
    ax.annotate("", xy=(9.95, 4.0), xytext=(9.55, 4.0), arrowprops=arrow_props, zorder=5)
    ax.annotate("", xy=(13.05, 4.0), xytext=(12.65, 4.0), arrowprops=arrow_props, zorder=5)

    # Bottom takeaway banner
    banner = patches.FancyBboxPatch(
        (0.6, 0.3), 15.0, 0.75,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        facecolor="#1e293b",
        edgecolor="#475569",
        linewidth=1,
        zorder=2
    )
    ax.add_patch(banner)
    ax.text(8, 0.68, "Key Takeaway: Dispersed low-and-slow requests aggregate into distinct macro-behavioral anomaly vectors over time.",
            ha="center", va="center", color="#38bdf8", fontsize=10.5, fontweight="semibold")

    plt.tight_layout()
    target_path = ASSETS_DIR / "horizontal_system_architecture.png"
    plt.savefig(target_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    logger.info(f"Saved horizontal system architecture diagram to {target_path}")

def create_horizontal_tcn_architecture():
    logger.info("Generating horizontal TCN architecture diagram...")
    fig, ax = plt.subplots(figsize=(16, 7.5), dpi=300, facecolor="#0f172a")
    ax.set_facecolor("#0f172a")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Title
    ax.text(8, 7.9, "TEMPORAL CONVOLUTIONAL NETWORK (TCN) ARCHITECTURE", 
            ha="center", va="center", color="#a855f7", fontsize=18, fontweight="bold", fontfamily="sans-serif")
    ax.text(8, 7.45, "Dilated Causal Convolutions with Residual Connections | Receptive Field = 29 Steps | Total Parameters = 28,241", 
            ha="center", va="center", color="#cbd5e1", fontsize=11, fontfamily="sans-serif")

    blocks = [
        {
            "name": "INPUT SEQUENCE",
            "dim": "(batch, 4, 10)",
            "details": ["10-min History (L=10)", "4 Macro Telemetry Features:", "1. Failure Rate", "2. Unique IPs", "3. JA3 Diversity", "4. Total Requests"],
            "color": "#1e293b", "border": "#38bdf8", "header": "#0284c7",
            "x": 0.5, "y": 1.4, "w": 2.4, "h": 5.2
        },
        {
            "name": "RESIDUAL BLOCK 1",
            "dim": "in: 4 -> out: 16 | d=1",
            "details": ["Causal Conv1D (k=3, pad=2)", "ReLU Activation", "Dropout (0.20)", "Causal Conv1D (k=3, pad=2)", "ReLU + Dropout (0.20)", "1x1 Conv Shortcut (4->16)", "Receptive Field: +4 steps"],
            "color": "#1e293b", "border": "#818cf8", "header": "#4f46e5",
            "x": 3.4, "y": 1.4, "w": 2.6, "h": 5.2
        },
        {
            "name": "RESIDUAL BLOCK 2",
            "dim": "in: 16 -> out: 32 | d=2",
            "details": ["Causal Conv1D (k=3, pad=4)", "Dilation d = 2 (Skip 1)", "ReLU Activation", "Dropout (0.20)", "Causal Conv1D (k=3, pad=4)", "1x1 Conv Shortcut (16->32)", "Receptive Field: +8 steps"],
            "color": "#1e293b", "border": "#a855f7", "header": "#7e22ce",
            "x": 6.5, "y": 1.4, "w": 2.6, "h": 5.2
        },
        {
            "name": "RESIDUAL BLOCK 3",
            "dim": "in: 32 -> out: 64 | d=4",
            "details": ["Causal Conv1D (k=3, pad=8)", "Dilation d = 4 (Skip 3)", "ReLU Activation", "Dropout (0.20)", "Causal Conv1D (k=3, pad=8)", "1x1 Conv Shortcut (32->64)", "Receptive Field: +16 steps"],
            "color": "#1e293b", "border": "#ec4899", "header": "#be185d",
            "x": 9.6, "y": 1.4, "w": 2.6, "h": 5.2
        },
        {
            "name": "CLASSIFICATION HEAD",
            "dim": "Linear(64 -> 1)",
            "details": ["Global Sequence Slicing", "Last Timestep t = 10", "Fully Connected Layer", "Sigmoid Activation σ(z)", "Output: Attack Prob [0, 1]", "Decision Boundary: 0.50 / 0.90", "Loss: BCEWithLogitsLoss"],
            "color": "#1e293b", "border": "#10b981", "header": "#047857",
            "x": 12.7, "y": 1.4, "w": 2.8, "h": 5.2
        }
    ]

    for blk in blocks:
        rect = patches.FancyBboxPatch(
            (blk["x"], blk["y"]), blk["w"], blk["h"],
            boxstyle="round,pad=0.15,rounding_size=0.2",
            facecolor=blk["color"],
            edgecolor=blk["border"],
            linewidth=2,
            zorder=2
        )
        ax.add_patch(rect)

        # Header badge
        badge = patches.FancyBboxPatch(
            (blk["x"] + 0.12, blk["y"] + blk["h"] - 0.95), blk["w"] - 0.24, 0.75,
            boxstyle="round,pad=0.08,rounding_size=0.12",
            facecolor=blk["header"],
            edgecolor="none",
            zorder=3
        )
        ax.add_patch(badge)

        ax.text(blk["x"] + blk["w"]/2, blk["y"] + blk["h"] - 0.45, blk["name"],
                ha="center", va="center", color="#ffffff", fontsize=9.5, fontweight="bold", zorder=4)
        ax.text(blk["x"] + blk["w"]/2, blk["y"] + blk["h"] - 0.75, blk["dim"],
                ha="center", va="center", color="#e2e8f0", fontsize=8.5, fontfamily="monospace", zorder=4)

        ax.plot([blk["x"] + 0.2, blk["x"] + blk["w"] - 0.2], [blk["y"] + blk["h"] - 1.25, blk["y"] + blk["h"] - 1.25],
                color="#334155", linewidth=1.2, zorder=3)

        y_txt = blk["y"] + blk["h"] - 1.6
        for line in blk["details"]:
            is_hl = "Receptive Field:" in line or "Attack Prob" in line or "10-min" in line
            c = "#38bdf8" if is_hl else "#cbd5e1"
            fw = "bold" if is_hl else "normal"
            ax.text(blk["x"] + 0.18, y_txt, line, ha="left", va="center", color=c,
                    fontsize=8.5, fontweight=fw, fontfamily="sans-serif", zorder=4)
            y_txt -= 0.48

    # Connect blocks with arrows
    arrow_props = dict(arrowstyle="-|>", color="#a855f7", lw=3, mutation_scale=22)
    ax.annotate("", xy=(3.35, 4.0), xytext=(2.95, 4.0), arrowprops=arrow_props, zorder=5)
    ax.annotate("", xy=(6.45, 4.0), xytext=(6.05, 4.0), arrowprops=arrow_props, zorder=5)
    ax.annotate("", xy=(9.55, 4.0), xytext=(9.15, 4.0), arrowprops=arrow_props, zorder=5)
    ax.annotate("", xy=(12.65, 4.0), xytext=(12.25, 4.0), arrowprops=arrow_props, zorder=5)

    # Receptive field formula banner at bottom
    banner = patches.FancyBboxPatch(
        (0.5, 0.3), 15.0, 0.75,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        facecolor="#1e293b",
        edgecolor="#64748b",
        linewidth=1,
        zorder=2
    )
    ax.add_patch(banner)
    formula_txt = r"Receptive Field Formula: $RF = 1 + \sum_{l=0}^{2} 2 \cdot (k-1) \cdot d_l = 1 + 2 \cdot (3-1) \cdot (1 + 2 + 4) = 29$ steps ($> L=10$ sequence length)"
    ax.text(8, 0.68, formula_txt, ha="center", va="center", color="#38bdf8", fontsize=11, fontweight="semibold")

    plt.tight_layout()
    target_path = ASSETS_DIR / "horizontal_tcn_architecture.png"
    plt.savefig(target_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    logger.info(f"Saved horizontal TCN architecture diagram to {target_path}")

def create_attack_vs_defense_infographic():
    logger.info("Generating attack vs defense infographic...")
    fig, ax = plt.subplots(figsize=(16, 7.5), dpi=300, facecolor="#0f172a")
    ax.set_facecolor("#0f172a")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Main Title
    ax.text(8, 7.9, "THE PERIMETER BLIND SPOT: STATIC GATEWAYS VS. ADAPTIVE TCN", 
            ha="center", va="center", color="#f87171", fontsize=18, fontweight="bold", fontfamily="sans-serif")
    ax.text(8, 7.45, "Why Static Volumetric Thresholds Fail Against Evasive, Distributed Botnets", 
            ha="center", va="center", color="#cbd5e1", fontsize=11, fontfamily="sans-serif")

    # Left Box: Traditional Defense (Failure)
    trad_box = patches.FancyBboxPatch(
        (0.6, 0.9), 6.9, 6.1,
        boxstyle="round,pad=0.15,rounding_size=0.25",
        facecolor="#1e293b",
        edgecolor="#ef4444",
        linewidth=2.5,
        zorder=2
    )
    ax.add_patch(trad_box)

    # Header badge left
    badge_left = patches.FancyBboxPatch(
        (0.9, 6.1), 6.3, 0.75,
        boxstyle="round,pad=0.08,rounding_size=0.15",
        facecolor="#b91c1c",
        edgecolor="none",
        zorder=3
    )
    ax.add_patch(badge_left)
    ax.text(4.05, 6.47, "TRADITIONAL STATIC GATEWAY (WAF / RATE-LIMIT)", 
            ha="center", va="center", color="#ffffff", fontsize=10.5, fontweight="bold", zorder=4)

    # Content left
    items_left = [
        ("• Operational Logic:", "#94a3b8", "bold"),
        ("  Static Per-IP quota (e.g. max 60-100 req/min/IP)", "#e2e8f0", "normal"),
        ("• Attacker Strategy:", "#f87171", "bold"),
        ("  Distributed residential proxy pool (10,000+ nodes)", "#e2e8f0", "normal"),
        ("  Throttled velocity: Exactly 1 req/min per IP", "#fbbf24", "semibold"),
        ("• Telemetry Visibility:", "#94a3b8", "bold"),
        ("  Evaluates IPs in isolation; ignores TLS handshake dynamics", "#e2e8f0", "normal"),
        ("• The Outcome:", "#ef4444", "bold"),
        ("  [FAIL] 1 < 100 threshold -> Rate limit NEVER triggers!", "#ef4444", "bold"),
        ("  [FAIL] Full credential stuffing campaign executes undetected.", "#fca5a5", "normal")
    ]
    y_l = 5.75
    for text, col, fw in items_left:
        ax.text(1.0, y_l, text, ha="left", va="center", color=col, fontsize=9.2, fontweight=fw, zorder=4)
        y_l -= 0.38

    # Big Red Verdict Left
    verdict_left = patches.FancyBboxPatch(
        (1.0, 1.1), 6.1, 0.65,
        boxstyle="round,pad=0.08,rounding_size=0.12",
        facecolor="#7f1d1d",
        edgecolor="#ef4444",
        linewidth=1.5,
        zorder=3
    )
    ax.add_patch(verdict_left)
    ax.text(4.05, 1.42, "STATUS: 100% BYPASS - CREDENTIALS COMPROMISED", 
            ha="center", va="center", color="#fca5a5", fontsize=10.5, fontweight="bold", zorder=4)

    # Right Box: Proposed TCN Defense (Success)
    prop_box = patches.FancyBboxPatch(
        (8.5, 0.9), 6.9, 6.1,
        boxstyle="round,pad=0.15,rounding_size=0.25",
        facecolor="#1e293b",
        edgecolor="#10b981",
        linewidth=2.5,
        zorder=2
    )
    ax.add_patch(prop_box)

    # Header badge right
    badge_right = patches.FancyBboxPatch(
        (8.8, 6.1), 6.3, 0.75,
        boxstyle="round,pad=0.08,rounding_size=0.15",
        facecolor="#047857",
        edgecolor="none",
        zorder=3
    )
    ax.add_patch(badge_right)
    ax.text(11.95, 6.47, "ADAPTIVE SELF-LEARNING TCN DEFENSE", 
            ha="center", va="center", color="#ffffff", fontsize=10.5, fontweight="bold", zorder=4)

    # Content right
    items_right = [
        ("• Operational Logic:", "#94a3b8", "bold"),
        ("  Campaign-level sliding sequence modeling (L=10 min)", "#e2e8f0", "normal"),
        ("• Attacker Strategy Countered:", "#34d399", "bold"),
        ("  Cross-IP correlation tracks macro anomaly signatures", "#e2e8f0", "normal"),
        ("  TLS cipher suite & JA3/JA4 cryptographic invariant anchoring", "#38bdf8", "semibold"),
        ("• Multi-Dimensional Telemetry:", "#94a3b8", "bold"),
        ("  Failure rate (40%+) + IP cardinality surge + cipher stunting", "#e2e8f0", "normal"),
        ("• The Outcome:", "#10b981", "bold"),
        ("  [SUCCESS] 1.0000 Detection Recall across 33.7M requests!", "#10b981", "bold"),
        ("  [SUCCESS] 0.65 ms CPU inference with 0.04% False Alarm Rate.", "#38bdf8", "semibold")
    ]
    y_r = 5.75
    for text, col, fw in items_right:
        ax.text(8.9, y_r, text, ha="left", va="center", color=col, fontsize=9.2, fontweight=fw, zorder=4)
        y_r -= 0.38

    # Big Green Verdict Right
    verdict_right = patches.FancyBboxPatch(
        (8.9, 1.1), 6.1, 0.65,
        boxstyle="round,pad=0.08,rounding_size=0.12",
        facecolor="#064e3b",
        edgecolor="#10b981",
        linewidth=1.5,
        zorder=3
    )
    ax.add_patch(verdict_right)
    ax.text(11.95, 1.42, "STATUS: NEUTRALIZED - ZERO USER FRICTION", 
            ha="center", va="center", color="#6ee7b7", fontsize=10.5, fontweight="bold", zorder=4)

    # VS icon in middle
    vs_circle = plt.Circle((8.0, 3.95), 0.55, color="#334155", ec="#64748b", lw=2, zorder=5)
    ax.add_patch(vs_circle)
    ax.text(8.0, 3.95, "VS", ha="center", va="center", color="#f8fafc", fontsize=12, fontweight="black", zorder=6)

    # Bottom Takeaway Banner
    banner = patches.FancyBboxPatch(
        (0.6, 0.15), 14.8, 0.58,
        boxstyle="round,pad=0.08,rounding_size=0.15",
        facecolor="#1e293b",
        edgecolor="#475569",
        linewidth=1,
        zorder=2
    )
    ax.add_patch(banner)
    ax.text(8, 0.44, "Thesis Insight: Low-frequency attacks are invisible per-IP, but glaringly anomalous when aggregated across time.",
            ha="center", va="center", color="#38bdf8", fontsize=10, fontweight="semibold")

    plt.tight_layout()
    target_path = ASSETS_DIR / "attack_vs_defense_infographic.png"
    plt.savefig(target_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    logger.info(f"Saved attack vs defense infographic to {target_path}")

if __name__ == "__main__":
    create_horizontal_system_pipeline()
    create_horizontal_tcn_architecture()
    create_attack_vs_defense_infographic()
    logger.info("Diagram generation complete!")

