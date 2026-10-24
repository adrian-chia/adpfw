import os
import sys
from pathlib import Path
from datetime import datetime, timezone
from loguru import logger
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Dynamic path detection
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
OUTPUT_PPTX = BASE_DIR / "slides.pptx"

# Loguru logging setup
iso_now = datetime.now(timezone.utc).astimezone().strftime("%Y%m%d_%H%M%S")
log_path = BASE_DIR / f"generate_powerpoint_{iso_now}.log"
logger.add(log_path, rotation="10 MB", level="INFO")
logger.info("Initializing PowerPoint generator for Master's thesis presentation")

# Color Palette
BG_COLOR = RGBColor(9, 13, 22)        # Deep Slate #090D16
CARD_BG = RGBColor(19, 27, 46)        # Dark Blue Card #131B2E
BORDER_COLOR = RGBColor(36, 50, 79)   # Border #24324F
TEXT_MAIN = RGBColor(248, 250, 252)   # Pure White #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)  # Muted Slate #94A3B8
TEXT_DIM = RGBColor(100, 116, 139)    # Dim Slate #64748B
ACCENT_CYAN = RGBColor(56, 189, 248)  # Cyan #38BDF8
ACCENT_GREEN = RGBColor(16, 185, 129) # Emerald #10B981
ACCENT_RED = RGBColor(239, 68, 68)    # Coral Red #EF4444
ACCENT_PURPLE = RGBColor(168, 85, 247)# Purple #A855F7
ACCENT_AMBER = RGBColor(245, 158, 11) # Amber #F59E0B

def set_slide_background(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_header(slide, tag_text, target_time, title_text, subtitle_text):
    # Header container
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.3))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    # Line 1: Tag & Time
    p1 = tf.paragraphs[0]
    r_tag = p1.add_run()
    r_tag.text = tag_text.upper()
    r_tag.font.size = Pt(9.5)
    r_tag.font.bold = True
    r_tag.font.color.rgb = ACCENT_CYAN
    r_tag.font.name = "Arial"

    r_space = p1.add_run()
    r_space.text = "   |   "
    r_space.font.size = Pt(9.5)
    r_space.font.color.rgb = TEXT_DIM

    r_time = p1.add_run()
    r_time.text = f"Target: {target_time}"
    r_time.font.size = Pt(9.5)
    r_time.font.color.rgb = TEXT_MUTED
    r_time.font.name = "Arial"

    # Line 2: Title
    p2 = tf.add_paragraph()
    p2.space_before = Pt(4)
    r_title = p2.add_run()
    r_title.text = title_text
    r_title.font.size = Pt(21)
    r_title.font.bold = True
    r_title.font.color.rgb = TEXT_MAIN
    r_title.font.name = "Arial"

    # Line 3: Subtitle
    p3 = tf.add_paragraph()
    p3.space_before = Pt(2)
    r_sub = p3.add_run()
    r_sub.text = subtitle_text
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = TEXT_MUTED
    r_sub.font.name = "Arial"

def add_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = notes_text

def add_card(slide, left, top, width, height, border_color=BORDER_COLOR, bg_color=CARD_BG):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)
    return shape

