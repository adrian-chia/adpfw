## 15. Self-learning systems

### Overview

In this topic, the main research contribution is an **adaptive learning system** that recognizes low-and-slow bot behavior from streaming login telemetry and dynamically adjusts API-gateway controls.

The system learns a behavioral profile from authentication events rather than relying on a fixed rule such as:

$$
\text{Block if requests per IP} > N
$$

That conventional rule fails when attackers distribute one attempt per minute across thousands of proxy IP addresses. The relevant unit of analysis becomes the **behavioral entity**, not merely the IP address.

A self-learning detector can use aggregated, privacy-aware features across several levels:


| Level | Example signals |
| :-- | :-- |
| Request | Timestamp, HTTP method, endpoint, status code, request size, header order/consistency |
| Network | IP/ASN category, proxy reputation, geo-velocity, IP churn, subnet diversity |
| TLS | JA3/JA4-style fingerprint, TLS version, cipher-suite/extension profile, ALPN |
| Device/client | Cookie/session continuity, device/browser fingerprint, claimed User-Agent versus TLS/HTTP consistency |
| Account | Failed attempts per account, account-target diversity, historical login pattern |
| Campaign | Reuse of TLS/header/device patterns across many IPs, coordinated timing, credential-list traversal pattern |

A risk model could calculate:

$$
R_t=f(F_{\text{IP}},F_{\text{TLS}},F_{\text{headers}},F_{\text{device}},F_{\text{account}},F_{\text{time}})
$$

and select an action:

$$
\operatorname{Action}(R_t)=
\begin{cases}
\text{Allow} & R_t < \tau_1\\
\text{Monitor / delay} & \tau_1 \le R_t < \tau_2\\
\text{Step-up MFA or challenge} & \tau_2 \le R_t < \tau_3\\
\text{Throttle / deny / quarantine} & R_t \ge \tau_3
\end{cases}
$$

This is a **self-learning systems** project because the model must learn evolving bot patterns, update or recalibrate as legitimate traffic changes, and adapt gateway responses based on observed outcomes.

TLS fingerprints are useful because they expose characteristics of a client’s TLS implementation rather than its current network address. JA3 is derived from values in the TLS ClientHello, including protocol version, cipher suites, extensions, supported elliptic curves, and point formats.  However, these fingerprints must be treated as probabilistic evidence rather than unique identity: sophisticated attackers can use real browsers, emulate client stacks, or deliberately mimic common fingerprints.[^3]

### Thesis statements

**Thesis Statement 15.1 — Recommended**

> A streaming self-learning system that fuses TLS fingerprints, HTTP-header consistency, device signals, account-level failure patterns, and cross-IP temporal behavior can detect low-and-slow credential-stuffing campaigns more effectively than static IP-based API rate limiting.

**Thesis Statement 15.2 — Adaptive throttling**

> Reinforcement-learning-based adaptive API throttling can reduce successful low-and-slow credential-stuffing attempts while causing less friction for legitimate users than fixed per-IP thresholds.

**Thesis Statement 15.3 — Feature ablation**

> Combining TLS fingerprinting with device and request-header behavioral features produces higher precision for distributed credential-stuffing detection than IP reputation, request rate, or TLS fingerprinting alone.

**Thesis Statement 15.4 — Resilience to adversarial adaptation**

> A continuously recalibrated bot-detection model with campaign-level aggregation maintains stronger detection performance against IP rotation and slow request pacing than a static supervised classifier trained on historical login logs.

### Literature review

#### Credential stuffing as an automated threat

OWASP characterizes credential stuffing as mass login attempts that test credentials stolen elsewhere to identify valid reused username/password pairs.  OWASP’s API-security guidance treats credential stuffing as an authentication failure and recommends stricter anti-brute-force mechanisms for authentication endpoints than ordinary API rate limits, alongside MFA, CAPTCHA/account lockouts, secure token validation, and protection for recovery endpoints.[^4][^1]

The low-and-slow scenario is a specific evasion form: attackers reduce per-IP request rates and rotate source addresses, so an isolated IP appears benign. This makes cross-event correlation essential.

#### Adaptive and streaming approaches

NIST’s cloud-native API protection guidance explicitly recommends rate limits and account lockouts, MFA, bot detection/CAPTCHAs, breach-credential screening, and **adaptive authentication** that changes controls according to login behavior and risk.  That establishes a standards-supported motivation for a learning-based adaptive gate rather than fixed thresholds.[^2]

