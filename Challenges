SELECT h.hacker_id, h.name, COUNT(c.challenge_id)
FROM Hackers h
JOIN Challenges c
ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
ORDER BY COUNT(c.challenge_id) DESC, h.hacker_id;
