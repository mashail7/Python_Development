def loading_bar(number: int) -> str:
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        loaded_percent = number // 10
        not_loaded_percent = 10 - loaded_percent
        return f"{number}% [{'%' * loaded_percent}{'.' * not_loaded_percent}]\nStill loading..."

number = int(input())

print(loading_bar(number))