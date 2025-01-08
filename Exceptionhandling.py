# compile time error
# run time error
# logical error

# try:
#     a=int(input())
#     b=int(input())
#     print(a+b)
# except Exception:
#     print("Something")


# --------------------------
# try:
#     a=int(input())
#     b=int(input())
#     print(a+b)
# except Exception as e:
#     print("Something", e)

# -----------------------
# try:
#     a=input()
#     b=input()
#     print(a/b)
# except Exception as e:
#     print("Something", e)
# finally:
#     print("something")

# ---------------------------
try:
    a=int(input())
    b=int(input())
    c=input()
    print(c/a)
except ValueError as e:
    print("Something", e)
except TypeError as e:
    print("Something", e)
finally:
    print("something")