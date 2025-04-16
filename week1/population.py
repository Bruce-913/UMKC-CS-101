#I believe Computer Science is important because it is the root of innovation in technology.
#As technology becomes more popular over time, more force and knowledge is needed to improve these forms of technology being used.
#This includes using programming languages like Python.
#Python is an amazing languages that is easy to understand in comparison to others making it beginner friendly for those who wish to learn.
#Although Python is a very good language, it is not the best language. 
#Every language has it’s strong points that strive better than others depending on what you use them for and Python’s main strong points are it’s abundant resources, readability, versatility, and its open-source as well. 
#Even though it has many strong points, it also has weaknesses to it. Some of these weaknesses are it’s slow speeds because it is an interpreted language and it’s large memory consumption.
#Despite its weaknesses, it is still an amazing language to learn.


#Request input from user
number_of_years = int(input("Estimate of future U.S Population in how many years:"))

def estimated_population(years):
    #Given Constants
    starting_population = 307357870
    year_in_seconds = 31536000

    total_years = years * year_in_seconds

    #Operations done beforehand
    births_in_years = total_years // 7
    deaths_in_years = total_years // 13
    immigrants_in_years = total_years // 35

    future_population = starting_population + births_in_years + immigrants_in_years - deaths_in_years

    return future_population



future_population = estimated_population(number_of_years)
print ("in", number_of_years, "years, the U.S population will be roughly around:", future_population)