Research on streaming anomaly detection emphasizes the difficulty of processing high-volume traffic and logs while detecting novel attacks. It also supports studying incremental detection systems where behavioral baselines shift over time.[^5]

An adaptive-rate-limiting study modeled the gateway decision as a Markov Decision Process and used Q-learning to modify limits based on observed user behavior. It reported improved abuse-detection accuracy and lower legitimate-user friction than fixed models, though the study’s e-commerce setting and publication venue mean its findings should be treated as a design precedent to reproduce rigorously rather than as conclusive banking evidence.[^6]

#### TLS, device, and header fingerprints

TLS fingerprinting gives a signal that is harder to defeat with simple proxy rotation because it reflects the client TLS stack and ClientHello configuration. JA3 derives a fingerprint from the TLS version, ordered cipher suites, extensions, elliptic curves, and EC point formats.  JA4-style research argues that protocol-level TLS features can help distinguish bots from humans; one preprint evaluated XGBoost and CatBoost using a JA4 dataset and reported strong classification metrics, but it also acknowledges limits against bots using full browser automation or accurate TLS mimicry. Since it is a preprint, use it as emerging evidence rather than final proof.[^7][^3]

Recent work on enriched TLS fingerprints also argues that combining TLS and HTTP-header information can improve granularity over TLS-only indicators. Its malicious-domain study used enriched fingerprints and similarity mapping to identify previously unknown malicious domains, supporting your feature-fusion rationale even though the target task differs from credential stuffing.[^8]

#### Research gap

Existing research and guidance support bot detection, TLS fingerprinting, adaptive authentication, and dynamic rate limiting. The clearest gap for your thesis is a reproducible evaluation of whether **campaign-level behavioral aggregation** defeats a deliberately constructed low-and-slow login botnet more effectively than per-IP controls.

Your novel contribution can be:

- A containerized, reproducible login API and gateway testbed.
- Controlled credential-stuffing campaigns using simulated proxy rotation and slow pacing.
- A streaming risk model that links requests through TLS/header/device/account behavior.
- A comparison against fixed per-IP, per-account, per-device, and hybrid rate limits.
- A multi-objective evaluation of security, false positives, user friction, latency, and throughput.

***

## 20. Access control

### Overview

For this research route, access control is not about detecting bots with ML. It is about **controlling what a client may do after authentication**, and using risk-sensitive policies to contain the impact of suspected credential compromise.

Credential stuffing is fundamentally an authentication attack, but a successful login becomes damaging when access control grants broad or poorly constrained permissions. In a bank API, an account-takeover session should not automatically receive unrestricted capability to export all account data, change contact details, add payment beneficiaries, or initiate high-value transfers.

A risk-adaptive access decision can be expressed as:

$$
\operatorname{Permit}(s,a,r,c)
$$

where:

- $s$ is the authenticated subject or session.
- $a$ is the requested action.
- $r$ is the protected resource.
- $c$ is the context: session risk, device history, TLS fingerprint, geolocation, MFA status, velocity, and current threat score.

For low-risk sessions, the usual policy may permit normal read actions. For a suspicious low-and-slow campaign, the policy may require a stronger factor or restrict sensitive operations:

$$
\operatorname{Permit} \iff
\operatorname{Authenticated}
\land
\operatorname{Authorized}
\land
\operatorname{SessionRisk}<\tau
$$

Otherwise, the policy requires **step-up authentication**, applies a temporary restriction, or denies the operation.

This framing makes access control the topic if your thesis focuses on post-login **account-takeover containment**, rather than the initial bot-detection classifier.

### Thesis statements

**Thesis Statement 20.1 — Recommended**

> A risk-adaptive access-control model that incorporates login-session risk derived from device, TLS, and behavioral signals can limit account-takeover impact from low-and-slow credential stuffing more effectively than static role-based access control.

**Thesis Statement 20.2 — Step-up authentication**

> Context-aware step-up authentication for sensitive banking API actions reduces unauthorized account changes and data-export activity following credential-stuffing attacks while preserving routine low-risk user access.

**Thesis Statement 20.3 — Least-privilege containment**

> Fine-grained, operation-level authorization policies reduce the post-compromise blast radius of credential-stuffing attacks more effectively than session-wide access grants after password-only authentication.

**Thesis Statement 20.4 — Policy enforcement**

> A policy decision point that combines identity assurance, session risk, device continuity, and action sensitivity can identify high-risk account-takeover sessions and enforce proportional controls with lower unnecessary challenge rates than uniform MFA enforcement.

