# CS412 User Modeling - Midterm Project Presentation
## From User Interaction Data to User Segments and Adaptive User Models

---

## Slide 1: Title Slide

**CS412 USER MODELING**
**MIDTERM PROJECT PRESENTATION**

**From User Interaction Data to User Segments and Adaptive User Models**

**Presented by:** [Your Name/Group Names]  
**Date:** October 1, 2026  
**Course:** CS412 User Modeling

---

## Slide 2: Project Overview

**The Challenge**
- 500 users interacting with a game-based learning platform
- 30-minute sessions per user
- 120 observations captured every 15 seconds
- **Total: 60,000 interaction records**

**Our Goal**
> What meaningful types of users can be identified from their behavior, affective states, and performance—and how could the system adapt to these different users?

---

## Slide 3: The Dataset

**What We Observed About Each User:**

**Behavioral Data:**
- Screen State: Reading, Answering, Exploring
- Clicks per 15-second interval
- Activity transitions

**Affective Data:**
- 7 emotional states captured via facial recognition
- Bored, Confused, Engaged, Focused, Frustrated, Happy, Neutral

**Performance Data:**
- Answer correctness (Correct/Incorrect)
- Response times
- Narrative progress percentage

---

## Slide 4: Our Methodology

**Step 1: Feature Engineering**
- Transformed 60,000 event-level observations → 500 user-level features
- Created 25 features representing behavior, affect, performance, engagement
- Selected 19 non-redundant features for clustering

**Step 2: User Segmentation**
- Applied K-Means clustering
- Evaluated k=2 to k=10 clusters
- Selected **k=4** based on Elbow Method, Silhouette Score, Davies-Bouldin Index

**Step 3: Interpretation**
- Analyzed cluster characteristics
- Developed data-driven personas
- Proposed system adaptations

---

## Slide 5: Determining the Number of Clusters

**Evaluation Metrics:**

| K | Silhouette Score | Davies-Bouldin | Interpretation |
|---|------------------|----------------|----------------|
| 2 | 0.314 (best) | 1.306 (best) | Too simplistic |
| 3 | 0.283 | 1.405 | One cluster dominates (64%) |
| **4** | **0.179** | **1.889** | **Well-balanced, interpretable** |
| 5+ | Decreasing | Increasing | Over-segmentation |

**Decision: K=4 clusters**
- Balances statistical validity with practical interpretability
- Creates actionable user segments (16%, 29%, 20%, 35%)
- Each cluster has distinct characteristics

---

## Slide 6: Meet Our Four User Segments

| Segment | Size | Key Characteristic |
|---------|------|-------------------|
| **Marcus** - Struggling Readers | 80 (16%) | High reading time, low comprehension |
| **Sophia** - Confident Learners | 147 (29%) | High accuracy, fast, engaged |
| **Jordan** - Struggling Answerers | 98 (20%) | Many attempts, high confusion |
| **Alex** - Balanced Explorers | 175 (35%) | Curious, well-balanced approach |

---

## Slide 7: Segment 1 - Marcus (Struggling Readers)

**Profile: 80 users (16%)**

**Behavioral Pattern:**
- Spends **47% of time reading** (highest)
- Only 26% answering, 26% exploring
- Slow response times: 8.52 seconds

**Emotional State:**
- 🙁 **29% Bored** (highest of all segments)
- 😕 13.5% Confused
- 😤 8.8% Frustrated
- Only 31% positive affect

**Performance:**
- ⚠️ **55% Accuracy** (lowest)
- 89.9% Progress (lowest)
- 17.6 correct answers

**Interpretation:** Invests effort in reading but struggles with comprehension, leading to disengagement and low confidence.

---

## Slide 8: Evidence for Marcus - Activity & Emotion

**How Marcus Spends Time:**
- Reading: 47.3% ████████████████████
- Answering: 26.2% ███████████
- Exploring: 26.4% ███████████

**Marcus's Emotional Journey:**
- Positive States: 31% ████████ (Engaged, Happy, Focused)
- Negative States: 52% █████████████ (Bored, Confused, Frustrated)

**Key Insight:** Despite spending the most time reading, Marcus has the lowest accuracy—suggesting **reading comprehension is the bottleneck**.

---

## Slide 9: Segment 2 - Sophia (Confident Learners)

**Profile: 147 users (29%)**

**Behavioral Pattern:**
- Balanced: 38% reading, **36% answering** (highest), 27% exploring
- Fast response times: **7.59 seconds** (fastest)
- Efficient, strategic approach

**Emotional State:**
- 😊 **71% Positive affect** (highest)
- 26% Engaged, 30% Focused
- Only 21% negative affect

**Performance:**
- ✅ **86% Accuracy** (highest)
- 93.6% Progress (highest)
- 36.3 correct answers (most)

