# Preliminary Literature Review

**R.1**

*   **Title:** *When Handshakes Tell the Truth: Detecting Web Bad Bots via TLS Fingerprints*
*   **Authors:** Ghalia Jarad, Kemal Bicakci
*   **Methodology and Findings:** Automated traffic now exceeds human-generated traffic on the web, and much of it is malicious. Because evasive bots can solve Captchas and mimic human interaction, the authors propose a protocol level detection method using JA4 TLS fingerprinting. They trained two gradient boosted classifiers (XGBoost and CatBoost) on the JA4DB dataset. The CatBoost model achieved an AUC of 0.998, an F1 score of 0.9734, and 0.9863 accuracy on the test set, with XGBoost performing similarly. The JA4 components ja4_b, cipher_count, and ext_count were the most predictive features. The authors plan to extend this method to HTTP/3 and incorporate additional device-fingerprinting features to evaluate resistance to advanced evasion tactics.
*   **Link:** http://arxiv.org/abs/2602.09606v1
*   **Link to Article:** [PDF](/finalizing/papers/R.1_When_Handshakes_Tell_the_Truth_Detecting_Web_Bad_Bots_via_TLS_Fingerprints.pdf)

**R.2**

*   **Title:** *FP-Inconsistent: Measurement and Analysis of Fingerprint Inconsistencies in Evasive Bot Traffic*
*   **Authors:** Hari Venugopalan, Shaoor Munir, Shuaib Ahmed, Tangbaihe Wang, Samuel T. King, Zubair Shafiq
*   **Methodology and Findings:** Bots increasingly alter their browser fingerprints to evade detection. To evaluate this tactic, the authors deployed a honey site running two anti-bot services (DataDome and BotD) and gathered half a million requests from 20 bot services selling "undetectable traffic." These bots evaded DataDome 52.93% of the time and BotD 44.56% of the time. Comparing fingerprints of successful bots showed that they alter different attributes to bypass each service. However, the bots often fail to keep these attributes consistent over time or across related fields. The authors developed data-driven rules to detect these spatial and temporal inconsistencies, which reduced the evasion rates against DataDome and BotD by 48.11% and 44.95%.
*   **Link:** http://arxiv.org/abs/2406.07647v3
*   **Link to Article:** [PDF](/finalizing/papers/R.2_FP-Inconsistent_Measurement_and_Analysis_of_Fingerprint_Inconsistencies_in_Evasive_Bot_Traffic.pdf)

**R.3**

*   **Title:** *Positional-Unigram Byte Models for Generalized TLS Fingerprinting*
*   **Authors:** Hector A. Valdez, Sean McPherson
*   **Methodology and Findings:** The authors present a TLS fingerprinting method based on positional unigram byte models and maximum likelihood estimation. It models TLS client hello traffic for specific client applications. When fingerprinting a connection, the system calculates the likelihood against its models and selects the application that maximizes this function. This data driven approach avoids side-channel information and supports on the fly updates. Testing on an internal dataset showed the method is robust to cipher stunting, maintaining an unbiased F1 score even as synthetic randomization increased.
*   **Link:** http://arxiv.org/abs/2405.07848v1
*   **Link to Article:** [PDF](/finalizing/papers/R.3_Positional-Unigram_Byte_Models_for_Generalized_TLS_Fingerprinting.pdf)

**R.4**

*   **Title:** *Accurate TLS Fingerprinting using Destination Context and Knowledge Bases*
*   **Authors:** Blake Anderson, David McGrew
*   **Methodology and Findings:** Network fingerprinting relies on identifying applications from traffic, but TLS encryption prevents methods based on clear text data. While existing TLS techniques extract a fingerprint string from the client_hello message, hundreds of processes can produce the same string. To fix this, the authors built a system that adds destination context specifically the destination address, port, and server name to the fingerprint. By using a weighted naive Bayes classifier, this destination context disambiguates the processes and improves fingerprinting performance.
*   **Link:** http://arxiv.org/abs/2009.01939v1
*   **Link to Article:** [PDF](/finalizing/papers/R.4_Accurate_TLS_Fingerprinting_using_Destination_Context_and_Knowledge_Bases.pdf)

