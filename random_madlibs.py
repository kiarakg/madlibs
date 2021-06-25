from sample_madlibs import hungergames, zombie
import random

if __name__ == "__main__":
    m = random.choice([hungergames, zombie])
    m.madlib()