**Interpretation:** High-achieving, confident learners who master content quickly and stay engaged throughout.

---

## Slide 10: Evidence for Sophia - Performance Excellence

**Sophia's Performance:**
- Accuracy: **86.1%** ████████████████████
- Response Time: **7.59s** (30% faster than average)
- Progress: **93.6%** ███████████████████

**Sophia's Emotional State:**
- Engaged: 26.1% ███████
- Focused: 29.8% ████████
- Happy: 15.2% ████
- Confused: 9.7% ██
- Frustrated: 5.7% █

**Key Insight:** Sophia shows mastery and confidence. She's efficient, rarely confused, and needs **intellectual challenge** to stay engaged.

---

## Slide 11: Segment 3 - Jordan (Struggling Answerers)

**Profile: 98 users (20%)**

**Behavioral Pattern:**
- 41% reading, **36% answering** (high practice focus), 23% exploring
- Slowest response times: **8.82 seconds**
- Many attempts, low success

**Emotional State:**
- 😰 **25.5% Confused** (highest)
- 😤 19.4% Frustrated (highest)
- 55% negative affect (highest)
- Only 38% positive affect

**Performance:**
- ❌ **47% Accuracy** (lowest)
- **22.8 incorrect answers** (most)
- 88.7% Progress (lowest)

**Interpretation:** Persistent learners who try hard but lack foundational understanding, leading to a negative emotional spiral.

---

## Slide 12: Evidence for Jordan - The Struggle is Real

**Jordan's Dilemma:**
- Attempts: **36% of time answering** (high engagement)
- Success: **47% accuracy** (lowest)
- Result: **22.8 incorrect answers** (most of any segment)

**Jordan's Emotional Pattern:**
- Confusion: 25.5% ███████ (HIGHEST)
- Frustration: 19.4% ██████
- Negative Affect: 55% ██████████████ (HIGHEST)

**Key Insight:** Jordan wants to succeed and practices heavily, but **repeated failures without proper feedback** create frustration and cognitive overload.

---

## Slide 13: Segment 4 - Alex (Balanced Explorers)

**Profile: 175 users (35%)**

**Behavioral Pattern:**
- Well-balanced: 37% reading, 27% answering, **36% exploring** (highest)
- Moderate response times: 8.07 seconds
- Curious, measured approach

**Emotional State:**
- 🙂 58% Positive affect (moderate)
- 30% Negative affect (moderate)
- Healthy emotional balance

**Performance:**
- ✓ **73% Accuracy** (moderate-good)
- 92.6% Progress (good)
- 23.2 correct answers

**Interpretation:** Thoughtful learners who value understanding and discovery, taking a balanced approach with steady results.

---

## Slide 14: Evidence for Alex - The Explorer

**Alex's Time Distribution:**
- Reading: 37.2% ███████████████
- Answering: 26.9% ███████████
- Exploring: 35.9% ██████████████ (HIGHEST)

**Alex's Balanced Affect:**
- Positive: 57.5% ██████████████
- Negative: 30.2% ███████

**Key Insight:** Alex is **intrinsically motivated** by curiosity and understanding, not just test scores. Exploration is part of healthy learning.

---

## Slide 15: Visual Comparison - How Segments Spend Time

**Activity Distribution Across Segments:**

```
              Reading    Answering   Exploring
Marcus        47.3%      26.2%       26.4%      (High reading, low success)
Sophia        37.7%      35.5%       26.9%      (Balanced, high answering)
Jordan        41.1%      36.1%       22.8%      (High answering, low success)
Alex          37.2%      26.9%       35.9%      (High exploration)
```

**Key Takeaway:** Different segments allocate time very differently—one-size-fits-all pacing will fail.

---

## Slide 16: Visual Comparison - Performance & Emotion

**Accuracy by Segment:**
- Marcus: 55.3% ███████ (struggling)
- Sophia: 86.1% █████████████ (excelling)
- Jordan: 47.2% ██████ (struggling badly)
- Alex: 72.7% ██████████ (solid)

**Positive vs Negative Affect:**
- Marcus: 31% positive | 52% negative ⚠️
- Sophia: 71% positive | 21% negative ✅
- Jordan: 38% positive | 55% negative ⚠️
- Alex: 58% positive | 30% negative ✓

**Key Takeaway:** Emotion tracks performance—struggling users experience negative affect that compounds learning difficulties.

---

## Slide 17: System Adaptation Strategy

**Our Approach:**

For each segment, we follow:
**Evidence → User Need → System Adaptation**

**Not generic recommendations like:**
- ❌ "Improve user experience"
- ❌ "Make content easier"

**But specific, targeted interventions like:**
- ✅ "Provide comprehension scaffolding for struggling readers"
- ✅ "Unlock advanced challenge tracks for high performers"

