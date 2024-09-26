--1
SELECT air_force, COUNT(*), target_city
FROM public.mission
WHERE EXTRACT(YEAR FROM mission_date) = 1942
GROUP BY target_city , air_force
ORDER BY COUNT(*) DESC
LIMIT 1

--2
SELECT Bomb_Damage_Assessment , COUNT(target_country)
FROM public.mission
WHERE
COALESCE(airborne_aircraft, 0) + COALESCE(attacking_aircraft, 0) + COALESCE(bombing_aircraft, 0) > 5
AND Bomb_Damage_Assessment IS NOT NULL
GROUP BY Bomb_Damage_Assessment, target_country
ORDER BY COUNT(Bomb_Damage_Assessment) DESC
LIMIT 1