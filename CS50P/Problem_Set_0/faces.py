def main():
    answer = input()
    convert(answer)

def convert(a_string): 
    if ":)" or ":(" in a_string:
        a_string = a_string.replace(":)", "🙂")
        a_string = a_string.replace(":(", "🙁")
        print(a_string)
      
if __name__ == "__main__":
    main()

