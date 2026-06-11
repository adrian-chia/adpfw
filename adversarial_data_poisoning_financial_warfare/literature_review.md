# Comprehensive Literature Review
<!-- FINAL VERSION — exhaustively compiled via /goal multi-database sweep -->
## Adversarial Data Poisoning & Financial Warfare

> **Thesis:** Master's in Computer Science  
> **Compiled via:** Multi-database sweep (arXiv, IEEE Xplore, ACM DL, SSRN, NeurIPS, ECML PKDD, IJCAI, DiVA, ProQuest, regulatory archives)  
> **Date:** June 2026 | **Papers catalogued:** 40+

---

## How to Use This Document

Each entry contains: **arXiv ID or DOI / link**, verified **authors**, **venue & year**, and a **methodology & findings summary**. Entries are tiered:
- ⭐⭐⭐ = **Critical** — must cite in thesis
- ⭐⭐ = **Important** — should review; cite if relevant
- ⭐ = **Contextual** — useful background

---

## PART I — Foundational & Methodological Background

### F.1 ⭐⭐⭐ — The Canonical Attack Taxonomy
**Title:** Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations  
**Author:** National Institute of Standards and Technology (NIST)  
**Reference:** NIST AI 100-2 (2023 draft; 2025 update)  
**Link:** https://airc.nist.gov/Publications  

**Summary:**  
The definitive reference taxonomy for all adversarial ML research. Classifies attacks across five dimensions: (1) AI system type — predictive vs. generative, (2) lifecycle stage — training vs. inference, (3) attacker goal — integrity/availability/privacy, (4) attacker capability, and (5) attacker knowledge — white/grey/black-box. Specific attack categories covered: evasion attacks (adversarial examples), poisoning attacks (data and model), privacy attacks (membership inference, model extraction), and GenAI-specific attacks (prompt injection, supply-chain). **Every thesis in this space must anchor its threat model to this taxonomy.** The 2025 update expands coverage of LLM-specific threats, directly relevant to LLM-augmented trading systems.

---

### F.2 ⭐⭐⭐ — The Canonical Time-Series ML Baseline
**Title:** DeepLOB: Deep Convolutional Neural Networks for Limit Order Books  
**Authors:** Zihao Zhang, Stefan Zohren, Stephen Roberts *(University of Oxford)*  
**Venue:** IEEE Transactions on Signal Processing, 2019  
**arXiv:** https://arxiv.org/abs/1808.03668  

**Summary:**  
Introduces the DeepLOB architecture — dilated CNN + LSTM — for mid-price prediction from 10-level limit order book data. Trained on the FI-2010 benchmark dataset (the standard for LOB research). Achieves state-of-the-art accuracy and demonstrates universal feature extraction that transfers across unseen instruments. **This is the primary attack target in all subsequent adversarial LOB papers (including Paper 1.7 and Area 3 papers).** Any thesis evaluating adversarial attacks on LOB data must evaluate against DeepLOB.

---

### F.3 ⭐⭐ — Adversarial Attacks on Time Series Classification (Foundational)
**Title:** Adversarial Attacks on Deep Neural Networks for Time Series Classification  
**Authors:** Hassan Ismail Fawaz, Germain Forestier, Jonathan Weber, Lhassane Idoumghar, Pierre-Alain Muller  
**Venue:** International Joint Conference on Neural Networks (IJCNN), 2019  
**Link:** https://ieeexplore.ieee.org/document/8852247  

**Summary:**  
Foundational paper adapting image-domain adversarial perturbation methods (FGSM, PGD) to 1D time-series classification. Demonstrates that CNNs and ResNets trained on UCR time-series datasets are highly vulnerable to small gradient-based perturbations. Proposes adversarial training as the primary mitigation. Directly applicable to financial time-series attack methodology. Most subsequent financial adversarial papers cite this work as the methodological baseline.

---

### F.4 ⭐⭐ — Adversarial Attacks on Time Series (IEEE TPAMI, 2021)
**Title:** Adversarial Attacks on Time Series  
**Authors:** Fazle Karim, Somshubra Majumdar, Houshang Darabi  
**Venue:** IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), Vol. 43, No. 10, 2021  
**Link:** https://ieeexplore.ieee.org/document/9008005  

**Summary:**  
Uses an Adversarial Transformation Network (ATN) trained on a distilled model to generate adversarial examples for time-series classifiers (1-NN DTW, FCN, ResNet). Adapts the image-domain blackbox distillation approach to sequential data. Key result: adversarial examples transfer across time-series architectures, establishing that financial time-series models face transferable adversarial threats even without white-box access to the target model.

---

### F.5 ⭐⭐ — AI Systemic Risk in Finance (Economic Theory)
**Title:** Artificial Intelligence and Systemic Risk  
**Authors:** Jón Danielsson, Robert Macrae, Andreas Uthemann *(London School of Economics)*  
**Venue:** Journal of Banking & Finance, Vol. 140, Article 106290, July 2022  
**Link:** https://doi.org/10.1016/j.jbankfin.2022.106290  

**Summary:**  
Formal economic analysis arguing that AI adoption creates four systemic risk drivers: procyclicality (AI models amplify market cycles), unknown-unknowns (model failures in out-of-distribution regimes), need-for-trust (opacity reducing counterparty confidence), and optimization-against-the-system (individual AI objectives conflicting with systemic stability). Demonstrates that adversarial micro-perturbations in AI trading signals can amplify into macro market shocks when correlated AI agents respond simultaneously. **Provides the economic-theoretical foundation for why adversarial attacks on trading AI constitute financial warfare.** Essential for thesis introduction.

---

---

## PART II — Area 1: Adversarial ML Attacks on Algorithmic & High-Frequency Trading

### 1.1 ⭐⭐⭐ — Foundational HFT Adversarial Attack Paper
**Title:** Adversarial Attacks on Machine Learning Systems for High-Frequency Trading  
**Authors:** Micah Goldblum, et al. *(Multiple US institutions)*  
**Venue:** ACM Conference on AI in Finance (ICAIF), 2021 | arXiv:2002.09565 (2020 preprint)  
**Link:** https://arxiv.org/abs/2002.09565  

**Summary:**  
The seminal paper in adversarial attacks on HFT. Introduces domain-specific adversarial attacks with **financial size constraints** — unlike image attacks (L∞ norm), these attacks are bounded by plausible price movements and position limits that a real trader faces. Key contributions: (1) adaptation of FGSM/PGD to the financial constraint set; (2) evaluation against LSTM and CNN valuation models; (3) demonstration that an adversarial trader can fool automated systems into inaccurate predictions through feasible market interactions; (4) proposal to use these attacks as robustness analysis tools. This paper defines the threat model that all subsequent work in the field builds upon.

