# **CS412 - USER MODELING** 

# **MIDTERM PROJECT** 

# **From User Interaction Data to User Segments and Adaptive User Models** 

|**Group Size**|3 students(15 students in the class – 5groups)|
|---|---|
|**Dataset**|500 synthetic users;30-minutegame sessionper user|
|**Main Output**|User segmentation, personas,andproposed system adaptations|



# **1. Project Overview** 

For the midterm project, you will work in a group of 3 students to analyze the behavior of users interacting with a game-based learning platform. 

The platform is a narrative educational game in which learners perform three major types of activities: Reading, Answering, and Exploring. The dataset represents 500 users, each of whom used the platform for 30 minutes. During each session, observations were recorded every 15 seconds, resulting in 120 observations per user and 60,000 interaction records in the complete dataset. 

At every observation, the user's screen activity and affective state were classified. Additional behavioral and performance information is also available. Your task is not simply to run a clustering algorithm. You are expected to use concepts from CS412 User Modeling to discover meaningful patterns among users, construct interpretable user segments, represent these segments through personas, and propose ways the game could adapt to different types of users. 

# **2. Project Goal** 

Your group will answer the following main question: 

**_What meaningful types of users can be identified from their behavior, affective states, and performance while using the game-based learning platform, and how could the system adapt to these different users?_** 

Your analysis should demonstrate the following progression: 

**Interaction Data**  **User Features**  **User Segmentation**  **Segment Interpretation**  **Personas**  **System Adaptation** 

# **3. Dataset** 

Use the dataset provided by the instructor containing the simulated interaction data of the 500 users. 

|**Variable**|**Description**|
|---|---|
|User_ID|Unique identifier assigned to each user.|
|Capture_No|Sequence number of the 15-second observation.|
|Elapsed_Seconds|Time elapsed since the start of the session.|
|Elapsed_Time|Elapsed session time.|
|Screen_State|Reading, Answering, or Exploring.|
|Affective_State|Classified affective state of the user.|
|Answer_Outcome|Correct or Incorrect when the user is answering.|
|Response_Time_sec|Response time during answering activities.|
|Clicks_15sec|Number of interactions/clicks during the interval.|
|Narrative_Progress_pct|Estimated progress through the game.|



**Important:** The event-level dataset contains multiple observations for each user. Your clustering should represent users, not individual 15-second observations. You will therefore need to transform the interaction records into meaningful user-level features. 

# **4. Part A - Understanding the User Data** 

Before performing clustering, examine the dataset and explain what information is available about each user. Identify which variables or derived measures could represent aspects of the user discussed in class, such as: 

- behavior; 

- performance or knowledge indicators; 

- affective information; 

- interaction patterns; 

- possible goals or engagement indicators. 

Distinguish, where appropriate, between observed information and information inferred about the user. Explain which variables you believe are useful for segmentation and which variables should not be directly included in clustering. 

For example, User_ID identifies the user but does not describe the user's behavior. It therefore should not become a numerical clustering feature. Your group must justify your decisions rather than simply including every available variable. 

# **5. Part B - Feature Engineering** 

Transform the event-level interaction data into a representation where one row represents one user. 

Develop numerical features that summarize each user's 30-minute interaction. Possible features may include, but are not limited to: 

- proportion of observations spent Reading, Answering, and Exploring; 

- frequency or proportion of different affective states; 

- accuracy during answering; 

- average response time; 

- total or average number of clicks; 

- number of transitions between activities; 

- final narrative progress. 

You are not required to use all possible features. Select features that you believe meaningfully represent the users. You may construct additional features if they are reasonable and can be justified. 

For every derived feature, briefly explain what the feature measures and why it might help distinguish one type of user from another. Before clustering, examine whether the selected numerical features require preprocessing such as scaling or standardization. 

# **6. Part C - User Segmentation Through Clustering** 

Apply an appropriate clustering technique to group similar users. You may use K-Means clustering as the primary technique. Other appropriate clustering methods may also be used, provided that your group can explain the method. 

Your analysis must include: 

- features included in clustering; 

- preprocessing performed; 

- clustering technique used; 

- method used to determine an appropriate number of clusters; 

- resulting cluster membership; 

- number of users in each cluster. 

