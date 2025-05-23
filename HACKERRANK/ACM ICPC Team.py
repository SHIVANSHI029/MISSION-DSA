def acmTeam(topic):
    max_topics = 0
    team_count = 0

    n = len(topic)

    for i in range(n):
        for j in range(i + 1, n):
            # Combine topics using bitwise OR
            combined = bin(int(topic[i], 2) | int(topic[j], 2))
            # Count the number of '1's in the result
            topics_known = combined.count('1')

            if topics_known > max_topics:
                max_topics = topics_known
                team_count = 1
            elif topics_known == max_topics:
                team_count += 1

    return [max_topics, team_count]
