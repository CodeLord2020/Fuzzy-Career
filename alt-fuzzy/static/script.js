// document.addEventListener('DOMContentLoaded', function () {
//     const subjectsContainer = document.getElementById('subjects-container');
//     const submitButton = document.getElementById('submit-button');
//     const errorMessage = document.getElementById('error-message');

//     window.selectField = function (field) {
//         console.log('Selected field:', field);
//         fetch('/get_subjects', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ field })
//         })
//         .then(response => response.json())
//         .then(data => {
//             console.log('Subjects received:', data);
//             subjectsContainer.innerHTML = '';
//             data.forEach(subject => {
//                 const div = document.createElement('div');
//                 div.classList.add('form-group');
//                 div.innerHTML = `
//                     <label for="${subject}">${subject}</label>
//                     <input type="number" class="form-control" id="${subject}" name="${subject}" min="0" max="100" required>
//                 `;
//                 subjectsContainer.appendChild(div);
//             });
//             document.getElementById('subject-selection').style.display = 'block';
//         })
//         .catch(error => {
//             console.error('Error fetching subjects:', error);
//         });
//     };

//     window.submitScores = function () {
//         const field = document.querySelector('input[name="field"]:checked').id;
//         const inputs = subjectsContainer.querySelectorAll('input');
//         const scores = {};

//         inputs.forEach(input => {
//             scores[input.name] = parseInt(input.value);
//         });

//         if (Object.keys(scores).length < 6) {
//             errorMessage.textContent = 'Please enter scores for all six subjects.';
//             return;
//         }

//         fetch('/submit_scores', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ field, scores })
//         })
//         .then(response => response.json())
//         .then(data => {
//             localStorage.setItem('recommendations', JSON.stringify(data));
//             window.location.href = '/results';
//         })
//         .catch(error => {
//             console.error('Error submitting scores:', error);
//         });
//     };

//     if (window.location.pathname === '/results') {
//         const recommendations = JSON.parse(localStorage.getItem('recommendations'));
//         if (recommendations) {
//             const listGroup = document.querySelector('.list-group');
//             recommendations.forEach(([career, score]) => {
//                 const li = document.createElement('li');
//                 li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
//                 li.innerHTML = `
//                     ${career}
//                     <span class="badge badge-primary badge-pill">${score}</span>
//                 `;
//                 listGroup.appendChild(li);
//             });
//         }
//     }
// });




document.addEventListener('DOMContentLoaded', function () {
    const subjectsContainer = document.getElementById('subjects-container');
    const errorMessage = document.getElementById('error-message');
    const gradeMap = {
        'A1': 'A1',
        'B2': 'B2',
        'B3': 'B3',
        'C4': 'C4',
        'C5': 'C5',
        'C6': 'C6',
        'D7': 'D7',
        'E8': 'E8',
        'F9': 'F9'
    };

    window.selectField = function (field) {
        fetch('/get_subjects', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ field })
        })
        .then(response => response.json())
        .then(data => {
            subjectsContainer.innerHTML = '';
            data.mandatory.forEach(subject => {
                const div = document.createElement('div');
                div.classList.add('form-group');
                div.innerHTML = `
                <label for="${subject}" style="color: whitesmoke;">${subject}</label>
                <select class="form-control" id="${subject}" name="${subject}" required>
                    <option value="" selected disabled>Select grade</option>
                    <option value="A1">A1 - Excellent</option>
                    <option value="B2">B2 - Very Good</option>
                    <option value="B3">B3 - Good</option>
                    <option value="C4">C4 - Credit</option>
                    <option value="C5">C5 - Credit</option>
                    <option value="C6">C6 - Credit</option>
                    <option value="D7">D7 - Pass</option>
                    <option value="E8">E8 - Pass</option>
                    <option value="F9">F9 - Fail</option>
                </select>
                `;
                subjectsContainer.appendChild(div);
            });

            const optionalDiv = document.createElement('div');
            optionalDiv.classList.add('form-group');
            optionalDiv.innerHTML = `
            <label for="optional" style="color: whitesmoke;">Optional Subject</label>
            <select class="form-control" id="optional" name="optional" required>
                ${data.optional.map(sub => `<option value="${sub}">${sub}</option>`).join('')}
            </select>
            <select class="form-control mt-2" id="optional_score" name="optional_score" required>
                <option value="" selected disabled>Select grade</option>
                <option value="A1">A1 - Excellent</option>
                <option value="B2">B2 - Very Good</option>
                <option value="B3">B3 - Good</option>
                <option value="C4">C4 - Credit</option>
                <option value="C5">C5 - Credit</option>
                <option value="C6">C6 - Credit</option>
                <option value="D7">D7 - Pass</option>
                <option value="E8">E8 - Pass</option>
                <option value="F9">F9 - Fail</option>
            </select>
            `;
            subjectsContainer.appendChild(optionalDiv);
            document.getElementById('subject-selection').style.display = 'block';
        })
        .catch(error => {
            console.error('Error fetching subjects:', error);
        });
    };

    window.submitScores = function () {
        const field = document.querySelector('input[name="field"]:checked').id;
        const selects = subjectsContainer.querySelectorAll('select');
        const scores = {};
        const optionalSubject = document.getElementById('optional').value;
        let valid = true;

        selects.forEach(select => {
            const value = select.value;
            if (!value) {
                valid = false;
            } else {
                if (select.id === 'optional_score') {
                    scores[optionalSubject] = gradeMap[value];
                } else {
                    scores[select.name] = gradeMap[value];
                }
            }
        });

        if (!valid) {
            errorMessage.textContent = 'Please select a grade for all subjects.';
            errorMessage.style.display = 'block';
            return;
        }

        errorMessage.style.display = 'none';

        fetch('/submit_scores', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ field, scores })
        })
        .then(response => response.json())
        .then(data => {

            localStorage.setItem('recommendations', JSON.stringify(data));
            console.log('localStorage:',localStorage);
            window.location.href = '/results';
        })
        .catch(error => {
            console.error('Error submitting scores:', error);
        });
    };

    if (window.location.pathname === '/results') {
     
        const recommendations = JSON.parse(localStorage.getItem('recommendations'));
  

        if (recommendations) {
            const listGroup = document.querySelector('.list-group');
            recommendations.forEach(([career, score, courses]) => {
                const li = document.createElement('li');
                li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
                li.innerHTML = `
                <div class="d-flex justify-content-between align-items-center">
                <h3 class="mb-1">${career}</h3>
                <span class="badge badge-primary score-badge">${score.toFixed(2)}</span>
                </div>
                <ul class="list-group mt-2">
                    ${courses.map(course => `<li class="list-group-item">${course}</li>`).join('')}
                </ul>
                `;
                listGroup.appendChild(li);
            });

        } else {
            console.error('No recommendations found in localStorage');
        }
    }  else {
        console.log('Not in the window location');
    }
});
