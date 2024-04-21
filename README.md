## Inspiration 💡
Parkinson's is the second-most common neurodegenerative disease after Alzheimer's disease, affecting 90,000 US citizens each year. Leveraging advancements in machine learning and artificial intelligence, we aimed to develop a tool that could effectively address this need.

Our decision to create a website for quick Parkinson's disease detection was sparked by a personal connection within our team - one of our members has a grandfather affected by the condition. Recognizing the global need for accessible detection methods to enable early intervention and improve treatment outcomes, we are motivated to employ the transformative power of technology to drive positive social impact. We are committed to using our skills and expertise to empower individuals to take control of their health and contribute to the collective effort to combat Parkinson's disease. Through our project, we aspire to make a meaningful difference in the lives of those affected by the condition, while also bettering society as a whole.

## What it does 🤔
Our website offers a simple yet powerful solution for early detection, not only enhancing the effectiveness of treatment but also contributing to ongoing research efforts and allowing individuals worldwide to gain awareness of their condition promptly. By collecting data through our platform, we aim to provide valuable insights into disease progression and treatment outcomes, ultimately advancing our understanding of Parkinson's disease.

ParkinDetectAI prompts users to submit a drawing - either a spiral or wave - from their system. Utilizing past data, the API analyzes the drawing to determine the presence of Parkinson's disease, offering swift and accurate detection for proactive health management. Through innovative technology, it sets a new standard in early diagnosis, ultimately transforming lives.

## How we built it 🛠
We started off by searching for the best-performing machine learning model, which ended up being XGBoost, and finetuning and perfecting it since it is the most vital part of this project, and later on, we ended up creating two models: one for spirals and another for waves since the two drawing types were too different from each other. We used Kaggle for the dataset, Scikit-Learn and XGBoost for model testing, OpenCV for image processing, and Pickle for model persistence. Once we were pleased with the results, we began developing the interactive and easy-to-use website using React Native and Expo and the accompanying Django API, which opens the pre-trained model saved with Pickle for a swifter diagnosis and allows the user to specify the type of drawing they are sending.

## Challenges we ran into
While developing our waves model, it initially had a significantly lower accuracy (77% 📉) than our spirals model, but after tweaking the data preprocessing and adjusting model parameters, we were able to vastly increase our spirals model's accuracy, reaching 93% 📈.

## Accomplishments that we're proud of
- Our AI model's ability to achieve a 90% accuracy rate in determining whether the user of the application has Parkinson's disease.

- Our website's intuitive interface and clear directions, enabling users to utilize our website without any difficulties.

## What we learned 🎓
This was our first time working with computer vision, so we learned a lot about the preprocessing phase and several image manipulation techniques, such as Canny edge detection, and we also picked up knowledge on how to work with files, both on the frontend, for the feature that lets users upload files, and the backend, which takes the image and saves it locally to analyze it.

## What's next for ParkinDetectAI
Our focus is on accessibility and excellence. We aim to continually refine the application, striving for near-perfect recognition capabilities with each update. This ensures ParkinDetectAI remains a reliable tool for accurate and timely detection of Parkinson's disease, accessible worldwide.

We also plan to enhance the website's usability and provide comprehensive information about the app's features. Additionally, we're committed to integrating user feedback for continuous improvements, ensuring ParkinDetectAI remains effective and user-friendly. We're forging partnerships with medical professionals to validate its efficacy and secure endorsements within the healthcare community. This collaboration will pave the way for ParkinDetectAI's integration into healthcare systems, establishing it as a standard diagnostic tool nationally and internationally.

Looking forward, ongoing research and development will leverage advancements in AI and machine learning to boost accuracy and broaden the app's functionalities, enhancing its utility in Parkinson's disease detection. Our goal is to become a globally trusted resource, making a significant impact in Parkinson's disease detection and improving outcomes and quality of life for individuals worldwide.

## Website 💻
Our amazing website was created by Sanjay Javangula, letting users interact with the model and API and choose whether they want to send a spiral or a wave. Then, the prediction of the model is displayed in a clear and concise manner. (https://github.com/sanjayshreeyans/Parkinson-Detection-Website)
