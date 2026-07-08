# Reinforcement Learning

Reinforcement learning teaches agents to make sequential decisions by maximizing cumulative reward. It powers game-playing agents, robotic control, and—via RLHF—the alignment of large language models. This section builds from tabular methods to deep RL, covering both value-based and policy-gradient approaches.

**Prerequisites:** [Section 03 – Neural Network Foundations](../03-neural-network-foundations/README.md), basic probability and statistics

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Reinforcement Learning: An Introduction – Sutton & Barto (2nd ed.) | Book (free) | 🔑 | [incompleteideas.net](http://incompleteideas.net/book/the-book-2nd.html) |
| 2 | RL Course – David Silver (DeepMind, YouTube) | Course | 🔑 | [YouTube Playlist](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ) |
| 3 | DQN – Mnih et al. (2013) | Paper | 🔑 | [arxiv.org/abs/1312.5602](https://arxiv.org/abs/1312.5602) |
| 4 | Human-Level Control (Nature DQN) – Mnih et al. (2015) | Paper | | [nature.com](https://www.nature.com/articles/nature14236) |
| 5 | DDPG – Lillicrap et al. (2015) | Paper | | [arxiv.org/abs/1509.02971](https://arxiv.org/abs/1509.02971) |
| 6 | AlphaGo – Silver et al. (2016) | Paper | 🔑 | [nature.com](https://www.nature.com/articles/nature16961) |
| 7 | AlphaGo Zero – Silver et al. (2017) | Paper | | [nature.com](https://www.nature.com/articles/nature24270) |
| 8 | PPO – Schulman et al. (2017) | Paper | 🔑 | [arxiv.org/abs/1707.06347](https://arxiv.org/abs/1707.06347) |
| 9 | Stanford CS234 – Reinforcement Learning (YouTube) | Course | | [YouTube Playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOSOPzutgyCTapiGlY2Nd8u) |

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## RL for Language Models

Reinforcement learning has become central to aligning large language models with human preferences. RLHF (via PPO) was the key technique behind ChatGPT's behavior, while DPO simplifies the pipeline by eliminating the reward model entirely. Self-play and self-taught reasoning push the boundaries further.

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 10 | Deep RL from Human Preferences – Christiano et al. (2017) | Paper | 🔑 | [arxiv.org/abs/1706.03741](https://arxiv.org/abs/1706.03741) |
| 11 | Direct Preference Optimization (DPO) – Rafailov et al. (2023) | Paper | 🔑 | [arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290) |
| 12 | Self-Play Fine-Tuning (SPIN) – Chen et al. (2024) | Paper | | [arxiv.org/abs/2401.01335](https://arxiv.org/abs/2401.01335) |
| 13 | STaR – Self-Taught Reasoner – Zelikman et al. (2022) | Paper | | [arxiv.org/abs/2203.14465](https://arxiv.org/abs/2203.14465) |

---

## Suggested Order

1. **Foundations** – Work through Sutton & Barto chapters 1–6 (bandits, MDPs, dynamic programming, MC, TD learning).
2. **Lectures** – Watch David Silver's RL Course alongside the textbook for complementary explanations.
3. **Value-based deep RL** – Read the DQN paper (2013), then the Nature DQN (2015) for experience replay and target networks.
4. **Continuous control** – Read DDPG for actor-critic methods in continuous action spaces.
5. **Policy gradients** – Read PPO to understand clipped surrogate objectives and why PPO became the default algorithm.
6. **Game-playing agents** – Read AlphaGo, then AlphaGo Zero to see how self-play and MCTS combine with deep RL.
7. **Deeper study** – Optionally follow Stanford CS234 for a more rigorous mathematical treatment.
8. **RLHF origins** – Read Christiano et al. to understand learning reward models from human comparisons.
9. **DPO** – Read Rafailov et al. to see how preference optimization can replace RL entirely.
10. **Self-play** – Read SPIN and STaR for self-improvement without human feedback.