---

## Slide 18: Adaptations for Marcus (Struggling Readers)

**Evidence:**
- 47% reading time but only 55% accuracy
- 29% boredom, 52% negative affect
- Slowest progress

**User Need:**
Build reading comprehension and regain confidence through manageable challenges

**System Adaptations:**

1️⃣ **Comprehension Scaffolding**
   - Highlight key concepts in text
   - "Explain this" buttons for complex paragraphs
   - Mini-comprehension checks during reading
   - Visual aids alongside text

2️⃣ **Progressive Difficulty with Success Building**
   - Start with easier questions (60-70% target vs. 86% for Sophia)
   - Celebrate consecutive correct answers
   - Visual progress/confidence meter

3️⃣ **Alternative Explanations**
   - Multiple formats: text, visual, video, simulation
   - Worked examples after incorrect answers
   - Analogies to familiar scenarios

---

## Slide 19: Adaptations for Sophia (Confident Learners)

**Evidence:**
- 86% accuracy, fastest responses
- 71% positive affect
- May become bored without challenge

**User Need:**
Intellectual challenge and recognition to maintain engagement and develop expertise

**System Adaptations:**

1️⃣ **Advanced Content & Challenge Tracks**
   - Unlock "Expert Mode" at 80%+ accuracy
   - Bonus advanced narrative branches
   - Content synthesis questions
   - "What if?" scenarios

2️⃣ **Achievement Recognition**
   - Badges: Accuracy Streak, Speed Demon, Perfect Score
   - Expert certificates
   - Narrative recognition of competence
   - Optional mentorship opportunities

3️⃣ **Personalized Pacing & Choice**
   - Time-limited challenges
   - Choice of content sequence
   - Skip explanations if confident
   - Self-directed exploration

---

## Slide 20: Adaptations for Jordan (Struggling Answerers)

**Evidence:**
- 47% accuracy despite 36% answering time
- 25.5% confusion, 19.4% frustration (highest)
- 8.82s slowest responses

**User Need:**
Immediate detailed feedback and guided support to build understanding and prevent frustration spiral

**System Adaptations:**

1️⃣ **Intelligent Feedback & Worked Examples**
   - Show correct answer immediately
   - Explain WHY answer is correct (step-by-step)
   - Provide worked example with same structure
   - Link to foundational concepts

2️⃣ **Hints & Scaffolding Before Answering**
   - Optional hint button (guide without revealing)
   - Scaffold complex questions into sub-questions
   - "Check my thinking" before submission
   - Show similar solved examples first

3️⃣ **Adaptive Difficulty with Success Building**
   - Review foundational/prerequisite content
   - Start with easier problem versions
   - Increase difficulty after 3 consecutive correct
   - Celebrate progress: "2 right in a row!"

---

## Slide 21: Adaptations for Alex (Balanced Explorers)

**Evidence:**
- 36% exploration time (highest)
- 73% accuracy (good but not highest)
- Balanced emotional state
- Values understanding over speed

**User Need:**
Content that rewards curiosity and provides gentle challenge while supporting deeper learning

**System Adaptations:**

1️⃣ **Enriched Exploration Opportunities**
   - Bonus narrative branches
   - Interactive simulations
   - "Dig deeper" sections
   - Easter eggs for thorough exploration
   - Optional world-building lore

2️⃣ **Optional Depth Tracks**
   - "Learn more" vs "Move on" choices
   - Depth badges for topic mastery
   - Optional creative projects
   - Community discussion prompts

3️⃣ **Gentle Challenge & Growth Nudges**
   - Stretch goals for harder problems
   - Reflection prompts
   - Optional time challenges (no penalty)
   - "You're close to mastery" encouragement

---

## Slide 22: Implementation Roadmap

**Phase 1: Deploy & Monitor (Months 1-3)**
- Implement adaptations for each segment
- Track student outcomes
- Collect user feedback
- Measure: Does accuracy improve? Does affect improve?

**Phase 2: Refine & Scale (Months 4-6)**
- Dynamic re-clustering (monthly)
- A/B test adaptations
- Audit for demographic bias
- Address within-cluster variation

**Phase 3: Personalize (Months 7+)**
- Move toward continuous personalized models
- Student preferences and goals integration
- Build transparent, explainable systems
- Privacy-preserving alternatives to facial recognition

---

## Slide 23: Limitations & Critical Reflection

**We Must Acknowledge:**

🤔 **Affective Classification Limitations**
- Facial expressions are culturally variable
- Same expression can mean different things in context
- Classifiers can be biased across demographics
- Risk: Misclassification leads to wrong support

🔍 **Segmentation Limitations**
- Clusters are AVERAGES, not perfect categories
- Within-cluster variation is significant
- Risk: Stereotyping users based on cluster membership

