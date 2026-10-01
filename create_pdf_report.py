"""
Create a comprehensive PDF report for CS412 User Modeling Project
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from datetime import datetime

# Create PDF
pdf_filename = "CS412_User_Modeling_Analysis_Report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

# Title Page
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=30,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontSize=16,
    textColor=colors.HexColor('#4a4a4a'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

# Title
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph("CS412 USER MODELING", title_style))
elements.append(Paragraph("MIDTERM PROJECT REPORT", title_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("From User Interaction Data to User Segments<br/>and Adaptive User Models", subtitle_style))
elements.append(Spacer(1, 1.5*inch))
elements.append(Paragraph("October 1, 2026", subtitle_style))
elements.append(PageBreak())

# Table of Contents
elements.append(Paragraph("TABLE OF CONTENTS", styles['Heading1']))
elements.append(Spacer(1, 12))

toc_items = [
    "1. Introduction",
    "2. Understanding the User Data",
    "3. Data Preparation and Feature Engineering",
    "4. User Segmentation Method",
    "5. Results and User Segment Profiles",
    "6. User Personas",
    "7. Proposed System Adaptations",
    "8. Limitations, Ethics, and Critical Reflection",
    "9. Conclusion"
]

for item in toc_items:
    elements.append(Paragraph(item, styles['Normal']))
    elements.append(Spacer(1, 6))

elements.append(PageBreak())

# 1. INTRODUCTION
elements.append(Paragraph("1. INTRODUCTION", styles['Heading1']))
elements.append(Spacer(1, 12))

intro_text = """
This project analyzes interaction data from 500 users of a narrative educational game-based
learning platform. Each user participated in a 30-minute session, with observations captured
every 15 seconds, resulting in 120 observations per user and 60,000 total interaction records.
<br/><br/>
The primary objective is to answer the following research question: <i>What meaningful types of
users can be identified from their behavior, affective states, and performance while using the
game-based learning platform, and how could the system adapt to these different users?</i>
<br/><br/>
This analysis demonstrates the progression from raw interaction data to actionable user models:
Interaction Data → User Features → User Segmentation → Segment Interpretation → Personas →
System Adaptation.
"""

elements.append(Paragraph(intro_text, styles['Justify']))
elements.append(Spacer(1, 12))

# Dataset Overview Table
data_overview = [
    ['Metric', 'Value'],
    ['Total Users', '500'],
    ['Observations per User', '120 (every 15 seconds)'],
    ['Session Duration', '30 minutes'],
    ['Total Records', '60,000'],
    ['Observation Interval', '15 seconds']
]

t = Table(data_overview, colWidths=[3*inch, 3*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(t)
elements.append(PageBreak())

# 2. UNDERSTANDING THE USER DATA
elements.append(Paragraph("2. UNDERSTANDING THE USER DATA", styles['Heading1']))
elements.append(Spacer(1, 12))

data_text = """
The dataset contains multiple types of information about each user's interaction with the
game-based learning platform. These variables can be categorized as follows:
"""

elements.append(Paragraph(data_text, styles['Justify']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Behavioral Data:</b>", styles['Heading3']))
behavioral_text = """
• Screen State: Reading, Answering, or Exploring activities<br/>
• Clicks per 15-second interval: Interaction frequency<br/>
• Activity transitions: Switching between different activities<br/>
"""
elements.append(Paragraph(behavioral_text, styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Affective Data:</b>", styles['Heading3']))
affective_text = """
Seven emotional states captured via facial recognition:<br/>
• Bored, Confused, Engaged, Focused, Frustrated, Happy, Neutral<br/>
"""
elements.append(Paragraph(affective_text, styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Performance Data:</b>", styles['Heading3']))
performance_text = """
• Answer Outcome: Correct or Incorrect responses<br/>
• Response Time: Time taken to answer questions<br/>
• Narrative Progress: Percentage completion through the game<br/>
"""
elements.append(Paragraph(performance_text, styles['Normal']))
elements.append(Spacer(1, 12))

important_note = """
<b>Important Distinction:</b> Variables like User_ID and Capture_No identify observations but
do not describe user behavior. These are excluded from clustering. Variables like Answer_Outcome
and Response_Time are only present during answering activities (by design), appearing in
approximately 31% of observations.
"""
elements.append(Paragraph(important_note, styles['Justify']))
elements.append(PageBreak())

# 3. DATA PREPARATION AND FEATURE ENGINEERING
elements.append(Paragraph("3. DATA PREPARATION AND FEATURE ENGINEERING", styles['Heading1']))
elements.append(Spacer(1, 12))

feature_eng_text = """
The event-level data (60,000 observations) was transformed into user-level features where one
row represents one user (500 rows total). This transformation involved aggregating and
summarizing each user's 30-minute interaction session.
"""

elements.append(Paragraph(feature_eng_text, styles['Justify']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Feature Categories Created:</b>", styles['Heading3']))
elements.append(Spacer(1, 12))

feature_categories = [
    ['Category', 'Features', 'Count'],
    ['Behavioral', 'Proportions of time in Reading, Answering, Exploring', '2*'],
    ['Affective', 'Proportions of 6 emotional states', '6*'],
    ['Performance', 'Accuracy, avg response time, correct/incorrect counts', '4'],
    ['Interaction', 'Average clicks during each activity type', '3'],
    ['Engagement', 'Progress, transitions, positive/negative affect', '4'],
    ['', 'TOTAL SELECTED FOR CLUSTERING', '19']
]

t2 = Table(feature_categories, colWidths=[1.5*inch, 3*inch, 1*inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -2), colors.lightgrey),
    ('BACKGROUND', (0, -1), (-1, -1), colors.yellow),
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(t2)
elements.append(Spacer(1, 12))

redundancy_text = """
<b>* Redundancy Removal:</b> From the initial 25 features created, 6 were removed to avoid
multicollinearity. For example, since activity proportions sum to 1.0, we dropped 'Exploring'
and kept 'Reading' and 'Answering'. Similarly, one affective state was dropped as they sum to 1.0.
"""
elements.append(Paragraph(redundancy_text, styles['Normal']))
elements.append(Spacer(1, 12))

preprocessing_text = """
<b>Preprocessing:</b> All 19 features were standardized using StandardScaler (mean=0, std=1)
to ensure all features contribute equally to the clustering algorithm, regardless of their
original scales.
"""
elements.append(Paragraph(preprocessing_text, styles['Normal']))
elements.append(PageBreak())

# 4. USER SEGMENTATION METHOD
elements.append(Paragraph("4. USER SEGMENTATION METHOD", styles['Heading1']))
elements.append(Spacer(1, 12))

method_text = """
<b>Clustering Technique:</b> K-Means clustering was applied to identify groups of similar users.
<br/><br/>
<b>Determining Optimal k:</b> We evaluated cluster numbers from k=2 to k=10 using three metrics:
"""
elements.append(Paragraph(method_text, styles['Justify']))
elements.append(Spacer(1, 12))

metrics_table = [
    ['k', 'Silhouette Score', 'Davies-Bouldin Index', 'Assessment'],
    ['2', '0.314', '1.306', 'Too simplistic (only 2 types)'],
    ['3', '0.283', '1.405', 'One cluster dominates (64%)'],
    ['4', '0.179', '1.889', 'SELECTED - Well balanced'],
    ['5+', 'Decreasing', 'Increasing', 'Over-segmentation']
]

t3 = Table(metrics_table, colWidths=[0.5*inch, 1.5*inch, 1.5*inch, 2.5*inch])
t3.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 3), (-1, 3), colors.lightgreen),
    ('FONTNAME', (0, 3), (-1, 3), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(t3)
elements.append(Spacer(1, 12))

decision_text = """
<b>Decision: k=4 Clusters</b>
<br/><br/>
The selection of k=4 balances statistical validity with practical interpretability. While k=2
showed the best silhouette score, it provides insufficient granularity for adaptive system design.
The k=4 solution creates well-distributed segments (16%, 29%, 20%, 35%) with distinct, actionable
characteristics for each user type.
"""
elements.append(Paragraph(decision_text, styles['Justify']))
elements.append(PageBreak())

# 5. RESULTS AND USER SEGMENT PROFILES
elements.append(Paragraph("5. RESULTS AND USER SEGMENT PROFILES", styles['Heading1']))
elements.append(Spacer(1, 12))

results_intro = """
Four distinct user segments were identified through clustering analysis. Each segment exhibits
unique behavioral patterns, affective states, and performance characteristics.
"""
elements.append(Paragraph(results_intro, styles['Justify']))
elements.append(Spacer(1, 12))

# Segment 1: Marcus
elements.append(Paragraph("SEGMENT 1: MARCUS - Struggling Readers (80 users, 16%)", styles['Heading2']))
elements.append(Spacer(1, 6))

marcus_data = [
    ['Metric', 'Value', 'Rank'],
    ['Reading Time', '47.3%', 'HIGHEST'],
    ['Accuracy', '55.3%', 'LOWEST'],
    ['Boredom Rate', '29.2%', 'HIGHEST'],
    ['Positive Affect', '30.8%', 'LOWEST'],
    ['Response Time', '8.52s', 'SLOWEST'],
    ['Progress', '89.9%', 'LOWEST']
]

t4 = Table(marcus_data, colWidths=[2*inch, 2*inch, 2*inch])
t4.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B6B')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey)
]))

elements.append(t4)
elements.append(Spacer(1, 12))

marcus_interp = """
<b>Interpretation:</b> Marcus represents learners who invest significant effort in reading but
struggle with comprehension. This leads to low confidence, high disengagement (boredom), and
the slowest progress through the narrative. The high reading time paired with low accuracy
suggests reading comprehension is the primary bottleneck for this segment.
"""
elements.append(Paragraph(marcus_interp, styles['Justify']))
elements.append(Spacer(1, 12))

# Segment 2: Sophia
elements.append(Paragraph("SEGMENT 2: SOPHIA - Confident Learners (147 users, 29%)", styles['Heading2']))
elements.append(Spacer(1, 6))

sophia_data = [
    ['Metric', 'Value', 'Rank'],
    ['Accuracy', '86.1%', 'HIGHEST'],
    ['Response Time', '7.59s', 'FASTEST'],
    ['Positive Affect', '71.0%', 'HIGHEST'],
    ['Answering Time', '35.5%', 'HIGHEST'],
    ['Correct Answers', '36.3', 'MOST'],
    ['Progress', '93.6%', 'HIGHEST']
]

t5 = Table(sophia_data, colWidths=[2*inch, 2*inch, 2*inch])
t5.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4ECDC4')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey)
]))

elements.append(t5)
elements.append(Spacer(1, 12))

sophia_interp = """
<b>Interpretation:</b> Sophia represents high-achieving, confident learners who master content
quickly and efficiently. They spend the most time actively answering questions, respond quickly
and accurately, and maintain high positive emotional states throughout. This segment risks
becoming bored if content lacks sufficient challenge.
"""
elements.append(Paragraph(sophia_interp, styles['Justify']))
elements.append(Spacer(1, 12))

# Segment 3: Jordan
elements.append(Paragraph("SEGMENT 3: JORDAN - Struggling Answerers (98 users, 20%)", styles['Heading2']))
elements.append(Spacer(1, 6))

jordan_data = [
    ['Metric', 'Value', 'Rank'],
    ['Accuracy', '47.2%', 'LOWEST'],
    ['Confusion', '25.5%', 'HIGHEST'],
    ['Frustration', '19.4%', 'HIGHEST'],
    ['Negative Affect', '55.0%', 'HIGHEST'],
    ['Incorrect Answers', '22.8', 'MOST'],
    ['Response Time', '8.82s', 'SLOWEST']
]

t6 = Table(jordan_data, colWidths=[2*inch, 2*inch, 2*inch])
t6.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FFE66D')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey)
]))

elements.append(t6)
elements.append(Spacer(1, 12))

jordan_interp = """
<b>Interpretation:</b> Jordan represents persistent learners who attempt many questions (36%
answering time) but struggle with accuracy. Despite their effort, they experience the highest
rates of confusion and frustration, creating a negative emotional spiral. The pattern suggests
they lack foundational understanding needed to answer correctly.
"""
elements.append(Paragraph(jordan_interp, styles['Justify']))
elements.append(Spacer(1, 12))

# Segment 4: Alex
elements.append(Paragraph("SEGMENT 4: ALEX - Balanced Explorers (175 users, 35%)", styles['Heading2']))
elements.append(Spacer(1, 6))

alex_data = [
    ['Metric', 'Value', 'Rank'],
    ['Exploring Time', '35.9%', 'HIGHEST'],
    ['Accuracy', '72.7%', 'Moderate-Good'],
    ['Positive Affect', '57.5%', 'Moderate'],
    ['Negative Affect', '30.2%', 'Moderate'],
    ['Progress', '92.6%', 'Good'],
    ['Response Time', '8.07s', 'Average']
]

t7 = Table(alex_data, colWidths=[2*inch, 2*inch, 2*inch])
t7.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#95E1D3')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey)
]))

elements.append(t7)
elements.append(Spacer(1, 12))

alex_interp = """
<b>Interpretation:</b> Alex represents thoughtful, balanced learners who take an exploratory
approach to the game. They distribute time across all activities, with the highest exploration
rate. Their moderate-to-good accuracy and balanced emotional state suggest they value understanding
and discovery over speed or efficiency.
"""
elements.append(Paragraph(alex_interp, styles['Justify']))
elements.append(PageBreak())

# 6. USER PERSONAS
elements.append(Paragraph("6. USER PERSONAS", styles['Heading1']))
elements.append(Spacer(1, 12))

personas_intro = """
Evidence-based personas were developed for each segment to humanize the data and guide system
adaptation design. Each persona is grounded in actual cluster characteristics.
"""
elements.append(Paragraph(personas_intro, styles['Justify']))
elements.append(Spacer(1, 12))

# Continue with personas...
# Due to length, I'll create a condensed version

elements.append(Paragraph("<b>PERSONA 1: Marcus (Struggling Readers)</b>", styles['Heading3']))
marcus_persona = """
<b>Typical Behavior:</b> Spends 47% of time reading but achieves only 55% accuracy. Slow
responses (8.52s) suggest he struggles to understand material.
<br/><br/>
<b>Emotional State:</b> 29% bored (highest), 52% negative affect overall. Only 31% positive
emotions. Predominantly discouraged and disengaged.
<br/><br/>
<b>Pain Points:</b> Cannot understand reading material effectively, feels confused and frustrated,
low confidence in answers, frequent failures.
<br/><br/>
<b>System Needs:</b> Scaffolding for reading comprehension, gradual difficulty progression,
encouragement and positive feedback, alternative explanations, shorter reading segments.
"""
elements.append(Paragraph(marcus_persona, styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>PERSONA 2: Sophia (Confident Learners)</b>", styles['Heading3']))
sophia_persona = """
<b>Typical Behavior:</b> Balanced approach (38% reading, 36% answering, 27% exploring). Fastest
responses (7.6s), 86% accuracy. Strategic and efficient.
<br/><br/>
<b>Emotional State:</b> 71% positive affect (highest). Rarely confused (9.7%) or frustrated (5.7%).
Emotionally stable and confident.
<br/><br/>
<b>Pain Points:</b> May feel unchallenged by current difficulty, could become bored if content
lacks adequate challenge.
<br/><br/>
<b>System Needs:</b> Advanced or challenging content, recognition and achievement milestones,
faster pace, opportunities to tackle harder problems.
"""
elements.append(Paragraph(sophia_persona, styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>PERSONA 3: Jordan (Struggling Answerers)</b>", styles['Heading3']))
jordan_persona = """
<b>Typical Behavior:</b> High answering time (36%) despite low accuracy (47%). Most incorrect
answers (22.8). Slowest responses (8.82s).
<br/><br/>
<b>Emotional State:</b> Highest confusion (25.5%) and frustration (19.4%). 55% negative affect
(highest). Repeated failures create negative spiral.
<br/><br/>
<b>Pain Points:</b> Gets answers wrong repeatedly despite effort, feels confused by questions,
frustration from lack of progress, may feel incapable.
<br/><br/>
<b>System Needs:</b> Immediate detailed feedback, guided worked examples, hints before answering,
foundational content review, success experiences with easier problems.
"""
elements.append(Paragraph(jordan_persona, styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>PERSONA 4: Alex (Balanced Explorers)</b>", styles['Heading3']))
alex_persona = """
<b>Typical Behavior:</b> Highest exploration (36%), well-balanced across activities. Moderate-good
accuracy (73%). Curious and measured approach.
<br/><br/>
<b>Emotional State:</b> Balanced - 58% positive, 30% negative. Occasionally confused (12%) or
bored (11%) but not excessively. Healthy emotional state.
<br/><br/>
<b>Pain Points:</b> May not be challenged enough for mastery, exploration might not optimize
efficiency, lacks push to move from competent to excellent.
<br/><br/>
<b>System Needs:</b> Content rewarding exploration and discovery, optional depth tracks, gentle
challenge encouraging skill growth, narrative elements making learning meaningful.
"""
elements.append(Paragraph(alex_persona, styles['Normal']))
elements.append(PageBreak())

# 7. PROPOSED SYSTEM ADAPTATIONS
elements.append(Paragraph("7. PROPOSED SYSTEM ADAPTATIONS", styles['Heading1']))
elements.append(Spacer(1, 12))

adaptations_intro = """
For each segment, we propose specific system adaptations following the framework:
Evidence → User Need → System Adaptation. These are not generic recommendations but targeted
interventions based on observed patterns.
"""
elements.append(Paragraph(adaptations_intro, styles['Justify']))
elements.append(Spacer(1, 12))

# Marcus Adaptations
elements.append(Paragraph("<b>Adaptations for Marcus (Struggling Readers)</b>", styles['Heading3']))
marcus_adapt = """
<b>1. Comprehension Scaffolding:</b> Highlight key concepts, provide 'explain this' buttons for
complex paragraphs, insert mini-comprehension checks during reading, use visual aids alongside text.
<br/><br/>
<b>2. Progressive Difficulty:</b> Start with easier questions (60-70% target accuracy vs 86% for
Sophia), gradually increase difficulty with success, celebrate consecutive correct answers.
<br/><br/>
<b>3. Alternative Explanations:</b> After incorrect answers show explanation plus worked example,
provide concepts in multiple formats (text, visual, video, simulation), link to prerequisite content.
"""
elements.append(Paragraph(marcus_adapt, styles['Normal']))
elements.append(Spacer(1, 12))

# Sophia Adaptations
elements.append(Paragraph("<b>Adaptations for Sophia (Confident Learners)</b>", styles['Heading3']))
sophia_adapt = """
<b>1. Advanced Content:</b> Unlock 'Expert Mode' at 80%+ accuracy, provide bonus advanced narrative
branches, offer synthesis questions applying concepts across topics.
<br/><br/>
<b>2. Achievement Recognition:</b> Provide badges (Accuracy Streak, Speed Demon, Perfect Score),
display skill rankings, offer expert certificates, narrative recognition of competence.
<br/><br/>
<b>3. Personalized Pacing:</b> Optional time-limited challenges, choice of content sequence,
self-directed exploration, skip explanations if confident, custom difficulty settings.
"""
elements.append(Paragraph(sophia_adapt, styles['Normal']))
elements.append(Spacer(1, 12))

# Jordan Adaptations
elements.append(Paragraph("<b>Adaptations for Jordan (Struggling Answerers)</b>", styles['Heading3']))
jordan_adapt = """
<b>1. Intelligent Feedback:</b> Show correct answer immediately, explain WHY answer is correct
step-by-step, provide worked example with same structure, link to foundational concepts that led
to error.
<br/><br/>
<b>2. Hints & Scaffolding:</b> Optional hint button guiding without revealing answer, scaffold
complex questions into sub-questions, 'check my thinking' before submission, show similar solved
examples first.
<br/><br/>
<b>3. Adaptive Difficulty:</b> Start with foundational/prerequisite content review, begin with
easier versions of problem types, increase difficulty only after 3 consecutive correct, celebrate
progress ('You got 2 right in a row!').
"""
elements.append(Paragraph(jordan_adapt, styles['Normal']))
elements.append(Spacer(1, 12))

# Alex Adaptations
elements.append(Paragraph("<b>Adaptations for Alex (Balanced Explorers)</b>", styles['Heading3']))
alex_adapt = """
<b>1. Enriched Exploration:</b> Bonus narrative branches with no wrong answers, interactive
simulations of concepts, 'dig deeper' sections on topics of interest, easter eggs rewarding
thorough exploration.
<br/><br/>
<b>2. Optional Depth Tracks:</b> After each concept: 'Learn more' or 'Move on' choices, optional
Depth Badges for topic mastery, curated collections of related content, optional creative projects.
<br/><br/>
<b>3. Gentle Challenge:</b> Stretch goals for slightly harder problems, reflection prompts
('Try explaining this to a friend'), optional time challenges without penalties, encouragement
like 'You're close to mastery'.
"""
elements.append(Paragraph(alex_adapt, styles['Normal']))
elements.append(PageBreak())

# 8. LIMITATIONS, ETHICS, AND CRITICAL REFLECTION
elements.append(Paragraph("8. LIMITATIONS, ETHICS, AND CRITICAL REFLECTION", styles['Heading1']))
elements.append(Spacer(1, 12))

ethics_intro = """
User models are powerful but imperfect tools. This section addresses the limitations of our
analysis and ethical considerations for implementation.
"""
elements.append(Paragraph(ethics_intro, styles['Justify']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Affective State Classification Limitations</b>", styles['Heading3']))
affect_limits = """
Facial expressions are culturally variable and context-dependent. The same expression can mean
different things: a smile might indicate confusion (nervous humor), a frown might indicate deep
concentration. Classifiers can be biased across demographics (skin tone, age, gender).
<br/><br/>
<b>Risk:</b> Misclassification leads to wrong support. If Marcus is misclassified as 'bored'
when actually confused, the system provides wrong intervention.
<br/><br/>
<b>Mitigation:</b> Use affect as one signal among many, combine with behavioral data, allow
self-reporting, audit classifier performance across demographics, provide override options.
"""
elements.append(Paragraph(affect_limits, styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Segmentation Limitations</b>", styles['Heading3']))
segment_limits = """
Clusters represent AVERAGES, not perfect categories. Within-cluster variation exists and can be
significant. Marcus's cluster accuracy ranges from 40-70%, not uniformly 55.3%.
<br/><br/>
<b>Risk:</b> Stereotyping users based on cluster membership, missing individual differences,
premature labeling affecting growth mindset.
<br/><br/>
<b>Mitigation:</b> Use clustering as starting point, implement periodic re-clustering, track
individual change, allow individuation, focus on growth rather than fixed labels.
"""
elements.append(Paragraph(segment_limits, styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Privacy Concerns</b>", styles['Heading3']))
privacy_text = """
Facial data is biometric and uniquely identifying. Behavioral data reveals learning challenges
that could affect student opportunities if leaked. Emotional state data is intimate and could be
used to manipulate rather than support.
<br/><br/>
<b>Mitigation:</b> Minimize data collection, encrypt in transit and at rest, delete facial images
after processing, limit access, transparency reports, clear deletion policies, informed parental
consent for minors, alternative pathways to opt out.
"""
elements.append(Paragraph(privacy_text, styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Bias and Fairness</b>", styles['Heading3']))
bias_text = """
Facial recognition systems show documented bias (higher error rates on darker skin tones, different
genders, ages). Clusters may correlate with demographic groups rather than just learning styles.
Different adaptations may benefit some groups more than others.
<br/><br/>
<b>Mitigation:</b> Test classifier and clustering for bias across demographics, ensure training
data represents diverse populations, audit whether all groups benefit equally from adaptations,
provide diverse adaptation options, regular fairness audits.
"""
elements.append(Paragraph(bias_text, styles['Normal']))
elements.append(PageBreak())

# 9. CONCLUSION
elements.append(Paragraph("9. CONCLUSION", styles['Heading1']))
elements.append(Spacer(1, 12))

conclusion_text = """
This analysis demonstrates the power of user modeling for educational technology. Through
systematic analysis of 60,000 interaction records from 500 users, we identified four distinct
learner types with fundamentally different needs:
<br/><br/>
• <b>Marcus (16%)</b> - Struggling readers who need scaffolding and confidence building<br/>
• <b>Sophia (29%)</b> - Confident learners who need challenge and recognition<br/>
• <b>Jordan (20%)</b> - Struggling answerers who need feedback and foundational support<br/>
• <b>Alex (35%)</b> - Balanced explorers who need enrichment and gentle challenge<br/>
<br/>
Each segment requires specific, targeted adaptations. A one-size-fits-all approach will fail
for the majority of users.
<br/><br/>
<b>Key Insights:</b>
<br/><br/>
1. Emotional state matters as much as performance metrics<br/>
2. Practice alone is insufficient - feedback quality matters<br/>
3. Different users require fundamentally different support strategies<br/>
4. Within-cluster variation exists - models are starting points, not final labels<br/>
<br/>
<b>Ethical Responsibility:</b>
<br/><br/>
User models are REPRESENTATIONS of people, not perfect descriptions. Implementation must
prioritize: (1) Transparency - students understand system choices, (2) Autonomy - students can
override decisions, (3) Consent - informed agreement for data collection, (4) Monitoring - track
whether adaptations help or harm, (5) Fairness - test for disparate impact across demographics.
<br/><br/>
The goal is not perfect prediction, but respectful, beneficial, transparent support for diverse
learners.
<br/><br/>
<b>Students are individuals first, cluster members second.</b>
"""
elements.append(Paragraph(conclusion_text, styles['Justify']))
elements.append(Spacer(1, 24))

# Add date and signature line
elements.append(Paragraph("Report completed: October 1, 2026", styles['Normal']))
elements.append(Spacer(1, 12))
elements.append(Paragraph("CS412 User Modeling - Midterm Project", styles['Normal']))

# Build PDF
doc.build(elements)
print(f"PDF report created: {pdf_filename}")
print(f"Total pages: ~15-18 pages")
print(f"Location: {pdf_filename}")