---

### 1.2 ⭐⭐⭐ — Universal Adversarial Perturbations Against Trading Algorithms
**Title:** Taking Over the Stock Market: Adversarial Perturbations Against Algorithmic Traders  
**Authors:** Elior Nehemya, Yael Mathov, Asaf Shabtai, Yuval Elovici *(Ben-Gurion University of the Negev)*  
**Venue:** ECML PKDD 2021 | arXiv:2010.09246 (2020 preprint)  
**Link:** https://arxiv.org/abs/2010.09246  

**Summary:**  
Demonstrates that **universal adversarial perturbations (UAPs)** — noise vectors computed once and applied to any future market state — can fool algorithmic traders. Unlike instance-specific attacks, UAPs do not require re-computation per input, making them deployable in real-time HFT environments. Evaluated on real-world market data streams against three trading algorithm types in both white-box and black-box settings. Key finding: the same universal perturbation successfully fools models at *future unseen data points*, establishing that time-agnostic attacks are viable. Proposes mitigation methods and discusses their limitations in HFT contexts. This paper directly motivates the "universal adversarial perturbation" concept referenced in your thesis topic.

---

### 1.3 ⭐⭐⭐ — Ephemeral Perturbations: System-Level End-to-End Evaluation
**Title:** The Ephemeral Threat: Assessing the Security of Algorithmic Trading Systems Powered by Deep Learning  
**Authors:** Advije Rizvani, Giovanni Apruzzese, Pavel Laskov *(University of Liechtenstein)*  
**Venue:** ACM CODASPY 2025 | arXiv:2505.10430  
**Link:** https://arxiv.org/abs/2505.10430  

**Summary:**  
Introduces the concept of **ephemeral perturbations (EP)** — transient, statistically undetectable input modifications applied to stock-price data streams. The critical and counterintuitive finding: EPs have negligible effect on raw numerical predictions of the underlying LSTM model, yet they measurably induce the broader **Algorithmic Trading System (ATS)** to make suboptimal buy/sell decisions, resulting in significantly lower cumulative financial returns. This demonstrates that adversarial robustness must be evaluated at the **system level** — not just model prediction accuracy — and that the gap between model-level and system-level impact is an underappreciated research blind spot. Directly relevant to designing realistic evaluations for thesis experiments.

---

### 1.4 ⭐⭐⭐ — DRL Trading Agent Attacks
**Title:** Adversarial Attacks on Deep Algorithmic Trading Policies  
**Authors:** Yaser Faghan, Nancirose Pierson, Vahid Behzadan, Ali Fathi  
**Venue:** arXiv:2010.11388 (2020)  
**Link:** https://arxiv.org/abs/2010.11388  

**Summary:**  
First systematic adversarial study targeting **Deep Reinforcement Learning (DRL) trading agents** specifically. Develops a formal threat model for DRL trading policies and proposes two test-time attacks: (1) white-box gradient-based policy perturbation; (2) transferable black-box attack. Both attacks are evaluated against real-world DQN-based trading agents (Bitcoin and stock trading). Demonstrates that DRL policy manipulation is achievable with minimal adversary knowledge. Key insight: the DRL *policy layer* is an independent and under-studied attack surface compared to the underlying prediction models studied in 1.1 and 1.2.

---

### 1.5 ⭐⭐ — Adversarial News Manipulation in LLM-Driven Trading
**Title:** Adversarial News and Lost Profits: Manipulating Headlines in LLM-Driven Algorithmic Trading  
**Authors:** Advije Rizvani, Giovanni Apruzzese, Pavel Laskov  
**Venue:** IEEE SaTML 2026 | arXiv:2601.07722  
**Link:** https://arxiv.org/abs/2601.07722  

**Summary:**  
Extends adversarial trading attacks to **LLM-augmented trading systems** that incorporate news sentiment. Adversarial headlines use human-imperceptible textual modifications — Unicode homoglyph substitutions, hidden-text clauses — to cause LLM-based trading agents to misprice equities. Quantifies monetary risk per adversarial news insertion. Establishes an LLM-specific threat model for trading pipelines. Highly relevant given increasing deployment of LLM-based sentiment analysis in systematic trading desks.

---

### 1.6 ⭐⭐ — Stock Market Crash via Self-Fulfilling Adversarial Forecasts
**Title:** The Black Tuesday Attack: How to Crash the Stock Market with Adversarial Examples to Financial Forecasting Models  
**Authors:** (Multiple; see arXiv page)  
**Venue:** arXiv:2510.18990 (October 2025)  
**Link:** https://arxiv.org/abs/2510.18990  

**Summary:**  
Investigates whether small coordinated manipulations of individual stock values can trigger a market crash via adversarial examples — causing financial forecasting models to predict a crash, which then becomes self-fulfilling as automated systems sell off. Argues this threat is "vastly underappreciated." The attack is difficult to detect because the model's predictions would be accurate (the crash does occur) and the individual interventions are minor. Discusses systemic risk dimensions: attacks can be targeted at whole economies or individual companies' valuations.

---

### 1.7 ⭐⭐ — Slope-Based Adversarial Attacks on Financial Time-Series Forecasting
**Title:** Targeted Manipulation: Slope-Based Attacks on Financial Time-Series Data  
**Authors:** (See arXiv page)  
**Venue:** arXiv:2511.19330 (November 2025)  
**Link:** https://arxiv.org/abs/2511.19330  

**Summary:**  
Introduces two novel slope-based adversarial attack methods against N-HiTS time-series forecasting models: the **General Slope Attack** and **Least-Squares Slope Attack**. These attacks manipulate the predicted trend by doubling the slope compared to correct N-HiTS predictions. Key findings: (1) attacks bypass CNN-based discriminators, reducing specificity to 28% and accuracy to 57%; (2) slope attacks are incorporated into a GAN to generate realistic synthetic data while fooling the model; (3) proposes a sample malware that injects adversarial attacks directly into the ML model's inference library — demonstrating that security must extend to the entire ML deployment pipeline.

---

### 1.8 ⭐⭐ — Adversarial-Robust DRL for Crypto HFT with Explainable AI
**Title:** Adversarial-Robust Deep Reinforcement Learning for High-Frequency Cryptocurrency Trading with Explainable AI Framework  
**Authors:** Joy Sinha et al.  
**Venue:** November 2025 (ResearchGate preprint)  
**Link:** Search ResearchGate by title  

**Summary:**  
Proposes a multi-scale adversarial training methodology specifically for cryptocurrency HFT DRL agents. Defends against FGSM, PGD, C&W attacks, order book manipulation, and latency-based attacks. Integrates **SHAP** (global feature importance) and **LIME** (local decision interpretation) for regulatory transparency. Results: 94.3% of baseline trading performance retained while defending against 89.7% of attacks. Explainability component operates at 8.3ms average latency, compatible with HFT requirements. Demonstrates that defense and interpretability can coexist in real-time financial systems.

