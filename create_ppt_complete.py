"""
Complete PowerPoint presentation creator for CS412 User Modeling Project
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Slide 1: Title
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = 'CS412 User Modeling - Midterm Project'
    slide.placeholders[1].text = 'From User Interaction Data to User Segments\nand Adaptive User Models\n\nOctober 1, 2026'

    # Slide 2: Overview
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Project Overview'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Challenge: 500 users on game-based learning platform'
    tf.add_paragraph().text = 'Dataset: 60,000 interaction records (120 per user)'
    tf.add_paragraph().text = 'Session: 30 minutes, captured every 15 seconds'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Goal: What meaningful user types exist, and how should'
    tf.add_paragraph().text = 'the system adapt to these different users?'

    # Slide 3: Dataset
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'The Dataset'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Behavioral: Reading, Answering, Exploring activities'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Affective: 7 emotional states (facial recognition)'
    p = tf.add_paragraph()
    p.text = 'Bored, Confused, Engaged, Focused, Frustrated, Happy, Neutral'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Performance: Accuracy, response times, progress'

    # Slide 4: Methodology
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Methodology'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Feature Engineering: 60,000 events to 500 users'
    p = tf.add_paragraph()
    p.text = '25 features created, 19 selected for clustering'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Clustering: K-Means with k=2 to k=10 evaluated'
    p = tf.add_paragraph()
    p.text = 'Selected k=4 (balanced, interpretable)'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Interpretation: Evidence-based personas and adaptations'

    # Slide 5: Cluster Selection (placeholder for screenshot)
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.7))
    tf = title_box.text_frame
    tf.text = 'Determining Number of Clusters'
    tf.paragraphs[0].font.size = Pt(32)
    tf.paragraphs[0].font.bold = True

    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(1.5))
    tf = content_box.text_frame
    tf.text = 'k=2: Silhouette 0.314 (best), DB 1.306 - Too simplistic'
    tf.add_paragraph().text = 'k=3: Silhouette 0.283, DB 1.405 - One cluster dominates 64%'
    tf.add_paragraph().text = 'k=4: Silhouette 0.179, DB 1.889 - SELECTED (balanced)'
    tf.add_paragraph().text = 'k=5+: Decreasing scores - Over-segmentation'

    note_box = slide.shapes.add_textbox(Inches(0.5), Inches(3), Inches(9), Inches(1))
    tf = note_box.text_frame
    tf.text = '[INSERT SCREENSHOT: Elbow Method & Silhouette Score charts from notebook]'
    tf.paragraphs[0].font.size = Pt(14)
    tf.paragraphs[0].font.italic = True

    # Slide 6: Four Segments
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Four User Segments Identified'
    tf = slide.placeholders[1].text_frame
    tf.text = '1. Marcus - Struggling Readers (80 users, 16%)'
    p = tf.add_paragraph()
    p.text = 'High reading time, low comprehension'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '2. Sophia - Confident Learners (147 users, 29%)'
    p = tf.add_paragraph()
    p.text = 'High accuracy, fast, highly engaged'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '3. Jordan - Struggling Answerers (98 users, 20%)'
    p = tf.add_paragraph()
    p.text = 'Many attempts, high confusion/frustration'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '4. Alex - Balanced Explorers (175 users, 35%)'
    p = tf.add_paragraph()
    p.text = 'Curious, balanced approach, steady performance'
    p.level = 1

    # Slide 7: Marcus
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Marcus - Struggling Readers (16%)'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Behavior: 47% reading (HIGHEST), slow responses (8.52s)'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Emotion: 29% Bored (HIGHEST), 52% negative affect'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Performance: 55% accuracy (LOWEST), 89.9% progress'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Interpretation: Invests effort in reading but struggles'
    tf.add_paragraph().text = 'with comprehension, leading to disengagement'

    # Slide 8: Sophia
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Sophia - Confident Learners (29%)'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Behavior: Balanced activities, fastest responses (7.59s)'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Emotion: 71% positive affect (HIGHEST), rarely confused'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Performance: 86% accuracy (HIGHEST), 93.6% progress'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Interpretation: High-achieving, confident learners who'
    tf.add_paragraph().text = 'master content quickly and stay engaged'

    # Slide 9: Jordan
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Jordan - Struggling Answerers (20%)'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Behavior: 36% answering, slowest responses (8.82s)'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Emotion: 25.5% Confused (HIGHEST), 55% negative affect'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Performance: 47% accuracy, 22.8 incorrect (MOST)'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Interpretation: Persistent but lacking foundational'
    tf.add_paragraph().text = 'understanding, creating negative emotional spiral'

    # Slide 10: Alex
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Alex - Balanced Explorers (35%)'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Behavior: 36% exploring (HIGHEST), well-balanced'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Emotion: 58% positive affect, healthy balance'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Performance: 73% accuracy (moderate-good), 92.6% progress'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Interpretation: Thoughtful learners who value'
    tf.add_paragraph().text = 'understanding and discovery'

    # Slide 11: Activity Comparison (placeholder for screenshot)
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.7))
    tf = title_box.text_frame
    tf.text = 'How Segments Spend Their Time'
    tf.paragraphs[0].font.size = Pt(32)
    tf.paragraphs[0].font.bold = True

    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(2))
    tf = content_box.text_frame
    tf.text = 'Marcus:  47% Reading | 26% Answering | 26% Exploring'
    tf.add_paragraph().text = 'Sophia:  38% Reading | 36% Answering | 27% Exploring'
    tf.add_paragraph().text = 'Jordan:  41% Reading | 36% Answering | 23% Exploring'
    tf.add_paragraph().text = 'Alex:    37% Reading | 27% Answering | 36% Exploring'

    note_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.5), Inches(9), Inches(1))
    tf = note_box.text_frame
    tf.text = '[INSERT SCREENSHOT: Activity Distribution bar chart from notebook]'
    tf.paragraphs[0].font.size = Pt(14)
    tf.paragraphs[0].font.italic = True

    # Slide 12: Performance Comparison (placeholder for screenshot)
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.7))
    tf = title_box.text_frame
    tf.text = 'Performance & Emotional State'
    tf.paragraphs[0].font.size = Pt(32)
    tf.paragraphs[0].font.bold = True

    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(4), Inches(2))
    tf = content_box.text_frame
    tf.text = 'Accuracy:'
    tf.add_paragraph().text = 'Marcus: 55.3%'
    tf.add_paragraph().text = 'Sophia: 86.1%'
    tf.add_paragraph().text = 'Jordan: 47.2%'
    tf.add_paragraph().text = 'Alex: 72.7%'

    content_box2 = slide.shapes.add_textbox(Inches(5), Inches(1.2), Inches(4.5), Inches(2))
    tf = content_box2.text_frame
    tf.text = 'Positive vs Negative Affect:'
    tf.add_paragraph().text = 'Marcus: 31% | 52%'
    tf.add_paragraph().text = 'Sophia: 71% | 21%'
    tf.add_paragraph().text = 'Jordan: 38% | 55%'
    tf.add_paragraph().text = 'Alex: 58% | 30%'

    note_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.5), Inches(9), Inches(1))
    tf = note_box.text_frame
    tf.text = '[INSERT SCREENSHOT: Accuracy & Affect charts from notebook]'
    tf.paragraphs[0].font.size = Pt(14)
    tf.paragraphs[0].font.italic = True

    # Slide 13: Adaptation Strategy
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'System Adaptation Strategy'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Evidence → User Need → System Adaptation'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'NOT generic: "Improve user experience"'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'SPECIFIC, targeted:'
    p = tf.add_paragraph()
    p.text = 'Comprehension scaffolding for struggling readers'
    p.level = 1
    p = tf.add_paragraph()
    p.text = 'Advanced challenge tracks for high performers'
    p.level = 1
    p = tf.add_paragraph()
    p.text = 'Immediate feedback with worked examples'
    p.level = 1
    p = tf.add_paragraph()
    p.text = 'Enriched exploration opportunities'
    p.level = 1

    # Slide 14: Marcus Adaptations
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Adaptations for Marcus'
    tf = slide.placeholders[1].text_frame
    tf.text = '1. Comprehension Scaffolding'
    p = tf.add_paragraph()
    p.text = 'Highlight key concepts, mini-checks, visual aids'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '2. Progressive Difficulty'
    p = tf.add_paragraph()
    p.text = 'Start easier (60-70%), celebrate wins, show progress'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '3. Alternative Explanations'
    p = tf.add_paragraph()
    p.text = 'Multiple formats: text, visual, video, simulation'
    p.level = 1

    # Slide 15: Sophia Adaptations
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Adaptations for Sophia'
    tf = slide.placeholders[1].text_frame
    tf.text = '1. Advanced Content & Challenge Tracks'
    p = tf.add_paragraph()
    p.text = 'Expert Mode, bonus branches, synthesis questions'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '2. Achievement Recognition'
    p = tf.add_paragraph()
    p.text = 'Badges, certificates, narrative recognition'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '3. Personalized Pacing & Choice'
    p = tf.add_paragraph()
    p.text = 'Time challenges, content choice, skip if confident'
    p.level = 1

    # Slide 16: Jordan Adaptations
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Adaptations for Jordan'
    tf = slide.placeholders[1].text_frame
    tf.text = '1. Intelligent Feedback & Worked Examples'
    p = tf.add_paragraph()
    p.text = 'Immediate correct answer, explain WHY step-by-step'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '2. Hints & Scaffolding'
    p = tf.add_paragraph()
    p.text = 'Hint button, sub-questions, check my thinking'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '3. Adaptive Difficulty'
    p = tf.add_paragraph()
    p.text = 'Review prerequisites, start easier, celebrate progress'
    p.level = 1

    # Slide 17: Alex Adaptations
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Adaptations for Alex'
    tf = slide.placeholders[1].text_frame
    tf.text = '1. Enriched Exploration'
    p = tf.add_paragraph()
    p.text = 'Bonus branches, simulations, dig deeper sections'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '2. Optional Depth Tracks'
    p = tf.add_paragraph()
    p.text = 'Learn more vs Move on, depth badges, projects'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '3. Gentle Challenge & Growth'
    p = tf.add_paragraph()
    p.text = 'Stretch goals, reflection, encouragement'
    p.level = 1

    # Slide 18: Key Takeaways
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Key Takeaways'
    tf = slide.placeholders[1].text_frame
    tf.text = '1. Four distinct user types with different needs'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '2. Emotion matters as much as performance'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '3. Practice alone is not enough'
    p = tf.add_paragraph()
    p.text = 'Quality of feedback matters more than quantity'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = '4. One-size-fits-all will fail'
    p = tf.add_paragraph()
    p.text = 'Personalization is necessary, not optional'
    p.level = 1

    # Slide 19: Ethics
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Limitations & Ethics'
    tf = slide.placeholders[1].text_frame
    tf.text = 'Limitations:'
    p = tf.add_paragraph()
    p.text = 'Affective classifiers may misclassify'
    p.level = 1
    p = tf.add_paragraph()
    p.text = 'Clusters are averages (variation exists)'
    p.level = 1
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Ethical Concerns:'
    p = tf.add_paragraph()
    p.text = 'Privacy: Facial recognition, behavior tracking'
    p.level = 1
    p = tf.add_paragraph()
    p.text = 'Bias: In classifiers, clustering, adaptations'
    p.level = 1
    p = tf.add_paragraph()
    p.text = 'Autonomy: Students should override decisions'
    p.level = 1

    # Slide 20: Conclusion
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = 'Conclusion'
    tf = slide.placeholders[1].text_frame
    tf.text = 'User modeling is powerful but imperfect'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Models are REPRESENTATIONS, not perfect descriptions'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Goal: Respectful, beneficial, transparent support'
    tf.add_paragraph().text = ''
    tf.add_paragraph().text = 'Students are individuals first, cluster members second'

    # Slide 21: Thank You
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = 'Thank You!'
    slide.placeholders[1].text = 'Questions?\n\nCS412 User Modeling - Midterm Project\nOctober 1, 2026'

    # Save
    prs.save('CS412_User_Modeling_Presentation.pptx')
    return len(prs.slides)

if __name__ == '__main__':
    num_slides = create_presentation()
    print(f'PowerPoint presentation created successfully!')
    print(f'Total slides: {num_slides}')
    print(f'File: CS412_User_Modeling_Presentation.pptx')
    print(f'')
    print(f'Note: Slides 5, 11, and 12 have placeholders for screenshots.')
    print(f'Insert visualizations from the Jupyter notebook:')
    print(f'  - Slide 5: Elbow Method and Silhouette Score charts')
    print(f'  - Slide 11: Activity Distribution bar chart')
    print(f'  - Slide 12: Accuracy and Affect comparison charts')
