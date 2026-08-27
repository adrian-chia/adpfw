# Thesis Paper Summaries

## R.1: When Handshakes Tell the Truth

**Citation:**
Ghalia Jarad and Kemal Bıçakcı, *When Handshakes Tell the Truth: Detecting Web Bad Bots via TLS Fingerprints*, place missing, arXiv preprint arXiv:2602.09606, 2026.

**Detailed Main Point:**
The authors test whether protocol-level TLS fingerprinting (specifically JA4) and gradient-boosted machine learning (XGBoost and CatBoost) can distinguish malicious web bots from human traffic. They analyze unencrypted handshake metadata, such as cipher lists, extension sets, and ALPN preferences, in the TLS ClientHello packet. Their models achieved 98.6% accuracy on a real-world dataset (JA4DB). The study shows that automated scripts have different cryptographic configurations than standard web browsers, making protocol-level artifacts more robust against evasion tactics like header spoofing or IP rotation.

**Relevance to Thesis:**
This paper shows that TLS fingerprinting works as a privacy-preserving feature set for detecting evasive bots. "Low-and-slow" credential stuffing campaigns rotate through thousands of IPs to bypass volume-based rate limiting. This research confirms that the underlying TLS handshake—specifically the `ja4_b` cipher hash and extension counts—remains consistent. An adaptive defense mechanism can use these TLS features to identify the botnet, neutralizing the attack even when the request frequency per IP is low.

## R.2: FP-Inconsistent: Measurement and Analysis of Fingerprint Inconsistencies in Evasive Bot Traffic

**Citation:**
Hari Venugopalan, Shaoor Munir, Shuaib Ahmed, Tangbaihe Wang, Samuel T. King and Zubair Shafiq, *FP-Inconsistent: Measurement and Analysis of Fingerprint Inconsistencies in Evasive Bot Traffic*, place missing, arXiv preprint arXiv:2406.07647v3, 2025.

**Detailed Main Point:**
This research measures how evasive bots manipulate their browser fingerprints to bypass commercial anti-bot services like DataDome and BotD. The authors deployed a honey site and purchased traffic from 20 blackhat bot services. They found that while evasive bots alter their fingerprints to mimic legitimate devices, they often introduce spatial and temporal inconsistencies, such as reporting a non-existent screen resolution for a spoofed iPhone or showing mismatched IP geolocation and browser time zones. The authors propose "FP-Inconsistent," a method that detects these attribute mismatches and reduces bot evasion by 44.95% to 48.11%.

**Relevance to Thesis:**
This paper exposes the limits of application-layer browser fingerprinting and static rules. Evasive bots mutate higher-layer attributes, such as User-Agent strings and screen resolution, to bypass traditional gateway defenses. This supports the thesis argument for adaptive machine learning models. Evasive bots often leave traces when trying to spoof multiple data points over time. An adaptive API gateway can track these temporal inconsistencies and integrate harder-to-spoof TLS fingerprints to neutralize credential stuffing campaigns.

## R.3: Positional-Unigram Byte Models for Generalized TLS Fingerprinting

**Citation:**
Hector A. Valdez and Sean McPherson, *Positional-Unigram Byte Models for Generalized TLS Fingerprinting*, place missing, arXiv preprint arXiv:2405.07848v1, 2024.

**Detailed Main Point:**
The authors propose a statistical TLS fingerprinting approach using "positional-unigram byte models" built from TLS Client Hello messages. Standard hash-based fingerprinting, like JA3, is vulnerable to "cipher stunting," where attackers randomize the cipher suite list to generate an unknown hash. The authors' method computes the maximum likelihood of byte occurrences at each position in the Client Hello message against models of known client applications. Experiments show that this probabilistic approach classifies applications accurately and resists synthetic cipher suite permutations.

**Relevance to Thesis:**
This paper points out a flaw in static defense mechanisms: botnets use cipher stunting to bypass rigid TLS hash-based blocks. This supports the thesis argument for using adaptive, machine-learning-based profiling instead of static signature matching. A self-learning defense system can analyze the probabilistic features of TLS telemetry and request headers to detect automated behavior, even when bots mutate their TLS fingerprints.