**R.5**

*   **Title:** *Adaptive Anomaly Detection Algorithm for Real-Time Identification of Phishing and Credential Stuffing Attacks in E-Learning Systems Using Deep Reinforcement Learning*
*   **Authors:** Nilufar Madaminova, Akram Maxammatov, Svetlana Sadchikova, Gulbakhor Altibaeva, Mahzuna Hamdamova, Zokir Alimov, Sadoqat Jurayeva
*   **Methodology and Findings:** E-learning platforms and cloud-based LMS face a growing risk of phishing and credential stuffing attacks targeting user authentication. Traditional intrusion detection and static machine learning struggle to adapt to dynamic attack patterns, often generating high false positive rates. The authors propose an Adaptive Anomaly Detection Algorithm using Deep Reinforcement Learning (DRL) to identify these attacks in real time. The algorithm monitors behavioral features like failed login attempts, IP change rates, session lengths, URL reputation, and device mismatch. Tested on a dataset of 125,000 instances containing both malicious and legitimate actions, the DRL model achieved 98.4% accuracy, 98.1% precision, 97.8% recall, and an F1-score of 97.9%, with a 1.9% false positive rate. This outperformed SVM, Random Forest, CNN, and LSTM models on the same data.
*   **Link:** https://doi.org/10.58346/jisis.2026.i2.013
*   **Link to Article:** [PDF](/finalizing/papers/R.5_Adaptive_Anomaly_Detection_Algorithm.pdf)

**R.6**

*   **Title:** *HTTP Low and Slow DoS Attack Detection using LSTM based deep learning*
*   **Authors:** Bronjon Gogoi, Tasiruddin Ahmed
*   **Methodology and Findings:** The authors built a multi-layer LSTM network to detect HTTP low and slow DoS attacks. They combined the CIC DoS (2017) dataset with synthetic attack data to increase training volume. After extracting timestamps and IP addresses from PCAP files to separate attack traces from benign traffic, they converted the traffic into time series sequences of request rates. The resulting LSTM model achieved an accuracy and AUC of 0.99, with false positive and false negative rates around 0.01. The model's loss curves show proper convergence without significant overfitting.
*   **Link:** https://doi.org/10.1109/indicon56171.2022.10039772
*   **Link to Article:** [PDF](/finalizing/papers/R.6_HTTP_Low_and_Slow_DoS_Attack_Detection.pdf)

**R.7**

*   **Title:** *Eliminating Credential Stuffing Attack Surfaces: A Comparative Analysis of OAuth 2.0 and Password-Based Authentication*
*   **Authors:** Harsh Kumar, Isha Singh, Aakanksha Singh, Vishal Tiwari, Isha Sharma.
*   **Methodology and Findings:** Credential stuffing attacks account for 24% of global security breaches. While rate limiting and challenge response systems harden traditional password based authentication, they do not eliminate the risk. This study compared the resilience of traditional authentication against OAuth 2.0 federated identity during a credential stuffing attack. The authors set up a testbed with both endpoints and tested 101 compromised credential pairs. Traditional authentication blocked 100 out of 101 attempts. OAuth 2.0 blocked all 101 attempts because its delegated architecture removes the credential submission surface entirely. OAuth 2.0 also returned responses 2.27% faster, contradicting assumptions about delegation overhead.
*   **Link:** https://doi.org/10.2139/ssrn.6576013
*   **Link to Article:** [PDF](/finalizing/papers/R.7_Eliminating_Credential_Stuffing_Attack_Surfaces.pdf)

**R.8**