---

### 1.9 ⭐⭐ — Conditional Adversarial Fragility Under Economic Stress
**Title:** Conditional Adversarial Fragility in Financial Machine Learning under Macroeconomic Stress  
**Authors:** Samruddhi Baviskar  
**Venue:** arXiv:2512.19935 (December 2025)  
**Link:** https://arxiv.org/abs/2512.19935  

**Summary:**  
Introduces **Conditional Adversarial Fragility** — the empirical finding that financial ML models exhibit systematically amplified adversarial vulnerability during macroeconomic stress periods. Key metrics: while baseline AUROC remains stable across calm vs. stress regimes, adversarial impact nearly doubles during stress (Risk Amplification Factor = 1.97×). False negative rates increase substantially during stress, elevating the risk of missed high-risk cases precisely when the economic environment is most dangerous. Also introduces an LLM-based interpretive governance layer for semantic auditing of model explanations. **Argues that adversarial robustness in financial ML is a regime-dependent property — static testing is insufficient.**

---

### 1.10 ⭐⭐ — TradeTrap: System-Level Adversarial Stress Testing of LLM Trading Agents
**Title:** TradeTrap: Are LLM-based Trading Agents Truly Reliable and Faithful?  
**Authors:** Yanle Wen et al. *(Shanghai AI Laboratory and collaborators)*  
**Venue:** arXiv:2512.02261 (December 2025) | Code: https://github.com/Yanlewen/TradeTrap  
**Link:** https://arxiv.org/abs/2512.02261  

**Summary:**  
Introduces TradeTrap, a unified evaluation framework stress-testing autonomous LLM-based trading agents. Targets four system components: market intelligence, strategy formulation, portfolio/ledger handling, and trade execution. Attack vectors include: prompt injection, Model Context Protocol (MCP) hijacking, state tampering, memory poisoning, and DoS/latency flooding. Evaluated in closed-loop historical backtesting on real US equity data. Key finding: small perturbations at a single component propagate through the agent decision loop, inducing extreme portfolio concentration, runaway exposure, and large drawdowns. Establishes that current autonomous trading agents are systematically exploitable at the system architecture level.

---

### 1.11 ⭐⭐ — Robust Market Making via Adversarial RL (Defense Side)
**Title:** Robust Market Making via Adversarial Reinforcement Learning  
**Authors:** Thomas Spooner, Rahul Savani *(University of Liverpool)*  
**Venue:** IJCAI 2020 | arXiv:2003.01820  
**Link:** https://arxiv.org/abs/2003.01820  

**Summary:**  
Converts the Avellaneda-Stoikov market-making model into a zero-sum game between a market maker and adversary (proxy for informed traders). Uses adversarial reinforcement learning (ARL) to produce market-making agents robust to adversarially-chosen market conditions. Results: (1) emergence of risk-averse behavior without explicit constraints; (2) improved performance metrics in both adversarial and non-adversarial test settings; (3) improved robustness to model uncertainty; (4) convergence profiles correspond to Nash equilibria in simplified single-stage games. **The key defensive use of adversarial RL in financial systems — a complement to the offensive attack papers.**

---

### 1.12 ⭐⭐ — CAIA Benchmark: AI Agents in Adversarial Financial Markets
**Title:** When Hallucination Costs Millions: Benchmarking AI Agents in High-Stakes Adversarial Financial Markets  
**Authors:** Multiple (crypto research team)  
**Venue:** arXiv:2510.00332 (September 2025)  
**Link:** https://arxiv.org/abs/2510.00332  

**Summary:**  
Presents CAIA, a benchmark for evaluating AI agent robustness in adversarial, high-stakes financial environments where misinformation is weaponized and decisions are irreversible. Uses crypto markets as testbed ($30B lost to exploits in 2024). Evaluates 17 models on 178 time-anchored tasks requiring agents to distinguish truth from manipulation. Key findings: (1) without tools, frontier models achieve only 28% accuracy — below junior analyst baselines; (2) tool augmentation plateaus at 67.4% vs. 80% human baseline; (3) models systematically choose unreliable web search over authoritative data, falling for SEO-optimized misinformation. Reveals that adversarial robustness — not just reasoning — is a necessary condition for financial AI autonomy.

---

### 1.13 ⭐ — Prior Master's Thesis: HFT Vulnerability Assessment
**Title:** When Milliseconds Matter: Evaluating the Vulnerability of High-Frequency Trading Models to Adversarial Manipulation  
**Authors:** Karmabir Chakraborty  
**Venue:** Master's Thesis, Pennsylvania State University, 2025  
**Link:** ProQuest / Penn State Electronic Theses (search title at etda.libraries.psu.edu)  

**Summary:**  
The most direct prior thesis to your proposed research. Evaluates LSTM, CNN-LSTM, and DeepLOB architectures under FGSM and PGD attacks applied to LOB feature vectors. Constructs a taxonomy of realistic attacker capabilities in HFT contexts. Assesses adversarial training as a primary defence. Key limitations (which your thesis can address): (1) does not evaluate universal perturbations; (2) does not study data poisoning / backdoor attacks at training time; (3) limited to inference-time attacks. **Treat this as the direct prior work your thesis must differentiate from.**

---

### 1.14 ⭐ — Prior Thesis: Adversarial Robustness of DRL Trading Software
**Title:** Adversarial Robustness Testing of Deep Reinforcement Learning Based Automated Trading Software  
**Authors:** (University of Lethbridge; available via Scholaris.ca)  
**Venue:** Research Thesis, 2022  
**Link:** https://scholaris.ca (search by title)  

**Summary:**  
Investigates grey-box adversarial attacks on DRL trading agents using a simulated market environment rather than historical replay, allowing more realistic attacker-victim dynamics. Findings show DRL agents are vulnerable even under partial-knowledge attacks. Highlights gap in existing robustness evaluation methodology relying on backtesting alone.

---

---

## PART III — Area 2: Data Poisoning, Backdoor Attacks & Label Flipping

### 2.1 ⭐⭐⭐ — Backdoor Poisoning of RL Trading Agents (NeurIPS 2024)
**Title:** SleeperNets: Universal Backdoor Poisoning Attacks Against Reinforcement Learning Agents  
**Authors:** Ethan Rathbun, Christopher Amato, Alina Oprea *(Northeastern University)*  
**Venue:** NeurIPS 2024 | arXiv:2405.20539  
**Link:** https://arxiv.org/abs/2405.20539  