### Literature review

#### Credential stuffing and authentication assurance

Credential stuffing reuses stolen username/password combinations, so a successful password check does not prove that the person authenticating is the legitimate account holder. OWASP describes it as automated injection of stolen credentials into login forms to fraudulently gain access to accounts.[^9]

OWASP recommends MFA where possible to mitigate credential stuffing, brute-force activity, and stolen-credential reuse. It also recommends logging failures, alerting on suspected attacks, hardening login and recovery flows against enumeration, and applying increasing delays carefully to avoid creating denial-of-service conditions.[^10]

This literature supports a fundamental premise for access-control research: password verification is an insufficient assurance signal for high-risk financial operations.

#### From RBAC to context-aware authorization

Traditional RBAC grants permissions according to roles: customer, staff member, API client, or administrator. However, two sessions may share the same “customer” role while having very different risk levels:

- A known device with a stable session and normal behavior.
- A fresh session from a new ASN with a new TLS/client fingerprint, unusual timing, and recent authentication failures.

Static RBAC gives both sessions identical privileges. Risk-adaptive access control instead evaluates subject, object, action, and environment. This is closest to ABAC, with dynamic risk attributes added to the policy.

A policy example is:

$$
\begin{aligned}
\operatorname{Allow}(&\text{account\_export}) \iff\\
&\operatorname{ValidSession} \land
\operatorname{MFARecent} \land
\operatorname{DeviceTrusted} \land
\operatorname{RiskScore}<\tau
\end{aligned}
$$

For suspicious sessions, the control can:

- Require MFA or transaction signing.
- Temporarily restrict export endpoints.
- Block beneficiary creation or payment initiation.
- Enforce lower data-export and transaction limits.
- Require a known-device confirmation.
- Terminate or revoke the current session/token.

NIST API protection guidance explicitly recommends adaptive authentication that adjusts controls based on login behavior and risk, together with MFA, bot detection, rate limits, and account lockouts.  This directly supports an adaptive-authorization thesis.[^2]

#### Financial API context

In Open Banking and finance, an identity typically accesses valuable data or payment functions through OAuth-protected APIs. FAPI 2.0 is a high-security API profile based on OAuth 2.0 and is intended for protecting high-security APIs.  The profile provides a protocol-security baseline, but it does not prevent a legitimate but compromised customer credential from being used unless the surrounding identity and risk controls detect and constrain the event.[^11]

Therefore, your research can investigate how adaptive authorization complements FAPI-compliant authentication rather than replacing it.

#### Evaluation gap

Much industry guidance recommends MFA and risk-based controls, but a focused practical study can evaluate the trade-off among:

- Account takeover containment.
- Legitimate-user challenge frequency.
- False-block or false-challenge rate.
- Authentication and API-operation latency.
- API availability under attack.
- Sensitivity to attacker evasion, such as proxy rotation and browser emulation.

A defensible experiment uses a mock banking API with risk-labeled sessions. Compare:

1. Password-only login plus static RBAC.
2. Password plus universal MFA.
3. Static conditional rules.
4. Risk-adaptive access control with step-up authentication.
5. Risk-adaptive control with distinct policies for read, export, profile-change, beneficiary, and payment actions.

This topic is best if you want a security-policy and identity-engineering thesis, with ML used only to produce a risk score.

***

## 19. Web security

### Overview

In this standalone topic, the research focuses on building and evaluating a **defense-in-depth API gateway architecture** for login endpoints exposed to distributed credential stuffing.

Web security here includes the HTTP/TLS API attack surface, reverse proxy/API gateway, WAF/bot-management controls, session handling, authentication flows, logging, observability, and automated mitigations.

The proposed system protects:

```text
Internet → CDN / WAF → API Gateway → Login API → Identity Provider → Banking Services
```

The gateway should not rely on IP rate limiting alone. Instead, it can apply controls at three distinct layers:


| Layer | Example controls |
| :-- | :-- |
| Edge | WAF/CDN, IP/ASN intelligence, TLS/HTTP fingerprints, coarse rate limits, known-bot rules |
| Application | Per-account and per-session limits, failed-login counters, CAPTCHA/attestation, request-header consistency checks |
| Identity/business | MFA, breached-password checks, anomaly scoring, session revocation, account-risk alerts, operation restrictions |

