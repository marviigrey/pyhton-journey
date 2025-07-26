from random import choice

capital = "ikeja"

bird = "kpekpeye"

flower = "roses"

song = "billionaires club"

def funfact():
    funfact = [
        "lagos is a very dirty city with poor drainage system and high cost of living.",
        "i wouldnt advice you to move here, touts everywhere with shits on every gutter you pass.",
        "only good thing in lagos is amala and probably bread from AM to PM superstore.",
        " its also over populated, resulting to traffic during work week."
    ]
    index = choice("0123")
    print(funfact[int(index)])

if __name__ == "__main__": #its advisable to put this if statement because if you the funfact function will always run when the module is called.
    funfact()