**Summary:**  
Introduces SleeperNets, a framework for backdoor poisoning of RL agents that exploits **dynamic reward poisoning** — interlinking adversary objectives with policy optimization. This makes attacks stealthier than static reward manipulation (which is easily detected by standard constraints). Key contributions: (1) proves theoretical impossibility of prior work to generalize across MDPs; (2) proposes a novel threat model; (3) demonstrates universal backdoor attack across 6 environments. The paper explicitly notes applicability to **stock trading portfolio management** as a safety-critical RL domain. Attack success substantially higher than prior SOTA while preserving benign episodic return.

---

### 2.2 ⭐⭐⭐ — Trigger-Free Backdoor Attack on Financial RL (2024)
**Title:** Trading Devil RL: Backdoor Attack via Stock Market, Bayesian Optimization and Reinforcement Learning  
**Authors:** Orson Mengara  
**Venue:** arXiv:2412.17908 (December 2024)  
**Link:** https://arxiv.org/abs/2412.17908  

**Summary:**  
Introduces **FinanceLLMsBackRL**, a backdoor attack framework requiring **no prior trigger** — the attacker corrupts the training dataset to embed malicious behavior that activates in target market conditions. Specifically targets LLMs and RL agents in HFT. The attack crafts a poisoned dataset Dₚ that, combined with clean data D, trains the model to exhibit malicious behavior while maintaining standard performance on benign inputs. Addresses HFT-specific constraints: attacks must survive rolling-window retraining cycles. Demonstrates persistence across multiple retraining rounds, which is uniquely dangerous in production financial systems.

---

### 2.3 ⭐⭐ — Bayesian-Optimised Backdoor Attack on Financial Models (2024)
**Title:** Trading Devil: Robust Backdoor Attack via Stochastic Investment Models and Bayesian Approach  
**Authors:** Orson Mengara  
**Venue:** arXiv:2406.10719 (June 2024)  
**Link:** https://arxiv.org/abs/2406.10719  

**Summary:**  
Precursor to 2.2. Uses a Bayesian framework to select the highest-impact poison samples from market data distributions, applying stochastic investment models to ensure poisoned data remains statistically plausible and passes standard validation checks. Demonstrates that Bayesian sample selection dramatically reduces the number of poison samples required to achieve a target attack success rate. Addresses survivability across retraining cycles — a critical factor in production financial systems. See also arXiv:2407.14573 for the "Final" variant.

---

### 2.4 ⭐⭐ — Adversarial Robustness in Financial Credit Scoring and Fraud Detection
**Title:** Adversarial Robustness in Financial Machine Learning: Defenses, Economic Impact, and Governance Evidence  
**Authors:** (Multiple)  
**Venue:** arXiv:2512.15780 (December 2025)  
**Link:** https://arxiv.org/abs/2512.15780  

**Summary:**  
Evaluates adversarial robustness in tabular financial ML models (credit scoring, fraud detection) using FGSM and PGD attacks with ε = 0.05. Critically, evaluates impact on *financial risk metrics* rather than just accuracy: Gini coefficient, KS statistic, AUC (discrimination); ECE, Brier score (calibration); Expected Loss, VaR 95%, ES 95% (financial risk). Key result: even small plausibility-bounded perturbations reduce AUC by ~10.6% and increase expected portfolio loss by ~5%. Adversarial training recovers most of the lost utility. Also finds that SHAP value stability degradation serves as an early-warning indicator of adversarial influence.

---

### 2.5 ⭐⭐ — Conditional Fragility Under Macroeconomic Stress (linked from Area 1)
*See entry 1.9 above — directly relevant to data poisoning resilience as it shows adversarial effectiveness doubles during stress periods.*

---

### 2.6 ⭐⭐ — Label Flipping & Poisoning in Financial ML (Survey Coverage)
**Title:** ML Attack Models: Adversarial Attacks and Data Poisoning Attacks  
**Authors:** Multiple  
**Venue:** arXiv:2112.02797 (2021)  
**Link:** https://arxiv.org/abs/2112.02797  

**Summary:**  
Provides a systematic taxonomy of adversarial attack models including label-flipping attacks. In financial contexts, label-flipping attacks flip target labels (e.g., "buy" to "sell", "default" to "non-default") in training data to corrupt decision boundaries. Core empirical finding across literature: as few as 0.1% poisoned labels can significantly degrade model performance while evading standard validation metrics (accuracy, F1 score). Survey highlights that financial applications — with long model reuse cycles and periodic retraining — are uniquely vulnerable to label-flip persistence effects.

---

### 2.7 ⭐ — Survey: Data Poisoning in Financial AI Lifecycles
**Title:** When AI Meets Wall Street: A Survey on Trustworthy AI in Fintech  
**Authors:** Qingwen Zeng, Zhenghao Zhao, Yitian Yang, Yiqi Zhu, Fangchen Liu, Zhaoge Bi, Moe Thandar Kyaw Wynn, Kim-Kwang Raymond Choo, Huaming Chen  
**Venue:** arXiv:2605.30650 (May 2026)  
**Link:** https://arxiv.org/abs/2605.30650  

**Summary:**  
Comprehensive lifecycle-centric survey proposing the **Financial AI Security and Robustness Taxonomy** with 17 attack subtypes. Partitions financial AI into three lifecycle stages: training/updating (data & model poisoning, backdoor attacks), deployment/inference (adversarial evasion attacks), and operation/feedback (prompt injection in LLM workflows, deepfake subversion of KYC). For each subtype: analyses algorithmic strategy, feasibility constraints, stealth/persistence, and downstream financial consequences. **The most comprehensive financial AI security survey available (2026).** Suitable as a survey citation in your literature review chapter.

---

---

## PART IV — Area 3: Limit Order Book Manipulation, Spoofing & Gradient-Based Attacks

### 3.1 ⭐⭐⭐ — Multilevel LOB Spoofing via Cascaded Contrastive Learning (2025)
**Title:** Detecting Multilevel Manipulation from Limit Order Book via Cascaded Contrastive Representation Learning  
**Authors:** Yushi Lin, Peng Yang  
**Venue:** arXiv:2508.17086 (2025)  
**Link:** https://arxiv.org/abs/2508.17086  

**Summary:**  
Addresses the specific challenge that sophisticated spoofing occurs across **multiple price levels simultaneously** — making it undetectable by single-level or flat-feature models. Proposes: (1) **Cascaded LOB Architecture** — hierarchically encodes the order book at each price depth; (2) **Supervised Contrastive Learning** — pulls manipulation instances together in embedding space while pushing apart legitimate trading patterns. Transformer-based instantiation achieves state-of-the-art detection performance. Directly relevant to adversarial evaluation: the learned cascaded representations can themselves be targeted by gradient-based adversarial attacks to study evasion of detection.

---