Do not simply choose a number of clusters because it produces convenient results. Use appropriate evidence to support your decision. For example, you may investigate different values of k using the Elbow Method and/or Silhouette Score. 

**There is no required number of clusters.** The objective is not to discover a predetermined number of groups. Your group should determine a reasonable segmentation based on the data and provide evidence supporting your decision. 

# **7. Part D - Analyze and Interpret the User Segments** 

This is one of the most important parts of the project. Clustering produces mathematical groups, but user modeling requires you to determine what those groups mean. 

For every cluster, examine its characteristics. Compare clusters in terms of Reading, Answering, and Exploring behavior; affective-state patterns; accuracy; response time; interaction frequency; narrative progress; and other features selected by your group. 

Create a cluster profile table summarizing the important characteristics of each cluster. Do not leave your clusters named simply Cluster 0, Cluster 1, and Cluster 2. After analyzing them, assign each cluster a meaningful descriptive name. 

For example, a hypothetical cluster might be described as 'Focused High-Progress Learners' or 'Persistent but Struggling Learners.' These are examples only. Do not use these names unless your actual results support them. 

Every segment name and interpretation must be supported by evidence from your analysis. Follow the reasoning: Observed Pattern -> Interpretation -> User Segment. 

# **8. Part E - Visualize the User Segments** 

Provide at least three meaningful visualizations that help explain the differences among your identified segments. 

Possible visualizations include: 

- cluster-size charts; 

- comparisons of behavioral characteristics across clusters; 

- comparisons of affective states; 

- accuracy or performance comparisons; 

- heatmaps of cluster characteristics; 

- scatter plots; 

- PCA-based two-dimensional visualization of clusters; 

- other appropriate visualizations. 

Do not include graphs simply to satisfy the requirement. Each visualization must have a clear purpose and must be explained in the report. For each visualization, explain what it tells you about the users or the identified segments. 

# **9. Part F - Develop User Personas** 

Create one persona for each major user segment identified through your clustering analysis. The personas must be based on your findings, not on arbitrary assumptions. 

Each persona should include at least: 

- Persona Name - use a fictional name; 

- Segment Represented - state which cluster the persona represents; 

- Short Description - briefly describe the type of learner represented; 

- Typical Behavior in the Game - how the user tends to interact with Reading, Answering, and Exploring activities; 

- Affective Pattern - affective states that commonly characterize the segment; 

- Performance Characteristics - how the segment typically performs; 

- Goals or Likely Motivation - what appears to drive this type of learner; 

- Pain Points or Difficulties - problems this type of user may encounter; 

- Needs from the System - what might help this user have a better learning experience. 

Do not invent characteristics that cannot reasonably be inferred from the dataset. For example, you cannot conclude that a user belongs to a particular socioeconomic group because the dataset does not measure that characteristic. Keep the persona grounded in the available evidence. 

# **10. Part G - Design Adaptive System Responses** 

Assume that the developers of the game-based learning platform want to use your user segments to personalize the experience. For each identified user segment, propose at least two system adaptations. 

Possible adaptations could involve difficulty adjustment, additional hints, review materials, pacing, feedback, narrative choices, exploration opportunities, encouragement, interface assistance, or recommendations for subsequent learning activities. 

Your proposals should follow this reasoning: **Evidence**  **User Need**  **System Adaptation** 

For example, if users in a segment demonstrate repeated incorrect answers, longer response times, and frequent confused states, these patterns may indicate difficulty with the learning material. The system could therefore provide progressive hints after repeated incorrect attempts. 

The adaptation must be based on characteristics actually observed in your segment. Avoid generic recommendations such as 'The system should improve the user experience.' Explain what the system should change, for whom, and why. 

# **11. Part H - Limitations, Ethics, and Critical Reflection** 

User models are representations of users. They are not perfect descriptions of people. Discuss the limitations of your analysis and address all of the following: 

- Affective-state classification: Can a facial image reliably tell us exactly what a learner is feeling? What could happen if the classifier makes an incorrect prediction? 

- Segmentation: Does belonging to a cluster mean that every user in that cluster behaves exactly the same way? 

- System adaptation: What could happen if the system adapts to a user based on an incorrect user model? 

- Privacy: What privacy concerns arise when a learning platform regularly captures users' faces and interaction behavior? 

