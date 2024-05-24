// script.js

let selectedField = '';

function selectField(field) {
    selectedField = field;

    // Hide field selection and show subject selection
    document.getElementById('field-selection').style.display = 'none';
    document.getElementById('subject-selection').style.display = 'block';

    // Get subjects for the selected field
    fetch('/get_subjects', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ field: field }),
    })
    .then(response => response.json())
    .then(subjects => {
        const subjectsContainer = document.getElementById('subjects-container');
        subjectsContainer.innerHTML = '';

        subjects.forEach(subject => {
            const subjectItem = document.createElement('div');
            subjectItem.className = 'subject-item';
            subjectItem.innerHTML = `
                <label>${subject}</label>
                <input type="number" name="${subject}" min="0" max="100" placeholder="Enter your score">
            `;
            subjectsContainer.appendChild(subjectItem);
        });
    })
    .catch(error => console.error('Error:', error));
}


function submitScores() {
    const form = document.getElementById('subject-form');
    const formData = new FormData(form);
    const scores = {};

    formData.forEach((value, key) => {
        scores[key] = parseInt(value);
    });

    
    fetch('/submit_scores', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ field: selectedField, scores: scores }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('subject-selection').style.display = 'none';
        document.getElementById('career-recommendation').style.display = 'block';

        const recommendationList = document.getElementById('recommendation-list');
        recommendationList.innerHTML = '';

        data.recommendations.forEach(([career, score]) => {
            const listItem = document.createElement('li');
            listItem.textContent = `${career}: ${score.toFixed(2)}`;
            recommendationList.appendChild(listItem);
        });


        const imagesContainer = document.getElementById('images-container');
        imagesContainer.innerHTML = '';

        data.image_urls.forEach(url => {
            const img = document.createElement('img');
            img.src = url;
            img.alt = 'Fuzzy plot for ' + url.split('/').pop().split('.')[0];
            img.style.width = '100%';
            img.style.marginTop = '20px';
            imagesContainer.appendChild(img);
        });
    })
    .catch(error => console.error('Error:', error));
}



// function submitScores() {
//     const form = document.getElementById('subject-form');
//     const formData = new FormData(form);
//     const scores = {};

//     formData.forEach((value, key) => {
//         scores[key] = parseInt(value);
//     });

//     fetch('/submit_scores', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ field: selectedField, scores: scores }),
//     })
//     .then(response => response.json())
//     .then(recommendations => {
//         document.getElementById('subject-selection').style.display = 'none';
//         document.getElementById('career-recommendation').style.display = 'block';

//         const recommendationList = document.getElementById('recommendation-list');
//         recommendationList.innerHTML = '';

//         for (const [career, score] of Object.entries(recommendations)) {
//             const listItem = document.createElement('li');
//             listItem.textContent = `${career}: ${score.toFixed(2)}`;
//             recommendationList.appendChild(listItem);
//         }
//     })
//     .catch(error => console.error('Error:', error));
// }
