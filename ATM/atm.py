# Задача - банкомат, выдаввй купюры минимальным номиналом, но каждой купюры не более 10 штук
def atm(value):
    nominal = [10, 20, 50, 100]
    result = {
        10: 0,
        20: 0,
        50: 0,
        100: 0
    }

    for i in range(len(nominal)):
        ostatok = value % nominal[i]
        deljenije  = value // nominal[i]

        if ostatok == 0 and deljenije <= 10:
            result[nominal[i]] = deljenije
            value -= nominal[i] * deljenije
            return result
        
        elif deljenije > 10:
            value -= nominal[i] * 10
            result[nominal[i]] = 10

        elif ostatok != 0 and deljenije <= 10:
            while value % nominal[i] != 0:
                result[nominal[i-1]] -= 1
                value += nominal[i-1]
                
            
            result[nominal[i]] = value // nominal[i]
            value -= nominal[i] * result[nominal[i]]

        if value == 0:
            break

print(atm(340))