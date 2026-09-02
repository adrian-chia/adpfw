# 1. Overview

Attackers today have shifted from high volume attacks to distributed, AI driven botnets that run "low-and-slow" credential stuffing campaigns. These botnets rotate through thousands of IP addresses to test stolen authentication credentials at low rates, often making just one attempt per minute per IP. This technique bypasses traditional rate limiting and network perimeter defences. Traditional cloud administration tools and API Gateways rely on static signatures and volume thresholds, so they are unable to detect these low-frequency attacks.

Organizations need to move to adaptive, machine learning based systems that continuously update their behavioural baselines to distinguish legitimate users from botnets. This requires data pipelines that capture real time HTTP request headers and cryptographic TLS fingerprints. By aggregating this telemetry at the campaign level, data science models can learn normal human traffic patterns. This allows dynamic throttling algorithms to isolate and neutralize botnet activity without locking out legitimate users.

# 2. Problem statement

Standard API Gateway rate limits miss "low-and-slow" credential stuffing attacks because attackers use distributed botnets that constantly rotate IP addresses. By keeping login attempts below predefined thresholds, attackers bypass conventional network defences and rigid edge security configurations. There is a need for advanced data analytics to analyse the massive telemetry generated at API login endpoints. A solution requires advanced database queries and programmatic feature extraction to find temporal patterns in timestamps, request headers, TLS fingerprints, and authentication failure rates. These patterns allow the system to differentiate legitimate human users from automated botnets.

# 3. Finalized thesis statement

> "Standard API Gateway rate limiting fails against highly distributed, ‘low-and-slow' credential stuffing botnets. This thesis proposes that training machine learning models on a combined telemetry of TLS fingerprints and request header analysis provide a highly accurate, adaptive defence mechanism capable of neutralizing low frequency authentication attacks."

# 4. Research methodology

## 4.1. Data simulation and ingestion pipelines

The research environment will be containerized and deployed on a local machine for controlled, reproducible experimentation. Inside this local deployment, a mock API login endpoint will serve as the target. Python proxy scripts will simulate highly distributed, AI-driven botnets running "low-and-slow" credential stuffing campaigns. The scripts will continuously rotate through thousands of IP addresses and test stolen credentials at suppressed frequencies (for example, a single attempt per minute per IP) to bypass traditional rate limiting.

## 4.2. Feature extraction and telemetry aggregation

The methodology requires database queries and programmatic feature extraction to isolate temporal patterns from sparse log datasets. The engineered data pipelines will capture and aggregate specific real-time telemetry: HTTP request headers, authentication failure rates, and cryptographic TLS fingerprints (specifically JA3 or JA4 hashes).

## 4.3. Algorithmic selection and training

The research evaluates several deep learning architectures that can process time-series data and detect behavioural anomalies:

- Deep Reinforcement Learning (DRL) models actively monitor behavioral telemetry such as failed login attempts and IP switching rates. They continuously update their defensive policies through reward optimization to isolate zero-day anomalies while keeping false-positive rates low.
- Long Short-Term Memory (LSTM) networks are sequence modelling architectures built to capture the temporal dependencies of distributed attacks. By converting network traffic into time-series sequences of request rates, multi-layer LSTMs can detect low-and-slow HTTP attacks.
- Temporal Convolutional Networks (TCNs) model sequential network events to predict complex attacker behaviours. Research shows that TCN models achieve between 85% and 97% prediction accuracy, outperforming both LSTM and Gated Recurrent Unit (GRU) architectures on identical anomaly detection tasks.

## 4.4. Model selection: Temporal Convolutional Networks (TCNs)

TCNs will serve as the selected model for this research methodology. It is selected because it empirically outperforms LSTMs in predicting complex, sequential attacker behaviours. TCNs provide the sequence modelling needed to capture hidden temporal dependencies of highly distributed botnets, and it does so with higher prediction accuracy and without the computationally heavy continuous reward optimization loops that DRL frameworks require.

# 5. Thesis design objective approaches

## 5.1. Real-time telemetry processing and contextual analysis

Evasive bots frequently change application-layer fingerprints (such as User-Agent strings and browser APIs) to mask their activity, so the system must process low-level artifacts in real time. The defence architecture will use a probabilistic approach that combines protocol-level TLS fingerprinting with contextual request header analysis. This dual-layered analysis identifies the underlying source processes and isolates actors who attempt to spoof generic TLS libraries.

## 5.2. Adaptive API throttling mechanism

The primary design objective is to move the API Gateway away from static signatures and rigid volume thresholds. By aggregating the extracted telemetry at the campaign level, the TCN model will learn and establish normal human traffic patterns. This continuous learning approach allows a dynamic throttling algorithm to autonomously isolate and neutralize botnet activity without locking legitimate users out.

## 5.3. Adversarial resilience and evasion mitigation

The self-learning system must withstand Adversarial Examples (AE), a vulnerability where attackers use Explainable Artificial Intelligence (XAI) to reverse-engineer the detection model and apply targeted mathematical perturbations that bypass classifiers. To keep the TCN mechanism resilient against AI-augmented evasion, the design will prioritize cryptographically secure features over easily manipulated metadata. By anchoring the detection model on TLS handshake structures (such as cipher lists and extension orders), the system mitigates evasion tactics like "cipher stunting," because these protocol-level configurations are very difficult for attackers to manipulate at scale.