OWASP’s Bot Management and Anti-Automation Cheat Sheet recommends exactly this layered model: edge controls using IP/ASN intelligence and TLS/HTTP fingerprints; application-layer identity/session-aware limits and behavioral signals; and backend/business-layer anomaly detection and fraud scoring. It specifically recommends separate per-username and per-IP limits, logging decisions and signals, and applying sliding-window controls.[^12]

A key scope correction: no single combination of fingerprints “completely neutralizes” low-and-slow credential stuffing. Sophisticated bots can rotate IPs, use residential proxies, automate real browsers, imitate headers, solve or outsource CAPTCHA, or compromise legitimate devices. The defensible goal is to **raise detection probability, reduce successful account takeover, and limit attacker dwell time while preserving legitimate user experience**.

### Thesis statements

**Thesis Statement 19.1 — Recommended**

> A multi-layer API-gateway defense combining per-account controls, TLS and HTTP-client fingerprinting, device continuity signals, and adaptive challenge mechanisms detects and mitigates low-and-slow credential-stuffing campaigns more effectively than fixed per-IP rate limiting.

**Thesis Statement 19.2 — Gateway architecture**

> A cloud-native, telemetry-driven API gateway can reduce successful distributed credential-stuffing attacks by correlating authentication events across IP, TLS, header, device, and account dimensions without exceeding a predefined p95 authentication-latency budget.

**Thesis Statement 19.3 — Comparative control study**

> Per-account and cross-fingerprint rate limits provide greater resistance to distributed low-rate credential stuffing than IP-only limits, while adaptive challenge escalation reduces user friction relative to always-on CAPTCHA or universal MFA.

**Thesis Statement 19.4 — Detection and mitigation**

> Integrating bot-risk scoring with gateway enforcement actions—monitoring, progressive delay, proof-of-work or challenge, MFA, and temporary denial—reduces account-compromise success under distributed botnet conditions more effectively than detection-only alerting.

### Literature review

#### API credential stuffing

OWASP identifies credential stuffing as an automated attack that replays credentials stolen from other services.  It is distinct from brute force: the attacker is not guessing passwords at scale but testing known credential pairs against targets where users may have reused passwords.[^1]

OWASP API guidance identifies APIs as vulnerable when they permit credential stuffing, brute force against an account without anti-automation controls, weak password practices, insecure token handling, or weak token validation. It recommends MFA, dedicated anti-brute-force protections, CAPTCHA/account lockouts, hardened recovery endpoints, and strict token validation.[^4]

Your low-and-slow model directly tests a known limitation of simplistic mitigation: per-IP thresholds are ineffective when attack attempts are intentionally dispersed across many sources.

#### Layered bot mitigation

OWASP recommends distributing anti-automation controls across edge, application, and backend/business layers rather than relying on a single WAF or gateway rule. Its guidance explicitly includes IP reputation, ASN filtering, TLS/HTTP fingerprinting, session-aware limits, behavior signals, MFA, CAPTCHA/attestation, account velocity, fraud scoring, and logging.[^12]

The most relevant design recommendations for your prototype are:

- Enforce distinct limits by IP **and** username/account.
- Use sliding windows rather than a single fixed counter.
- Record failure and decision telemetry.
- Apply increasing delays, challenges, or temporary holds as risk rises.
- Treat password recovery and registration as sensitive authentication-adjacent endpoints.
- Check credentials against breach sources in a privacy-preserving manner.
- Require MFA for suspicious behavior rather than treating a password match as conclusive proof of identity.[^13][^12]

NIST similarly recommends rate limits/account lockouts, MFA, bot detection/CAPTCHAs, adaptive authentication, and compromised-credential screening for cloud-native API protection.[^2]

#### TLS and device fingerprinting

TLS fingerprinting captures low-level ClientHello characteristics that are not changed merely by rotating an IP address. JA3 fingerprints derive from the TLS protocol version, cipher suites, extensions, elliptic curves, and elliptic-curve point formats offered by a client.[^3]

This makes TLS signatures useful for correlation. For instance, 5,000 login attempts from 3,000 IPs may still share only a small set of unusual TLS/header combinations, indicating an automated client family. But it is not a definitive identity mechanism:

- Enterprise proxies can create shared fingerprints among legitimate users.
- Browsers and OS updates change legitimate fingerprints.
- Real-browser automation can resemble normal traffic.
- Attackers can intentionally imitate common TLS configurations.

Therefore, a secure system should never block solely because of a JA3/JA4 value. It should use TLS identity as one weighted input alongside account behavior, client consistency, IP/ASN reputation, failure sequences, and prior session history.