## R.4: Accurate TLS Fingerprinting using Destination Context and Knowledge Bases

**Citation:**
Blake Anderson and David McGrew, *Accurate TLS Fingerprinting using Destination Context and Knowledge Bases*, place missing, arXiv preprint arXiv:2009.01939v1, 2020.

**Detailed Main Point:**
Traditional TLS fingerprinting often maps a single fingerprint to hundreds of different processes because they share the same TLS libraries, creating false positives. To fix this, the authors built a system that fuses the cryptographic fingerprint string with destination context, such as IP address, port, and Server Name Indication. Using a knowledge base and a weighted naïve Bayes classifier, the system disambiguates processes. It achieved an F1 score above 0.99 for process identification and 99.9% precision for malware detection by analyzing only the unencrypted Client Hello packet.

**Relevance to Thesis:**
This paper shows that using TLS fingerprinting in isolation causes false positives because legitimate and malicious tools share libraries. This validates the thesis methodology: fusing TLS fingerprints with request-header analysis. An adaptive machine learning model can use this combined telemetry to calculate joint probabilities. That separates legitimate users from automated botnets, reducing false positives and neutralizing the attack without locking out real users.

## R.5: Adaptive Anomaly Detection Algorithm for Real-Time Identification of Phishing and Credential Stuffing Attacks

**Citation:**
Nilufar Madaminova, Akram Maxammatov, Svetlana Sadchikova, Gulbakhor Altibaeva, Mahzuna Hamdamova, Zokir Alimov and Sadoqat Jurayeva, *Adaptive Anomaly Detection Algorithm for Real-Time Identification of Phishing and Credential Stuffing Attacks in E-Learning Systems Using Deep Reinforcement Learning*, Tashkent, Journal of Internet Services and Information Security (JISIS), 2026.

**Detailed Main Point:**
The authors use Deep Reinforcement Learning (DRL) to detect phishing and credential stuffing attacks in e-learning platforms. Traditional static signature-based detection models have high false-positive rates and struggle to adapt to new threats. The authors' DRL agent monitors behavioral telemetry, including failed login attempts, IP switching rates, session duration, and URL reputation. The model updates its detection policy through environmental feedback and a reward-penalty mechanism. It achieved 98.4% accuracy with a 1.9% false-positive rate, outperforming SVM, Random Forest, and LSTM models on the same data.

**Relevance to Thesis:**
This paper supports the thesis's proposal for an adaptive learning system. An API Gateway must use self-learning mechanisms like DRL to stop "low-and-slow" credential stuffing botnets that stay below static volume thresholds. The thesis can use this research to argue that an adaptive agent—one that updates its baseline of normal traffic using reward optimization—can dynamically adjust throttling algorithms. Applied to TLS fingerprints and request headers, a DRL framework could penalize low-frequency anomalies without blocking legitimate users.

## R.6: HTTP Low and Slow DoS Attack Detection using LSTM based deep learning

**Citation:**
Bronjon Gogoi and Tasiruddin Ahmed, *HTTP Low and Slow DoS Attack Detection using LSTM based deep learning*, Guwahati, 2022 IEEE 19th India Council International Conference (INDICON), 2022.

**Detailed Main Point:**
The authors propose an LSTM (Long Short-Term Memory) network for detecting HTTP "low-and-slow" DoS attacks, such as Slowloris, Slow Post, and Slow Read. These attacks use low-volume traffic to exhaust server threads, bypassing traditional network layer defenses by mimicking legitimate user requests. The authors converted HTTP traffic into three-dimensional temporal sequences, combining timestamps and requests-per-second, to train the LSTM network. Using the CIC DoS dataset and synthetic attack traces, the classifier achieved an accuracy and AUC-ROC score of 0.99.

**Relevance to Thesis:**
This paper explains the mechanics of "low-and-slow" network behavior and shows why static volume-based rate limiting fails against these attacks. The thesis can use these findings to argue for temporal sequence analysis, which extracts patterns over time rather than relying on instantaneous volume. While the paper focuses on resource exhaustion, the same temporal analysis applies to low-and-slow credential stuffing botnets. When combined with TLS fingerprinting and request-header analysis, temporal machine learning models can isolate slow, distributed attacks without triggering false alarms.

