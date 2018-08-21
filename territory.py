import time
import re
import itertools
import math
import random

def sameside(P,A,B,C):
    B_BC = (B[1]-C[1])*B[0] - (B[0]-C[0])*B[1]
    A_BC = (B[1]-C[1])*A[0] - (B[0]-C[0])*A[1] - B_BC
    P_BC = (B[1]-C[1])*P[0] - (B[0]-C[0])*P[1] - B_BC
    if A_BC != 0:                                       # exclude collinear
        if A_BC * P_BC >= 0:
            return True
    return False

def inside(P,A,B,C):
    if sameside(P,A,B,C):
        if sameside(P,B,C,A):
            if sameside(P,C,A,B):
                return True
    return False

def final(dots):                                        # global variable
    for subset in itertools.combinations(dots,3):
        A = subset[0]
        B = subset[1]
        C = subset[2]
        dots.remove(A)
        dots.remove(B)
        dots.remove(C)
        for P in dots:
            if inside(P,A,B,C):
                dots.append(A)
                dots.append(B)
                dots.append(C)
                random.shuffle(dots)                    # avoid endless final tests
                return False
        dots.append(A)
        dots.append(B)
        dots.append(C)
    return True

def reduce(dots):
    A = dots[0]
    B = dots[1]
    C = dots[2]
    dots.remove(A)
    dots.remove(B)
    dots.remove(C)
    for P in dots:
        if inside(P,A,B,C):
            dots.remove(P)
    dots.append(A)
    dots.append(B)
    dots.append(C)
    return dots

def deduplicate(dots):
    s = sorted(dots)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dots.remove(s[i])
    return dots

def triangle(A,B,C):
    u = (B[0]-A[0],B[1]-A[1],0)
    v = (C[0]-A[0],C[1]-A[1],0)
    cr = (u[0]*v[1]-u[1]*v[0],u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2])
    return math.sqrt(cr[0]*cr[0]+cr[1]*cr[1]+cr[2]*cr[2])/2

def convex(dots):
    convex = 0
    for i in range(len(dots)-2):
        convex += triangle(dots[0],dots[i+1],dots[i+2])
    return convex

def clockwise_from_left(dots):
    clockwise = []
    the_left = dots[-1]
    for i in range(len(dots)-1):                        # comparisons
        if dots[i][0] < the_left[0]:
            the_left = dots[i]
        elif dots[i][0] == the_left[0]:                 # get the lower left
            if dots[i][1] < the_left[1]:
                the_left = dots[i]
    clockwise.append(the_left)
    dots.remove(the_left)

    for the_nexts in range(len(dots)):                  # the_nexts
        the_next = dots[-1]
        try:
            m_next = (the_next[1]-the_left[1]) / (the_next[0]-the_left[0])
        except ZeroDivisionError:
            clockwise.append(the_next)
            dots.remove(the_next)
            continue
        for i in range(len(dots)-1):                    # comparisons
            try:
                m = (dots[i][1]-the_left[1]) / (dots[i][0]-the_left[0])
            except ZeroDivisionError:
                the_next = dots[i]
                break
            if m > m_next:
                m_next = m
                the_next = dots[i]
        clockwise.append(the_next)
        dots.remove(the_next)
    return clockwise

def main():
    start_time = time.time()
    dots = []
    with open('territory-data-1.csv') as f:
        for line in f:
            match = re.search('(.*),(.*)', line)
            if match:
                dots.append((float(match.group(1)),float(match.group(2))))
    dots = deduplicate(dots)
    loop = 0
    while True:
        loop += 1
        before = len(dots)
        dots = reduce(dots)
        after = len(dots)
        if before == after:
            if final(dots):
                break
    #print loop
    #print after
    dots = clockwise_from_left(dots)
    print "Dots: %s" % dots
    print "Area: %s" % convex(dots)
    print "Time: %s" % (time.time() - start_time)

if __name__ == "__main__":
	main()
