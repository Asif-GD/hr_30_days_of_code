t = int(input("Number of test cases? "))
for i in range(0, t):
    input_string = input("Enter your string: ")
    even_string, odd_string = "", ""
    for index in range(len(input_string)):
        if index % 2 == 0:
            even_string += input_string[index]
        else:
            odd_string += input_string[index]
    print(f"{even_string} {odd_string}")
