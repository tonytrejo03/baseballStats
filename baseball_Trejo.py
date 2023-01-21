# Anthony Trejo
# Baseball Stats
# HW#6

'''
Algorithm:
calculate hitters batting average, on_base_percentage, home_run_ratio, slugging_percentage
isolated_power, on_base_plus_slugging
pitchers, calculate, earned_run_average, WHIP, 
'''
# functions
def introduction():
    print("*"*88)
    print("BASEBALL STATISTICS".center(88))
    print("*"*88)
    print()
    print("")
    print("Welcome to Baseball Statistics. This program reads a file that contains statisitcs for")
    print("various players from the 2021 season. It will then calculate and print statistics for")
    print("hitters and then for pitchers.")
    print()

def goodbye():
    print()
    print("*"*88)
    print("Thanks. See you at the ballpark.".center(88))
    print("*"*88)

from baseball_stats_Trejo import batting_average, OBP, home_run_ratio, slugging_percentage, isolated_power, OPS, earned_run_average, WHIP, total_bases

# Main
introduction()

fname = input("Enter the name of the file to open: ")

success = False

while success == False:
    try:
        fvar = open(fname,"r")
        success = True
        print()
        print("File save to memory")
        print()
    except Exception as e:
        print("This error occurred: ")
        print(e)
        fname = input("Enter the name of a file: ")

line = fvar.readline()


# Hitters
print("*** Batting Statistics ***".center(88))
print()
while line:
    line = line.strip().lower()
    if line != "p":
        # position = fvar.readline()
        first_name = fvar.readline()
        last_name = fvar.readline()
        at_bats = int(fvar.readline())
        runs = int(fvar.readline())
        hits = int(fvar.readline())
        doubles = int(fvar.readline())
        triples = int(fvar.readline())
        home_runs = int(fvar.readline())
        runs_batted_in = int(fvar.readline())
        walks = int(fvar.readline())
        strikeouts = int(fvar.readline())
        stolen_bases = int(fvar.readline())
        avg = batting_average(at_bats,hits)
        hit_by_pitch = 0
        sacrifices = 0
        on_bp = OBP(hits,walks,hit_by_pitch,at_bats,sacrifices)
        HRR = home_run_ratio(at_bats,home_runs)
        singles = hits - doubles - triples - home_runs
        total_bases = singles + 2 * doubles + 3 * triples + 4 * home_runs
        slugging_per = slugging_percentage(total_bases,at_bats)
        ISO = isolated_power(slugging_per,avg)
        On_PS = OPS(on_bp,slugging_per)
        print("First name: %s" % first_name)
        print("Last name: %s" % last_name)
        print("avg %.3f" % avg)
        print("OBP %.3f" % on_bp)
        print("HRR %.2f" % HRR)
        print("SP %.3f" % slugging_per)
        print("ISO %.3f" % ISO)
        print("OPS %.3f" % On_PS)
    else:
        # position = fvar.readline()
        first_name = fvar.readline()
        last_name = fvar.readline()
        wins = int(fvar.readline())
        losses = int(fvar.readline())
        innings_pitched = float(fvar.readline())
        hits_allowed = int(fvar.readline())
        earned_runs = int(fvar.readline())
        home_runs = int(fvar.readline())
        walks = int(fvar.readline())
        strikeouts = int(fvar.readline())
    line = fvar.readline()
fvar.close()


# Pitchers
print("*** Pitching Statistics ***".center(88))
fvar = open(fname,"r")
line = fvar.readline()
while line:
    line = line.strip().lower()
    if line == "p":
        # postition = fvar.readline()
        first_name = fvar.readline()
        last_name = fvar.readline()
        wins = int(fvar.readline())
        losses = int(fvar.readline())
        innings_pitched = float(fvar.readline())
        hits_allowed = int(fvar.readline())
        earned_runs = int(fvar.readline())
        home_runs = int(fvar.readline())
        walks = int(fvar.readline())
        strikeouts = int(fvar.readline())
        ERA = earned_run_average(earned_runs,innings_pitched)
        WHP = WHIP(walks,hits,innings_pitched)
        # singles = (hits - doubles - triples - homers)
        # totalBases = total_bases(singles,doubles,triples,homers)
        print("First name: %s" % first_name)
        print("Last name: %s" % last_name)
        print("ERA %.2f" % ERA)
        print("WHIP %.2f" % WHP)
    else:
        first_name = fvar.readline()
        last_name = fvar.readline()
        at_bats = int(fvar.readline())
        runs = int(fvar.readline())
        hits = int(fvar.readline())
        doubles = int(fvar.readline())
        triples = int(fvar.readline())
        home_runs = int(fvar.readline())
        runs_batted_in = int(fvar.readline())
        walks = int(fvar.readline())
        strikeouts = int(fvar.readline())
        stolen_bases = int(fvar.readline())
    line = fvar.readline()
fvar.close()

input("Press enter to continue..")
goodbye()