### 3.2 ⭐⭐⭐ — Probabilistic NN for Real-Time Spoofability Detection
**Title:** Learning the Spoofability of Limit Order Books with Interpretable Probabilistic Neural Networks  
**Authors:** Fabre & Challet  
**Venue:** SSRN / arXiv preprint (2025–2026)  
**Link:** Search SSRN: "spoofability limit order book probabilistic neural"  

**Summary:**  
Novel approach to real-time spoofing detection in cryptocurrency markets. Introduces **multi-scale Hawkes process** order-flow variables that capture both order size and posting distance from best prices — features standard models neglect. A probabilistic neural network estimates the **expected manipulation gain** of each potential spoofing agent in real-time, providing an interpretable numerical score. Particularly relevant for regulatory applications (FCA, SEC surveillance) where explainability of detections is legally required.

---

### 3.3 ⭐⭐ — Conspiracy Spoofing via Transformer Graph Neural Networks (2023)
**Title:** Conspiracy Spoofing Orders Detection with Transformer-Based Deep Graph Learning  
**Authors:** Kang et al.  
**Venue:** 2023 (arXiv / IEEE conference proceedings)  
**Link:** https://arxiv.org/search/?query=conspiracy+spoofing+transformer+graph  

**Summary:**  
Models coordinated ("conspiracy") spoofing orders as a graph structure where nodes are orders and edges encode temporal and price-level proximity. A Transformer-based Graph Neural Network (GNN) learns relational patterns associated with multi-account coordinated spoofing. Addresses a blind spot of standard sequence models that treat each order independently. Particularly relevant as market manipulation increasingly involves coordination across multiple accounts to evade single-account rule-based detectors.

---

### 3.4 ⭐⭐ — Adversarial Robustness of LOB Generative Models
**Title:** Conditional Generators for Limit Order Book Environments: Explainability, Challenges, and Robustness  
**Authors:** Coletta et al.  
**Venue:** arXiv, 2023  
**Link:** https://arxiv.org/search/?query=conditional+generator+limit+order+book+robustness  

**Summary:**  
Investigates adversarial attacks on GAN-based LOB simulators (used for training and testing trading algorithms). Gradient-based perturbations of conditional inputs cause the simulator to produce non-physical, implausible market states — invalid from a market microstructure perspective. Key finding: LOB generative models are as vulnerable to adversarial perturbations as discriminative classifiers. Proposes input pre-processing and adversarial regularisation as defences. Relevant for evaluating the robustness of synthetic LOB data generation pipelines used in model training.

---

### 3.5 ⭐⭐ — Limit Order Book GAN Simulation (SSRN 2023)
**Title:** Limit Order Book Simulation with Generative Adversarial Networks  
**Authors:** Cont R., Cucuringu M., Kochems J., Prenzel F.  
**Venue:** SSRN:4512356 (2023)  
**Link:** https://ssrn.com/abstract=4512356  

**Summary:**  
Develops a GAN-based simulator for realistic LOB dynamics. While the primary purpose is synthetic data generation rather than adversarial attack, this work is foundational for understanding the LOB's statistical properties — properties that adversarial attacks must respect to remain "plausible." The simulator can also be used to generate synthetic adversarial LOB states for training detection models (see Area 4 autoencoders).

---

### 3.6 ⭐⭐ — Market Manipulation Detection: Survey and Taxonomy
**Title:** A Survey on Stock Market Manipulation Detectors Using Artificial Intelligence  
**Authors:** Multiple  
**Venue:** Open access journal / preprint (2023/2026)  
**Link:** Search techscience.com or Google Scholar by title  

**Summary:**  
Structured review of AI methods for detecting market manipulation. Categorises approaches into: (1) conventional ML (SVM, Random Forest, Gradient Boosting); (2) deep learning (LSTM, CNN, Transformer, GNN); defines manipulation taxonomies (spoofing, layering, wash trading, pump-and-dump). Discusses feature engineering approaches, evaluation metrics, regulatory context, and real-world deployment challenges. Essential reading for understanding the state of detection defences before introducing adversarial attacks as a novel threat to those defences.

---

### 3.7 ⭐ — DiVA Thesis: Spoofing Detection Comparative Study
**Title:** Spoofing Detection in Limit Order Books Using Machine Learning — A Comparative Study  
**Authors:** (Multiple; Swedish university — available via DiVA portal)  
**Venue:** Master's Thesis, KTH / Stockholm University, 2022–2023  
**Link:** https://diva-portal.org (search "spoofing detection limit order book machine learning")  

**Summary:**  
Compares traditional ML (SVM, Random Forest) vs. deep learning (LSTM, CNN) for LOB spoofing detection using real exchange data. Key finding: deep learning outperforms traditional methods but exhibits higher vulnerability to distributional shift. This is a direct precursor observation to the adversarial robustness problem — if models are fragile to distributional shift under normal market regime changes, they are also fragile to adversarial manipulation.

---

---

## PART V — Area 4: Defensive AI — Autoencoders, Anomaly Detection & Data Sanitisation

### 4.1 ⭐⭐⭐ — Adversarially Trained Autoencoder for Time-Series Anomaly Detection (WSDM 2023)
**Title:** DAEMON: Adversarial Autoencoder for Unsupervised Time Series Anomaly Detection and Interpretation  
**Authors:** Li et al.  
**Venue:** ACM WSDM 2023  
**Link:** https://dl.acm.org/doi/10.1145/3539597.3570371 (search ACM DL by title)  

**Summary:**  
Introduces DAEMON — an adversarially-trained autoencoder for unsupervised multivariate time-series anomaly detection. Uses **two discriminators** to adversarially regularise the latent space: (1) ensures the encoder learns compact, interpretable representations of "normal" behaviour; (2) forces the decoder to produce realistic reconstructions. At inference time, anomalies are detected by reconstruction error exceeding a dynamic threshold. The adversarial training loop makes the autoencoder itself more robust against distributional shift. **Directly applicable to financial data sanitisation as a pre-filter for adversarial market data inputs.** Strong empirical performance on synthetic and real time-series benchmarks.

---

### 4.2 ⭐⭐⭐ — Approximate Projection Autoencoder for Evasion-Aware Defence
**Title:** APAE: Approximate Projection Autoencoder for Adversarially Robust Anomaly Detection  
**Authors:** Multiple (IJCAI 2025/2026 proceedings)  
**Venue:** IJCAI 2025 or 2026  
**Link:** https://ijcai.org/proceedings (search "approximate projection autoencoder adversarial")  

