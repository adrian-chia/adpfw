# 5. Brief Literature Review

## The Rise of Evasive and "Low-and-Slow" Botnets

Attackers often use automated credential stuffing to exploit password reuse across different platforms[^1]. In these attacks, traditional authentication serves as a «password verification oracle» that adversaries query iteratively, bypassing static defenses even when cryptographic best practices are in place[^2]. To avoid network defenses and API Gateway rate limits, attackers use distributed botnets for "low-and-slow" attacks. These botnets rotate through thousands of IP addresses and keep request rates low to mimic legitimate traffic and evade threshold based detection[^3]. Evasive bots also alter application layer fingerprints, such as 'User-Agent' strings and browser APIs, to hide their activity. These changes often create spatial and temporal inconsistencies that static rules miss[^4].

## TLS Fingerprinting and Contextual Telemetry

Because attackers easily spoof higher layer attributes, researchers now examine protocol level artifacts. The cryptographic configurations of a TLS handshake, including cipher lists and extension orders, are difficult to manipulate at scale. This makes TLS fingerprinting a reliable, privacy preserving way to separate automated scripts from human users[^5]. However, traditional hash-based methods like JA3 remain vulnerable to «cipher stunting», a technique where attackers randomize cipher suite lists to generate unknown hashes and bypass blocklists[^6]. To improve accuracy and reduce false positives, defenses must combine TLS fingerprinting with contextual telemetry like request header analysis. This probabilistic approach identifies the source processes and isolates actors who spoof generic TLS libraries[^7].

## Adaptive Deep Learning Defenses

"Low-and-slow" attacks require adaptive defenses instead of static signatures. Deep Reinforcement Learning (DRL) models monitor behavioral telemetry, such as failed login attempts and IP switching rates, and update their policies through reward optimization. This approach isolates zero day anomalies with few false positives[^8]. Because low frequency attacks unfold over time, sequence modeling architectures like Long Short-Term Memory (LSTM) networks[^3] and Temporal Convolutional Networks (TCNs)[^9] can capture the temporal dependencies of distributed botnets.

Deep learning architectures like One-Dimensional Convolutional Neural Networks (1D CNNs) automate feature extraction, identifying nonlinear patterns of malicious behavior without manual selection[^10]. To run these models on API Gateways in real time, researchers use hybrid architectures, combining 1D CNNs with Gated Recurrent Units to reduce computational costs while maintaining accuracy[^11]. Graph Neural Networks (GNNs) offer a structural method, analyzing relationships in communication graphs to isolate the topology of decentralized botnets[^12]. If an environment needs auditable rules, lightweight models like Random Forests provide interpretable rapid triage before applying deep learning[^13].

## Adversarial Machine Learning Vulnerabilities

Deep learning improves botnet detection but introduces vulnerabilities through Adversarial Examples (AE)[^14]. Attackers use Explainable Artificial Intelligence (XAI) techniques to reverse engineer detection models. They identify the features that influence a model's prediction and apply targeted perturbations, such as altering a packet frame length, to bypass classifiers[^15]. An adaptive API Gateway defense must account for these tactics. The defense should prioritize cryptographically secure features, like TLS handshake structures, over simple metadata. It also requires adversarial training to keep the self-learning mechanism resilient against AI augmented evasion.

---

## Footnotes

[^1]: Jaehan Kim, Minkyoo Song, Minjae Seo, Youngjin Jin, Seungwon Shin and Jinwoo Kim, *PASSREFINDER-FL: Privacy-Preserving Credential Stuffing Risk Prediction via Graph-Based Federated Learning for Representing Password Reuse between Websites*, place missing, 2025, http://arxiv.org/abs/2510.16083v1, il August 26, 2026.

[^2]: Harsh Kumar, Isha Singh, Aakanksha Singh, Vishal Tiwari and Isha Sharma, *Eliminating Credential Stuffing Attack Surfaces: A Comparative Analysis of OAuth 2.0 and Password-Based Authentication*, place missing, 2025, https://doi.org/10.2139/ssrn.6576013, il August 26, 2026.