*   **Title:** *Adversarial Explainability: Utilizing Explainable Machine Learning in Bypassing IoT Botnet Detection Systems*
*   **Authors:** Mohammed M. Alani, Atefeh Mashatan, Ali Miri
*   **Methodology and Findings:** Adversarial attacks pose a growing threat to machine learning botnet detection systems. The authors introduce a blackbox attack that uses the detection model's explainability output to build adversarial samples. By testing this technique on a trained IoT botnet detection system, the authors bypassed detection completely (0% detection rate) while altering only a single feature to generate the adversarial samples.
*   **Link:** http://arxiv.org/abs/2310.00070v1
*   **Link to Article:** [PDF](/finalizing/papers/R.8_Adversarial_Explainability_Utilizing_Explainable_Machine_Learning_in_Bypassing_IoT_Botnet_Detection_.pdf)

**R.9**

*   **Title:** *Modeling and Analyzing Attacker Behavior in IoT Botnet using Temporal Convolution Network (TCN)*
*   **Authors:** Farhan Sadique, Shamik Sengupta
*   **Methodology and Findings:** Reactive blacklisting struggles against evolving botnets, and previous behavioral analysis has mostly focused on network traffic anomalies. The authors expanded this by analyzing a combination of network traffic, file downloads, SSH logins, and command chains typed by attackers. They gathered this data from several honeypots simulating Linux shells. Using a Temporal Convolutional Network (TCN), they modeled these events to predict attacker behavior. The TCN achieved an 85–97% prediction accuracy and outperformed Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) models on the same task. The authors also automated data collection and analysis using the CYbersecurity information Exchange (CYBEX).
*   **Link:** http://arxiv.org/abs/2108.12479v1
*   **Link to Article:** [PDF](/finalizing/papers/R.9_Modeling_and_Analyzing_Attacker_Behavior_in_IoT_Botnet_using_Temporal_Convolution_Network_(TCN).pdf)

**R.10**

*   **Title:** *Botnet Detection on CTU-13 Using Lightweight Machine Learning Models*
*   **Authors:** Subhash Gurappa, Yashas Hariprasad, Sundararaj Sitharama Iyengar, Naveen Kumar Chaudhary
*   **Methodology and Findings:** Deep learning models for botnet detection are often computationally intensive and hard to interpret. To test simpler alternatives, the authors compared Logistic Regression, Decision Tree, and Random Forest models on the CTU-13 dataset. They extracted flow-based features and evaluated detection accuracy, precision, recall, F1 score, and feature importance. The Random Forest model achieved a PR-AUC of 0.54 and a ROC-AUC of 0.97 while training 90% faster than existing CNN baselines. The study shows that lightweight models can perform competitively against deep learning under natural class imbalance, with lower computational costs and clearer forensic interpretability.
*   **Link:** http://arxiv.org/abs/2605.23004v2
*   **Link to Article:** [PDF](/finalizing/papers/R.10_Botnet_Detection_on_CTU-13_Using_Lightweight_Machine_Learning_Models.pdf)

**R.11**

*   **Title:** *Automating Botnet Detection with Graph Neural Networks*
*   **Authors:** Jiawei Zhou, Zhiying Xu, Alexander M. Rush, Minlan Yu
*   **Methodology and Findings:** Most traditional botnet detection relies on heuristic, multi-stage criteria. The authors explored whether deep learning can automatically learn detection policies. They synthesized botnet connections with various communication patterns overlaid on real network data for training. They designed graph neural networks (GNNs) specifically to identify the hierarchical structure of centralized botnets and the fast-mixing structure of decentralized botnets. When trained appropriately, GNNs captured botnet topologies better than existing non-learning methods, with deeper GNNs proving necessary for complex topologies.
*   **Link:** http://arxiv.org/abs/2003.06344v1
*   **Link to Article:** [PDF](/finalizing/papers/R.11_Automating_Botnet_Detection_with_Graph_Neural_Networks.pdf)

**R.12**

