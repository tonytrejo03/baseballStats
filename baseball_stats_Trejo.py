# Anthony Trejo
# Functions for baseball_Trejo
# HW#6

import math

# Hitters
def batting_average(at_bats,hits):
    avg = (hits/at_bats) #* 100
    return avg

def OBP(hits,walks,hit_by_pitch,at_bats,sacrifices):
    on_base = (hits + walks + hit_by_pitch) / (at_bats + walks + hit_by_pitch + sacrifices)
    return on_base

def home_run_ratio(at_bats,home_runs):
    ratio = at_bats / home_runs
    return ratio

def slugging_percentage(total_bases,at_bats):
    # total_bases = singles + 2 * doubles + 3 * triples + 4 * homers
    slugging = total_bases/at_bats
    return slugging

def isolated_power(slugging_per,avg):
    power = slugging_per - avg
    # power = (total_bases/at_bats)-((hits/at_bats) * 100)
    return power

def OPS(OBP,slugging_percentage):
    on_ps = OBP + slugging_percentage
    return on_ps

# pitchers
def earned_run_average(runs_allowed,innings_pitched):
    average = 9*(runs_allowed/innings_pitched)
    return average

def WHIP(walks,hits,innings_pitched):
    whp = (walks + hits) / innings_pitched
    return whp

def total_bases(singles,doubles,triples,homers):
    total = singles + 2 * doubles + 3 * triples + 4 * homers
    return total
