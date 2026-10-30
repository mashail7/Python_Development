def check_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ('@', '#', '$', '^')
    left_part = ticket[:10]
    right_part = ticket[10:]
    for symbol in winning_symbols:
        for uninterrupted_symbol_length in range(10, 6 - 1, -1):
            symbol_repetition = symbol * uninterrupted_symbol_length
            if symbol_repetition in left_part and symbol_repetition in right_part:
                if uninterrupted_symbol_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_symbol_length}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_symbol_length}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]

for current_ticket in tickets:
    print(check_ticket(current_ticket))