**Summary:**  
Addresses the specific adversarial attack scenario where an attacker **disguises anomalies as normal data** to evade autoencoder-based detectors — a critical and often overlooked threat model. The APAE optimises the latent representation with an approximate projection onto the manifold of normal data, enforcing a structural constraint that anomaly-disguise attacks cannot easily satisfy. Demonstrated on cyber-physical and financial sensor anomaly benchmarks. **Directly relevant to evaluating and hardening autoencoder defences in your thesis against evasion attacks.**

---

### 4.3 ⭐⭐ — ARTA: Adversarially Robust Time-Series Anomaly Detection (2026)
**Title:** ARTA: Adversarially Robust Multivariate Time-Series Anomaly Detection  
**Authors:** Multiple  
**Venue:** arXiv preprint (2026)  
**Link:** https://arxiv.org/search/?query=ARTA+adversarially+robust+time+series+anomaly  

**Summary:**  
Proposes a **min-max optimisation objective** for training anomaly detectors robust to structured noise and adversarially crafted temporal corruptions. The outer minimisation trains the detector; the inner maximisation crafts the worst-case perturbation within an Lp-ball around the normal data manifold. Establishes both empirical robustness (benchmark comparisons) and theoretical robustness certificates. Applied to financial sensor stream datasets. The min-max framework is directly applicable to designing the defence component of a financial data sanitisation pipeline.

---

### 4.4 ⭐⭐ — Hybrid LSTM-Autoencoder + One-Class SVM for HFT Sanitisation
**Title:** Anomaly Detection in High-Frequency Trading Using LSTM Autoencoders and One-Class SVMs  
**Authors:** Multiple  
**Venue:** Open-access journal / preprint (2023–2024)  
**Link:** https://preprints.org (search "LSTM autoencoder anomaly detection high-frequency trading")  

**Summary:**  
Proposes a two-stage pipeline for financial data sanitisation: (1) LSTM Autoencoder identifies anomalous data segments via reconstruction error thresholding; (2) One-Class SVM trained on latent representations refines anomaly scores. Functions as a **firewall** that pauses or reroutes trading signals when incoming data is flagged. Key result: the hybrid approach achieves higher precision than LSTM-AE alone, significantly reducing false-positive trade halts. Provides the architectural blueprint for a Task-Aware LSTM Autoencoder defence.

---

### 4.5 ⭐⭐ — Adversarial Contrastive Autoencoder for Multivariate Anomaly Detection
**Title:** Adversarial Contrastive Autoencoder for Multivariate Time-Series Anomaly Detection (2024)  
**Authors:** Meng et al.  
**Venue:** arXiv (2024)  
**Link:** https://arxiv.org/search/?query=adversarial+contrastive+autoencoder+multivariate+time+series+anomaly  

**Summary:**  
Combines contrastive learning with adversarial autoencoder training to produce latent representations that are: (1) compact and well-structured for normal data; (2) discriminative between normal and anomalous patterns; (3) robust to adversarial perturbations of input features. Evaluated on multiple multivariate time-series benchmarks. The contrastive component directly addresses the challenge of anomaly detection when anomalies and normal patterns occupy overlapping regions in raw feature space — a common occurrence in financial data.

---

### 4.6 ⭐⭐ — Transformer Autoencoder for HFT Manipulation Detection
**Title:** Transformer-Based Autoencoders for Limit Order Book Anomaly Detection (includes robustness against synthetic quote stuffing / pump-and-dump)  
**Authors:** Multiple  
**Venue:** preprints.org (2024–2025)  
**Link:** https://preprints.org (search "transformer autoencoder limit order book anomaly")  

**Summary:**  
Applies Transformer-based autoencoders to LOB anomaly detection, specifically testing resilience against synthetically injected manipulation patterns: quote stuffing, pump-and-dump, layering. The Transformer's attention mechanism enables the model to identify anomalous order patterns at arbitrary temporal lags — more flexible than LSTM for non-local temporal dependencies. Provides a direct bridge between Area 3 (LOB manipulation) and Area 4 (autoencoder defences) — the detection model that a sophisticated adversary would need to evade.

---

### 4.7 ⭐ — Systematic Survey of Temporal Adversarial Attacks on TS and RL
**Title:** Temporal Adversarial Attacks on Time Series and Reinforcement Learning Systems: A Systematic Survey, Taxonomy, and Benchmarking Roadmap  
**Authors:** Ade Kurniawan, Merios Gusan Putra, Dani Lukman Hakim, Mochammad Ariyanto  
**Venue:** Preprints.org (January 2026)  
**Link:** https://preprints.org (search "temporal adversarial attacks time series reinforcement learning systematic survey")  

**Summary:**  
Systematic review of 127 papers (2019–2025). Establishes a unified four-dimensional taxonomy covering: target modalities (including financial time series), perturbation strategies, temporal scope, and physical realizability. Benchmarking analysis shows digital attack success rates of 85–98% for time-series attacks. Introduces "Temporal AutoAttack" (T-AutoAttack) for standardized benchmarking. Defence evaluation: adversarial training, detection-based approaches, certified defences. **Useful for your methodology chapter to justify selection of attack/defence methods and benchmarking protocols.**

---

---

## PART VI — Regulatory, Policy & Industry Reports

### R.1 ⭐⭐⭐ — FSB Report: Financial Stability Implications of AI
**Title:** The Financial Stability Implications of Artificial Intelligence  
**Author:** Financial Stability Board (FSB)  
**Date:** 2024  
**Link:** https://www.fsb.org/2024/  

**Summary:**  
Landmark regulatory report assessing AI-induced systemic risk in global finance. Key findings: (1) correlated algorithmic trading failures — AI monocultures respond similarly to the same adversarial signal, amplifying market stress; (2) opacity of DL models to supervisors; (3) non-bank financial intermediaries (hedge funds) adopting opaque AI with minimal regulatory oversight; (4) AI-driven cyber attacks lowering cost of adversarial financial attacks. Recommends resilience frameworks, international coordination, and red-team exercises. **Essential for your introduction to establish the real-world regulatory stakes of your research topic.**

---

### R.2 ⭐⭐⭐ — IMF Global Financial Stability Report (AI Chapter)
**Title:** Global Financial Stability Report — AI and Financial Markets Chapter  
**Author:** International Monetary Fund (IMF)  
**Date:** 2024  
**Link:** https://www.imf.org/en/Publications/GFSR  

**Summary:**  
IMF chapter identifies that AI dramatically lowers the cost and time for adversarial financial attacks, enabling hostile actors to exploit model vulnerabilities at scale. Discusses "correlated failures" where AI-driven herd behaviour amplifies market stress — a macro-financial shock scenario. Warns of uneven access: large US-based firms have both offensive and defensive AI capabilities while smaller institutions remain more vulnerable. Calls for governance frameworks including red-team exercises simulating attacks from frontier AI tools. **Recommended citation for your policy implications section.**

---

