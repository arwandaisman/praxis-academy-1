# Latihan 
## 1. CRC Card
Bootcamp CRC-Card
Class and Responsibilities :
  1. Student :
    - createTask
    - readTask
    - deleteTask
    - updateTask
    - pullTask
    - pushTask
    - attendClass
  2. Mentor :
    - createAssesment
    - deleteAssesment
    - updateAssesment
    - pushAssesment
    - readTask
    - attendClass
  3. Headmaster:
    - createCurriculum
    - readCurriculum
    - deleteCurriculum
    - updateCurriculum
    - readAttendant
  4. Attendant :
    - create
    - update
    - delete
    
Terdapat 4 class dan beberapa bagian tugas-tugas yang bisa mereka kerjakan.

Collaborators :
  1. Studnet - Mentor
  2. Student - Attendant
  3. Mentor - Attendant
  4. Mentor - Headmaster
  5. Headmaster - Attendant
   
<table>
  <tr>
    <td colspan="2">Student</td>
  </tr>
  <tr>
    <td> -createTask
    -readTask
    -deleteTask
    -updateTask
    -pullTask
    -pushTask
    -attendClass </td>
    <td> -Mentor
    -Attentdant</td>
  </tr>
</table>

<table>
  <tr>
    <td colspan="2">Mentor</td>
  </tr>
  <tr>
    <td> 
      - createAssesment
      - deleteAssesment
      - updateAssesment
      - pushAssesment
      - readTask
      - attendClass
    </td>
    <td> - Headmaster
    - Attentdant</td>
  </tr>
</table>

<table>
  <tr>
    <td colspan="2">Headmaster</td>
  </tr>
  <tr>
    <td> -createCurriculum
    -readCurriculum
    -deleteCurriculum
    -updateCurriculum
    -readAttendant</td>
    <td>
    -Attentdant</td>
  </tr>
</table>


## 2. Class & OOP

