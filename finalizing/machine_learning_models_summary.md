## 1. Sequential & Temporal Deep Learning Models
These models are primarily used to capture the time-series dependencies of "low-and-slow" attacks.
* **Long Short-Term Memory (LSTM) Networks** [R.6]:
  * **Efficacy:** A multi-layer LSTM achieved an accuracy and AUC of **0.99**, with false-positive and false-negative rates around **0.01**. The loss curves showed proper convergence without overfitting.
* **Temporal Convolutional Networks (TCN)** [R.9]:
  * **Efficacy:** Achieved **85%–97% prediction accuracy** in modeling attacker behavior.
  * **Efficiency:** Outperformed LSTM and Gated Recurrent Unit (GRU) models on the same sequential tasks.

## 2. Convolutional Deep Learning Models
Used to automate feature extraction without manual selection.
* **One-Dimensional Convolutional Neural Networks (1D CNN)** [R.13]:
  * **Efficacy:** Achieved **98.9% accuracy** and an F1-score of **0.981**. Outperformed traditional classifiers like SVMs, Random Forests, and basic Artificial Neural Networks.
* **Hybrid Model (1D CNN + Gated Recurrent Unit (GRU))** [R.14]: 
  * **Efficacy:** Reached **99.75% accuracy**.
  * **Efficiency:** Designed specifically for resource-constrained environments (IoT). It reduced the trainable parameters to just 4,370, decreasing the computational budget by **76%** and significantly reducing training and detection times compared to other state-of-the-art models.

## 3. Reinforcement Learning Models
Used for dynamic, self-updating threat detection.
* **Deep Reinforcement Learning (DRL)** [R.5]:
  * **Efficacy:** Monitored behavioral telemetry and updated its baseline via reward optimization to achieve **98.4% accuracy, 98.1% precision, 97.8% recall**, and an **F1-score of 97.9%**, with a very low **false-positive rate of 1.9%**. It outperformed SVM, Random Forest, CNN, and LSTM models on the same data.

## 4. Graph-Based Neural Networks
Used to detect structural communication topologies and decentralized botnet networks.
* **Graph Neural Networks (GNN)** [R.11]:
  * **Efficacy:** Captured hierarchical and fast-mixing botnet topologies better than existing non-learning methods (e.g., BotGrep), leading to higher detection rates and lower false positives.
* **Graph-Based Federated Learning (GNN with FL)** [R.15]:
  * **Efficacy:** Achieved an **F1-score of 0.9153** when predicting credential stuffing risks across websites.
  * **Efficiency/Privacy:** The FL-based GNN outperformed other GNN models by **4–11%** while protecting user privacy by ensuring only model gradients (not raw data) were shared.

## 5. Gradient-Boosted Classifiers (Tree-based)
Used predominantly for protocol-level telemetry classification.
* **XGBoost and CatBoost** [R.1]:
  * **Efficacy:** CatBoost achieved an **AUC of 0.998**, an **F1-score of 0.9734**, and **98.63% accuracy** on test sets examining TLS fingerprint metadata, with XGBoost performing similarly.

## 6. Lightweight / Traditional Machine Learning Models
Tested for their computational viability and forensics interpretability against heavy deep learning alternatives.
* **Random Forest, Decision Trees, and Logistic Regression** [R.10]:
  * **Efficacy:** Random Forest achieved a **ROC-AUC of 0.97** and a PR-AUC of 0.54, staying highly competitive against deep learning models under natural class imbalance.
  * **Efficiency:** Trained **90% faster** than CNN baselines. Crucially, they offer much lower computational costs and clear forensic interpretability (via feature importance scoring), making them excellent for rapid triage.
* **Weighted Naïve Bayes Classifier** [R.4]:
  * **Efficacy:** Fused TLS fingerprints with destination context to achieve an **F1-score above 0.99** for process identification and **99.9% precision** for malware detection.
* **Positional-Unigram Byte Models (Maximum Likelihood Estimation)** [R.3]:
  * **Efficacy:** Proven to be robust to "cipher stunting", maintaining an unbiased F1 score even when synthetic randomization evasion tactics increased.

## 7. Adversarial Explainability Models
* **Explainable AI (XAI - e.g., SHAP)** [R.8, R.12]:
  * **Efficacy (Attacker capability):** Demonstrated the vulnerability of ML models. By altering just a single critical feature extracted using XAI tools, attackers completely bypassed an IoT botnet detection system (achieving a **100% evasion success rate / 0% detection rate** against a classifier that previously had 99% accuracy).

## Summary of Efficacy and Efficiency
Overall, the sources suggest that while **Deep Learning models (DRL, CNNs, LSTMs)** boast near-perfect efficacy metrics (often >98% accuracy) for detecting complex, distributed low-frequency attacks, they are computationally expensive and vulnerable to adversarial tampering. 

To achieve optimal **efficiency** (especially for real-time API Gateways), the research favors either **lightweight models (like Random Forests)** for fast, interpretable triage, or highly optimized **hybrid deep learning architectures (like 1D CNN + GRU)** that slash computational overhead while preserving high detection rates.
