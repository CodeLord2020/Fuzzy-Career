// script.js

const fields = {
    science: ['English Language', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Other (Agric, Geography, Further Math, Computer Studies)'],
    commercial: ['English Language', 'Mathematics', 'Government', 'Commerce', 'Economics', 'Financial Accounting'],
    arts: ['English Language', 'Literature in English', 'Law', 'Government', 'History', 'One other subject (Economics, Geography, Religious Studies, Nigerian Language)'],
    technology: ['English Language', 'Mathematics', 'Physics', 'Chemistry', 'Computer Studies', 'Data Processing']
};

function selectField(field) {
    const subjectSelectionSection = document.getElementById('subject-selection');
    const subjectsContainer = document.getElementById('subjects-container');
    subjectsContainer.innerHTML = '';

    fields[field].forEach(subject => {
        const subjectItem = document.createElement('div');
        subjectItem.className = 'subject-item';

        const label = document.createElement('label');
        label.textContent = `${subject}:`;
        subjectItem.appendChild(label);

        const input = document.createElement('input');
        input.type = 'number';
        input.name = subject;
        input.min = 0;
        input.max = 100;
        subjectItem.appendChild(input);

        subjectsContainer.appendChild(subjectItem);
    });

    subjectSelectionSection.style.display = 'block';
}

function submitScores() {
    const form = document.getElementById('subject-form');
    const formData = new FormData(form);
    const scores = {};

    for (let [subject, score] of formData.entries()) {
        scores[subject] = parseInt(score, 10);
    }

    console.log('User scores:', scores);

    const recommendations = computeRecommendations(scores);
    displayRecommendations(recommendations);
}

function computeRecommendations(scores) {
    // Dummy implementation for computing recommendations
    // Replace with actual fuzzy logic computation
    return {
        'Software Engineer': 0.85,
        'Data Scientist': 0.75,
        'Physicist': 0.65,
        'Accountant': 0.60,
        'Marketing Manager': 0.50
    };
}

function displayRecommendations(recommendations) {
    const recommendationSection = document.getElementById('career-recommendation');
    const recommendationList = document.getElementById('recommendation-list');
    recommendationList.innerHTML = '';

    for (let [career, score] of Object.entries(recommendations)) {
        const listItem = document.createElement('li');
        listItem.textContent = `${career}: ${(score * 100).toFixed(2)}% match`;
        recommendationList.appendChild(listItem);
    }

    recommendationSection.style.display = 'block';
}