Recent research explores TLS fingerprints for bot classification. A 2026 preprint using JA4-derived features and gradient-boosted classifiers reported high performance on its selected JA4DB dataset, but also acknowledges that full-browser automation and accurate TLS spoofing are material limitations. Treat it as an emerging feature-engineering reference, not as a banking-ready conclusion.[^7]

#### Research gap

Existing guidance clearly recommends layered anti-automation defenses, but there is room for a reproducible, cloud-native evaluation of adaptive gateway responses under **specifically slow, distributed credential-stuffing campaigns**.

A rigorous thesis can contribute:

1. A Docker/Kubernetes-style testbed with an API gateway, login API, observability pipeline, identity service, and simulated clients.
2. Attack generators that vary IP rotation, timing distribution, TLS/header profiles, credential reuse, and browser/device emulation.
3. A gateway policy engine that uses multiple correlated signals.
4. Experiments comparing:
    - IP-only rate limits.
    - IP + account limits.
    - IP + account + TLS/header correlation.
    - Fingerprint/device-aware risk scoring.
    - Progressive challenge/MFA controls.
5. Evaluation using attack success, time-to-mitigation, false positive/challenge rates, p95/p99 authentication latency, and throughput.

This topic is the best standalone choice if you want to emphasize your DevOps, Docker, reverse-proxy, cloud-administration, and secure API implementation experience.
<span style="display:none">[^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33]</span>

<div align="center">⁂</div>

[^1]: https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-008_Credential_Stuffing

[^2]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-228.pdf

[^3]: https://www.net.in.tum.de/fileadmin/TUM/NET/NET-2020-04-1/NET-2020-04-1_04.pdf

[^4]: https://owasp.org/API-Security/editions/2019/en/0xa2-broken-user-authentication/

[^5]: https://pubmed.ncbi.nlm.nih.gov/40989415/

[^6]: https://srcpublishers.com/mathematical-computer-applicatio/article/view/5298

[^7]: https://arxiv.org/html/2602.09606v1

[^8]: https://www.mdpi.com/1999-5903/17/3/120

[^9]: https://owasp.org/www-community/attacks/Credential_stuffing

[^10]: https://owasp.org/Top10/2021/A07_2021-Identification_and_Authentication_Failures/

[^11]: https://openid.net/specs/fapi-2_0-security-profile-ID2.html

[^12]: https://cheatsheetseries.owasp.org/cheatsheets/Bot_Management_and_Anti-Automation_Cheat_Sheet.html

[^13]: https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html

[^14]: https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-007_Credential_Cracking

[^15]: https://owasp.org/www-project-automated-threats-to-web-applications/

[^16]: https://arxiv.org/html/2606.30119

[^17]: https://github.com/OWASP/Top10/blob/master/2017/en/0xa2-broken-authentication.md

[^18]: https://owasp.deteact.com/cheat/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html

[^19]: https://www.themoonlight.io/en/review/when-handshakes-tell-the-truth-detecting-web-bad-bots-via-tls-fingerprints

[^20]: https://raw.githubusercontent.com/OWASP/Top10/master/2025/docs/en/A07_2025-Authentication_Failures.md

[^21]: https://ouci.dntb.gov.ua/en/works/4bPXRDbB/

[^22]: https://www.usenix.org/system/files/sec22fall_lin-xu.pdf

[^23]: https://dspace.vut.cz/server/api/core/bitstreams/1cff011c-7cf3-45b4-b237-0c103cbbbebf/content

[^24]: https://zenodo.org/records/8421241

[^25]: https://arxiv.org/html/2510.09645v1

[^26]: https://dione.lib.unipi.gr/xmlui/bitstream/handle/unipi/19326/Stathopoulou_21049.pdf?sequence=1\&isAllowed=y

[^27]: https://eudl.eu/pdf/10.1007/978-3-030-68734-2_1

[^28]: https://www.ijcesen.com/index.php/ijcesen/article/view/754

[^29]: https://urfjournals.org/open-access/a-machine-learning-framework-for-adaptive-authentication-in-mobile-and-web-applications.pdf

[^30]: https://www.ijmrset.com/upload/292_Deployment%20of%20AI-Based%20CAPTCHA%20Systems%20in%20Web%20Applications%20for.pdf

[^31]: http://arantxa.ii.uam.es/~jlopezv/publicaciones/ucami25ja4.pdf

[^32]: interests.devops.tools_and_setup

[^33]: work.projects.internal_api

