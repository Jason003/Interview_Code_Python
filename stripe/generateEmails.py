def generateEmails(invoices):
    prompts = [
        (-10, 'Upcoming'),
        (0, 'New'),
        (20, 'Reminder'),
        (30, 'Due')
    ]

    result = []

    for time, name, money in invoices:
        for deltaTime, message in prompts:
            result.append((time + deltaTime, '[{0}] Invoice for {1} for {2} dollars'.format(message, name, money)))

    return [email for time, email in sorted(result)]


print(generateEmails([[0, 'Alice', 200], [1, 'Bob', 100]]))