## R.7: Eliminating Credential Stuffing Attack Surfaces: A Comparative Analysis of OAuth 2.0 and Password-Based Authentication

**Citation:**
Harsh Kumar, Isha Singh, Aakanksha Singh, Vishal Tiwari and Isha Sharma, *Eliminating Credential Stuffing Attack Surfaces: A Comparative Analysis of OAuth 2.0 and Password-Based Authentication*, place missing, SSRN preprint, 2025.

**Detailed Main Point:**
This study compares traditional password-based authentication with OAuth 2.0 federated identity during a simulated credential stuffing attack. Using compromised credential lists, the authors showed that OAuth 2.0 provides 100% attack mitigation by architecturally eliminating the credential verification attack surface. Traditional authentication, even when following OWASP best practices, remains a vulnerable "password verification oracle" because it must evaluate every login attempt. The authors conclude that delegating authentication to Identity Providers is safer than hardening local authentication endpoints.

**Relevance to Thesis:**
This paper acts as an architectural counterpoint. It shows the fundamental flaw in traditional authentication: the "password verification oracle" problem that low-and-slow botnets exploit by testing reused passwords. The thesis can use this research to acknowledge that architectural elimination via OAuth 2.0 is the best defense, but not always feasible for legacy systems. For systems that keep traditional login endpoints, an adaptive machine learning defense using TLS fingerprinting and request-header analysis bridges the gap left by local password verification.

## R.8: Adversarial Explainability: Utilizing Explainable Machine Learning in Bypassing IoT Botnet Detection Systems

**Citation:**
Mohammed M. Alani, Atefeh Mashatan and Ali Miri, *Adversarial Explainability: Utilizing Explainable Machine Learning in Bypassing IoT Botnet Detection Systems*, Toronto, IEEE Computer Society, 2023.

**Detailed Main Point:**
The authors introduce "Adversarial Explainability," an attack method where adversaries use Explainable AI (XAI) techniques like SHAP to reverse-engineer and evade machine learning botnet detectors. By calculating SHAP values, an attacker finds the single feature—such as packet frame length—that most influences the model's prediction. The attacker then applies a minimal perturbation, changing only that feature, to bypass detection. In tests against an IoT botnet detection system, this single-feature manipulation achieved a 100% evasion success rate against a classifier that previously had 99% accuracy.

**Relevance to Thesis:**
This research introduces adversarial machine learning, a critical counter-measure the thesis must address. If an AI-driven botnet infers feature importance by probing an API Gateway, it can craft minimal perturbations to bypass the ML model. The thesis should argue that the proposed adaptive defense must focus on hard-to-forge cryptographic artifacts like TLS fingerprints, rather than easily spoofed metadata. It must also incorporate adversarial training to resist botnets that try to reverse-engineer the gateway's ML baselines.

## R.9: Modeling and Analyzing Attacker Behavior in IoT Botnet using Temporal Convolution Network (TCN)

**Citation:**
Farhan Sadique and Shamik Sengupta, *Modeling and Analyzing Attacker Behavior in IoT Botnet using Temporal Convolution Network (TCN)*, place missing, arXiv preprint arXiv:2108.12479v1, 2021.

**Detailed Main Point:**
The authors propose a method to model and predict IoT botnet behavior by analyzing threat data from honeypots. Instead of looking only at network traffic anomalies, their model integrates sequential events, including SSH logins, shell command chains, file downloads, and network traffic. The authors used a Temporal Convolutional Network (TCN) to process these sequences. The TCN captured long-term dependencies in the attacker's actions and predicted subsequent moves with 85% to 97% accuracy. It outperformed Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) models on the same task.

**Relevance to Thesis:**
This paper supports the need for advanced sequential analysis in botnet detection. "Low-and-slow" credential stuffing attacks are sparse sequences of events spread across time and multiple IP addresses. The thesis can use this research to validate temporal machine learning architectures, like TCNs, in the API Gateway's adaptive learning system. By treating TLS fingerprints and request-header data as a time-series sequence, the system can extract temporal patterns to update its baselines. This allows it to predict and isolate distributed authentication attacks even when their volume remains below rate-limiting thresholds.