def add_stat_card(slide, left, top, width, height, val_text, lbl_text, sub_text, val_color=ACCENT_CYAN):
    add_card(slide, left, top, width, height)
    tb = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.12), width - Inches(0.3), height - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_val = tf.paragraphs[0]
    r_val = p_val.add_run()
    r_val.text = val_text
    r_val.font.size = Pt(26)
    r_val.font.bold = True
    r_val.font.color.rgb = val_color
    r_val.font.name = "Arial"

    p_lbl = tf.add_paragraph()
    p_lbl.space_before = Pt(2)
    r_lbl = p_lbl.add_run()
    r_lbl.text = lbl_text.upper()
    r_lbl.font.size = Pt(9.5)
    r_lbl.font.bold = True
    r_lbl.font.color.rgb = TEXT_MUTED
    r_lbl.font.name = "Arial"

    p_sub = tf.add_paragraph()
    p_sub.space_before = Pt(2)
    r_sub = p_sub.add_run()
    r_sub.text = sub_text
    r_sub.font.size = Pt(8.5)
    r_sub.font.color.rgb = TEXT_DIM
    r_sub.font.name = "Arial"

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    logger.info("Building Slide 1: Title & Hook")
    # SLIDE 1
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)
    add_header(s1, "Master's Thesis Presentation", "0:00 - 1:15", 
               "Self-Learning Systems", 
               "Securing API login endpoints against “low and slow” botnet credential stuffing using self-learning systems")
    
    # Left Card
    c1 = add_card(s1, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.1), border_color=ACCENT_CYAN)
    tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.6), Inches(4.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    r = p.add_run()
    r.text = "RESEARCH CANDIDATE & SCOPE\n"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN
    
    r = p.add_run()
    r.text = "Adrian Chia\n"
    r.font.size = Pt(20)
    r.font.bold = True
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "Master's in Digital Security, Cloud Architecture & Deep Learning\n\n"
    r.font.size = Pt(11)
    r.font.color.rgb = TEXT_MUTED

    r = p.add_run()
    r.text = "THE OPENING HOOK: THE GHOST IN THE API\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER

    r = p.add_run()
    r.text = "«Imagine a burglar who doesn't blow the vault door open with dynamite. Instead, 10,000 disguised people walk in through 10,000 different branch doors, spaced 5 minutes apart, politely whispering a stolen PIN.\n\n"
    r.text += "That is low-and-slow credential stuffing — and your firewall welcomes them as legitimate customers.»\n\n"
    r.font.size = Pt(11.5)
    r.font.italic = True
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "• Telemetry Evaluated: 33.7 Million Requests | 233 Hours\n• Model: 3-Block Causal TCN (28,241 parameters)\n• Execution: 0.65ms on Commodity Server CPU"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MUTED

    # Right Stat Cards
    add_stat_card(s1, Inches(7.1), Inches(1.8), Inches(2.6), Inches(2.4), "22%", "Breach Access Vector", "Verizon DBIR (Stolen Credentials)", ACCENT_RED)
    add_stat_card(s1, Inches(9.9), Inches(1.8), Inches(2.6), Inches(2.4), "1 req/min", "Evasive Bot Cadence", "Operates below static rate limits", ACCENT_AMBER)
    add_stat_card(s1, Inches(7.1), Inches(4.5), Inches(2.6), Inches(2.4), "1.0000", "Detection Recall", "Enterprise 233-hr blind test", ACCENT_GREEN)
    add_stat_card(s1, Inches(9.9), Inches(4.5), Inches(2.6), Inches(2.4), "0.65 ms", "Commodity CPU Speed", "Inline gateway pass (< 1% SLA)", ACCENT_CYAN)

    add_speaker_notes(s1, 
        "[0:00 - 1:15] Open with confidence. Greet the audience and committee.\n\n"
        "Good morning, members of the evaluation committee, distinguished professors, and colleagues. Today, I am presenting my Master's thesis: \"Self-learning systems - Securing API login endpoints against 'low and slow' botnet credential stuffing using self-learning systems.\"\n\n"
        "I want you to imagine a bank heist. In the movies, robbers crash an armored truck through the lobby with alarms blaring. That is a traditional brute-force DDoS attack. We have firewalls and rate limiters that stop that in seconds.\n\n"
        "Now imagine 10,000 different people walking in through 10,000 branch doors, spaced 5 minutes apart, politely whispering a stolen PIN. That is low-and-slow credential stuffing. To your security tools, every single request looks like a harmless individual. But across your entire enterprise, your customer accounts are being drained.\n\n"
        "Today, I will show you how we solve this blind spot using deep sequence learning and transport-layer TLS invariants — operating directly on general-purpose CPUs in less than a millisecond."
    )

    # SLIDE 2: Threat Evolution
    logger.info("Building Slide 2: Threat Evolution")
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "The Threat Landscape", "1:15 - 2:15",
               "The Threat Evolution: When Brute-Force Went 'Low-and-Slow'",
               "How threat actors industrialize compromised identity verification at massive scale")

    # 3 Cards
    col_w = Inches(3.7)
    gap = Inches(0.3)
    
    # Col 1
    add_card(s2, Inches(0.8), Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_RED)
    tb = s2.shapes.add_textbox(Inches(1.0), Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "⚠️ Password Reuse Crisis\n\n"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = ACCENT_RED
    r = p.add_run()
    r.text = "• Rampant Reuse: Users reuse identical passwords across 51% of digital accounts (Verizon DBIR 2025).\n\n"
    r.text += "• Dark Web Supply: Billions of leaked credential pairs from third-party breaches are weaponized against API login endpoints.\n\n"
    r.text += "• The Verification Oracle: Attackers query standard login APIs as automated password verification oracles."
    r.font.size = Pt(11)
    r.font.color.rgb = TEXT_MAIN

    # Col 2
    add_card(s2, Inches(0.8) + col_w + gap, Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_AMBER)
    tb = s2.shapes.add_textbox(Inches(1.0) + col_w + gap, Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "🤖 AI & Residential Botnets\n\n"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "• Massive Proxy Pools: Rotates across 10,000+ distinct residential IP addresses (infected IoT & consumer broadband).\n\n"
    r.text += "• Suppressed Cadence: Request frequency throttled to 1 attempt per minute per IP, staying strictly beneath static quotas.\n\n"
    r.text += "• Explosive Growth: Akamai reports a 113% year-over-year surge in daily API attacks; 61% target authentication workflows."
    r.font.size = Pt(11)
    r.font.color.rgb = TEXT_MAIN

    # Col 3
    add_card(s2, Inches(0.8) + (col_w + gap)*2, Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_CYAN)
    tb = s2.shapes.add_textbox(Inches(1.0) + (col_w + gap)*2, Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "🎭 Browser Impersonation\n\n"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN
    r = p.add_run()
    r.text = "• Specialized HTTP Clients: Deploys curl_cffi and tls_client capable of mimicking Chrome and Safari TLS signatures.\n\n"
    r.text += "• Dynamic Header Spoofing: Injects randomized User-Agent strings and deceptive X-Forwarded-For topologies.\n\n"
    r.text += "• OWASP Top 10:2025: Categorized under A07:2025 Authentication Failures — lack of layered behavioral telemetry."
    r.font.size = Pt(11)
    r.font.color.rgb = TEXT_MAIN

    # Bottom Banner
    add_card(s2, Inches(0.8), Inches(6.6), Inches(11.733), Inches(0.6), border_color=BORDER_COLOR)
    tb_b = s2.shapes.add_textbox(Inches(1.0), Inches(6.65), Inches(11.3), Inches(0.5))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    r = p.add_run()
    r.text = "Industry Reality: Credential stuffing generates 19% to 25% of all enterprise authentication traffic. Attackers don't break encryption — they log in with valid credentials."
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN

    add_speaker_notes(s2,
        "[1:15 - 2:15] Build urgency with hard industry data.\n\n"
        "Let's look at why this problem has exploded. We are living through an unprecedented password reuse crisis. According to Verizon's 2025 Data Breach Investigations Report, stolen credentials remain the initial access vector in 22% of all breaches. Why? Because the average person reuses passwords across more than half of their accounts.\n\n"
        "When a breach occurs at an obscure online store, those millions of username-password pairs don't sit idle. Automated botnets immediately take those credentials and test them against your mobile and web APIs. They treat your login endpoint as a 'Password Verification Oracle'.\n\n"
        "And they aren't firing from Russian server farms anymore. They route traffic through millions of residential proxies — infected IoT devices and consumer home routers right in our neighborhoods. Each IP sends just one request every few minutes.\n\n"
        "To an external observer, it looks like an ordinary human browsing from home. But across the entire network, it is a coordinated attack wave."
    )

    # SLIDE 3: The Perimeter Blind Spot
    logger.info("Building Slide 3: The Perimeter Blind Spot")
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "The Problem Statement", "2:15 - 3:30",
               "The Great Perimeter Blind Spot: The Failure of Static Rate Limits",
               "Why traditional Web Application Firewalls (WAFs) and API Gateways are completely bypassed")

    img_path = ASSETS_DIR / "attack_vs_defense_infographic.png"
    if img_path.exists():
        s3.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.8), width=Inches(11.733))

    add_speaker_notes(s3,
        "[2:15 - 3:30] Walk through the diagram. Point out the core mathematical flaw.\n\n"
        "Here lies the fundamental vulnerability of modern API architecture. Look at the left side of this infographic. Every major cloud provider — whether AWS API Gateway, Azure, Kong, or traditional WAFs — operates on static rate limiting.\n\n"
        "A typical production rule says: 'If any IP sends more than 100 requests per minute, throttle it.' That sounds reasonable until you realize how botnets operate. The adversary distributes the attack across 10,000 residential nodes. Each IP makes exactly ONE request per minute.\n\n"
        "One is less than 100. So the gateway smiles, says 'Welcome friend!', and passes the request straight to your authentication database. In one hour, 10,000 credentials are validated, and not a single alert triggers in your SOC.\n\n"
        "And you cannot just block those IPs! Those are legitimate Comcast, Verizon, and Singtel residential broadband IPs. If you block them, you lock out your actual customers. We need a completely different defensive paradigm."
    )

    # SLIDE 4: The Paradigm Shift
    logger.info("Building Slide 4: The Paradigm Shift")
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "The Defensive Paradigm", "3:30 - 4:45",
               "The Paradigm Shift: From Brittle Rules to Self-Learning Baselines",
               "Why low-frequency distributed attacks must be modeled as multi-dimensional temporal sequences")

    # Left Card
    add_card(s4, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1), border_color=ACCENT_PURPLE)
    tb = s4.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "CORE THESIS HYPOTHESIS\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_PURPLE

    r = p.add_run()
    r.text = "«Standard API Gateway rate limiting fails against highly distributed, ‘low-and-slow' credential stuffing botnets.\n\n"
    r.text += "This thesis proposes that training machine learning models on a combined telemetry of TLS fingerprints and request header analysis provides a highly accurate, adaptive defence mechanism capable of neutralizing low frequency authentication attacks.»\n\n"
    r.font.size = Pt(11.5)
    r.font.italic = True
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "• Point-in-Time Blindness: Any single request from a residential proxy looks indistinguishable from human browsing.\n\n"
    r.text += "• Macro-Temporal Visibility: When aggregated over continuous time windows, coordinated botnet campaigns produce distinct statistical spikes in failure rates and client diversity."
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MUTED

    # Right Card: 3 Pillars
    add_card(s4, Inches(6.8), Inches(1.8), Inches(5.733), Inches(5.1), border_color=ACCENT_GREEN)
    tb = s4.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "THE THREE ARCHITECTURAL PILLARS\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    r = p.add_run()
    r.text = "1. Cryptographic Invariant Grounding\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN
    r = p.add_run()
    r.text = "Anchor classifications in lower-level TLS handshake artifacts (cipher suites, extensions) that botnets cannot fake without prohibitive CPU cost.\n\n"
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "2. Multi-Dimensional Temporal Aggregation\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "Aggregate high-frequency request streams into contiguous 1-minute behavioral vectors capturing failure velocity, unique IP cardinality, and TLS entropy.\n\n"
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "3. Dilated Causal Sequence Modeling\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_PURPLE
    r = p.add_run()
    r.text = "Process 10-minute historical sequences using feedforward Temporal Convolutional Networks, achieving sub-millisecond inference on commodity CPUs."
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    add_speaker_notes(s4,
        "[3:30 - 4:45] Deliver the thesis statement clearly and explain the conceptual leap.\n\n"
        "This brings us to the core hypothesis of my thesis. If an attack is invisible when viewed as an isolated point in time, the solution is not to look harder at that single point. The solution is to change the dimension of analysis from space to time.\n\n"
        "Low-and-slow botnets are invisible per-IP. But when you aggregate authentication telemetry across 1-minute windows over a 10-minute sliding sequence, a glaring signature emerges: an abnormal surge in unique residential IP cardinality, elevated longitudinal failure rates, and subtle transport-layer fingerprint clustering.\n\n"
        "Our goal is not to replace the API gateway, but to infuse it with self-learning sequence intelligence that detects campaign-level coordination in real time."
    )

    # SLIDE 5: TLS Handshake Invariants
    logger.info("Building Slide 5: TLS Handshake Invariants")
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Cryptographic Ground Truth", "4:45 - 6:00",
               "Ground Truth at the Wire: Anchoring in Cryptographic TLS Invariants",
               "Why higher-layer HTTP headers lie, but transport-layer TLS handshakes tell the truth")

    # Left: L7 vs L4 text
    add_card(s5, Inches(0.8), Inches(1.8), Inches(5.0), Inches(5.1), border_color=ACCENT_CYAN)
    tb = s5.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(4.6), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "L7 HEADERS VS. TLS HANDSHAKES\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN

    r = p.add_run()
    r.text = "❌ Why Layer 7 Headers Lie:\n"
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = ACCENT_RED
    r = p.add_run()
    r.text = "• User-Agents, Accept headers, and IP headers can be forged in a single line of Python code.\n• Relying on L7 headers alone is an invitation to be deceived.\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "✅ Why TLS Handshakes Tell the Truth:\n"
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "• The TLS Client Hello negotiation specifies exact cipher suites, extension sequences, and elliptic curve ordering.\n"
    r.text += "• Modifying cryptographic client parameters at scale introduces massive CPU overhead and broken handshakes for botnets.\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "🛡️ Defeating 'Cipher Stunting':\n"
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "• Attackers randomize ciphers to evade static JA3 hashes.\n• Our model analyzes fingerprint diversity as a macro statistical signal, converting evasion into detection!"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    # Right: Image
    img_path = ASSETS_DIR / "v2_feature_distributions.png"
    if img_path.exists():
        s5.shapes.add_picture(str(img_path), Inches(6.0), Inches(1.8), width=Inches(6.5))

    add_speaker_notes(s5,
        "[4:45 - 6:00] Highlight the technical depth of TLS fingerprinting.\n\n"
        "Now, any cybersecurity researcher will tell you: machine learning is only as good as the features you feed it. If you train a model on User-Agent strings and HTTP headers, you have built a house on sand. Why? Because an attacker can spoof a User-Agent in literally one line of Python code.\n\n"
        "That is why our methodology drops down to the transport layer — the TLS Client Hello handshake. When a genuine Chrome browser connects to your server, it advertises a very specific ordered list of cipher suites, supported elliptic curves, and TLS extensions.\n\n"
        "Automated bot tools like Python Requests or Go HTTP clients have distinct, hardcoded TLS signatures. Even advanced tools like curl_cffi that attempt browser impersonation exhibit subtle structural discrepancies or introduce cipher stunting — randomizing ciphers to evade static JA3 hash blacklists.\n\n"
        "By pairing TLS invariants with behavioral telemetry, we create a feature space that is computationally expensive and operationally painful for an attacker to fake."
    )

    # SLIDE 6: End-to-End Pipeline
    logger.info("Building Slide 6: End-to-End Pipeline")
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "System Architecture", "6:00 - 7:15",
               "The End-to-End Architecture: From Wire Telemetry to Adaptive Throttling",
               "A containerized, streaming pipeline engineered for production edge environments")

    img_path = ASSETS_DIR / "horizontal_system_architecture.png"
    if img_path.exists():
        s6.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.8), width=Inches(11.733))

    add_speaker_notes(s6,
        "[6:00 - 7:15] Guide the audience step-by-step across the 5 stages.\n\n"
        "Here is our end-to-end operational blueprint. Let's trace a live request from left to right.\n\n"
        "Stage 1: Incoming requests hit the API Gateway shielding our FastAPI authentication service. Custom middleware captures both Layer 7 headers and lower-level TLS connection metadata in real time, streaming them to a PostgreSQL telemetry store.\n\n"
        "Stage 2: Feature engineering pipelines summarize streaming logs into contiguous 1-minute aggregation windows. We compute four core macro signals: longitudinal failure rate, unique IP cardinality, JA3 hash diversity, and aggregate request volume.\n\n"
        "Stage 3: The sequence engine assembles these into a sliding window of length L=10 — representing a 10-minute historical perspective.\n\n"
        "Stage 4 & 5: The TCN performs a forward pass on commodity CPU in 0.65 milliseconds. If the attack score exceeds the confidence threshold, the gateway triggers progressive throttling — penalizing the distributed bot campaign while genuine human logins pass through unhindered."
    )

    # SLIDE 7: Algorithmic Selection
    logger.info("Building Slide 7: Algorithmic Selection")
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Model Selection & Rationale", "7:15 - 8:30",
               "Algorithmic Selection: Why TCNs Outshine LSTMs & Reinforcement Learning",
               "Solving the latency, gradient stability, and training bottlenecks of sequence modeling")

    col_w = Inches(3.7)
    gap = Inches(0.3)

    # Card 1: DRL
    add_card(s7, Inches(0.8), Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_RED)
    tb = s7.shapes.add_textbox(Inches(1.0), Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "❌ Deep Reinforcement Learning\n\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_RED
    r = p.add_run()
    r.text = "• The Pitch: Agent learns adaptive throttling policies via continuous reward optimization.\n\n"
    r.text += "• Operational Flaw: Exploration policies are dangerous in production routing — can throttle VIP traffic during training.\n\n"
    r.text += "• High Overhead: Unstable convergence loops make DRL impractical for inline gateway latency budgets.\n\n"
    r.text += "• Verdict: High operational instability."
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    # Card 2: LSTM
    add_card(s7, Inches(0.8) + col_w + gap, Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_AMBER)
    tb = s7.shapes.add_textbox(Inches(1.0) + col_w + gap, Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "⚠️ Recurrent Networks (LSTM/GRU)\n\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "• The Pitch: Standard industry baseline for modeling chronological time series telemetry.\n\n"
    r.text += "• Operational Flaw: Sequential execution bottleneck: step t+1 depends strictly on hidden state of step t. No parallel training.\n\n"
    r.text += "• Gradient Degradation: Suffers from vanishing gradients across long temporal sequences.\n\n"
    r.text += "• Verdict: Slow training, limited context."
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    # Card 3: TCN
    add_card(s7, Inches(0.8) + (col_w + gap)*2, Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_GREEN)
    tb = s7.shapes.add_textbox(Inches(1.0) + (col_w + gap)*2, Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "✅ Temporal ConvNet (TCN)\n\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "• Feedforward Parallelism: Dilated causal 1D convolutions allow complete sequence evaluation in parallel.\n\n"
    r.text += "• Stable Gradients: Residual shortcut connections eliminate vanishing/exploding gradients entirely.\n\n"
    r.text += "• Benchmark Proven: Outperforms LSTMs (Bai et al. 2018); scored 96.72% on Edge-IIoTset intrusion benchmark.\n\n"
    r.text += "• Verdict: Sub-millisecond CPU speed."
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    # Bottom Banner
    add_card(s7, Inches(0.8), Inches(6.6), Inches(11.733), Inches(0.6), border_color=BORDER_COLOR)
    tb_b = s7.shapes.add_textbox(Inches(1.0), Inches(6.65), Inches(11.3), Inches(0.5))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    r = p.add_run()
    r.text = "Academic Anchor: Bai, Kolter & Koltun (2018) systematically verified that convolutional networks outperform recurrent baselines across benchmark sequence problems while offering longer memory and order-of-magnitude faster training."
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN

    add_speaker_notes(s7,
        "[7:15 - 8:30] Explain the algorithmic trade-offs clearly. Anticipate committee questions on LSTMs.\n\n"
        "Now, let's address the most important modeling question: Why Temporal Convolutional Networks? When people hear 'time series sequence modeling', the default knee-jerk reaction in cybersecurity is often: 'Why didn't you use an LSTM or Deep Reinforcement Learning?'\n\n"
        "Let's dismantle both options. Deep Reinforcement Learning sounds fancy, but in a live API Gateway, DRL exploration is catastrophic. If an agent tries an exploratory policy during a traffic shift, it might block thousands of legitimate paying users to test a hypothesis. We cannot afford that risk.\n\n"
        "Recurrent models like LSTMs and GRUs have a different Achilles' heel: sequential execution. Because step 2 requires the hidden state of step 1, you cannot parallelize training across GPU or multi-core hardware. And over long sequences, LSTMs suffer from vanishing gradients.\n\n"
        "TCNs use feedforward 1D causal convolutions. They evaluate all timesteps simultaneously during training. With residual shortcut connections and dilated filters, they capture longer historical memory than LSTMs while executing inference in a fraction of a millisecond."
    )

    # SLIDE 8: Inside the TCN Architecture
    logger.info("Building Slide 8: Inside the TCN Architecture")
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Deep Learning Mechanics", "8:30 - 9:45",
               "Inside the TCN: Dilated Causal Convolutions & Receptive Field Geometry",
               "Capturing 10-minute attack trajectories with only 28,241 parameters")

    img_path = ASSETS_DIR / "horizontal_tcn_architecture.png"
    if img_path.exists():
        s8.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.8), width=Inches(11.733))

    add_speaker_notes(s8,
        "[8:30 - 9:45] Walk through the convolutional block math and receptive field.\n\n"
        "Let's look under the hood of the neural network. How does this architecture achieve both deep temporal vision and sub-millisecond execution?\n\n"
        "The network consists of three stacked residual blocks. The core engine uses two mathematical properties:\n\n"
        "First, Causal Padding: A causal filter ensures that the prediction for minute 10 cannot peek into minute 11. It only convolves over past and present data, completely eliminating look-ahead bias.\n\n"
        "Second, Dilations: Instead of convolving over adjacent entries, each subsequent layer skips inputs by a factor of d = 1, 2, 4. This increases the receptive field exponentially.\n\n"
        "Our formula yields a total receptive field of 29 time steps. Since our input window is L=10 minutes, 29 is nearly three times larger than the sequence length. That means when the network makes a decision at minute 10, it has unobstructed, full-fidelity visibility across the entire 10-minute attack trajectory.\n\n"
        "And best of all: the entire network has only 28,241 parameters! It is smaller than a JPEG thumbnail."
    )

    # SLIDE 9: The Realistic Cyber-Range
    logger.info("Building Slide 9: The Realistic Cyber-Range")
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Experimental Methodology", "9:45 - 11:00",
               "The Realistic Cyber-Range: Simulating State-of-the-Art Evasive Botnets",
               "A containerized testbed generating over 8 million real-time authentication requests")

    # Left: Cyber-Range specs
    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.2), Inches(5.1), border_color=ACCENT_CYAN)
    tb = s9.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(4.8), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "PRODUCTION TESTBED & ADVERSARY HARNESS\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN

    r = p.add_run()
    r.text = "🎯 Target Infrastructure:\n"
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "• Containerized FastAPI authentication service.\n• Simulated API Gateway proxy capturing Layer 7 headers & TLS Client Hello metadata.\n• PostgreSQL relational telemetry store.\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "👾 Automated Botnet Harness:\n"
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = ACCENT_RED
    r = p.add_run()
    r.text = "• Rotating residential proxy pools across thousands of IPs.\n• Browser impersonation using curl_cffi and tls_client (Chrome 110 & Safari 15.3).\n• Dynamic header randomization & spoofed proxy topologies.\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "📊 Simulation Scale:\n"
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "• 15–20 req/sec across concurrent workers.\n• 5.5 hours continuous execution: 8,095,202 raw transactions!"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    # Right: Feature Correlation Matrix
    img_path = ASSETS_DIR / "v2_feature_correlation.png"
    if img_path.exists():
        s9.shapes.add_picture(str(img_path), Inches(6.2), Inches(1.8), width=Inches(6.3))

    add_speaker_notes(s9,
        "[9:45 - 11:00] Demonstrate experimental rigor and realism.\n\n"
        "To evaluate this defense rigorously, we couldn't rely on synthetic toy datasets or academic simulations from a decade ago. We built a fully containerized, dedicated cyber-range.\n\n"
        "Our target environment was a high-performance FastAPI authentication endpoint placed behind an instrumented API Gateway proxy. Then, we built an automated adversary harness programmed with the exact tactics used by modern criminal botnets.\n\n"
        "The botnet deployed specialized HTTP client libraries — curl_cffi and tls_client — capable of programmatically impersonating the exact cryptographic handshakes of modern web browsers like Chrome 110 and Safari 15.\n\n"
        "The simulation ran continuously for 5.5 hours, maintaining 15 to 20 requests per second across concurrent execution workers. In total, the pipeline ingested and analyzed 8,095,202 raw authentication requests.\n\n"
        "Notice the correlation matrix on the right: Unique IPs and Failure Rate show a strong positive correlation of 0.782 during attack phases, providing the primary macro signal for our temporal detector."
    )

    # SLIDE 10: Data Engineering & Labeling
    logger.info("Building Slide 10: Data Engineering & Labeling")
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Data Engineering & Training", "11:00 - 12:15",
               "Data Engineering: Aggregation, Labeling & Zero-Leakage Splitting",
               "Transforming 8 million packet logs into clean, balanced temporal training tensors")

    # Left: Methodology details
    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.2), Inches(5.1), border_color=ACCENT_PURPLE)
    tb = s10.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(4.8), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "DATA PIPELINE & TEMPORAL INTEGRITY\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_PURPLE

    r = p.add_run()
    r.text = "⏱️ 1-Minute Chronological Aggregation:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN
    r = p.add_run()
    r.text = "8,095,202 raw transactions &rarr; 3,187 consecutive 1-min windows. Captures failure rate, unique IPs, JA3 diversity, and volume.\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "⚖️ Dual Ground-Truth Labeling Heuristic:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "Window is Attack (1) iff failure_rate > 0.30 AND unique_ips > 5.\n"
    r.text += "Prevents human password typos from triggering spurious attack classifications!\n"
    r.text += "Balanced: 1,595 attack windows vs. 1,592 benign windows.\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "🔒 Strict 70/15/15 Chronological Split:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "Zero sequence shuffling. Eliminates look-ahead bias and data leakage completely. StandardScaler fitted exclusively on 70% train split."
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    # Right: Loss Curve
    img_path = ASSETS_DIR / "v2_training_loss_curve.png"
    if img_path.exists():
        s10.shapes.add_picture(str(img_path), Inches(6.2), Inches(1.8), width=Inches(6.3))

    add_speaker_notes(s10,
        "[11:00 - 12:15] Emphasize methodological hygiene — no data leakage!\n\n"
        "Now, how did we turn 8 million raw database logs into training data? We aggregated raw request points into 3,187 contiguous 1-minute temporal windows.\n\n"
        "To establish ground truth, we applied a strict dual-condition labeling heuristic: a window is marked as an attack if both the failure rate exceeds 30% AND the unique IP count exceeds 5. Why both? Because if an individual human mistypes their password three times, their failure rate is high, but their unique IP count is 1. That is NOT an attack. Requiring both conditions prevents false alarms on human typos.\n\n"
        "This produced 1,595 attack windows and 1,592 benign windows — an exceptionally balanced dataset.\n\n"
        "In machine learning research, the most common sin is random shuffling of time-series data. If you shuffle, future information leaks into the past. We enforced a strict 70/15/15 chronological split. Our StandardScaler normalization was fitted strictly on the first 70% of the timeline.\n\n"
        "As you can see in the loss curve, training converged smoothly over 30 epochs, reaching a validation loss approaching zero at epoch 27."
    )

    # SLIDE 11: The Overfitting Trap
    logger.info("Building Slide 11: The Overfitting Trap")
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "Crucial Research Insight", "12:15 - 13:30",
               "The Overfitting Trap: How Constrained Training Led to a 74% Recall Collapse",
               "A dramatic cautionary tale: Why small-data deep learning fails catastrophically in cybersecurity")

    # Left: Comparison image
    img_path = ASSETS_DIR / "v2_old_vs_new_comparison.png"
    if img_path.exists():
        s11.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.8), width=Inches(6.5))

    # Right: Narrative breakdown
    add_card(s11, Inches(7.5), Inches(1.8), Inches(5.033), Inches(5.1), border_color=ACCENT_RED)
    tb = s11.shapes.add_textbox(Inches(7.7), Inches(2.0), Inches(4.6), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "THE DANGEROUS ILLUSION OF LAB TESTING\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_RED

    r = p.add_run()
    r.text = "🧪 Small-Data Illusion (Old Model, 335 Windows):\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "• Tested on a short 154-min sequence: 1.0000 Precision and 0.7500 Recall.\n• Looked like a complete triumph in the lab!\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "💥 The Catastrophic Collapse:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_RED
    r = p.add_run()
    r.text = "• Evaluated against 13,351 sequences (33.7M requests, 233 hours):\n"
    r.text += "• Detection Recall collapsed from 100% to 25.75%!\n"
    r.text += "• Missed 1,479 attack windows (74.25% of attacks slipped through)!\n"
    r.text += "• ROC-AUC dropped to 0.3576 (worse than random guessing)!\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "🏆 The Scaled V2 Remedy (8M+ Requests):\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "• Scaling to 3,187 windows completely cured the collapse: Recall surged to 1.0000 with a perfect 1.0000 ROC-AUC!"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = TEXT_MAIN

    add_speaker_notes(s11,
        "[12:15 - 13:30] This is the dramatic peak of the presentation. Tell this as a story!\n\n"
        "Now, I want to share the most profound empirical discovery of this research — and frankly, a humbling cautionary tale for anyone applying deep learning to cybersecurity.\n\n"
        "In our initial iteration, we trained our TCN on an abbreviated dataset of 335 windows. In laboratory testing on a short 154-minute run, the model looked phenomenal! It had 100% precision and zero false positives. We were celebrating.\n\n"
        "Then, we deployed that model against a sustained 233-hour blind test with 33.7 million requests. And the model suffered a catastrophic collapse. Its detection recall plummeted to 25.75%! It missed 74 out of every 100 attacks! Its ROC-AUC dropped to 0.3576 — literally worse than flipping a coin.\n\n"
        "Why did this happen? Because with limited training data, the convolutional filters memorized localized quirks rather than invariant temporal dynamics.\n\n"
        "When we expanded training to the full 8-million-request corpus (3,187 windows), look at the green bar on the right: detection recall surged to a flawless 1.0000 across all 2,000 attack windows! Training volume and distributional diversity are everything."
    )

    # SLIDE 12: Chaotic Burst Blind Test
    logger.info("Building Slide 12: Chaotic Burst Blind Test")
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Blind Evaluation Suite 1", "13:30 - 14:45",
               "Stress-Testing Resilience: Surviving the 154-Minute Chaotic Blind Test",
               "Challenging the TCN against abrupt operational shifts, sudden quiet phases, and attack spikes")

    img_path = ASSETS_DIR / "v2_chaotic_traffic_timeseries.png"
    if img_path.exists():
        s12.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.8), width=Inches(6.8))

    add_card(s12, Inches(7.8), Inches(1.8), Inches(4.733), Inches(5.1), border_color=ACCENT_AMBER)
    tb = s12.shapes.add_textbox(Inches(8.0), Inches(2.0), Inches(4.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "THE CHAOTIC STRESS BENCHMARK\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER

    r = p.add_run()
    r.text = "🌪️ 3 Unpredictable Traffic Regimes:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = TEXT_MAIN
    r = p.add_run()
    r.text = "1. Phase 1 (28 min): Heavy, sustained credential assault.\n"
    r.text += "2. Phase 2 (85 min): Sudden, peaceful benign baseline recovery.\n"
    r.text += "3. Phase 3 (41 min): Intermittent, unpredictable attack bursts.\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MUTED

    r = p.add_run()
    r.text = "📊 Verified Scores (@ 50% Threshold):\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "• Overall Accuracy: 0.9034\n"
    r.text += "• Detection Recall: 0.7727 (34/44 attacks detected)\n"
    r.text += "• Precision: 0.8947\n"
    r.text += "• F1-Score: 0.8293\n"
    r.text += "• Empirical ROC-AUC: 0.9876\n"
    r.text += "• False Positive Rate: 0.0396 (4 false alarms)\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "Key Takeaway: The TCN recovered to baseline within 2 minutes of the attack stopping, proving zero policy hysteresis."
    r.font.size = Pt(9.5)
    r.font.italic = True
    r.font.color.rgb = ACCENT_CYAN

    add_speaker_notes(s12,
        "[13:30 - 14:45] Walk through the chaotic traffic timeseries.\n\n"
        "In production, attacks don't happen on a neat, predictable schedule. Threat actors start, stop, pause for an hour, and strike again in bursts.\n\n"
        "To stress-test our model, we generated an out-of-sample 'Chaotic' blind dataset spanning 154 minutes. Look at the top graph: we hit the gateway with a 28-minute attack, followed by an 85-minute completely quiet benign recovery phase, and then sporadic, localized attack spikes.\n\n"
        "Even under these erratic shifts, the TCN recorded an ROC-AUC of 0.9876 and a PR-AUC of 0.9711. It correctly identified 34 out of 44 attack sequences while maintaining a false alarm rate below 4%.\n\n"
        "Most importantly, the model rapidly transitioned back to benign baseline within 2 minutes of the attack stopping — proving it does not suffer from lingering hysteresis or policy lag."
    )

    # SLIDE 13: Sustained Enterprise Scale
    logger.info("Building Slide 13: Sustained Enterprise Scale")
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)
    add_header(s13, "Blind Evaluation Suite 2", "14:45 - 16:00",
               "Enterprise Scale: Sustained 233-Hour Validation Across 33.7M Requests",
               "Demonstrating near-perfect discriminative capability under realistic 15:85 class imbalance")

    img_path = ASSETS_DIR / "v2_performance_across_datasets.png"
    if img_path.exists():
        s13.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.8), width=Inches(6.8))

    add_card(s13, Inches(7.8), Inches(1.8), Inches(4.733), Inches(5.1), border_color=ACCENT_GREEN)
    tb = s13.shapes.add_textbox(Inches(8.0), Inches(2.0), Inches(4.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "ENTERPRISE SUSTAINED BENCHMARK\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    r = p.add_run()
    r.text = "🏢 Massive Enterprise Test Corpus:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = TEXT_MAIN
    r = p.add_run()
    r.text = "• 33,731,232 raw API transactions.\n• 13,360 contiguous 1-min windows (233 continuous hours &asymp; 10 days).\n• Realistic 15:85 attack-to-benign imbalance (2,000 attack vs. 11,360 benign).\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MUTED

    r = p.add_run()
    r.text = "🏆 Verified Results (@ 50% Threshold):\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN
    r = p.add_run()
    r.text = "• Recall (Detection Rate): 1.0000 (Zero missed attacks! 2,000/2,000 intercepted)\n"
    r.text += "• Precision: 0.9945\n"
    r.text += "• F1-Score: 0.9972\n"
    r.text += "• Overall Accuracy: 0.9992 (13,340 / 13,351)\n"
    r.text += "• Empirical ROC-AUC: 1.0000\n"
    r.text += "• PR-AUC: 0.9999\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "Conclusion: Proves conclusively that dilated causal convolutions achieve drift-free stability across hundreds of operational hours."
    r.font.size = Pt(9.5)
    r.font.italic = True
    r.font.color.rgb = ACCENT_GREEN

    add_speaker_notes(s13,
        "[14:45 - 16:00] Present the crowning empirical validation of the thesis.\n\n"
        "Now we arrive at our largest evaluation: the Large/SH Sustained dataset. To prove this model can survive in enterprise production, we subjected it to 10 continuous days of traffic — 13,360 minutes and over 33.7 million requests.\n\n"
        "In this dataset, the class distribution is realistically skewed: 85% of the time traffic is completely benign, and attacks occur in 15% of windows.\n\n"
        "Look at the numbers on this slide. At the nominal 50% threshold, our TCN achieved a perfect Recall of 1.0000. It intercepted every single one of the 2,000 attack sequences. Not one slipped through! And it achieved 0.9945 precision with a 0.9992 overall accuracy.\n\n"
        "This proves that dilated causal convolutions, when trained on sufficiently diverse data, do not drift or degrade over hundreds of hours of continuous operations."
    )

    # SLIDE 14: Precision Engineering & Threshold Tuning
    logger.info("Building Slide 14: Precision Engineering")
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14)
    add_header(s14, "Operational Tuning", "16:00 - 17:15",
               "Precision Engineering: Threshold Tuning & Zero-Alarm Operations",
               "Calibrating decision boundaries to eliminate false alarms in high-volume production")

    img_path = ASSETS_DIR / "v2_confusion_matrices.png"
    if img_path.exists():
        s14.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.8), width=Inches(6.8))

    add_card(s14, Inches(7.8), Inches(1.8), Inches(4.733), Inches(5.1), border_color=ACCENT_PURPLE)
    tb = s14.shapes.add_textbox(Inches(8.0), Inches(2.0), Inches(4.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "DECISION BOUNDARY CALIBRATION\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_PURPLE

    r = p.add_run()
    r.text = "🎯 The Production Dilemma:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = TEXT_MAIN
    r = p.add_run()
    r.text = "• False alarms lock out legitimate users and flood SOC teams with bogus alerts.\n• We calibrated the decision threshold from 50% to 90%.\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MUTED

    r = p.add_run()
    r.text = "✨ Impact at 90% Confidence Threshold:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "• Large Dataset Precision: Rises to 0.9975!\n"
    r.text += "• Detection Recall: Holds firm at 1.0000!\n"
    r.text += "• False Alarm Rate (FPR): Drops to 0.0004!\n"
    r.text += "• Only 4 false alarms across 11,360 benign windows (10 days of traffic)!\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "Dynamic Mitigation: Even on those 4 false alarms, triggering a CAPTCHA challenge solves user friction completely without account lockout."
    r.font.size = Pt(9.5)
    r.font.italic = True
    r.font.color.rgb = ACCENT_CYAN

    add_speaker_notes(s14,
        "[16:00 - 17:15] Address the practical operational reality of false positives.\n\n"
        "Every DevOps engineer and CISO will ask the same question: 'What happens when your model gets it wrong? Are you going to block our VIP customers?'\n\n"
        "In cybersecurity, precision is king. If an algorithm generates 50 false alarms an hour, the security team turns it off. So we investigated decision boundary calibration.\n\n"
        "By shifting the decision threshold from 50% to a conservative 90% confidence boundary, our model on the large enterprise dataset increased precision to 99.75%, while recall stayed pinned at a perfect 1.0000. The false alarm rate dropped to 0.04% — that is only 4 false alarms across 11,360 minutes of benign traffic.\n\n"
        "And because our mitigation policy is dynamic — triggering a CAPTCHA challenge rather than a permanent account ban — those four edge cases experience a 3-second puzzle rather than an account lockout."
    )

    # SLIDE 15: Production Feasibility & Latency
    logger.info("Building Slide 15: Production Feasibility")
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15)
    add_header(s15, "Production Feasibility", "17:15 - 18:15",
               "Production Breakthrough: 0.65ms Inline CPU Inference (No GPUs Needed)",
               "Inserting deep learning inline without violating strict API Gateway SLA latency budgets")

    img_path = ASSETS_DIR / "v2_latency_profile.png"
    if img_path.exists():
        s15.shapes.add_picture(str(img_path), Inches(0.8), Inches(1.8), width=Inches(6.8))

    add_card(s15, Inches(7.8), Inches(1.8), Inches(4.733), Inches(5.1), border_color=ACCENT_CYAN)
    tb = s15.shapes.add_textbox(Inches(8.0), Inches(2.0), Inches(4.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "CPU INFERENCE BENCHMARK (N=500 WARM PASSES)\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN

    r = p.add_run()
    r.text = "⚡ Measured Latency Profile:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = TEXT_MAIN
    r = p.add_run()
    r.text = "• Average Latency: 0.65 ms\n"
    r.text += "• Median (P50): 0.62 ms\n"
    r.text += "• 95th Percentile (P95): 0.81 ms\n"
    r.text += "• 99th Percentile Tail (P99): 1.64 ms (Passed < 2ms SLA!)\n"
    r.text += "• Min / Max: 0.52 ms / 2.50 ms\n\n"
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "💰 Economic & Production Reality:\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "• Zero GPU Clusters Required: Runs directly on general-purpose server CPUs hosting the gateway proxy.\n"
    r.text += "• < 1% Transaction Impact: Authentication SLAs permit 100–500 ms budgets; 0.65 ms consumes less than 1%.\n"
    r.text += "• Ready for production edge deployment today."
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_MAIN

    add_speaker_notes(s15,
        "[17:15 - 18:15] Address the elephant in the room: latency and hardware cost.\n\n"
        "Now let's tackle the elephant in the room: Can you actually put a deep neural network directly in the synchronous routing path of an API Gateway without causing a traffic jam?\n\n"
        "The answer is an unequivocal YES. Look at our empirical latency benchmark on the left. Over 500 warm-cache execution passes on commodity server CPUs, our compiled PyTorch TCN achieved an average single-call inference latency of 0.65 milliseconds!\n\n"
        "Our P95 was 0.81 milliseconds, and our P99 tail latency was 1.64 ms — well under the 2-millisecond edge SLA. In a production login endpoint where SLA budgets are typically 200 to 500 milliseconds, our model consumes less than 1% of the permissible transaction time.\n\n"
        "And best of all: you don't need a $30,000 edge GPU cluster. This runs directly on the general-purpose CPU instances already hosting your API gateways. It is lightweight, practical, and immediately deployable."
    )

    # SLIDE 16: Operational Hardening
    logger.info("Building Slide 16: Operational Hardening")
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16)
    add_header(s16, "DevOps & Production Hardening", "18:15 - 19:15",
               "Operational Hardening: Residential Proxies, Drift & Continuous Retraining",
               "Building an adaptive lifecycle to counter evolving zero-day evasion tactics")

    col_w = Inches(3.7)
    gap = Inches(0.3)

    add_card(s16, Inches(0.8), Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_CYAN)
    tb = s16.shapes.add_textbox(Inches(1.0), Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "🛡️ Residential Proxy Resilience\n\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN
    r = p.add_run()
    r.text = "• IP Agnostic: Does not rely on brittle IP reputation blocklists.\n\n"
    r.text += "• Invariant Grounding: Tracks cross-IP campaign coordination and transport-layer TLS cipher invariants.\n\n"
    r.text += "• Neutralizes Cycling: Makes residential proxy rotation ineffective because the underlying machine signature remains exposed."
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    add_card(s16, Inches(0.8) + col_w + gap, Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_AMBER)
    tb = s16.shapes.add_textbox(Inches(1.0) + col_w + gap, Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "📉 Data Drift Management\n\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "• Telemetry Tracking: Continuously monitors model logit distributions over sliding 24-hour windows.\n\n"
    r.text += "• Early Warning: Statistically significant shifts in prediction confidence trigger SOC triage alerts.\n\n"
    r.text += "• Prevents Silently Aging Models: Counters emerging bot clients and seasonal human traffic shifts."
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    add_card(s16, Inches(0.8) + (col_w + gap)*2, Inches(1.8), col_w, Inches(4.6), border_color=ACCENT_GREEN)
    tb = s16.shapes.add_textbox(Inches(1.0) + (col_w + gap)*2, Inches(2.0), col_w - Inches(0.4), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "🔄 Automated Retraining Pipeline\n\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "• Continuous Data Buffer: PostgreSQL pipelines log verified authentication telemetry into weekly splits.\n\n"
    r.text += "• Background Fine-Tuning: Automated jobs re-tune the 28,241 parameters using pos_weight balancing.\n\n"
    r.text += "• Shadow Canary Deployment: New model checkpoints are evaluated on mirrored production traffic before promotion."
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MAIN

    add_card(s16, Inches(0.8), Inches(6.6), Inches(11.733), Inches(0.6), border_color=BORDER_COLOR)
    tb_b = s16.shapes.add_textbox(Inches(1.0), Inches(6.65), Inches(11.3), Inches(0.5))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    r = p.add_run()
    r.text = "Adversarial Robustness: Anchoring in lower-level TLS handshake mechanics insulates the network from Explainable AI (XAI) feature perturbation attacks."
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = ACCENT_PURPLE

    add_speaker_notes(s16,
        "[18:15 - 19:15] Discuss how the system survives long-term in the real world.\n\n"
        "A machine learning model is not a statue that you sculpt once and leave in a museum. In cybersecurity, adversaries adapt. How does our architecture handle the messy real world?\n\n"
        "First, residential proxy cycling. We don't care if an IP changes every 60 seconds. Our model doesn't look at IP identities — it looks at macro-temporal coordination and TLS handshake integrity across the entire pool.\n\n"
        "Second, concept drift. As botnets adopt new TLS client libraries or alter their submission schedules, we maintain an automated monitoring pipeline that tracks inference confidence distributions. If drift is detected, an automated retraining pipeline re-tunes the 28,000 weights on fresh gateway telemetry and verifies the checkpoint on shadow canary traffic before promoting it to production."
    )

    # SLIDE 17: Conclusion
    logger.info("Building Slide 17: Conclusion")
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17)
    add_header(s17, "Conclusions & Strategic Impact", "19:15 - 20:00",
               "Conclusion: The Future of API Perimeter Defense",
               "Three definitive findings from this Master's research")

    col_w = Inches(3.7)
    gap = Inches(0.3)

    add_card(s17, Inches(0.8), Inches(1.8), col_w, Inches(3.6), border_color=ACCENT_CYAN)
    tb = s17.shapes.add_textbox(Inches(1.0), Inches(2.0), col_w - Inches(0.4), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "1. Temporal Defense Wins\n\n"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = ACCENT_CYAN
    r = p.add_run()
    r.text = "Static rate limiting is mathematically broken against distributed residential botnets. Aggregating multi-dimensional telemetry into sliding causal temporal sequences unmasks low-and-slow campaigns with 1.0000 recall."
    r.font.size = Pt(11)
    r.font.color.rgb = TEXT_MAIN

    add_card(s17, Inches(0.8) + col_w + gap, Inches(1.8), col_w, Inches(3.6), border_color=ACCENT_PURPLE)
    tb = s17.shapes.add_textbox(Inches(1.0) + col_w + gap, Inches(2.0), col_w - Inches(0.4), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "2. Training Scale Matters\n\n"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = ACCENT_PURPLE
    r = p.add_run()
    r.text = "Small-data deep learning creates a dangerous illusion of security (74% recall collapse). Scaling training to 8M+ requests (3,187 windows) unlocked rock-solid, drift-free enterprise generalization across 233 hours."
    r.font.size = Pt(11)
    r.font.color.rgb = TEXT_MAIN

    add_card(s17, Inches(0.8) + (col_w + gap)*2, Inches(1.8), col_w, Inches(3.6), border_color=ACCENT_GREEN)
    tb = s17.shapes.add_textbox(Inches(1.0) + (col_w + gap)*2, Inches(2.0), col_w - Inches(0.4), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "3. Inline CPU Viability\n\n"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN
    r = p.add_run()
    r.text = "With an average latency of 0.65 ms and 28,241 parameters, Temporal Convolutional Networks can be deployed directly into production edge proxies today on commodity CPUs — zero expensive GPU clusters required."
    r.font.size = Pt(11)
    r.font.color.rgb = TEXT_MAIN

    # Bottom Stat Scorecard
    add_stat_card(s17, Inches(0.8), Inches(5.6), Inches(2.6), Inches(1.5), "1.0000", "Detection Recall", "Zero missed attacks", ACCENT_GREEN)
    add_stat_card(s17, Inches(3.8), Inches(5.6), Inches(2.6), Inches(1.5), "0.65 ms", "Avg CPU Latency", "P99 tail = 1.64 ms", ACCENT_CYAN)
    add_stat_card(s17, Inches(6.8), Inches(5.6), Inches(2.6), Inches(1.5), "28,241", "Total Weights", "Ultra-compact footprint", ACCENT_PURPLE)
    add_stat_card(s17, Inches(9.8), Inches(5.6), Inches(2.733), Inches(1.5), "0.04%", "False Alarm Rate", "@ 90% threshold tuning", ACCENT_AMBER)

    add_speaker_notes(s17,
        "[19:15 - 20:00] Deliver the conclusion with authority and vision.\n\n"
        "To conclude: We set out to answer a critical question: Can we protect API login endpoints against distributed, low-and-slow botnets without adding disruptive user friction or relying on brittle static thresholds?\n\n"
        "Our research proves three definitive conclusions:\n\n"
        "First: Static rate limiting is mathematically obsolete against distributed residential botnets. Shifting defense to temporal convolutional modeling restores complete visibility.\n\n"
        "Second: Data scale is decisive. Our 74% recall collapse proved that small-data ML is dangerous in security, while large-scale training achieved flawless generalization.\n\n"
        "Third: Deep learning does not have to be slow or expensive. At 0.65 milliseconds on standard CPUs, this defense is ready for production edge integration today.\n\n"
        "By anchoring in cryptographic invariants and modeling the temporal dynamics of incoming traffic, we can turn the tables on automated botnets — keeping our digital identity perimeters safe."
    )

    # SLIDE 18: Q&A
    logger.info("Building Slide 18: Q&A")
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18)
    add_header(s18, "Defense & Academic Discussion", "20:00+ (Q&A)",
               "Self-Learning Systems",
               "Securing API login endpoints against “low and slow” botnet credential stuffing using self-learning systems")

    # Left: Presenter & Repo
    add_card(s18, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1), border_color=ACCENT_CYAN)
    tb = s18.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "Adrian Chia\n"
    r.font.size = Pt(22)
    r.font.bold = True
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "Master's Research Candidate\n\n"
    r.font.size = Pt(13)
    r.font.color.rgb = ACCENT_CYAN

    r = p.add_run()
    r.text = "Research Artifacts & Codebase:\n"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "• Thesis Repository: adrian-chia/adpfw\n"
    r.text += "• Trained Weights: best_tcn_model_v2.pt (28,241 params)\n"
    r.text += "• Verified Telemetry: verified_results_latest.json\n"
    r.text += "• Thesis Document: Project_Work_Template_AC.md\n\n"
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_MUTED

    r = p.add_run()
    r.text = "Ready for Committee Inquiries & Theoretical Defense."
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

    # Right: Prepared Defense Q&A
    add_card(s18, Inches(6.8), Inches(1.8), Inches(5.733), Inches(5.1), border_color=ACCENT_PURPLE)
    tb = s18.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "PREPARED DEFENSE COMMITTEE INQUIRIES\n\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_PURPLE

    r = p.add_run()
    r.text = "1. 'Why not rely on commercial Cloudflare/Akamai bot managers?'\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "Commercial WAFs rely on client-side JS challenges (invisible to pure mobile/headless APIs) and black-box IP reputation with high subscription costs. Our TCN operates server-side directly on raw TLS telemetry.\n\n"
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "2. 'What if the botnet slows down to 1 request per hour?'\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "Slowing to 1 req/hour renders credential verification economically non-viable for adversaries, who must validate millions of stolen credentials before passwords are reset.\n\n"
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_MAIN

    r = p.add_run()
    r.text = "3. 'How does TLS 1.3 Encrypted Client Hello (ECH) impact this?'\n"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER
    r = p.add_run()
    r.text = "The API Gateway is the termination point of the TLS session; it decrypts and inspects the inner Client Hello with full visibility."
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_MAIN

    add_speaker_notes(s18,
        "[20:00+] Open the floor for questions from the committee.\n\n"
        "Thank you very much for your time and attention. This concludes my presentation on \"Self-learning systems - Securing API login endpoints against 'low and slow' botnet credential stuffing using self-learning systems.\" I now welcome your questions, feedback, and academic discussion.\n\n"
        "If you'd like to dive into specific confusion matrices, hyperparameter tuning curves, or code implementations, I have all verified telemetry and code artifacts available immediately."
    )

    prs.save(str(OUTPUT_PPTX))
    logger.info(f"Successfully generated PowerPoint presentation at {OUTPUT_PPTX}")

if __name__ == "__main__":
    build_presentation()