⚠️ **Adaptation Risks**
- Incorrect models can harm learning (false positives/negatives)
- Self-fulfilling prophecies possible
- Cascading mistakes compound over time

---

## Slide 24: Ethical Considerations

**Privacy Concerns:**
- Facial data is biometric and uniquely identifying
- Behavioral data reveals sensitive learning challenges
- Questions: Who owns this data? How long is it kept? Can it be deleted?

**Bias & Fairness:**
- Facial recognition shows documented bias (skin tone, age, gender)
- Clusters may correlate with demographic groups
- Adaptations may benefit some groups more than others

**Our Responsibility:**
1. **Transparency:** Students understand why system makes choices
2. **Autonomy:** Students can override cluster assignments
3. **Consent:** Informed, meaningful consent (especially minors)
4. **Monitoring:** Continuously check if adaptations help or harm
5. **Fairness:** Test for disparate impact across demographics

---

## Slide 25: Key Takeaways

**What We Discovered:**

1️⃣ **Four Distinct User Types** with fundamentally different needs
   - Struggling readers need scaffolding
   - Confident learners need challenge
   - Struggling answerers need feedback
   - Explorers need enrichment

2️⃣ **Emotion Matters as Much as Performance**
   - Negative affect predicts struggle and disengagement
   - System should monitor and respond to emotional state

3️⃣ **Practice Alone Isn't Enough**
   - Quality of feedback matters more than quantity of attempts
   - Jordan segment proves this

4️⃣ **One-Size-Fits-All Will Fail**
   - Different segments allocate time differently
   - Different segments respond to different motivations
   - Personalization is necessary, not optional

---

## Slide 26: The Big Picture

**User modeling is powerful but imperfect.**

Models are **REPRESENTATIONS** of people, not perfect descriptions.

Our goal is not:
- ❌ Perfect prediction
- ❌ Labeling students permanently
- ❌ Replacing teacher judgment

Our goal IS:
- ✅ Respectful, beneficial support
- ✅ Transparent, explainable decisions
- ✅ Empowering diverse learners
- ✅ Ethical use of data

**Students are individuals first, cluster members second.**

---

## Slide 27: Questions?

**Thank you for your attention!**

**Contact:**
[Your Name]
[Your Email]

**Project Materials:**
- Full analysis notebook
- User-level dataset (500 users, 26 features)
- Detailed report
- Visualizations

**Open for Discussion:**
- Methodology choices
- Adaptation strategies
- Ethical implications
- Implementation challenges

---

## Slide 28: Appendix - Technical Details

**Clustering Features Used (19 total):**

**Behavioral (2):**
- prop_reading, prop_answering

**Affective (6):**
- affect_bored, affect_confused, affect_engaged, affect_focused, affect_frustrated, affect_happy

**Performance (4):**
- accuracy, avg_response_time, num_correct, num_incorrect

**Interaction (3):**
- avg_clicks_reading, avg_clicks_answering, avg_clicks_exploring

**Progress & Engagement (4):**
- final_narrative_progress, activity_transitions, prop_positive_affect, prop_negative_affect

**Preprocessing:**
- StandardScaler (mean=0, std=1)

---

## Slide 29: Appendix - Cluster Evaluation Metrics

**K-Means Evaluation Results:**

| K | Inertia | Silhouette | Davies-Bouldin | Cluster Sizes |
|---|---------|------------|----------------|---------------|
| 2 | 6217.82 | 0.314 | 1.306 | 183, 317 |
| 3 | 5511.96 | 0.283 | 1.405 | 83, 318, 99 |
| **4** | **4935.97** | **0.179** | **1.889** | **80, 147, 98, 175** |
| 5 | 4658.98 | 0.165 | 1.922 | - |
| 6 | 4491.79 | 0.157 | 2.006 | - |

**Decision rationale:**
- k=2: Too simplistic (only 2 types)
- k=3: Cluster 1 dominates at 63.6%
- **k=4: Best balance of interpretability and distribution**
- k=5+: Over-segmentation, decreasing silhouette scores

---

## Slide 30: Appendix - References & Data Source

**Dataset:**
- CS412_EventLog_500Users_60000Rows.csv
- Provided by course instructor
- Synthetic data simulating game-based learning platform

**Tools & Libraries:**
- Python 3.9
- pandas, numpy (data processing)
- scikit-learn (clustering, evaluation)
- matplotlib, seaborn (visualization)

**Methodology References:**
- K-Means Clustering (scikit-learn implementation)
- Elbow Method for optimal k
- Silhouette Score (higher = better separation)
- Davies-Bouldin Index (lower = better compactness)

**Course:**
CS412 User Modeling
Instructor: [Instructor Name]
Institution: [Your University]
Date: October 1, 2026

---

**END OF PRESENTATION**