## R.10: Botnet Detection on CTU-13 Using Lightweight Machine Learning Models

**Citation:**
Subhash Gurappa, Yashas Hariprasad, Sundararaj Sitharama Iyengar and Naveen Kumar Chaudhary, *Botnet Detection on CTU-13 Using Lightweight Machine Learning Models*, place missing, arXiv preprint arXiv:2605.23004v2, 2026.

**Detailed Main Point:**
The authors evaluate lightweight machine learning models—Logistic Regression, Decision Trees, and Random Forests—for botnet detection on the CTU-13 dataset. They extracted flow-based network features, such as bytes-per-packet ratios. A Random Forest classifier achieved a ROC-AUC of 0.97 and a PR-AUC of about 0.54 while training 90% faster than complex deep learning architectures like CNNs. These lightweight models also offer clear interpretability through feature importance scoring, letting analysts trace the exact rules that triggered a botnet classification.

**Relevance to Thesis:**
This paper covers the trade-off between computational efficiency, explainability, and detection accuracy. Deep learning models excel at recognizing patterns in "low-and-slow" attacks but are resource-intensive and hard to interpret. The thesis can use this research to propose a hybrid adaptive learning system at the API Gateway. Lightweight, interpretable machine learning models like Random Forests can run at the edge for rapid triage of incoming telemetry. More complex deep learning models can handle long-term sequential baselines to stop low-frequency credential stuffing.

## R.11: Automating Botnet Detection with Graph Neural Networks

**Citation:**
Jiawei Zhou, Zhiying Xu, Alexander M. Rush and Minlan Yu, *Automating Botnet Detection with Graph Neural Networks*, Austin, AutoML for Networking and Systems Workshop of MLSys, 2020.

**Detailed Main Point:**
The authors use Graph Neural Networks (GNNs) to automate the detection of centralized and decentralized botnets by analyzing their communication topologies. Traditional methods require manually engineered heuristics or predefined signatures. The authors' GNN approach uses non-attributed communication graphs and deep message-passing layers to learn the topological properties of botnet traffic within background Internet data. Experiments show that GNNs achieve higher detection rates and lower false-positive rates than non-learning algorithms like BotGrep.

**Relevance to Thesis:**
This paper provides a structural approach to botnet detection that complements the thesis's temporal and cryptographic methods. "Low-and-slow" botnets use a distributed network of IP addresses to evade volume thresholds. By modeling API login requests as a communication graph, an adaptive defense system could use GNNs to identify the botnet's topology. The thesis can cite this research to argue that combining spatial analysis via GNNs with TLS fingerprinting and temporal modeling creates a comprehensive defense against distributed credential stuffing attacks.

## R.12: Comprehensive Survey on Adversarial Examples in Cybersecurity: Impacts, Challenges, and Mitigation Strategies

**Citation:**
Li Li, *Comprehensive Survey on Adversarial Examples in Cybersecurity: Impacts, Challenges, and Mitigation Strategies*, place missing, arXiv preprint arXiv:2412.12217v1, 2024.

**Detailed Main Point:**
This survey covers the threat that Adversarial Examples (AE)—subtle perturbations to input data—pose to deep learning models in cybersecurity. Attackers use techniques like Generative Adversarial Networks or Jacobian Saliency Maps to alter traffic features, such as packet size or domain names, to deceive classifiers while keeping the attack functional. The paper reviews mitigation strategies, emphasizing that deep learning defenses must use adversarial training, gradient masking, and feature compression to remain resilient against AI-driven evasion.

**Relevance to Thesis:**
This paper highlights the vulnerability of machine learning models to adversarial manipulation. If a low-and-slow botnet uses AI to alter its request headers or TLS properties, it could blend into the learned "benign" baseline and bypass the defense. The thesis can use this survey to argue that the adaptive learning algorithm must dynamically track behavioral baselines while proactively incorporating adversarial training and robust feature selection. It must rely on hard-to-spoof cryptographic artifacts to withstand adversarial evasion.

## R.13: Mobile Botnet Detection: A Deep Learning Approach Using Convolutional Neural Networks