*   **Title:** *Comprehensive Survey on Adversarial Examples in Cybersecurity: Impacts, Challenges, and Mitigation Strategies*
*   **Authors:** Li Li
*   **Methodology and Findings:** Adversarial examples (AE) can deceive deep learning models through subtle perturbations, causing misclassification and system vulnerabilities in cybersecurity tools. This paper reviews how AE attacks affect malware detection, botnet identification, intrusion detection, user authentication, and encrypted traffic analysis. It covers methods for generating adversarial examples, their domain specific effects, and the trade-offs attackers face between efficacy and resource costs. It also reviews recent defenses such as gradient masking, adversarial training, and detection techniques that aim to improve model resilience.
*   **Link:** http://arxiv.org/abs/2412.12217v1
*   **Link to Article:** [PDF](/finalizing/papers/R.12_Comprehensive_Survey_on_Adversarial_Examples_in_Cybersecurity_Impacts,_Challenges,_and_Mitigation_St.pdf)

**R.13**

*   **Title:** *Mobile Botnet Detection: A Deep Learning Approach Using Convolutional Neural Networks*
*   **Authors:** Suleiman Y. Yerima, Mohammed K. Alzaylaee
*   **Methodology and Findings:** The authors propose a Convolutional Neural Network (CNN) model for detecting botnets on Android devices. They trained the CNN on 342 static application features to separate botnet apps from benign apps. Evaluating the model on 6,802 applications from the ISCX botnet dataset (which included 1,929 botnets) showed that the CNN achieved higher prediction accuracy than standard machine learning classifiers tested on the same data. The model also outperformed accuracy scores reported in previous studies on machine learning for Android botnet detection.
*   **Link:** http://arxiv.org/abs/2007.00263v1
*   **Link to Article:** [PDF](/finalizing/papers/R.13_Mobile_Botnet_Detection_A_Deep_Learning_Approach_Using_Convolutional_Neural_Networks.pdf)

**R.14**

*   **Title:** *IoT Botnet Detection Using an Economic Deep Learning Model*
*   **Authors:** Nelly Elsayed, Zag ElSayed, Magdy Bayoumi
*   **Methodology and Findings:** Intrusion detection systems for the Internet of Things (IoT) must account for the computing and bandwidth limits of IoT devices. The authors proposed a resource efficient deep learning model to detect IoT botnets and other network attacks. Compared to existing state of the art detection models, their approach achieved higher accuracy while requiring a smaller implementation budget and reducing both training and detection times.
*   **Link:** http://arxiv.org/abs/2302.02013v4
*   **Link to Article:** [PDF](/finalizing/papers/R.14_IoT_Botnet_Detection_Using_an_Economic_Deep_Learning_Model.pdf)

**R.15**

*   **Title:** *PassREfinder-FL: Privacy-Preserving Credential Stuffing Risk Prediction via Graph-Based Federated Learning for Representing Password Reuse between Websites*
*   **Authors:** Jaehan Kim, Minkyoo Song, Minjae Seo, Youngjin Jin, Seungwon Shin, Jinwoo Kim
*   **Methodology and Findings:** Existing methods to detect password reuse often limit usability or rely on complex account-sharing mechanisms. The authors propose PassREfinder-FL, a framework that predicts credential stuffing risks by representing password reuse likelihood as edges in a website graph. It uses graph neural networks (GNNs) for link prediction to assess reuse risk between sites, scaling to new websites by linking them as nodes based on public information. To maintain privacy without sharing sensitive user data between site administrators, the framework uses federated learning (FL). The authors evaluated PassREfinder-FL on a dataset of 360 million breached accounts across 22,378 websites, achieving an F1-score of 0.9153 in the FL setting. In an ablation study, their FL-based GNN outperformed other state-of-the-art GNN models by 4–11%. The output risk scores can be used to quantify password reuse likelihood directly.
*   **Link:** http://arxiv.org/abs/2510.16083v1
*   **Link to Article:** [PDF](/finalizing/papers/R.15_PassREfinder-FL_Privacy-Preserving_Credential_Stuffing.pdf)
