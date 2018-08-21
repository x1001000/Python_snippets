def ways(n):      # How many ways when n stairs left
    if n<0:
        return 0  # No way there are minus stairs left
    if n==0:
        return 1  # Always one way for the final
    if n==1:
        return 1  # Only one way for 1 step
    return ways(n-1)+ways(n-2)+ways(n-3)
                # 1   or    2   or    3 step(s) as the final
