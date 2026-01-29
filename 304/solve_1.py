def base_exp(base,exp):
    if exp==0:
        return 1
    return base_exp(base,exp-1)*base

base=float(input())
exp=int(input())
print(f"{base_exp(base,exp):.3f}")

# Mohammad Yousefipour