- Bias and fairness: Could the data collection, affect classifier, selected features, or clustering process produce unfair or misleading representations of particular users? 

Your discussion should demonstrate that you understand that user modeling involves both technical and human considerations. 

# **12. Required Outputs** 

# **A. Midterm Project Report** 

Recommended length: 8-12 pages, excluding appendices. Use the following structure: 

1. Introduction - brief description of the problem and objective. 

2. Understanding the User Data - description and interpretation of available user information. 

3. Data Preparation and Feature Engineering - explain how event data were transformed into user-level features. 

4. User Segmentation Method - explain preprocessing, clustering method, and selection of the number of clusters. 

5. Results and User Segment Profiles - present cluster results, comparisons, visualizations, names, and interpretations. 

6. User Personas - present one evidence-based persona for each major segment. 

7. Proposed System Adaptations - explain how the platform could adapt to each segment. 

8. Limitations, Ethics, and Critical Reflection. 

9. Conclusion - summarize what your analysis reveals about the users of the game. 

# **B. Analysis File** 

Submit your complete Google Colab notebook (.ipynb) or Python notebook containing data loading, data cleaning, feature engineering, preprocessing, clustering, cluster evaluation, visualizations, and relevant outputs. The notebook must be capable of being followed from beginning to end. 

# **C. Final User-Level Dataset** 

Submit the final dataset used for clustering. It should contain 500 rows representing the 500 users, the user-level features created or selected by your group, and the assigned cluster of each user. 

# **D. Presentation** 

Prepare a 10-12 minute presentation summarizing the project. Focus primarily on: Who are the users you discovered, how do you know, and what should the system do differently for them? Do not spend most of the presentation explaining Python code. 

# **13. Grading Criteria** 

|**Component**|**Weight**|
|---|---|
|Understanding of User Data|10%|
|Feature Engineering and Data Preparation|15%|



|Clustering Method and Technical Analysis|20%|
|---|---|
|Interpretation and Profiling of User Segments|20%|
|Data-Based Personas|10%|
|Proposed Adaptive System Responses|10%|
|Limitations, Ethics, and Critical Reflection|10%|
|Quality and Clarity of Report/Presentation|5%|
|**TOTAL**|**100%**|



A technically functioning clustering model does not automatically receive a high grade. Greater emphasis will be placed on whether your group can interpret the results as meaningful user models. 

# **14. Group Work** 

This project must be completed in groups of 3 students. All members are expected to participate in understanding and preparing the data, analysis, interpretation, development of personas, preparation of the report, and presentation. 

Your group should be able to explain the entire project, not only the section completed by an individual member. During the presentation, the instructor may ask any member questions about any part of the analysis. 

Individual grades may be adjusted when there is clear evidence of unequal participation or inability to explain the group's submitted work. 

# **<mark>15. Use of AI Tools</mark>** 

You may use generative AI tools as supporting tools for this project. Acceptable uses include asking for explanations of Python errors, learning how a clustering function works, improving code readability, checking grammar and organization, and asking for explanations of statistical or machine-learning concepts. 

**However, AI-generated output is not evidence.** If an AI tool suggests that a cluster represents 'highly engaged learners,' your group must verify that interpretation using the actual characteristics of that cluster. 

You remain responsible for selecting appropriate features, verifying code and outputs, determining the number of clusters, interpreting the resulting segments, constructing defensible personas, proposing evidence-based adaptations, and explaining your decisions. 

During the presentation, you may be asked to explain your code, feature choices, clustering results, visualizations, and interpretations. Reliance on AI alone does not guarantee that your analysis, interpretation, or conclusions are correct. 

# **16. Important Reminder** 

**There is no single expected clustering solution for this project.** Two groups may use the same dataset and obtain different but defensible user segments because of differences in feature selection, preprocessing, clustering parameters, or interpretation. 

What matters is whether your group can demonstrate a clear and defensible chain of reasoning: 

- **What did the users do?** 

- **How did you represent those behaviors computationally?** 

- **What patterns did your analysis discover?** 

- **What do those patterns tell you about different types of users?** 

- **How should the system respond to those differences?** 

The purpose of the project is to demonstrate user modeling, not simply the execution of a machine-learning clustering algorithm. 

