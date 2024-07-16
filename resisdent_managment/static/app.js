document.getElementById('addStudentForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const studentData = {
        student_id: document.getElementById('student_id').value,
        name: document.getElementById('name').value,
        gender: document.getElementById('gender').value,
        dorm_number: document.getElementById('dorm_number').value,
        phone: document.getElementById('phone').value
    };
    addStudent(studentData);
});

function fetchStudents() {
    fetch('/students')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('studentsTable').getElementsByTagName('tbody')[0];
            tableBody.innerHTML = '';  // Clear existing rows
            data.forEach(student => {
                const row = tableBody.insertRow();
                Object.values(student).forEach(text => {
                    const cell = row.insertCell();
                    cell.appendChild(document.createTextNode(text));
                });
                const deleteCell = row.insertCell();
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = function() { deleteStudent(student.student_id); };
                deleteCell.appendChild(deleteButton);
            });
        });
}

function addStudent(studentData) {
    fetch('/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(studentData)
    }).then(response => response.json())
      .then(data => {
          alert(data.message);
          if (data.message.includes('successfully')) {
              window.location.href = '/'; // Redirect to the index page
          }
      });
}
function searchStudent() {
    const studentId = document.getElementById('searchStudentId').value;
    fetch(`/students/${studentId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const infoDiv = document.getElementById('studentInfo');
            infoDiv.innerHTML = '';  // 清空之前的信息
            if (data && data.student_id) {  // 确认数据包含 student_id
                const infoContent = `ID: ${data.student_id}, Name: ${data.name}, Gender: ${data.gender}, Dorm: ${data.dorm_number}, Phone: ${data.phone}`;
                infoDiv.textContent = infoContent;
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = function() { deleteStudent(data.student_id); };
                infoDiv.appendChild(deleteButton);
            } else {
                infoDiv.textContent = 'No student found with that ID.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error fetching data: ' + error.message);
        });
}

function deleteStudent(studentId) {
    fetch(`/students/${studentId}`, {
        method: 'DELETE'
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to delete the student');
        }
    })
    .then(data => {
        alert(data.message);
        const infoDiv = document.getElementById('studentInfo');
        if (infoDiv) {
            infoDiv.innerHTML = '';  // 此处添加检查确保infoDiv不为null
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error.message);
    });
}