[^3]: Bronjon Gogoi and Tasiruddin Ahmed, *HTTP Low and Slow DoS Attack Detection using LSTM based deep learning*, Guwahati, 2022, https://doi.org/10.1109/indicon56171.2022.10039772, il August 26, 2026.

[^4]: Hari Venugopalan, Shaoor Munir, Shuaib Ahmed, Tangbaihe Wang, Samuel T. King and Zubair Shafiq, *FP-Inconsistent: Measurement and Analysis of Fingerprint Inconsistencies in Evasive Bot Traffic*, place missing, 2025, http://arxiv.org/abs/2406.07647v3, il August 26, 2026.

[^5]: Ghalia Jarad and Kemal Bıçakcı, *When Handshakes Tell the Truth: Detecting Web Bad Bots via TLS Fingerprints*, place missing, 2026, http://arxiv.org/abs/2602.09606v1, il August 26, 2026.

[^6]: Hector A. Valdez and Sean McPherson, *Positional-Unigram Byte Models for Generalized TLS Fingerprinting*, place missing, 2024, http://arxiv.org/abs/2405.07848v1, il August 26, 2026.

[^7]: Blake Anderson and David McGrew, *Accurate TLS Fingerprinting using Destination Context and Knowledge Bases*, place missing, 2020, http://arxiv.org/abs/2009.01939v1, il August 26, 2026.

[^8]: Nilufar Madaminova, Akram Maxammatov, Svetlana Sadchikova, Gulbakhor Altibaeva, Mahzuna Hamdamova, Zokir Alimov and Sadoqat Jurayeva, *Adaptive Anomaly Detection Algorithm for Real-Time Identification of Phishing and Credential Stuffing Attacks in E-Learning Systems Using Deep Reinforcement Learning*, Tashkent, 2026, https://doi.org/10.58346/jisis.2026.i2.013, il August 26, 2026.

[^9]: Farhan Sadique and Shamik Sengupta, *Modeling and Analyzing Attacker Behavior in IoT Botnet using Temporal Convolution Network (TCN)*, place missing, 2021, http://arxiv.org/abs/2108.12479v1, il August 26, 2026.

[^10]: Suleiman Y. Yerima and Mohammed K. Alzaylaee, *Mobile Botnet Detection: A Deep Learning Approach Using Convolutional Neural Networks*, place missing, 2020, http://arxiv.org/abs/2007.00263v1, il August 26, 2026.

[^11]: Nelly Elsayed, Zag ElSayed and Magdy Bayoumi, *IoT Botnet Detection Using an Economic Deep Learning Model*, place missing, 2023, http://arxiv.org/abs/2302.02013v4, il August 26, 2026.

[^12]: Jiawei Zhou, Zhiying Xu, Alexander M. Rush and Minlan Yu, *Automating Botnet Detection with Graph Neural Networks*, Austin, 2020, http://arxiv.org/abs/2003.06344v1, il August 26, 2026.

[^13]: Subhash Gurappa, Yashas Hariprasad, Sundararaj Sitharama Iyengar and Naveen Kumar Chaudhary, *Botnet Detection on CTU-13 Using Lightweight Machine Learning Models*, place missing, 2026, http://arxiv.org/abs/2605.23004v2, il August 26, 2026.

[^14]: Li Li, *Comprehensive Survey on Adversarial Examples in Cybersecurity: Impacts, Challenges, and Mitigation Strategies*, place missing, 2024, http://arxiv.org/abs/2412.12217v1, il August 26, 2026.

[^15]: Mohammed M. Alani, Atefeh Mashatan and Ali Miri, *Adversarial Explainability: Utilizing Explainable Machine Learning in Bypassing IoT Botnet Detection Systems*, Toronto, 2023, http://arxiv.org/abs/2310.00070v1, il August 26, 2026.
