/* write your SQL statement here: you are given a table 
'makeuppercase' with column 's', return a table with column 
's' and your result in a column named 'res'. */

-- SELECT s, UPPER(s) AS res FROM makeuppercase

------ 

/*write your SQL statement here: you are given a table 
'quarterof' with column 'month', return a table with column 
'month' and your result in a column named 'res'.*/

-- SELECT
--   month,
--   CASE
--     WHEN month BETWEEN 1 AND 3 THEN 1
--     WHEN month BETWEEN 4 AND 6 THEN 2
--     WHEN month BETWEEN 7 AND 9 THEN 3
--     WHEN month BETWEEN 10 AND 12 THEN 4
--   END AS res
-- FROM quarterof;

------ 

/* You are a data analyst at a prestigious UK university. As part of the university's 
ongoing efforts to understand student performance and provide effective learning support, 
you've been tasked with analyzing the course scores of students over the academic year 2022-2023. 
Universities in the UK follow a trimester system, with each year split into three terms:

Michaelmas term (Autumn term) - October to December
Lent term (Spring term) - January to March
Summer term (or Easter term) - April to June
Your task is to identify students who have shown consistent improvement in their course scores over 
the three trimesters. The university is particularly interested in these students to understand and 
potentially replicate their success.

You have access to two tables: students and courses.

students:

| id  | name     | email               |
|-----|----------|---------------------|
| 1   | John     | john@example.com    |
| 2   | Sarah    | sarah@example.com   |
| 3   | Robert   | robert@example.com  |
...
courses:

| id  | student_id | course_name | score |  course_date |
|-----|------------|-------------|-------|--------------|
| 1   | 1          | Math        | 90    | 2022-10-01   |
| 2   | 1          | Science     | 85    | 2022-10-15   |
| 3   | 1          | Physics     | 92    | 2023-01-10   | 
| 4   | 1          | Literature  | 80    | 2023-04-05   |
...
The students table has records of the students' id, name, and email. The courses table keeps a record 
of each course's id, the student_id of the student who took the course, the course name, the student's 
score in the course, and the date when the course was completed.

Your query should return the following columns:

student_id: the id of the student
name: the name of the student
trimesters_avg_scores: a string aggregating the average score for each trimester, with each trimester's 
average score rounded to two decimal places and placed in brackets. The trimesters should appear in this 
order: Michaelmas, Lent, Summer.
consistent_improvement: a boolean indicating whether a student has shown consistent improvement in their 
scores. This should be true if a student's average score in the Lent term is higher than in the Michaelmas 
term, and their average score in the Summer term is higher than in the Lent term.
The results should be ordered by student_id in descending order. The trimester boundaries are defined by 
the start of the month of the first month of the trimester and the end of the month of the last month of 
the trimester. Only course records where course_date falls within these boundaries should be considered 
for the average calculation for that trimester.

GLHF!

Notes:

For this task, let's assume that each student has taken courses in all trimesters.
The academic year in consideration is from October 2022 to June 2023. Any records outside of this period 
should be disregarded.
Desired Output

The desired output should look like this:

student_id	name	trimesters_avg_scores	consistent_improvement
20	Mac Erdman DC	Michaelmas (84.14), Lent (85.43), Summer (81.14)	false
19	Lala Bradtke DO	Michaelmas (82.14), Lent (82.43), Summer (83.14)	true
18	Nolan Feil	Michaelmas (80.86), Lent (85.86), Summer (81.29)	false
... */

-- SELECT
--   students.id AS student_id,
--   students.name,
--   CONCAT(
--     'Michaelmas (',
--     ROUND(avg_michaelmas, 2),
--     '), ',
--     'Lent (',
--     ROUND(avg_lent, 2),
--     '), ',
--     'Summer (',
--     ROUND(avg_summer, 2),
--     ')'
--   ) AS trimesters_avg_scores,
--   avg_lent > avg_michaelmas AND avg_summer > avg_lent AS consistent_improvement
-- FROM students
-- JOIN (
--   SELECT
--     student_id,
--     AVG(CASE
--       WHEN EXTRACT(MONTH FROM courses.course_date) BETWEEN 10 AND 12 THEN courses.score
--       ELSE NULL
--     END) AS avg_michaelmas,
--     AVG(CASE
--       WHEN EXTRACT(MONTH FROM courses.course_date) BETWEEN 1 AND 3 THEN courses.score
--       ELSE NULL
--     END) AS avg_lent,
--     AVG(CASE
--       WHEN EXTRACT(MONTH FROM courses.course_date) BETWEEN 4 AND 6 THEN courses.score
--       ELSE NULL
--     END) AS avg_summer
--   FROM courses
--   WHERE courses.course_date >= '2022-10-01' AND courses.course_date <= '2023-06-30'
--   GROUP BY student_id
-- ) AS avg_scores ON students.id = avg_scores.student_id
-- ORDER BY students.id DESC;

/* Task:
Each day a plant is growing by upSpeed meters. Each night that plant's height decreases 
by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. 
We plant the seed at the beginning of a day. We want to know when the height of the plant 
will reach a certain level.

Example:
For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10. */

-- SELECT
--   id,
--   CASE
--     WHEN desired_height <= up_speed THEN 1
--     ELSE CEIL((desired_height * 1.0 - up_speed) / (up_speed - down_speed))::integer + 1
--   END AS num_days
-- FROM growing_plant;