### R.3 ⭐⭐⭐ — NIST AI 100-2 Adversarial ML Taxonomy
*See entry F.1 above — critical for anchoring your threat model.*

---

### R.4 ⭐⭐ — BIS Working Papers on AI and Financial Stability
**Title:** Various working papers on AI systemic risk  
**Author:** Bank for International Settlements (BIS)  
**Date:** 2023–2025  
**Link:** https://www.bis.org/research (search "artificial intelligence financial stability")  

**Summary:**  
BIS working papers examine specific channels through which AI-driven trading creates systemic risk, including: liquidity withdrawal during stress events, flash crashes from correlated algorithmic responses, and the inadequacy of traditional circuit-breaker mechanisms against AI-speed manipulation. Provides empirical evidence on market microstructure disruption consistent with the adversarial trading threat model.

---

---

## PART VI-B — Supplementary Papers (Additional Verified Entries)

### S.1 ⭐⭐ — Task-Aware Reconstruction for Time-Series Transformers (KDD 2022)
**Title:** TARNet: Task-Aware Reconstruction for Time-Series Transformer  
**Authors:** Ranak Roy Chowdhury, Xiyuan Zhang, Jingbo Shang, Rajesh K. Gupta, Dezhi Hong  
**Venue:** ACM KDD 2022, pp. 212–220  
**Link:** https://dl.acm.org/doi/10.1145/3534678.3539329 | arXiv:2205.11948  

**Summary:**  
Introduces TARNet, a framework using **task-aware masking** for time-series transformers. Rather than random masking (as in standard BERT-style pre-training), TARNet uses the transformer's aggregated attention map to identify and mask time segments most critical for the downstream task (classification, anomaly detection, regression). The model is trained with dual objectives: task performance + reconstruction of masked segments. Directly applicable to designing a **Task-Aware LSTM/Transformer Autoencoder** for financial anomaly detection — the specific architecture mentioned in your thesis topic. Adaptable by replacing the task head with a financial signal classifier or trading-direction predictor.

---

### S.2 ⭐⭐ — Adversarial Vulnerabilities in LLMs for Time-Series Forecasting (AISTATS 2025)
**Title:** Adversarial Vulnerabilities in Large Language Models for Time Series Forecasting  
**Authors:** Johnson Jiang et al.  
**Venue:** AISTATS 2025 | arXiv:2412.08099  
**Link:** https://arxiv.org/abs/2412.08099 | Code: https://github.com/JohnsonJiang1996/AdvAttack_LLM4TS  

**Summary:**  
First systematic adversarial attack study targeting LLMs deployed for time-series forecasting. Introduces a targeted attack framework using gradient-free and black-box optimisation to generate minimal perturbations. Evaluated on GPT-3.5, GPT-4, LLaMa, Mistral (via LLMTime), TimeGPT, and TimeLLM across multiple real-world datasets including financial time series. Key finding: adversarial attacks produce far more severe performance degradation than equivalent random noise — the LLMs' reliance on tokenised numerical patterns makes them uniquely vulnerable to structured input manipulation. Relevant to your thesis as financial institutions increasingly deploy LLM-based forecasting, and this paper provides the attack methodology and benchmark.

---

### S.3 ⭐⭐ — Learning Not to Spoof: Emergent Spoofing in DRL Market Simulations (ICAIF 2022)
**Title:** Learning Not to Spoof  
**Authors:** Donald J. Byrd  
**Venue:** ACM ICAIF 2022 (3rd International Conference on AI in Finance)  
**Link:** https://dl.acm.org/doi/10.1145/3533271.3561706 | Search ACM DL by title  

**Summary:**  
Demonstrates that profit-maximising DRL agents in multi-agent market simulations **independently discover spoofing** as an optimal strategy without being explicitly programmed to spoof. This emergent manipulation behaviour arises because spoofing is genuinely effective at moving prices in an agent-based environment. The paper proposes a normative framework to shape agent rewards and prevent such unwanted behaviours. Critically important for your LOB manipulation area: it proves that gradient-based RL optimization (gradient ascent on the policy) naturally converges to adversarial market behaviours including LOB spoofing — providing a theoretical basis for the "gradient ascent optimization attacks" mentioned in your thesis topic.

---

---

## PART VII — Structured Search Queries for Further Discovery

Use these targeted queries on each database to systematically discover additional relevant papers:

| Database | Query | Focus Area |
|---|---|---|
| **arXiv cs.LG + q-fin.TR** | `"adversarial" AND "limit order book" AND ("attack" OR "evasion")` | Area 1+3 |
| **arXiv cs.CR** | `"data poisoning" AND ("trading" OR "financial") AND ("LSTM" OR "transformer")` | Area 2 |
| **arXiv q-fin.ST** | `"adversarial perturbation" AND "financial time series" AND "autoencoder"` | Area 1+4 |
| **IEEE Xplore** | `"adversarial machine learning" AND "algorithmic trading"` | Area 1 |
| **IEEE Xplore** | `"high frequency trading" AND ("anomaly detection" OR "spoofing")` | Area 3+4 |
| **ACM Digital Library** | `"adversarial" AND "financial" AND "autoencoder" conference:WSDM OR SIGKDD` | Area 4 |
| **ACM Digital Library** | `"limit order book" AND "machine learning" AND "manipulation"` | Area 3 |
| **Google Scholar** | `"adversarial data poisoning" "algorithmic trading" after:2022` | Area 2 |
| **Google Scholar** | `"task-aware LSTM autoencoder" financial trading defense` | Area 4 |
| **SSRN q-fin** | `"adversarial" "limit order book" OR "spoofing" machine learning` | Area 3 |
| **SSRN q-fin** | `"adversarial perturbations" "high frequency trading" 2024..2026` | Area 1 |
| **ProQuest Theses** | `"adversarial attack" "algorithmic trading" master thesis 2022..2026` | Prior theses |
| **DiVA Portal** | `adversarial AND "deep learning" AND "financial" AND "trading"` | Prior theses |
| **Semantic Scholar** | `"universal adversarial perturbation" financial time series trading` | Area 2 |

---

## PART VIII — Master Reference Table (All Entries)