**Citation:**
Suleiman Y. Yerima and Mohammed K. Alzaylaee, *Mobile Botnet Detection: A Deep Learning Approach Using Convolutional Neural Networks*, place missing, International Conference on Cyber Security and Protection of Digital Services, 2020.

**Detailed Main Point:**
The authors use a One-Dimensional Convolutional Neural Network (1D CNN) to detect Android mobile botnets. They extracted 342 static features—such as API calls, permissions, and commands—from applications in the ISCX botnet dataset. The 1D CNN acted as an automated feature extractor to identify nonlinear patterns of malicious behavior without manual feature selection. It achieved 98.9% accuracy and an F1-score of 0.981, outperforming traditional classifiers like Support Vector Machines, Random Forests, and Artificial Neural Networks.

**Relevance to Thesis:**
While this research focuses on static mobile malware analysis, the underlying principle supports the thesis: deep learning models can automatically extract complex patterns from high-dimensional data where traditional methods fail. Just as the 1D CNN identified mobile botnets by learning from static app features, the proposed API Gateway must use deep learning to process high-dimensional network telemetry, like TLS fingerprints and HTTP headers. To combat evolving botnets, security systems must move from rigid rules to self-learning, feature-extracting neural networks.

## R.14: IoT Botnet Detection Using an Economic Deep Learning Model

**Citation:**
Nelly Elsayed, Zag ElSayed and Magdy Bayoumi, *IoT Botnet Detection Using an Economic Deep Learning Model*, place missing, IEEE World AI IoT Congress (AIIoT), 2023.

**Detailed Main Point:**
The authors propose a lightweight deep learning architecture for detecting botnet attacks on resource-constrained IoT devices. Because traditional deep learning models are too computationally expensive for real-time edge deployment, they built a hybrid model combining a 1D Convolutional Neural Network for spatial feature extraction with a Gated Recurrent Unit for temporal sequence learning. Using global average pooling, they reduced the trainable parameters to 4,370. Tested on the UNSW 2018 IoT Botnet Dataset, the model achieved 99.75% accuracy and reduced the computational budget by 76% compared to other state-of-the-art models.

**Relevance to Thesis:**
This paper offers an operational solution for the thesis's defense mechanism. Deploying deep learning models on an API Gateway to analyze TLS fingerprints and request-header streams in real time poses latency and resource challenges. The thesis can use this research to propose that the adaptive defense algorithm should utilize optimized hybrid architectures. The API Gateway can perform complex temporal anomaly detection to stop credential stuffing without degrading the authentication endpoint's performance.

## R.15: PASSREFINDER-FL: Privacy-Preserving Credential Stuffing Risk Prediction via Graph-Based Federated Learning

**Citation:**
Jaehan Kim, Minkyoo Song, Minjae Seo, Youngjin Jin, Seungwon Shin and Jinwoo Kim, *PASSREFINDER-FL: Privacy-Preserving Credential Stuffing Risk Prediction via Graph-Based Federated Learning for Representing Password Reuse between Websites*, place missing, arXiv preprint arXiv:2510.16083v1, 2025.

**Detailed Main Point:**
The authors propose `PASSREFINDER-FL`, a framework that predicts credential stuffing risks by estimating the likelihood of password reuse across different websites. Because sharing user credentials between website administrators causes privacy and regulatory problems, the authors model password reuse relationships as edges in a website graph. They use Graph Neural Networks for link prediction to find high-risk reuse relationships, and Federated Learning so administrators exchange only model gradients, not raw user data. Tested on a dataset of 360 million breached accounts, the system achieved an F1-score of 0.9153. This lets administrators quantify credential stuffing risks and enforce security measures, like two-factor authentication, without compromising privacy.

**Relevance to Thesis:**
This paper provides a predictive complement to the thesis's real-time defense. While the thesis focuses on an adaptive machine learning mechanism at the API Gateway to throttle credential stuffing botnets, `PASSREFINDER-FL` addresses the root cause: password reuse. The thesis can integrate this research to advocate for a multi-layered security architecture. A defense should use privacy-preserving federated graph models to assess systemic password reuse risk, while relying on the adaptive ML gateway algorithm to stop the botnets exploiting those vulnerabilities.
