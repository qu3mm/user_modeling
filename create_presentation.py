"""
Create PowerPoint presentation for CS412 User Modeling Project
with screenshots from the analysis
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

def add_title_slide(prs, title, subtitle):
    """Add title slide"""
    slide_layout = prs.slide_layouts[0]  # Title slide layout
    slide = prs.slides.add_slide(slide_layout)

    title_shape = slide.shapes.title
    subtitle_shape = slide.placeholders[1]

    title_shape.text = title
    subtitle_shape.text = subtitle

    return slide

def add_content_slide(prs, title, content_lines):
    """Add content slide with bullet points"""
    slide_layout = prs.slide_layouts[1]  # Title and content layout
    slide = prs.slides.add_slide(slide_layout)

    title_shape = slide.shapes.title
    title_shape.text = title

    body_shape = slide.placeholders[1]
    tf = body_shape.text_frame

    for i, line in enumerate(content_lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()

        p.text = line
        p.level = 0
        p.font.size = Pt(18)

    return slide

def add_two_column_slide(prs, title, left_content, right_content):
    """Add slide with two columns"""
    slide_layout = prs.slide_layouts[5]  # Blank layout
    slide = prs.slides.add_slide(slide_layout)

    # Add title
    left = Inches(0.5)
    top = Inches(0.5)
    width = Inches(9)
    height = Inches(0.8)

    title_box = slide.shapes.add_textbox(left, top, width, height)
    title_frame = title_box.text_frame
    title_para = title_frame.paragraphs[0]
    title_para.text = title
    title_para.font.size = Pt(32)
    title_para.font.bold = True

    # Left column
    left_col = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.5), Inches(5.5))
    left_frame = left_col.text_frame
    left_frame.word_wrap = True
    for line in left_content:
        p = left_frame.add_paragraph()
        p.text = line
        p.font.size = Pt(14)

    # Right column
    right_col = slide.shapes.add_textbox(Inches(5.2), Inches(1.5), Inches(4.5), Inches(5.5))
    right_frame = right_col.text_frame
    right_frame.word_wrap = True
    for line in right_content:
        p = right_frame.add_paragraph()
        p.text = line
        p.font.size = Pt(14)

    return slide

# Slide 1: Title
add_title_slide(
    prs,
    "CS412 User Modeling\nMidterm Project",
    "From User Interaction Data to User Segments\nand Adaptive User Models\n\nOctober 1, 2026"
)

# Slide 2: Project Overview
add_content_slide(
    prs,
    "Project Overview",
    [
        "Challenge: Analyze 500 users on game-based learning platform",
        "Dataset: 60,000 interaction records (120 observations per user)",
        "Session: 30 minutes per user, captured every 15 seconds",
        "",
        "Goal: Identify meaningful user types and propose system adaptations",
        "",
        "Key Question:",
        "What meaningful types of users can be identified from their",
        "behavior, affective states, and performance—and how could",
        "the system adapt to these different users?"
    ]
)

# Slide 3: The Dataset
add_content_slide(
    prs,
    "The Dataset - What We Observed",
    [
        "Behavioral Data:",
        "  • Screen State: Reading, Answering, Exploring",
        "  • Clicks per 15-second interval",
        "  • Activity transitions",
        "",
        "Affective Data:",
        "  • 7 emotional states via facial recognition",
        "  • Bored, Confused, Engaged, Focused, Frustrated, Happy, Neutral",
        "",
        "Performance Data:",
        "  • Answer correctness (Correct/Incorrect)",
        "  • Response times",
        "  • Narrative progress percentage"
    ]
)

# Slide 4: Methodology
add_content_slide(
    prs,
    "Our Methodology",
    [
        "Step 1: Feature Engineering",
        "  • 60,000 events → 500 user-level features",
        "  • Created 25 features (selected 19 for clustering)",
        "",
        "Step 2: User Segmentation",
        "  • Applied K-Means clustering",
        "  • Evaluated k=2 to k=10",
        "  • Selected k=4 based on multiple metrics",
        "",
        "Step 3: Interpretation & Adaptation",
        "  • Analyzed cluster characteristics",
        "  • Developed evidence-based personas",
        "  • Proposed targeted system adaptations"
    ]
)

# Slide 5: Determining Clusters
add_content_slide(
    prs,
    "Determining Number of Clusters",
    [
        "Evaluation Metrics:",
        "  k=2: Silhouette 0.314 (best), DB 1.306 (best) - Too simplistic",
        "  k=3: Silhouette 0.283, DB 1.405 - One cluster dominates 64%",
        "  k=4: Silhouette 0.179, DB 1.889 - SELECTED ✓",
        "  k=5+: Decreasing scores - Over-segmentation",
        "",
        "Decision: K=4 Clusters",
        "  ✓ Balances statistical validity with interpretability",
        "  ✓ Well-distributed: 16%, 29%, 20%, 35%",
        "  ✓ Each cluster has distinct, actionable characteristics"
    ]
)

# Slide 6: Four Segments Overview
add_content_slide(
    prs,
    "Meet Our Four User Segments",
    [
        "1. Marcus - Struggling Readers (80 users, 16%)",
        "   High reading time, low comprehension, disengaged",
        "",
        "2. Sophia - Confident Learners (147 users, 29%)",
        "   High accuracy, fast responses, highly engaged",
        "",
        "3. Jordan - Struggling Answerers (98 users, 20%)",
        "   Many attempts, high confusion/frustration, low success",
        "",
        "4. Alex - Balanced Explorers (175 users, 35%)",
        "   Curious, well-balanced approach, steady performance"
    ]
)

# Slide 7: Marcus Profile
add_content_slide(
    prs,
    "Segment 1: Marcus - Struggling Readers",
    [
        "Profile: 80 users (16%)",
        "",
        "Behavioral Pattern:",
        "  • 47% reading time (HIGHEST) but only 55% accuracy",
        "  • Slow responses: 8.52 seconds",
        "",
        "Emotional State:",
        "  • 29% Bored (HIGHEST of all segments)",
        "  • 52% negative affect overall",
        "  • Only 31% positive emotions",
        "",
        "Performance:",
        "  • 55% accuracy (LOWEST)",
        "  • 89.9% progress (LOWEST)",
        "",
        "Interpretation: Invests effort but struggles with",
        "comprehension, leading to disengagement"
    ]
)

# Slide 8: Sophia Profile
add_content_slide(
    prs,
    "Segment 2: Sophia - Confident Learners",
    [
        "Profile: 147 users (29%)",
        "",
        "Behavioral Pattern:",
        "  • Balanced: 38% reading, 36% answering, 27% exploring",
        "  • Fastest responses: 7.59 seconds",
        "",
        "Emotional State:",
        "  • 71% positive affect (HIGHEST)",
        "  • 26% Engaged, 30% Focused",
        "  • Only 21% negative emotions",
        "",
        "Performance:",
        "  • 86% accuracy (HIGHEST)",
        "  • 93.6% progress (HIGHEST)",
        "  • 36.3 correct answers (MOST)",
        "",
        "Interpretation: High-achieving, confident learners",
        "who master content quickly"
    ]
)

# Slide 9: Jordan Profile
add_content_slide(
    prs,
    "Segment 3: Jordan - Struggling Answerers",
    [
        "Profile: 98 users (20%)",
        "",
        "Behavioral Pattern:",
        "  • 36% answering time (high practice focus)",
        "  • Slowest responses: 8.82 seconds",
        "",
        "Emotional State:",
        "  • 25.5% Confused (HIGHEST)",
        "  • 19.4% Frustrated (HIGHEST)",
        "  • 55% negative affect (HIGHEST)",
        "",
        "Performance:",
        "  • 47% accuracy (LOWEST)",
        "  • 22.8 incorrect answers (MOST)",
        "  • 88.7% progress (LOWEST)",
        "",
        "Interpretation: Persistent but lacking foundational",
        "understanding, creating negative spiral"
    ]
)

# Slide 10: Alex Profile
add_content_slide(
    prs,
    "Segment 4: Alex - Balanced Explorers",
    [
        "Profile: 175 users (35%)",
        "",
        "Behavioral Pattern:",
        "  • 36% exploring (HIGHEST)",
        "  • Well-balanced across all activities",
        "  • Moderate response times: 8.07 seconds",
        "",
        "Emotional State:",
        "  • 58% positive affect (moderate)",
        "  • 30% negative affect (moderate)",
        "  • Healthy emotional balance",
        "",
        "Performance:",
        "  • 73% accuracy (moderate-good)",
        "  • 92.6% progress (good)",
        "",
        "Interpretation: Thoughtful learners who value",
        "understanding and discovery"
    ]
)

# Slide 11: Activity Comparison
add_content_slide(
    prs,
    "How Segments Spend Their Time",
    [
        "Activity Distribution:",
        "",
        "Marcus:  47% Reading | 26% Answering | 26% Exploring",
        "         (High reading, low success)",
        "",
        "Sophia:  38% Reading | 36% Answering | 27% Exploring",
        "         (Balanced, high answering)",
        "",
        "Jordan:  41% Reading | 36% Answering | 23% Exploring",
        "         (High answering, low success)",
        "",
        "Alex:    37% Reading | 27% Answering | 36% Exploring",
        "         (High exploration)",
        "",
        "Key Takeaway: Different segments allocate time very",
        "differently—one-size-fits-all pacing will fail"
    ]
)

# Slide 12: Performance Comparison
add_content_slide(
    prs,
    "Performance & Emotional State Comparison",
    [
        "Accuracy by Segment:",
        "  Marcus: 55.3% (struggling)",
        "  Sophia: 86.1% (excelling)",
        "  Jordan: 47.2% (struggling badly)",
        "  Alex:   72.7% (solid)",
        "",
        "Positive vs Negative Affect:",
        "  Marcus: 31% positive | 52% negative ⚠",
        "  Sophia: 71% positive | 21% negative ✓",
        "  Jordan: 38% positive | 55% negative ⚠",
        "  Alex:   58% positive | 30% negative ✓",
        "",
        "Key Insight: Emotion tracks performance—struggling",
        "users experience negative affect that compounds difficulties"
    ]
)

# Slide 13: Adaptation Strategy
add_content_slide(
    prs,
    "System Adaptation Strategy",
    [
        "Our Approach:",
        "Evidence → User Need → System Adaptation",
        "",
        "NOT generic recommendations:",
        "  ✗ 'Improve user experience'",
        "  ✗ 'Make content easier'",
        "",
        "But SPECIFIC, targeted interventions:",
        "  ✓ 'Comprehension scaffolding for struggling readers'",
        "  ✓ 'Advanced challenge tracks for high performers'",
        "  ✓ 'Immediate feedback with worked examples'",
        "  ✓ 'Enriched exploration opportunities'",
        "",
        "Each adaptation is grounded in actual user behavior",
        "and addresses specific identified needs"
    ]
)

# Slide 14: Marcus Adaptations
add_content_slide(
    prs,
    "Adaptations for Marcus (Struggling Readers)",
    [
        "Evidence: 47% reading, 55% accuracy, 29% bored, 52% negative",
        "",
        "User Need: Build comprehension and regain confidence",
        "",
        "Adaptations:",
        "",
        "1. Comprehension Scaffolding",
        "   • Highlight key concepts, 'explain this' buttons",
        "   • Mini-comprehension checks, visual aids",
        "",
        "2. Progressive Difficulty with Success Building",
        "   • Start easier (60-70% target), celebrate wins",
        "   • Visual progress meter",
        "",
        "3. Alternative Explanations",
        "   • Multiple formats: text, visual, video, simulation",
        "   • Worked examples, analogies"
    ]
)

# Slide 15: Sophia Adaptations
add_content_slide(
    prs,
    "Adaptations for Sophia (Confident Learners)",
    [
        "Evidence: 86% accuracy, 7.59s responses, 71% positive affect",
        "",
        "User Need: Challenge and recognition to maintain engagement",
        "",
        "Adaptations:",
        "",
        "1. Advanced Content & Challenge Tracks",
        "   • Unlock 'Expert Mode' at 80%+ accuracy",
        "   • Bonus advanced branches, synthesis questions",
        "",
        "2. Achievement Recognition",
        "   • Badges, expert certificates",
        "   • Narrative recognition of competence",
        "",
        "3. Personalized Pacing & Choice",
        "   • Time-limited challenges",
        "   • Content sequence choice, skip if confident"
    ]
)

# Slide 16: Jordan Adaptations
add_content_slide(
    prs,
    "Adaptations for Jordan (Struggling Answerers)",
    [
        "Evidence: 47% accuracy, 36% answering, 25.5% confused, 19.4% frustrated",
        "",
        "User Need: Immediate feedback and guided support",
        "",
        "Adaptations:",
        "",
        "1. Intelligent Feedback & Worked Examples",
        "   • Show correct answer immediately",
        "   • Explain WHY (step-by-step), link to concepts",
        "",
        "2. Hints & Scaffolding Before Answering",
        "   • Optional hint button, scaffold sub-questions",
        "   • 'Check my thinking' before submission",
        "",
        "3. Adaptive Difficulty with Success Building",
        "   • Review prerequisites, start easier",
        "   • Celebrate progress: '2 right in a row!'"
    ]
)

# Slide 17: Alex Adaptations
add_content_slide(
    prs,
    "Adaptations for Alex (Balanced Explorers)",
    [
        "Evidence: 36% exploration, 73% accuracy, 58% positive, balanced",
        "",
        "User Need: Enrichment and gentle challenge",
        "",
        "Adaptations:",
        "",
        "1. Enriched Exploration Opportunities",
        "   • Bonus narrative branches, interactive simulations",
        "   • 'Dig deeper' sections, easter eggs",
        "",
        "2. Optional Depth Tracks",
        "   • 'Learn more' vs 'Move on' choices",
        "   • Depth badges, creative projects",
        "",
        "3. Gentle Challenge & Growth Nudges",
        "   • Stretch goals, reflection prompts",
        "   • 'You're close to mastery' encouragement"
    ]
)

# Slide 18: Key Takeaways
add_content_slide(
    prs,
    "Key Takeaways",
    [
        "1. Four Distinct User Types with different needs",
        "   • Struggling readers need scaffolding",
        "   • Confident learners need challenge",
        "   • Struggling answerers need feedback",
        "   • Explorers need enrichment",
        "",
        "2. Emotion Matters as Much as Performance",
        "   • Negative affect predicts struggle",
        "   • System should monitor emotional state",
        "",
        "3. Practice Alone Isn't Enough",
        "   • Quality of feedback > quantity of attempts",
        "",
        "4. One-Size-Fits-All Will Fail",
        "   • Personalization is necessary, not optional"
    ]
)

# Slide 19: Limitations & Ethics
add_content_slide(
    prs,
    "Limitations & Ethical Considerations",
    [
        "Limitations:",
        "  • Affective classifiers may misclassify emotions",
        "  • Clusters are averages (within-cluster variation exists)",
        "  • Incorrect models can lead to harmful adaptations",
        "",
        "Ethical Concerns:",
        "  • Privacy: Facial recognition, behavior tracking",
        "  • Bias: Classifiers, clustering, adaptations",
        "  • Autonomy: Students should override system decisions",
        "",
        "Our Principles:",
        "  ✓ Transparency: Explain why system makes choices",
        "  ✓ Consent: Informed agreement for data collection",
        "  ✓ Monitoring: Track if adaptations help or harm",
        "  ✓ Fairness: Test for demographic disparities"
    ]
)

# Slide 20: Conclusion
add_content_slide(
    prs,
    "Conclusion",
    [
        "User modeling is powerful but imperfect.",
        "",
        "Models are REPRESENTATIONS of people,",
        "not perfect descriptions.",
        "",
        "Our goal is NOT:",
        "  ✗ Perfect prediction",
        "  ✗ Labeling students permanently",
        "",
        "Our goal IS:",
        "  ✓ Respectful, beneficial support",
        "  ✓ Transparent, explainable decisions",
        "  ✓ Empowering diverse learners",
        "",
        "Students are individuals first,",
        "cluster members second."
    ]
)

# Slide 21: Thank You
add_title_slide(
    prs,
    "Thank You!",
    "Questions?\n\nCS412 User Modeling - Midterm Project\nOctober 1, 2026"
)

# Save presentation
output_path = "CS412_User_Modeling_Presentation.pptx"
prs.save(output_path)
print(f"✓ PowerPoint presentation created: {output_path}")
print(f"✓ Total slides: {len(prs.slides)}")
print(f"\nNext: Run the analysis notebook to generate visualizations,")
print(f"then manually insert screenshots into slides 5, 11, and 12")