| ID | Title (short) | Authors | Year | Venue | Priority | Area |
|---|---|---|---|---|---|---|
| F.1 | NIST AI 100-2 Adversarial ML Taxonomy | NIST | 2023/2025 | NIST Technical Report | ⭐⭐⭐ | Foundation |
| F.2 | DeepLOB | Zhang, Zohren, Roberts | 2019 | IEEE TSP | ⭐⭐⭐ | Foundation |
| F.3 | Adversarial Attacks on DNN for TS Classification | Fawaz, Forestier et al. | 2019 | IJCNN | ⭐⭐ | Foundation |
| F.4 | Adversarial Attacks on Time Series (ATN) | Karim, Majumdar, Darabi | 2021 | IEEE TPAMI | ⭐⭐ | Foundation |
| F.5 | AI and Systemic Risk | Danielsson, Macrae, Uthemann | 2022 | J. Banking & Finance | ⭐⭐ | Foundation |
| 1.1 | Adversarial Attacks on ML for HFT | Goldblum et al. | 2021 | ICAIF | ⭐⭐⭐ | Area 1 |
| 1.2 | Taking Over the Stock Market | Nehemya, Mathov et al. | 2021 | ECML PKDD | ⭐⭐⭐ | Area 1 |
| 1.3 | The Ephemeral Threat | Rizvani, Apruzzese, Laskov | 2025 | CODASPY | ⭐⭐⭐ | Area 1 |
| 1.4 | Adversarial Attacks on Deep Trading Policies | Faghan et al. | 2020 | arXiv | ⭐⭐⭐ | Area 1 |
| 1.5 | Adversarial News and Lost Profits | Rizvani, Apruzzese, Laskov | 2026 | SaTML | ⭐⭐ | Area 1 |
| 1.6 | The Black Tuesday Attack | Multiple | 2025 | arXiv | ⭐⭐ | Area 1 |
| 1.7 | Slope-Based Attacks on Financial TS | Multiple | 2025 | arXiv | ⭐⭐ | Area 1 |
| 1.8 | Adversarial-Robust DRL Crypto HFT | Sinha et al. | 2025 | ResearchGate | ⭐⭐ | Area 1 |
| 1.9 | Conditional Adversarial Fragility | Baviskar | 2025 | arXiv | ⭐⭐ | Area 1 |
| 1.10 | TradeTrap | Wen et al. | 2025 | arXiv | ⭐⭐ | Area 1 |
| 1.11 | Robust Market Making via ARL | Spooner, Savani | 2020 | IJCAI | ⭐⭐ | Area 1 (defense) |
| 1.12 | CAIA Benchmark | Multiple | 2025 | arXiv | ⭐⭐ | Area 1 |
| 1.13 | HFT Vulnerability Thesis (PSU) | Chakraborty | 2025 | MSc Thesis | ⭐ | Prior Thesis |
| 1.14 | DRL Trading Robustness Thesis | Anonymous | 2022 | MSc Thesis | ⭐ | Prior Thesis |
| 2.1 | SleeperNets | Rathbun, Amato, Oprea | 2024 | NeurIPS | ⭐⭐⭐ | Area 2 |
| 2.2 | Trading Devil RL | Mengara | 2024 | arXiv | ⭐⭐⭐ | Area 2 |
| 2.3 | Trading Devil (Bayesian) | Mengara | 2024 | arXiv | ⭐⭐ | Area 2 |
| 2.4 | Adversarial Robustness in Financial ML | Multiple | 2025 | arXiv | ⭐⭐ | Area 2 |
| 2.6 | ML Attack Models: Poisoning Taxonomy | Multiple | 2021 | arXiv | ⭐⭐ | Area 2 |
| 2.7 | When AI Meets Wall Street (Survey) | Zeng, Zhao et al. | 2026 | arXiv | ⭐ | Area 2 survey |
| 3.1 | Detecting Multilevel LOB Manipulation | Lin, Yang | 2025 | arXiv | ⭐⭐⭐ | Area 3 |
| 3.2 | Learning LOB Spoofability (Probabilistic NN) | Fabre & Challet | 2025-26 | SSRN/arXiv | ⭐⭐⭐ | Area 3 |
| 3.3 | Conspiracy Spoofing via GNN | Kang et al. | 2023 | IEEE | ⭐⭐ | Area 3 |
| 3.4 | LOB Conditional Generators Robustness | Coletta et al. | 2023 | arXiv | ⭐⭐ | Area 3 |
| 3.5 | LOB Simulation with GANs | Cont, Cucuringu et al. | 2023 | SSRN | ⭐⭐ | Area 3 |
| 3.6 | Survey: Stock Market Manipulation AI | Multiple | 2023-26 | Open Access | ⭐⭐ | Area 3 |
| 3.7 | Spoofing Detection LOB Thesis | DiVA portal | 2022-23 | MSc Thesis | ⭐ | Area 3 |
| 4.1 | DAEMON Adversarial Autoencoder | Li et al. | 2023 | ACM WSDM | ⭐⭐⭐ | Area 4 |
| 4.2 | APAE Robust Autoencoder | Multiple | 2025-26 | IJCAI | ⭐⭐⭐ | Area 4 |
| 4.3 | ARTA Robust TS Anomaly Detection | Multiple | 2026 | arXiv | ⭐⭐ | Area 4 |
| 4.4 | LSTM-AE + OC-SVM for HFT Sanitisation | Multiple | 2023-24 | preprints.org | ⭐⭐ | Area 4 |
| 4.5 | Adversarial Contrastive Autoencoder | Meng et al. | 2024 | arXiv | ⭐⭐ | Area 4 |
| 4.6 | Transformer AE for LOB Anomaly Detection | Multiple | 2024-25 | preprints.org | ⭐⭐ | Area 4 |
| 4.7 | Temporal Adversarial Attacks Survey | Kurniawan et al. | 2026 | preprints.org | ⭐ | Area 4 |
| R.1 | FSB AI Financial Stability Report | FSB | 2024 | Regulatory Report | ⭐⭐⭐ | Policy |
| R.2 | IMF GFSR AI Chapter | IMF | 2024 | Policy Report | ⭐⭐⭐ | Policy |
| R.4 | BIS AI Systemic Risk Working Papers | BIS | 2023-25 | Working Papers | ⭐⭐ | Policy |

---

> [!IMPORTANT]
> **Verification Required:** Always verify author names, arXiv IDs, and publication venues directly at arxiv.org, ieeexplore.ieee.org, dl.acm.org, or ssrn.com before citing in your thesis. Preprint metadata can change post-publication.

> [!TIP]
> **For papers behind paywalls:** Use your institutional library's Elsevier/IEEE/Springer access. Most arXiv preprints are freely accessible at the URLs listed. Authors' personal/university websites and ResearchGate often host accepted-manuscript versions.

> [!NOTE]
> **Research Gap Opportunity:** The literature review reveals a clear gap in the intersection of universal adversarial perturbations + label-flipping data poisoning + LOB-specific defences. Specifically, no existing paper simultaneously evaluates: (1) gradient-ascent LOB manipulation attacks, (2) their interaction with training-time data poisoning (label flipping), and (3) a Task-Aware LSTM Autoencoder as a joint defence for both inference-time evasion and training-time poisoning. This three-part intersection is your thesis's unique contribution space.
